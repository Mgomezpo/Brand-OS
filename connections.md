# Connections

Registry of every system and production engine your Brand OS can reach. Pre-configured for local rendering engines and expandable as you wire third-party APIs and MCP servers. Run `/brand-audit` to verify system reachability and tool health.

> 🔑 **Autenticación:** copia `.env.example` → `.env` en la raíz y llena SOLO las llaves que actives (revisa `vault/Repos.md` si necesitas convenciones). **Sin llave = `not yet connected`**; el default del OS es la ruta gratis (Whisper local, imagen manual, render local), así que la plantilla corre end-to-end **sin costo ni credenciales**.

| # | Domain | Tool / Engine | Mechanism | Auth | Status / Location |
|---|---|---|---|---|---|
| 1 | 3:4 Carousel Engine | Playwright (Node.js) | script + headless | local | `Content Manager/carousel-studio/capture.cjs` |
| 2 | 9:16 Video Engine | HyperFrames + GSAP | script + render | local | `Content Manager/video-studio/` |
| 3 | Transcripción | Whisper local (whisper.cpp) — **default gratis** / ElevenLabs Scribe — opcional de pago | CLI local / API | local sin key / api-key | gratis: `hyperframes transcribe` · pago: `scripts/transcribe-elevenlabs.mjs` |
| 4 | Silence & Mistake Cuts | Video Studio cut-silences / cut-mistakes | skill + script | local | `Content Manager/video-studio/.claude/skills/` |
| 5 | AI Visual Backgrounds | Recraft / FLUX / Midjourney | prompt pipeline | api / manual | Clean AI prompts (zero text), CSS compositing |
| 6 | Funnel & DM Automation | Zernio (Comment-to-DM) | mcp / webhook | api-key | `Content Manager/helper/zernio.py` |
| 7 | Social Distribution | Zernio (Posts & Queue) | mcp / script | api-key | `Content Manager/helper/zernio.py` |
| 8 | Voz Narrada (TTS) | **Grabar voz real (default gratis)** · ElevenLabs TTS como **placeholder** pendiente de activar | manual / API | micrófono / api-key | placeholder no wired: activar con key en `video-studio/.env` y documentar en `vault/Repos.md` |
| 9 | Design System Tokens | Deterministic CSS | native local | local | `design-system/tokens.css` & `index.css` |
| 10 | Brand Brain Knowledge | Obsidian Markdown Vault | native local | local | `vault/` (Brand Brain + SOPs + hallazgos) |
| 11 | Referentes Ingesta (roadmap) | Apify (web scraping) | script / api | api-key | `not yet connected` — estandarizará la ingesta de `vault/Estrategia/Referentes-y-Benchmarking/` |

**Mechanism options:**
- `local`: Native script running locally in the workspace (Playwright, Python, CSS).
- `mcp`: Model Context Protocol server integrated into Claude Code, Codex, or Antigravity.
- `script`: Python or Node.js script hitting an external REST API (located in `Content Manager/`).
- `export`: CSV/JSON batch dump pipeline for multi-slide asset ingestion.
- `prompt pipeline`: Structured prompt engineering for deterministic UI/visual asset separation.
- `not yet connected`: Optional integration ready to be configured.

## 🔑 Llaves por conexión (`.env`)

| Conexión (#) | Variable(s) en `.env` | Comportamiento si la llave está vacía |
|---|---|---|
| 3 Transcripción | `ELEVENLABS_API_KEY` · `OPENAI_API_KEY` · `GROQ_API_KEY` | corre **gratis** con Whisper local (`hyperframes transcribe`) |
| 8 Voz narrada (TTS) | reutiliza `ELEVENLABS_API_KEY` | voz real grabada por micrófono (placeholder no wired) |
| 5 Fondos IA | `RECRAFT_API_KEY` | imagen pegada a mano desde `batches/<vuelta>/<slug>/assets/` |
| 6–7 Zernio | `ZERNIO_API_KEY` · `ZERNIO_PROFILE_ID` · `ZERNIO_ACCOUNT_ID` | publicación/embudo manual |
| 11 Apify | `APIFY_API_TOKEN` | ingesta de referentes manual (roadmap) |

Las llaves del kit de video (`KIE_API_KEY`, `GEMINI_API_KEY` y demás) viven en `Content Manager/video-studio/.env.example`.

When wiring a new service, record its configuration, credentials schema, and endpoint conventions in `vault/Repos.md` so future agent runs retain persistent access.
