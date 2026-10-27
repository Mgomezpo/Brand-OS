# 📓 NOTEBOOK — Runbook de Brand OS (skills + conexiones)

> **Propósito:** una sola página con todo lo que una persona necesita para **correr este OS**: prerequisitos, orden de arranque, inventario completo de skills, y el mapa de conexiones con su **política de costo** (gratis por defecto, servicios de pago como placeholder opcional).
> **Compañero de:** `connections.md` (registry técnico) · `AGENTS.md` (manual operativo) · `vault/SOPs/` (canon).
> Formato Markdown a propósito: es un *notebook de operación*, y así los agentes lo leen y grep-ean igual que cualquier otro documento del OS.

---

## 🚀 1. Requisitos y primera corrida

| Requisito | Para qué | Costo |
|---|---|---|
| **Node ≥ 22** | video-studio (HyperFrames) + carousel-studio (Playwright) | gratis |
| **Python 3.11+** | `batch_manager.py`, `scripts/sync-skills.py` | gratis |
| **ffmpeg** (binario en PATH) | cortes de audio/video en el video-studio | gratis |
| Obsidian (opcional) | leer el `vault/` como grafo de conocimiento | gratis |
| `.env` keys | **solo si activas servicios de pago** (Zernio, ElevenLabs) | según plan |

**Orden de arranque:**

```bash
cd "Content Manager/video-studio" && npm install       # solo la primera vez
cd "Content Manager/carousel-studio" && npm install    # Playwright + Chromium
```

1. `/using-brand-os-skills` — la guía de entrada (mapa del OS + router de tareas).
2. `/brand-onboard` — 8 bloques; **el Bloque 8 genera tu Sistema de Diseño** y llena las plantillas intencionales (`{{NOMBRE_MARCA}}`, `ROTATION.md`, `design_lines/`…). ✅ *Esas plantillas están vacías a propósito: la idea del brand interview es llenarlas.*
3. `/brand-audit` — el chequeo de nacimiento (crea la carpeta `audits/` y salva el primer reporte fechado).

## 🧰 2. Inventario completo de skills (22)

### Raíz — `.claude/skills/` (espejadas a `.agents/` por `scripts/sync-skills.py`)

| Skill | Rueda qué | Cuándo |
|---|---|---|
| `using-brand-os-skills` | **Guía de orquestación** — mapa de anillos, orden de lectura del Brand Brain, router de tareas | Siempre, es la entrada |
| `brand-onboard` | Entrevista de 8 bloques; genera brand brain + sistema de diseño y llena las plantillas | Día 1 / pivotar |
| `brand-audit` | 6 checks (placeholders, ratios 3:4/9:16, 96px, wiki-links…) → reporte en `audits/YYYY-MM-DD-*` | Semanal o pre-batch |
| `script-shortform` | Guiones 9:16 en 4 movimientos (hook ≤12 palabras → dolor → mecanismo → CTA) | Antes de grabar |
| `grill-me` | Stress-test adversarial de ángulos contra el Brand Core | Antes de redactar |
| `level-up` | Calibración semanal → `vault/Findings.md` + `vault/Repos.md` | Retro semanal |

⚠️ **`carousel-batch` NO vive en raíz** — es residente del carousel-studio (cae en el grupo siguiente).

### `Content Manager/carousel-studio/.claude/skills/` — 1 skill residente

| Skill | Rueda qué |
|---|---|
| `carousel-batch` | 3 fases (research → 🛑 copy → 🛑 prompts+compilación), prompts por `line-<id>.md`, compila con `batch_manager.py status/compile` |

### `Content Manager/video-studio/.claude/skills/` — 15 skills del kit vendido HeyGen/HyperFrames

| Grupo | Skills | Para qué |
|---|---|---|
| Pipeline de edición | `cut-silences` → `cut-mistakes` → `short-form-edit` | Cortar, pulir y editar el raw 9:16 (requiere transcript) |
| Alternativa | `edit-video` | Edición general no-shortform |
| Creación | `make-a-video`, `video-storytelling`, `motion-showreel`, `style-library` | Videos motion, estilos visuales, showreels y storytellings |
| Legacy | `short-form-video` | Scaffold viejo 10–30s (prefiere `short-form-edit`) |
| Plataforma HyperFrames | `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `hyperframes-video-beats`, `gsap`, `website-to-hyperframes` | Composiciones, CLI, registry, beats, GSAP, portear un sitio |

**Mantenimiento:** `python scripts/sync-skills.py` (raíz + carousel-studio) · `npm run sync:skills` dentro de video-studio (kit vendido) — nunca mezclar alcances.

## 🔌 3. Mapa de conexiones y política de costo

> **Política del dueño:** correr **gratis por defecto** (Whisper local) y dejar los servicios de pago como **placeholder opcional** que se activa solo cuando lo pida y ponga su key.

| Conexión | Para qué la usamos | Default (gratis) | Placeholder (pago) |
|---|---|---|---|
| **Transcripción** | guion/raw → `transcript.json` con timestamps por palabra (alimenta cortes y captions) | **Whisper local** vía la CLI del kit: `hyperframes transcribe` (whisper.cpp, **sin API key**) | ElevenLabs Scribe u OpenAI/Groq — solo si el usuario paga (`scripts/transcribe-elevenlabs.mjs`) |
| **Voz narrada (TTS)** | voz digital para voiceovers del video 9:16 | **Grabar voz real** (cero costo: la voz de la marca ES el activo) | **ElevenLabs TTS — placeholder**: se conecta por API cuando decidas activarlo (hoy ⏳ no está wired) |
| **Fondos IA (imágenes)** | fondos 3:4 100% limpios de texto para los carruseles | **Manual / prompt pipeline**: los prompts salen del skill + `design_lines/` y la imagen se pega en `batches/<vuelta>/<slug>/assets/` | Recraft / FLUX / Midjourney por API si quieres automatizar |
| **Render 3:4 (PNG)** | compilar `carousel.html` → `slides/*.png` (2160×2880) | **Playwright + Chromium** (local, gratis, se instala con `npm install`) | — |
| **Render/edición 9:16** | composiciones, overlays, preflight, export | **HyperFrames + GSAP + ffmpeg** (local, gratis) | — |
| **Publicación & embudo** | comment-to-DM + cola de posts | — | **Zernio** (`helper/zernio.py post-package`) — tier gratuito inicial: 2 cuentas |
| **Referentes (roadmap)** | ingesta estándar de `vault/Estrategia/Referentes-y-Benchmarking/` | copiar/pegar manual (hoy) | **Apify** — declarado en `connections.md` fila 11, aún no conectado |

> **Regla transversal:** aunque el kit vendido de video diga "ElevenLabs es el default del kit", en este Brand OS **prevalece la política del OS**: ruta gratis por defecto, y el proveedor de pago solo entra si el usuario lo pide y coloca su key en `video-studio/.env`.

## 🗂️ 4. Estado propio del usuario (no son residuos)

- **`Content Manager/carousel-studio/ROTATION.md`** — documento de **estado propio del dueño**: su mecanismo de rotación de carruseles (la "vuelta" activa = qué línea toca ahora). Está en estado plantilla (checkboxes sin marcar, `{{line_1}}`…) hasta que el onboarding o el usuario lo llenen. **Es un documento que se necesita; no borrarlo ni fusionarlo jamás.**
- **Plantillas del vault y `design-system/` (`{{NOMBRE_MARCA}}`, `{{HEX_…}}`, etc.)** — intencionales: la entrevista `/brand-onboard` las llena.
- **`audits/`** — todavía no existe porque nadie ha corrido `/brand-audit`: se crea en la primera corrida y ahí se acumulan los reportes fechados (`YYYY-MM-DD-brand-audit.md`) con las 6 verificaciones (placeholders, ratios, márgenes, pruebas reales, wiki-links, anti-AI-slop).
- **`CURRENT_BATCH.json`** — se genera con `batch_manager.py new-week`; apunta al lote vivo del batch.
