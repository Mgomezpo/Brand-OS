# Connections

Registry of every system and production engine your Brand OS can reach. Pre-configured for local rendering engines and expandable as you wire third-party APIs and MCP servers. Run `/brand-audit` to verify system reachability and tool health.

| # | Domain | Tool / Engine | Mechanism | Auth | Status / Location |
|---|---|---|---|---|---|
| 1 | 3:4 Carousel Engine | Playwright (Node.js) | script + headless | local | `AI Content Manager/carousel-studio/capture.cjs` |
| 2 | 9:16 Video Engine | HyperFrames + GSAP | script + render | local | `AI Content Manager/video-studio/` |
| 3 | Audio & Captions | Whisper (OpenAI / Local) | script + CLI | local / api | `AI Content Manager/video-studio/tools/whisper.py` |
| 4 | AI Visual Backgrounds | Recraft / FLUX / Midjourney | prompt pipeline | api / manual | Clean AI prompts (zero text), CSS compositing |
| 5 | Funnel & DM Automation | Zernio (Comment-to-DM) | mcp / webhook | api-key | `AI Content Manager/helper/zernio/` |
| 6 | Social Distribution | Metricool / Zernio Queue | mcp / script | api-key | Multi-platform scheduler & tracking |
| 7 | Voice Narration | ElevenLabs / Cartesia | script / api | api-key | Voice cloning for 9:16 shortform reels |
| 8 | Design System Tokens | Deterministic CSS | native local | local | `design-system/tokens.css` & `index.css` |
| 9 | Brand Brain Knowledge | Obsidian Markdown Vault | native local | local | `vault/` (7 core concept files) |

**Mechanism options:**
- `local`: Native script running locally in the workspace (Playwright, Python, CSS).
- `mcp`: Model Context Protocol server integrated into Claude Code, Codex, or Antigravity.
- `script`: Python or Node.js script hitting an external REST API (located in `AI Content Manager/`).
- `export`: CSV/JSON batch dump pipeline for multi-slide asset ingestion.
- `prompt pipeline`: Structured prompt engineering for deterministic UI/visual asset separation.
- `not yet connected`: Optional integration ready to be configured.

When wiring a new service, record its configuration, credentials schema, and endpoint conventions in `vault/Repos.md` so future agent runs retain persistent access.
