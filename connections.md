# Connections — servicios externos del Brand OS

> **Qué es:** el registro de las conexiones del Brand OS con elementos de **afuera** (APIs y servicios) y su estado de conexión. Los motores **locales** (Playwright, HyperFrames, GSAP, ffmpeg, tokens CSS, vault) NO son conexiones: están documentados en `AGENTS.md` (*Motores del Sistema*).
> **Regla de conexión:** una conexión está **conectada** solo si su llave está dentro de `.env` (cópialo desde `.env.example`). **Sin llave = no conectada**, y el flujo corre con su default **gratis**.
> **Defaults gratis del OS:** transcripción con Whisper local (`hyperframes transcribe`), voz narrada grabada a mano, imagen de fondo pegada a mano — el workspace corre end-to-end **sin costo ni credenciales**.

| # | Servicio externo | Para qué en este OS | Estado | Sin llave… | Llave(s) en `.env` |
| :-: | :--- | :--- | :-: | :--- | :--- |
| 1 | **ElevenLabs Scribe** (transcripción) | transcript premium para cortes/captions de video 9:16 | ❌ **placeholder** | transcripción **gratis** con Whisper local | `ELEVENLABS_API_KEY` |
| 2 | **ElevenLabs TTS** (voz digital) | voiceover sintético opcional para videos | ⏳ **no wired** | grabar **voz real** (default del OS) | reutiliza `ELEVENLABS_API_KEY` |
| 3 | **Nano Banana / Gemini CLI** (fondos IA) | generar fondos 3:4 por CLI en vez de pegar a mano | ❌ **placeholder** | prompts del skill + imagen pegada a `batches/<vuelta>/<slug>/assets/` | `GEMINI_API_KEY` |
| 4 | **Zernio** (publicación + embudo) | cola de posts y comment-to-DM (`Content Manager/helper/zernio.py`) | ❌ **llaves vacías** | publicación manual | `ZERNIO_API_KEY` · `ZERNIO_PROFILE_ID` · `ZERNIO_ACCOUNT_ID` |
| 5 | **Apify** (roadmap) | ingesta estándar de `vault/Estrategia/Referentes-y-Benchmarking/` | ❌ **roadmap** | copiar/pegar manual | `APIFY_API_TOKEN` |

## Gobernanza del repo GitHub (blindaje, 2026-10-27)

- **Repo:** `Mgomezpo/Brand-OS` (público, base plantilla). **Branch protection en `main`:** sin force push, sin borrado, aplicable a admin (`enforce_admins`). Los agents y humanos con push normal a `main` siguen trabajando igual.
- **Interaction limits `collaborators_only`:** nadie fuera de colaboradores puede abrir PRs, issues ni comentar. GitHub expira este límite por diseño → se renueva **1 mes** cada vez con la tarea local `BrandOS-Renovar-Interacciones-GitHub` (día 1 de cada mes, 09:03) que corre `C:\Users\mgome\.brand-os\renew-interaction-limits.cmd` usando el token `gh` del keyring. Log: `C:\Users\mgome\.brand-os\renewal.log`.
- **Renovación manual:** `schtasks /Run /TN BrandOS-Renovar-Interacciones-GitHub`. Alternativa remota: `gh workflow run interactions-keeper.yml --repo Mgomezpo/Brand-OS` (solo hace el trabajo si existe el secret opcional `GH_ADMIN_TOKEN`; el `GITHUB_TOKEN` de Actions no tiene permiso `administration`).

## Al activar una conexión

1. Llena la llave en `.env` (nunca la subas a git).
2. Marca el Estado aquí como ✅ conectado.
3. Documenta la integración (endpoint, plan, límites) en `vault/Repos.md` para que las próximas sesiones la recuerden.

> El kit vendido de video trae sus propias llaves opcionales (`KIE_API_KEY`, `GEMINI_API_KEY`…) en `Content Manager/video-studio/.env.example` — úsalas **solo** si corres esos flujos del kit; no forma parte del costo base de este OS.
