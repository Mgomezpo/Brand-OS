---
name: using-brand-os-skills
description: Start here. Entry-point orchestration guide for Brand OS. Maps the workspace (Obsidian vault = brand brain, design-system = canonical visual source, Content Manager studios = factories), routes every task to its skill, SOP, or engine command, and states the immutable guardrails. Load before any content production, whenever unsure what to run, or after cloning this OS.
---

## Qué es Brand OS (mapa del OS)

Obsidian arriba, fábrica debajo:

| Anillo | Dónde | Rol |
| :--- | :--- | :--- |
| 🧠 Cerebro | `vault/` | 100% Markdown de instrucciones: Brand Brain (`Conceptos/`), frameworks y matriz de formatos (`Estrategia/`), SOPs canónicos (`SOPs/`), tableros (`00_Dashboard.md`, `Board.md`, `Findings.md`, `Repos.md`) |
| 🎨 Fuente visual | `design-system/` | Tokens canónicos (`tokens.css`), estilos deterministas de slide 3:4 (`index.css`), especificación (`DESIGN_SYSTEM.md`) |
| 🏭 Fábrica | `Content Manager/` | `carousel-studio/` (3:4) · `video-studio/` (9:16) · `postprocessing/` (mesa de publicación) · `helper/` (embudo Zernio) |
| 📖 Manual maestro | `AGENTS.md` / `CLAUDE.md` | La guía operativa completa — este skill **enruta**, el manual manda |

**Regla de oro:** los SOPs del vault prevalecen sobre cualquier skill o lista de este archivo. Números canon: carrusel **3:4** (canvas 1080 × 1440 px, export 2× = 2160 × 2880) · video **9:16** (1080 × 1920 px) · márgenes 96 px · Regla de 3 Colores (1 solo acento por slide + CTA) · fondos IA 100% sin texto · research → 🛑 aprobación → copy → prompts.

## Los tres anillos de skills

1. **Raíz (guía + marca):** `.claude/skills/` — este skill guía, más `brand-onboard`, `brand-audit`, `grill-me`, `level-up` y `script-shortform`. Cargan en toda sesión abierta en la raíz.
2. **carousel-studio (operador):** `Content Manager/carousel-studio/.claude/skills/carousel-batch/` — produce el batch 3:4. Úsala abriendo sesión dentro del estudio, o simplemente **leyendo su `SKILL.md`** (son Markdown: leerlo = cargarlo).
3. **video-studio (kit vendido HeyGen/HyperFrames):** `Content Manager/video-studio/.claude/skills/` — edición de video 9:16. Se usa desde ese directorio (su guía: `Content Manager/video-studio/README.md` + `docs/`).

## Router de tareas

| Quiero… | Ruta |
| :--- | :--- |
| Montar una marca nueva / pivotar posicionamiento | `/brand-onboard` — 8 bloques; el **Bloque 8 diseña y enchufa el Sistema de Diseño** (a punta de preguntas de vibe, sin pedir HEX) |
| Producir el batch semanal de carruseles 3:4 | Sesión en `Content Manager/carousel-studio/` → skill `carousel-batch` · canon: `vault/SOPs/carousel_batch.md` + `vault/SOPs/carousels.md` · estado: `python batch_manager.py status` |
| Redactar un guion 9:16 para grabar | `/script-shortform` |
| Editar video 9:16 con footage real | `Content Manager/video-studio/` → `npm run new-video -- <slug>` + kit de skills (`/short-form-edit`, `/cut-silences`, `/cut-mistakes`…) |
| Stress-test de un ángulo o creencia | `/grill-me` |
| Auditar la integridad del sistema | `/brand-audit` (placeholders 0, ratios 3:4/9:16, márgenes, wiki-links) |
| Retro semanal / aprendizajes compuestos | `/level-up` → `vault/Findings.md` + `vault/Repos.md` |
| Publicar | `Content Manager/postprocessing/<slug>/` → `Content Manager/helper/zernio.py post-package` (Zernio) |

## Orden de lectura del cerebro (antes de proponer o escribir contenido)

1. `vault/Conceptos/brand_core.md` → quién es la marca.
2. `vault/Conceptos/user_persona.md` → a quién le habla.
3. `vault/Conceptos/positioning.md` + `offer.md` → qué vende (keyword de DM incluida).
4. `vault/Conceptos/tone_of_voice.md` → cómo habla (lista negra anti-AI-slop).
5. `vault/Conceptos/content_pillars.md` → de qué habla y línea activa.
6. `vault/Conceptos/visual_identity.md` → cómo se ve (3:4 y 9:16).
7. `vault/Conceptos/proof_bank.md` → qué cifras puede citar (cero inventadas).

## Reglas Inmutables (resumen operativo)

1. El vault es 100% Markdown de instrucciones: sin MP4s ni renders pesados dentro.
2. Las piezas se producen **dentro de su estudio**; `postprocessing/` solo recibe piezas terminadas.
3. Ratio canónico carrusel 3:4 (1080 × 1440, export 2×) — prohibido 4:5 o cuadrado. Video 9:16 (1080 × 1920).
4. Cero texto en imágenes IA: la tipografía se estampa en HTML/CSS determinista.
5. Fases separadas: research puro → aprobación → copy → prompts. Prohibido adelantar fase.
6. Tokens del design-system: **solo se regeneran vía el Bloque 8 de `/brand-onboard`**; jamás editar `tokens.css` a mano.
7. Cifras y casos citables solo del `proof_bank.md`.

## Mantenimiento del sistema de skills

- Raíz + studios propios (carousel): `python scripts/sync-skills.py` — espejo `.claude/skills` ↔ `.agents/skills`, con `--check` (exit 1 si hay drift).
- Kit vendido de video-studio: `npm run sync:skills` **desde su directorio** — nunca mezclar alcances.
- Verificación global: `/brand-audit`.
