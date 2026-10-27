---
name: script-shortform
description: Write high-retention 9:16 shortform video scripts (30-60s) for Instagram Reels, TikTok, and YouTube Shorts. Implements the 4-movement architecture, hook under 12 words, double visual encoding, safe zone rules, and sound cues.
---

## What this skill does

Generates production-ready shortform video scripts in the canonical **9:16 aspect ratio (1080 × 1920 px)**. Every script coordinates spoken narration, on-screen text overlays, camera framing, and audio sound effects to ensure maximum viewer retention and comment-to-DM conversion.

## The 4-Movement Script Architecture

Each script must be formatted in a two-column or interleaved structure (Audio / Narration vs. Visual / Direction) following these 4 movements:

### Movement 1: The Hook (0:00 - 0:03) — Maximum 12 Words
- **Goal:** Instant pattern interrupt + cognitive friction.
- **Rules:** Must challenge a common assumption or present an unresolved question.
- **Visuals:** Fast camera snap, sharp prop movement, or bold on-screen title in the top third (avoiding UI icons on right edge).
- **Sound:** Crisp SFX (whoosh, hit, vinyl stop, or subtle bass drop).

### Movement 2: The Scene of Pain / Tension (0:03 - 0:15)
- **Goal:** Relatability and validation of the viewer's current struggle.
- **Source:** Pull the exact scenario from `vault/Conceptos/user_persona.md`.
- **Narration:** Concise, conversational sentences. No jargon or filler.
- **Visuals:** B-roll demonstration of the pain, screen recording of the error, or close-up talking head.

### Movement 3: The Unique Mechanism (0:15 - 0:40)
- **Goal:** Deliver the breakthrough insight and the named framework.
- **Source:** Cites verified data from `vault/Conceptos/proof_bank.md` and the mechanism from `vault/Conceptos/positioning.md`.
- **Narration:** Step 1, Step 2, Step 3. Plain language.
- **Visuals:** Kinetic typography, diagrams, or UI walkthrough with highlighted bounding boxes.

### Movement 4: The Actionable Step & CTA (0:40 - 0:55)
- **Goal:** Direct viewer to trigger the automated funnel.
- **Source:** Pull the exact DM keyword from `vault/Conceptos/offer.md`.
- **Script:** Clear instruction: *"Comenta `[KEYWORD]` y te envío el acceso directo a tu DM."*
- **Visuals:** Large text overlay showing the keyword + arrow pointing to the comment button.

---

## Safe Zone & Visual Framing Rules

- **Aspect Ratio:** Strict 9:16 (1080 × 1920 px).
- **Safe Zone:** Keep key faces and critical typography between Y=320px and Y=1500px.
- **Avoid Dead Zones:** Do not place captions on the bottom 420px (covered by username, sound title, and captions on Reels/TikTok) or the right 140px (covered by like, comment, share icons).
- **Caption Pacing:** Synchronized with the studio transcript in `Content Manager/video-studio/` (ElevenLabs Scribe is the default engine; honor the user's chosen transcription provider). 1-3 words per burst.
