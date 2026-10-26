#!/usr/bin/env python3
"""
Auto-source de imágenes (logos + personas) para carruseles y shorts de Donovan.

Flujo:
  - detect_entities_in_copy(slide_body) -> list[dict]
      detecta menciones de tools conocidas y @handles de personas.
  - source_logo(tool_name) -> str | None
      busca SVG del logo via svgl.app (free, sin API key).
  - source_person_photo(person_name) -> str | None
      busca thumbnail de Wikipedia (CC-BY-SA) via API pública.
  - Cache local en assets/known-tools/ para reusar (evita re-sourcear).

Licencias:
  - svgl.app logos: mayormente Apache/MIT/CC0 (ver cada SVG).
  - Wikimedia photos: CC-BY / CC-BY-SA — agregar footnote "Foto: Wikipedia (CC BY-SA)".

Si no se encuentra, retorna None — NUNCA fallar el pipeline por una imagen missing.
Better sin foto que con foto equivocada.
"""
from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

# Root del AI Content Manager (3 niveles arriba: helper/ → project root)
ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "assets" / "known-tools"
PEOPLE_CACHE_DIR = CACHE_DIR / "people"

# Lista de brands conocidas — ampliable. Rick (de Hermes) la alimenta dinámicamente
# via 00_input/from-studio/specs/known-tools-update.md.
KNOWN_TOOLS = {
    # SaaS / dev tools
    "linear", "notion", "stripe", "vercel", "github", "gitlab", "figma",
    "slack", "discord", "openai", "anthropic", "claude", "perplexity",
    "cursor", "windsurf", "vscode", "replit", "supabase", "firebase",
    "cloudflare", "aws", "gcp", "azure", "docker", "kubernetes",
    "huggingface", "replicate", "elevenlabs", "heygen", "runway",
    "midjourney", "nvidia", "google", "meta", "x", "twitter",
    "whatsapp", "telegram", "tiktok", "instagram", "youtube",
    "metricool", "zapier", "n8n", "make", "airtable", "obsidian",
    # Angus batch - added 2026-07-26
    "claude code", "hermes", "apollo", "clay", "prospeo",
}

# Map de @handle → nombre Wikipedia (para thumbnails de personas públicas)
HANDLE_TO_WIKI = {
    "@samaltman": "Sam Altman",
    "@satyanadella": "Satya Nadella",
    "@elonmusk": "Elon Musk",
    "@sundarpichai": "Sundar Pichai",
    "@clem": "Clément Delangue",  # huggingface CEO — fuzzy
    "@karpathy": "Andrej Karpathy",
    "@gitcasey": "Casey Kinross",  # placeholder — ajustar si necesario
    "@levelsio": "Pieter Levels",
}


def slug_from_name(name: str) -> str:
    """Normaliza un nombre a slug para svgl.app."""
    return re.sub(r"[^a-zA-Z0-9]+", "", name.lower())


def source_logo(tool_name: str, cache: bool = True) -> Optional[str]:
    """
    Busca el SVG de un logo via svgl.app (catálogo de tech logos, free, sin API key).

    Returns:
      - str con el SVG contenido si lo encuentra.
      - None si falla o no está.
    Cacha en assets/known-tools/<slug>.svg.
    """
    slug = slug_from_name(tool_name)
    cache_file = CACHE_DIR / f"{slug}.svg"

    if cache and cache_file.exists():
        return cache_file.read_text(encoding="utf-8")

    # svgl.app soporta multi-slug: ?slug1,slug2,slug3
    url = f"https://svgl.app/api/{slug}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "donovan-auto-source/1.0"})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode("utf-8"))
        # svgl.app retorna un array de objects con .svg
        if isinstance(data, list) and data and "svg" in data[0]:
            svg = data[0]["svg"]
            if cache:
                CACHE_DIR.mkdir(parents=True, exist_ok=True)
                cache_file.write_text(svg, encoding="utf-8")
            return svg
        # Algunos endpoints retornan un object directo
        if isinstance(data, dict) and "svg" in data:
            svg = data["svg"]
            if cache:
                CACHE_DIR.mkdir(parents=True, exist_ok=True)
                cache_file.write_text(svg, encoding="utf-8")
            return svg
        return None
    except Exception:
        return None


def source_person_photo(person_name: str, cache: bool = True) -> Optional[dict]:
    """
    Busca una foto recente de persona via Wikipedia API (pithumbsize=500, CC-BY-SA).

    Returns:
      - dict con {url, source_page, license: "CC-BY-SA Wikipedia"} si encuentra.
      - None si falla.
    Cacha en assets/known-tools/people/<slug>.jpg + <slug>.meta.json.
    """
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", person_name.lower()).strip("-")
    cache_file = PEOPLE_CACHE_DIR / f"{slug}.jpg"
    meta_file = PEOPLE_CACHE_DIR / f"{slug}.meta.json"

    if cache and cache_file.exists() and meta_file.exists():
        meta = json.loads(meta_file.read_text(encoding="utf-8"))
        return {"url": str(cache_file), "source_page": meta.get("source_page", ""), "license": "CC-BY-SA Wikipedia", "cached": True}

    api = (
        "https://en.wikipedia.org/w/api.php?action=query"
        f"&titles={urllib.parse.quote(person_name)}&prop=pageimages&format=json&pithumbsize=500"
    )
    try:
        req = urllib.request.Request(api, headers={"User-Agent": "donovan-auto-source/1.0"})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode("utf-8"))
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            thumb = page.get("thumbnail", {}).get("source")
            page_title = page.get("title", person_name)
            if thumb:
                # Download the photo
                if cache:
                    PEOPLE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
                    try:
                        req2 = urllib.request.Request(thumb, headers={"User-Agent": "donovan-auto-source/1.0"})
                        with urllib.request.urlopen(req2, timeout=10) as r2:
                            cache_file.write_bytes(r2.read())
                        meta_file.write_text(json.dumps({
                            "source_url": thumb,
                            "source_page": f"https://en.wikipedia.org/wiki/{urllib.parse.quote(page_title)}",
                            "license": "CC-BY-SA Wikipedia",
                            "wiki_page": page_title,
                        }, indent=2), encoding="utf-8")
                    except Exception:
                        pass
                return {
                    "url": thumb,
                    "source_page": f"https://en.wikipedia.org/wiki/{urllib.parse.quote(page_title)}",
                    "license": "CC-BY-SA Wikipedia",
                }
        return None
    except Exception:
        return None


def detect_entities_in_copy(slide_body: str) -> list[dict]:
    """
    Detecta menciones de tools conocidas y @handles de personas en un slide body.

    Returns list of dicts:
      [{"entity": "Linear", "type": "tool", "match": "Linear"}, ...]
    """
    found = []
    body_lower = slide_body.lower()

    # 1. Tools conocidas — match exacto pero respetando case en el output
    for tool in KNOWN_TOOLS:
        # Word-boundary match, case-insensitive
        pattern = r"\b" + re.escape(tool) + r"\b"
        m = re.search(pattern, body_lower)
        if m:
            found.append({
                "entity": tool.capitalize(),
                "type": "tool",
                "match": tool,
            })

    # 2. @handles de personas (Twitter-style)
    for m in re.finditer(r"@([a-zA-Z0-9_]+)", slide_body):
        handle = m.group(0).lower()
        wiki_name = HANDLE_TO_WIKI.get(handle)
        if wiki_name:
            found.append({
                "entity": wiki_name,
                "type": "person",
                "match": handle,
            })
        else:
            # Unknown @handle —рапортar como person sin wiki name (no sourceable)
            found.append({
                "entity": handle,
                "type": "person",
                "match": handle,
                "wiki_name": None,
            })

    # Dedupe by entity+type
    seen = set()
    unique = []
    for e in found:
        key = (e["entity"], e["type"])
        if key not in seen:
            seen.add(key)
            unique.append(e)
    return unique


def source_entity(entity: dict) -> Optional[dict]:
    """
    Para una entity detectada, sourcear su asset.
    Returns dict: {entity, type, asset_path_or_url, ...} o None.
    """
    if entity["type"] == "tool":
        svg = source_logo(entity["match"])
        if svg:
            return {"entity": entity["entity"], "type": "tool", "svg": svg}
        return None
    elif entity["type"] == "person":
        if not entity.get("wiki_name", "missing") and entity["entity"].startswith("@"):
            # Unknown handle — no sourceable via Wikipedia
            return None
        photo = source_person_photo(entity["entity"])
        if photo:
            return {
                "entity": entity["entity"],
                "type": "person",
                "photo_url": photo["url"],
                "license": photo["license"],
                "source_page": photo.get("source_page", ""),
            }
        return None
    return None


def detect_and_source(slide_body: str) -> list[dict]:
    """
    One-shot: detecta entities en el copy y retorna sólo las que se pudieron sourcear.
    No romper si alguna falla —si types sólo la que matchean.
    """
    entities = detect_entities_in_copy(slide_body)
    sourced = []
    for e in entities:
        result = source_entity(e)
        if result:
            sourced.append(result)
    return sourced


# ---------------- CLI mode ----------------
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: auto_source_image.py <slide_body_text|'tool:linear'|'person:Sam Altman'>", file=__import__("sys").stderr)
        sys.exit(1)

    arg = " ".join(sys.argv[1:])
    # Modos explícitos
    if arg.startswith("tool:"):
        r = source_logo(arg[5:])
        print(json.dumps({"tool": arg[5:], "found": bool(r)}, indent=2) if r else f"✗ no logo for {arg[5:]}")
    elif arg.startswith("person:"):
        r = source_person_photo(arg[7:])
        print(json.dumps(r, indent=2) if r else f"✗ no photo for {arg[7:]}")
    else:
        # Modo detect: pega slide body
        print("Detected entities:")
        for e in detect_entities_in_copy(arg):
            print(f"  - {e['entity']} ({e['type']})")
        print("\nSourced:")
        for s in detect_and_source(arg):
            print(f"  - {s['entity']}: {'SVG' if s.get('svg') else s.get('photo_url')}")
