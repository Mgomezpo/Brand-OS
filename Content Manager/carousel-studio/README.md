# Carousel Studio — Motor de Carruseles 3:4 (1080 × 1440 px)

Motor determinista de carruseles: fondos generados por IA (100% limpios de texto) + tipografía estampada en HTML/CSS con tokens de marca + compilación a PNG con Playwright.

> **Guía profunda:** `../../vault/SOPs/carousel_batch.md` · **Guía operativa general:** `../../AGENTS.md` (apartado *Motores del Sistema*) · **Tokens:** `../../design-system/tokens.css` + `../../vault/Conceptos/design_lines/`

---

## Comandos

```bash
npm install                              # solo la primera vez (Playwright + Chromium)
python batch_manager.py status           # retrato del batch: qué carrusel/fondo falta
python batch_manager.py compile <slug>   # compila <slug>/carousel.html → slides/*.png (3:4)
npm run capture -- <slug>/carousel.html  # compilación directa de una pieza suelta
```

## Anatomía de cada carrusel — `batches/<vuelta>/<slug>/`

| Archivo | Papel |
| :--- | :--- |
| `research.md` | Investigación de Fase 1: fuentes fechadas, datos, frameworks |
| `copy.md` | One-liners ≤ 12 palabras, acento por slide y prompts de fondos |
| `assets/bg_0*.jpg` | Fondos IA en 3:4 vertical, sujetos anclados abajo/lateral |
| `carousel.html` | Lienzo con los tokens de la línea de diseño |
| `slides/*.png` | PNG compilados (salida del motor, se recompilan sin pérdida) |

Los proyectos pueden vivir en `batches/<vuelta>/<slug>/` o directamente en `carousel-studio/<slug>/` — `batch_manager.py` busca en ambos sitios.

## Paneles del estudio

| Archivo | Papel |
| :--- | :--- |
| `ROTATION.md` | Rotación pentagonal de líneas: 1 carrusel por línea y vuelta |
| `BATCH_TRACKER.md` | Tablero de estado del lote semanal |
| `CURRENT_BATCH.json` | Estado interno del gestor (efímero, ignorado por git) |

## Reglas canónicas (inquebrantables)

1. **Proporción 3:4 (1080 × 1440 px)** — prohibido 4:5 o cuadrado.
2. **Márgenes de 96 px** y **Regla de 3 Colores**: `--surface-page` fondo, `--text-strong` lectura, `--accent` acento (1 palabra por slide + CTA).
3. **Cero texto en la IA:** fondos sin letras, números, logos ni botones.
4. **Fases separadas:** Research → Aprobación → Copy → Prompts visuales. Nunca compilar prompts antes de aprobar el copy.
5. El paquete de publicación sale por `../postprocessing/` (SOP: `../../vault/SOPs/funnels_publicacion.md`).
