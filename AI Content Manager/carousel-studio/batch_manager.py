#!/usr/bin/env python3
"""
batch_manager.py — Gestor Determinista del Batch Semanal de Carruseles (Brand OS)

Permite:
  1. new-week : Inicializar el lote semanal de 5 carruseles leyendo ROTATION.md.
  2. status   : Escanear las carpetas assets/ de cada carrusel, chulear fondos subidos y mostrar qué falta.
  3. compile  : Renderizar los carruseles que tengan todos sus fondos completos usando Playwright.
"""

import os
import sys
import json
import re
import subprocess
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent
PROJECTS_DIR = ROOT_DIR
ROTATION_FILE = ROOT_DIR / "ROTATION.md"
BATCH_TRACKER_FILE = ROOT_DIR / "BATCH_TRACKER.md"
CURRENT_BATCH_FILE = ROOT_DIR / "CURRENT_BATCH.json"

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

def load_current_batch():
    if CURRENT_BATCH_FILE.exists():
        try:
            with open(CURRENT_BATCH_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return None

def save_current_batch(data):
    with open(CURRENT_BATCH_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def find_carousel_dir(slug):
    direct = PROJECTS_DIR / slug
    if direct.exists():
        return direct
    batches_dir = PROJECTS_DIR / "batches"
    if batches_dir.exists():
        for b in batches_dir.iterdir():
            cand = b / slug
            if cand.exists():
                return cand
    return direct

def check_carousel_assets(carousel_slug, expected_count=5):
    carousel_dir = find_carousel_dir(carousel_slug)
    assets_dir = carousel_dir / "assets"
    
    if not assets_dir.exists():
        return {
            "found_count": 0,
            "expected_count": expected_count,
            "missing_indices": list(range(1, expected_count + 1)),
            "found_files": []
        }
    
    found_files = {}
    for file in assets_dir.iterdir():
        if file.suffix.lower() in IMAGE_EXTENSIONS and file.stem.startswith("bg_"):
            # Extract number, e.g. bg_01 -> 1
            match = re.search(r"bg_(\d+)", file.stem)
            if match:
                idx = int(match.group(1))
                found_files[idx] = file.name

    missing = [i for i in range(1, expected_count + 1) if i not in found_files]
    return {
        "found_count": len(found_files),
        "expected_count": expected_count,
        "missing_indices": missing,
        "found_files": found_files
    }

def update_tracker_md(batch_data):
    lines = [
        f"# BATCH TRACKER — {batch_data.get('title', 'Semana Actual')}",
        f"> **Vuelta:** {batch_data.get('vuelta', 'Vuelta')} | **Fecha de Creación:** {batch_data.get('created_at', '')}",
        f"> **Última Verificación:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
        "## Resumen del Batch (5 Carruseles de Rotación)",
        "",
        "| # | Línea | Tema / Slug | Fondos Listos | Estado | Acción Inmediata |",
        "| :-: | :--- | :--- | :---: | :---: | :--- |"
    ]

    for item in batch_data.get("carousels", []):
        slug = item["slug"]
        line = item["line"]
        expected = item.get("slides_count", 5)
        check = check_carousel_assets(slug, expected)
        
        status_icon = "⏳ Pendiente"
        action = f"Subir bg_{check['missing_indices'][0]:02d}..." if check["missing_indices"] else "Listo para compilar"
        
        # Check if slides already compiled
        slides_dir = PROJECTS_DIR / slug / "slides"
        compiled = False
        if slides_dir.exists() and any(slides_dir.glob("slide-*.png")):
            compiled = True

        if compiled:
            status_icon = "🚀 En Cola (Publicación)"
            action = "Listo para Metricool"
        elif check["found_count"] >= expected:
            status_icon = "✅ Fondos Completos"
            action = f"`batch_manager.py compile {slug}`"

        progress_bar = f"{check['found_count']}/{expected} (" + "".join(["🟢" if i not in check["missing_indices"] else "⚪" for i in range(1, expected + 1)]) + ")"
        lines.append(f"| {item['index']} | `{line}` | [{slug}](./{slug}/copy.md) | {progress_bar} | {status_icon} | {action} |")

    lines.extend([
        "",
        "---",
        "",
        "## ¿Qué hay que hacer ahora?",
        ""
    ])

    # Find the first carousel that has missing images
    pending_found = False
    for item in batch_data.get("carousels", []):
        slug = item["slug"]
        expected = item.get("slides_count", 5)
        check = check_carousel_assets(slug, expected)
        if check["missing_indices"]:
            pending_found = True
            next_idx = check["missing_indices"][0]
            lines.append(f"👉 **Siguiente paso:** En `{slug}` falta **`bg_{next_idx:02d}.jpg`**.")
            lines.append(f"Copiá la imagen generada en: `pipeline/carousels/{slug}/assets/bg_{next_idx:02d}.jpg`")
            break

    if not pending_found:
        lines.append("🎉 **¡Todos los fondos del batch están completos!**")
        lines.append("Podés correr `python pipeline/carousels/batch_manager.py compile-all` para generar todos los PNGs.")

    with open(BATCH_TRACKER_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

def cmd_status():
    batch = load_current_batch()
    if not batch:
        print("⚠️ No hay ningún batch activo en CURRENT_BATCH.json.")
        print("Corré `python batch_manager.py new-week` para iniciar uno nuevo.")
        return

    update_tracker_md(batch)
    print("=" * 68)
    print(f"📊 ESTADO DEL BATCH: {batch.get('title', 'Semana')} ({batch.get('vuelta', '')})")
    print("=" * 68)

    all_done = True
    for item in batch.get("carousels", []):
        slug = item["slug"]
        line = item["line"]
        expected = item.get("slides_count", 5)
        check = check_carousel_assets(slug, expected)
        
        dots = "".join(["[✓]" if i not in check["missing_indices"] else "[ ]" for i in range(1, expected + 1)])
        print(f"\n• {item['index']}. [{line.upper()}] {slug}")
        print(f"   Fondos: {dots} ({check['found_count']}/{expected})")
        
        carousel_dir = find_carousel_dir(slug)
        slides_dir = carousel_dir / "slides"
        if slides_dir.exists() and any(slides_dir.glob("slide-*.png")):
            print("   Estado: 🚀 RENDERIZADO / EN COLA DE PUBLICACIÓN")
        elif check["found_count"] >= expected:
            print("   Estado: ✅ FONDOS COMPLETOS — Listo para compilar")
        else:
            all_done = False
            next_idx = check["missing_indices"][0]
            print(f"   Estado: ⏳ Falta bg_{next_idx:02d}...")

    print("\n" + "-" * 68)
    if all_done:
        print("✨ ¡Todos los carruseles tienen sus fondos completos!")
    else:
        print("💡 Para revisar los prompts de cada slide, abrí `copy.md` en la carpeta del carrusel.")
    print("El archivo `BATCH_TRACKER.md` ha sido actualizado.")
    print("=" * 68)

def cmd_compile(slug):
    carousel_dir = find_carousel_dir(slug)
    if not carousel_dir.exists():
        print(f"❌ Error: No existe la carpeta {slug}")
        return

    html_file = carousel_dir / "carousel.html"
    if not html_file.exists():
        print(f"❌ Error: No existe {slug}/carousel.html")
        return

    capture_script = PROJECTS_DIR / "capture.cjs"
    out_dir = carousel_dir / "slides"
    
    print(f"⚙️ Compilando carrusel: {slug}...")
    cmd = ["node", str(capture_script), str(html_file), str(out_dir)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    
    if res.returncode == 0:
        print(f"✅ ¡Compilación exitosa! Slides generados en {out_dir}")
        batch = load_current_batch()
        if batch:
            update_tracker_md(batch)
    else:
        print(f"❌ Error en compilación:\n{res.stderr or res.stdout}")

def main():
    if len(sys.argv) < 2:
        cmd_status()
        return

    action = sys.argv[1].lower()
    if action in {"status", "check", "info"}:
        cmd_status()
    elif action in {"compile", "render"} and len(sys.argv) >= 3:
        cmd_compile(sys.argv[2])
    elif action in {"new-week", "init"}:
        print("💡 Para inicializar la nueva vuelta de rotación, el agente o skill generará los 5 carruseles con sus One-Liners y prompts cinematográficos.")
        cmd_status()
    else:
        print(f"Uso: python batch_manager.py [status | compile <slug> | new-week]")

if __name__ == "__main__":
    main()
