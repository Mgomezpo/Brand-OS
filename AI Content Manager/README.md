# AI Content Manager — Short-Form Content Pipeline

A **local, Claude-Code-orchestrated** workflow that turns raw recordings into finished, on-brand
**9:16 short-form videos** (Reels / Shorts / TikTok) — no web app, no server. You drop a
recording in a folder, say "edit these," approve a quick plan, and finished shorts show up on
your phone via Google Drive. Raw footage archives itself; the pipeline stays clean.

It's the long-form video workflow from `references/pipeline-tutorial-transcript.md`, rebuilt for short-form with a disciplined
folder lifecycle and your **{{NOMBRE_MARCA}}** brand baked in.

## The daily loop

**Record → drop in `pipeline/00_input/` → tell Claude "edit these into shorts" → approve the
plan → collect from your phone.**

That's it. Behind the scenes the `/shortform` skill transcribes + trims (video-use), builds
{{NOMBRE_MARCA}}-branded motion graphics and renders (Hyperframes), then archives the raw and reports what's
on your phone.

## How it works

```
 you drop        video-use            PLAN GATE         Hyperframes + {{NOMBRE_MARCA}}        Google Drive
 a recording  ─► transcribe + trim ─► (you approve) ──► graphics + render 9:16 ─► → your phone
 00_input/       10_processing/        plan.md           20_output/                 (junction)
                                                            │
                          success → raw to 30_storage/      └ failure → _needs_attention/ + reason
```

- **Edit** — [video-use](https://github.com/browser-use/video-use): ElevenLabs Scribe word-level
  transcript, cuts filler/silence/retakes, subtitles.
- **Graphics + render** — [Hyperframes](https://github.com/heygen-com/hyperframes): HTML/GSAP
  compositions → deterministic 9:16 MP4.
- **Brand** — the **Brand Design System** in `brand/{{NOMBRE_MARCA}}/` (synced via `/design-sync`); graphics
  use its amber/dusk tokens by default.
- **Orchestration** — one skill, `.claude/skills/shortform/SKILL.md` (the "set of instructions").

## Folders

See [pipeline/README.md](pipeline/README.md). You only ever touch `00_input/` and `20_output/`.

## Setup

Full step-by-step (Windows): [specs/001-shortform-content-pipeline/quickstart.md](specs/001-shortform-content-pipeline/quickstart.md).

Short version:
1. `winget install OpenJS.NodeJS astral-sh.uv Gyan.FFmpeg`
2. `npx skills add heygen-com/hyperframes --all`
3. Install **video-use** into `%USERPROFILE%\.claude\skills\video-use` (ask Claude to run its
   `install.md`).
4. Transcription works out of the box with **free local Whisper** — no API key needed. (Optional:
   copy `.env.example` → `.env` and add an `ELEVENLABS_API_KEY` only if you want hosted Scribe.)
5. Connect output to phone: install **Google Drive for Desktop**, then junction the output:
   `mklink /J pipeline\20_output "G:\My Drive\Shorts"`.
6. Brand already synced to `brand/{{NOMBRE_MARCA}}/`; refresh anytime with `/design-sync`.

## Transcription options

This is a **talking-head** short-form editor: transcription only powers the filler/silence/retake
trimming — it never generates audio.

The pipeline defaults to **free local Whisper** (`faster-whisper`, on-device, **no API key, no
per-transcription cost**) — a bit slower, but private and free. Optional alternatives if you
prefer them:
- **ElevenLabs Scribe** — hosted, slightly better cut-point detection; opt in by setting
  `ELEVENLABS_API_KEY` and telling Claude "use ElevenLabs for transcription."
- **OpenAI Whisper API** — paid; opt in by setting `OPENAI_API_KEY`.

## Keeping it clean

- After you're happy with a piece, ask Claude to **clean `10_processing/<project>/`** — the
  finished MP4 is already in `20_output/` (and the raw in `30_storage/`), so the working folder
  is safe to clear. This keeps the pipeline tidy.
- `00_input/` should always show **only** recordings not yet done.
- Check `_needs_attention/` if something didn't process — it'll have a `.why.txt`.

## Cost note

Rendering is where Claude tokens go. The **plan-approval gate** is your main control — review the
plan carefully before approving so Claude doesn't build down the wrong path. Reuse **style
profiles** (`style-profiles/`) to make repeat formats cheaper and faster over time.

## Spec-driven docs

This project was built with Spec-Kit. The full spec, plan, and tasks live in
[specs/001-shortform-content-pipeline/](specs/001-shortform-content-pipeline/).
