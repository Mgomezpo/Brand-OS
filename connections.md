# Connections

Registry of every system and production engine your Brand OS can reach. Pre-configured for local rendering engines and expandable as you wire third-party APIs and MCP servers. Run `/brand-audit` to verify system reachability and tool health.

| # | Domain | Tool / Engine | Mechanism | Auth | Status / Location |
|---|---|---|---|---|---|
| 1 | 3:4 Carousel Engine | Playwright (Node.js) | script + headless | local | `Content Manager/carousel-studio/capture.cjs` |
| 2 | 9:16 Video Engine | HyperFrames + GSAP | script + render | local | `Content Manager/video-studio/` |
| 3 | Transcripción & Audio | ElevenLabs Scribe / Whisper | script + API | api-key / local | `Content Manager/video-studio/scripts/transcribe-elevenlabs.mjs` |
| 4 | Silence & Mistake Cuts | Video Studio cut-silences / cut-mistakes | skill + script | local | `Content Manager/video-studio/.claude/skills/` |
| 5 | AI Visual Backgrounds | Recraft / FLUX / Midjourney | prompt pipeline | api / manual | Clean AI prompts (zero text), CSS compositing |
| 6 | Funnel & DM Automation | Zernio (Comment-to-DM) | mcp / webhook | api-key | `Content Manager/helper/zernio.py` |
| 7 | Social Distribution | Zernio (Posts & Queue) | mcp / script | api-key | `Content Manager/helper/zernio.py` |
| 8 | Voice Narration | ElevenLabs Scribe | script / api | api-key | `Content Manager/video-studio/scripts/transcribe-elevenlabs.mjs` |
| 9 | Design System Tokens | Deterministic CSS | native local | local | `design-system/tokens.css` & `index.css` |
| 10 | Brand Brain Knowledge | Obsidian Markdown Vault | native local | local | `vault/` (7 core concept files) |

**Mechanism options:**
- `local`: Native script running locally in the workspace (Playwright, Python, CSS).
- `mcp`: Model Context Protocol server integrated into Claude Code, Codex, or Antigravity.
- `script`: Python or Node.js script hitting an external REST API (located in `Content Manager/`).
- `export`: CSV/JSON batch dump pipeline for multi-slide asset ingestion.
- `prompt pipeline`: Structured prompt engineering for deterministic UI/visual asset separation.
- `not yet connected`: Optional integration ready to be configured.

When wiring a new service, record its configuration, credentials schema, and endpoint conventions in `vault/Repos.md` so future agent runs retain persistent access.
