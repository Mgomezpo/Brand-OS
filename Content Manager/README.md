# Content Manager — La Fábrica de Contenidos

Capa operativa del Brand OS: los **motores de producción** (video 9:16 y carrusel 3:4), la **mesa de publicación** y el **helper de embudos**. El cerebro instructivo vive en `vault/` (Obsidian) y la guía operativa completa para agentes de IA está en el `AGENTS.md` de la raíz (apartado *Motores del Sistema — Quick Start*).

## 🗺️ Mapa

| Carpeta | Papel | Comando de entrada |
| :--- | :--- | :--- |
| `video-studio/` | Motor de video 9:16 (1080 × 1920 px): HyperFrames + GSAP. Transcripción: Whisper local gratis por defecto; ElevenLabs Scribe opcional de pago. Proyectos en `video-studio/video-projects/<slug>/` | `npm run new-video -- <slug>` |
| `carousel-studio/` | Motor de carruseles 3:4 (1080 × 1440 px): fondos IA + HTML/CSS determinista + Playwright. Proyectos en `carousel-studio/batches/<vuelta>/<slug>/` | `python batch_manager.py status` |
| `postprocessing/` | Mesa de publicación: paquete por pieza con `caption.md` + `funnel.md` + `post.json` + `media-url.txt` | `python helper/zernio.py post-package postprocessing/<slug>` |
| `helper/` | Automatización: `zernio.py` (MCP + REST de Zernio, disparo comment-to-DM), `auto_source_image.py` (búsqueda ubicativa de imágenes) | ver docstring de cada script |

> `postprocessing/` NO es un estudio ni aquí se produce nada: solo organiza el paquete final listo para publicar (SOP: `vault/SOPs/funnels_publicacion.md`).

## ⚙️ Setup

1. **Video:** `cd video-studio && npm install` (Node ≥ 22) · transcripción gratis vía Whisper ya incluida en el kit (`hyperframes transcribe`); el `.env` solo se necesita si activas ElevenLabs u otro proveedor de pago (`video-studio/.env.example` → `.env`).
2. **Carrusel:** `cd carousel-studio && npm install` (Playwright + Chromium).
3. **Funnels (Zernio):** en el `.env` **de la RAÍZ del workspace** (`cp .env.example .env`) rellena `ZERNIO_API_KEY` + `ZERNIO_PROFILE_ID` + `ZERNIO_ACCOUNT_ID` — `zernio.py` lee el `.env` raíz. Primeras 2 cuentas conectadas gratis.

## 🔗 Reglas transversales

- Formatos canónicos: **3:4 (1080 × 1440 px)** carruseles · **9:16 (1080 × 1920 px)** video. Prohibido 4:5 o cuadrado.
- Los fondos IA se piden **100% limpios de texto**; la tipografía se estampa en código (HTML/CSS determinista).
- Tokens de marca: `design-system/tokens.css` + la línea activa en `vault/Conceptos/design_lines/`.
- El vault es 100% Markdown instruccional: MP4s y renders masivos nunca entran a `vault/` (los ignora git por diseño).
