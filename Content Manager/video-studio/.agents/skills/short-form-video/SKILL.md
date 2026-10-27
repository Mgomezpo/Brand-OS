---
name: short-form-video
description: Apply the legacy face-mode, scene-overlay, and karaoke-caption patterns. Use only when explicitly requesting this legacy scaffold. For new reels, Shorts, or short advertisements, use short-form-edit.
---

# Short-Form Vertical Video (Hyperframes)

Short-form = 1080x1920 vertical, 10ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“30s, talking-head face + motion-graphic scene overlays + karaoke captions. Everything in this skill is distilled from a legacy iteration autopsy (v1 ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ v4) and is preserved as a standalone scaffold for legacy-style builds. Use `short-form-edit` for new recordings.

**Always invoke `/hyperframes` first.** This skill sits on top of it ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â it does not replace the framework rules (`data-*` attributes, `window.__timelines`, composition structure). Those are non-negotiable regardless of the format.

## When this skill fires

- Applying this legacy scaffold to one of your own short compositions.
- Explicitly requesting this legacy four-layer scaffold.

## The playbook (high-level)

1. **Audio is source of truth.** Edit audio FIRST (cut retakes, pauses). Save as `<name>-edit.mp4`. Measure exact duration with `ffprobe` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â this is the composition's `data-duration`.
2. **Transcribe the edited audio** with the root `scripts/transcribe-elevenlabs.mjs` helper (ElevenLabs Scribe), a student-selected alternative normalized per `docs/TOOLS-AND-API-KEYS.md`, or if retiming an existing build with a `shift()` function in captions, keep the existing captions and just shift scene starts.
3. **Author scene boundaries in edited-time** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â NEVER mix original-time and edited-time anchors in the same file. See "Audio-sync protocol" below.
4. **Build the composition scaffold** (4 layers: ambient-bg, seam-treatment, captions, face) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â see "Composition scaffold" below.
5. **Author scenes with LOCAL offsets** relative to each scene's `data-start`. Each scene is its own sub-composition under `compositions/scene<N>-<label>.html`.
6. **Lint ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ draft render ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ word-exact frame verification ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ final render.** This is the verification gate. Never skip step 3 (frame verification).

## Composition scaffold (the 4 always-on layers)

Every short-form vertical has these four sub-compositions under `compositions/`, loaded on shared tracks:

```
index.html (root, 1080x1920, data-composition-id="main")
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ ambient-bg.html        track-index="3" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â radial gradient + drift grid + particles + vignette
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ face-wrapper + <video> track-index="0" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â talking head (see face-mode choreography)
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ seam-treatment.html    track-index="5" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â feathers y=960 edge (bottom-half scenes only)
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ scene1-<label>.html    track-index="1" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â scene overlays (back-to-back, no gaps)
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ scene2-<label>.html    track-index="1"
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬ÂÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ captions.html          track-index="2" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â karaoke captions, word-synced
```

- `data-duration` is identical across root, ambient-bg, seam-treatment, face-video, face-audio, captions. Only scene overlays change over time.
- `<audio>` for the face is a SEPARATE element (mixer needs it), never use the video's own audio track.
- `class="clip"` goes on timed divs ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â NEVER on `<video>` or `<audio>`.

## Face-mode choreography (the signature move of short-form)

The face lives in a wrapper div sized at the source's native landscape (1920x1080). GSAP animates the WRAPPER (never the video element ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â animating `<video>` dimensions freezes frames).

Two modes:

```js
const BOTTOM     = { x: 0,       y: 1136, scale: 0.5625 }; // bottom-half, full landscape visible
const FULLSCREEN = { x: -1166.5, y: 0,    scale: 1.7778 }; // cropped-cover, fills 1080x1920
const MODE_DUR = 0.32;
```

`BOTTOM` renders the 1920x1080 source at 1080x607.5 centered in the bottom 960px. `FULLSCREEN` crops horizontally to fill the portrait frame.

**Transition 0.15s BEFORE the new scene's content lands**, using `ease: "expo.inOut"`:

```js
[
  { t: <scene-4-start>, mode: FULLSCREEN },
  { t: <scene-5-start>, mode: BOTTOM },
  ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦
].forEach(({ t, mode }) => {
  mainTl.to("#face-wrapper", { ...mode, duration: MODE_DUR, ease: "expo.inOut" }, t - 0.15);
});
```

A face that snaps modes instantly is the single most jarring frame in a vertical video. Always interpolate.

### Face grading (every short, no exceptions)

```css
#face-video {
  filter: contrast(1.08) saturate(1.08) brightness(0.97);
}
```

Plus a subtle 1.00 ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ 1.025 Ken Burns zoom over the full duration (`ease: "none"`) and a side-vignette `::after` pseudo-element so the face sinks into the surrounding navy instead of butting against a razor edge.

### Seam treatment (required for bottom-half scenes)

A navyÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢transparent gradient band (60ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“100px) at y=960 plus a 2px accent scan line with soft glow. Draw it AFTER the face so it sits on top; full-screen scenes will cover it when they take over. Razor-sharp y=960 cuts are the #2 tell for AI-edited content (after background flatness).

## Audio-sync protocol (DO NOT skip)

**Problem:** if audio is edited (retakes/pauses removed), timestamps in the source transcript no longer match the edited video. Scene starts authored in original-time will fire late.

**The rule:** ALL timing lives in edited-time. Never mix.

**Verification procedure for any short-form retime:**

1. Measure both audio files:
   ```bash
   ffprobe -v error -show_entries format=duration -of csv=p=0 assets/original.mp4
   ffprobe -v error -show_entries format=duration -of csv=p=0 assets/<name>-edit.mp4
   ```
   Difference = total cut time.
2. If using a `shift()` function in `captions.html` to map transcript words, treat that as the source of truth. The map `shift(originalTime) = editedTime` applies to EVERY scene `data-start` too.
3. Scene internal offsets (inside `compositions/sceneN.html`) are LOCAL relative to the scene's `data-start`. If a scene's parent `data-start` is correct in edited-time, internal offsets stay correct WITHOUT modification ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â UNLESS a scene straddles a cut, in which case both the parent duration AND internal offsets shift.
4. Face-mode transition array times MUST use edited-time. They are NOT automatically shifted.

**Plan format for retimes** (use this table structure every time):

| Scene | Current start | Current dur | New start | New dur | Rationale |
|-------|---------------|-------------|-----------|---------|-----------|
| ...   | ...           | ...         | ...       | ...     | ...       |

Then the face-mode array, then any internal-offset changes, then frame-verification list.

## Scene authoring

One scene = one sub-composition file. Scenes sit on the same `data-track-index` back-to-back (no gaps). Inside each scene:

- `data-duration` matches the parent's slot exactly
- All GSAP anchors are LOCAL (0-based from scene start)
- Use `tl.set({}, {}, <data-duration>)` to pad the timeline so GSAP `tl.duration()` matches `data-duration`

### Scene pacing rules (from the 10 principles)

- **No dead frames.** Every 100ms has ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¥1 animating element. Offset first entrance 0.1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“0.3s, not t=0.
- **Payoff ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¥ 1s hold.** The "big reveal" of the scene (stamp, number lock, punchline) must have ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¥1s on screen, ideally 1.5s. Budget scenes by reveal time, not total time.
- **Motion through full duration.** If entrance anims all land by local 2s on a 4s scene, add secondary motion: underline sweeps, checkmark pops, ambient drift on cards, small oscillating glows on pills. Dead pacing = swipe-away.
- **Vary eases.** At least 3 different eases per scene across entrances.
- **One jaw-dropper per 5s of runtime.** Typography slam, glitch/chromatic reveal, whip-pan, audio-sync slam. Without these, the video reads as "labeled talking head" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â correct but forgettable.

## Captions (karaoke style)

- Montserrat 900, 46ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“58px (for 1080 width), 100% white base
- Active word: scale-1.08 pop + color change to accent (`#37bdf8` for the brand, adapt to brand)
- Stroke via layered `text-shadow`, NEVER `-webkit-text-stroke` (renders inconsistently in Chromium render)
- Drop the rgba background pill ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â let the stroke hold readability. Captions should feel like graffiti on the frame, not a subtitle track.
- For retimes, use a `shift()` function inside `captions.html` to map transcript word timestamps ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ edited-time. This keeps the transcript JSON untouched and makes retimes mechanical.

See `references/captions.md` under `/hyperframes` for the full karaoke implementation. TL;DR: per-word `<span>` elements with `data-word-start`, GSAP tweens scoped to each span, tight 0.08ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“0.12s pop durations.

## Ambient background (never ship flat navy)

Minimum viable background stack:

1. **Radial gradient base** (center lighter than edges by 15ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“20%)
2. **Animated noise/grain overlay** at 8ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“12% opacity
3. **4ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“8 drifting particle dots** or grid traces
4. **Subtle vignette**

`background: #07121c` alone is a placeholder, not a design. For techy/control-room aesthetic, use the 6-layer stack from `feedback_techy_background_layers.md` (HUD grid masked to vignette + circuit traces + pulse nodes + scan beam + telemetry ticker + corner mono labels).

## Audio reactivity

- Headlines pulse 3ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“6% on beat. Backgrounds can go 10ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“30% on bass.
- Text reactivity kept subtle (3ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“6%) so captions stay readable; backgrounds can push harder.
- Use a SEEDED offline analyser (pre-compute the audio feature track) so renders are deterministic. Do NOT use `AnalyserNode` in the render path ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `Math.random()` and real-time audio nodes break determinism.

## Transitions

- **Rotate flavors.** No two consecutive transitions the same type. Six hard cuts in a row is the #1 tell for AI editing.
- Face-mode transitions (`BOTTOM ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬Â FULLSCREEN`) double as scene transitions when the mode changes between scenes.
- For pure overlay scene-to-scene, install from registry: `push-up`, `flash-through-white`, `sdf-iris`, or the full shader-transitions pack. `npx hyperframes catalog --type block` to browse.

## The verification gate (mandatory ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â DO NOT ship without)

Lint passing ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â  design working. Never report a short-form render done until you have extracted frames at word-exact timestamps and READ every PNG.

### Step 1 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â draft render

```bash
cd video-projects/<slug>
npx hyperframes lint
npx hyperframes render --quality draft --output renders/<slug>-vN-draft.mp4
```

### Step 2 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â word-exact frame extraction

Pick 8ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“15 timestamps that each correspond to a SPOKEN WORD where a specific visual should be on-screen. Not round numbers. Not mid-scene. The exact word.

```bash
mkdir -p renders/frames-vN
for pair in "<t>:<label>" "<t>:<label>" ...; do
  t="${pair%%:*}"; label="${pair##*:}"
  ffmpeg -y -ss "$t" -i renders/<slug>-vN-draft.mp4 \
    -frames:v 1 -q:v 2 "renders/frames-vN/t${t}-${label}.png"
done
```

### Step 3 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Read every PNG

Call `Read` on every PNG so the image loads into context. Do NOT just list filenames. For each frame confirm:

- The expected visual is on-screen at the expected moment (not 1s late, not early)
- Speaker's face is not cropped in any bottom-half scene
- Full-screen vs bottom-half face mode is correct for that scene
- Captions are on-brand, readable, not overflowing
- No blank frames, no unintentional overlap, no text-off-canvas

### Step 4 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â if anything fails, fix + re-verify. Never ship broken.

### Step 5 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â final render

```bash
npx hyperframes render --quality standard --output renders/<slug>-vN.mp4
```

Spot-check 3ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“4 frames from the final render (same timestamps, different folder `frames-vN-final/`) to confirm the standard-quality encode didn't change anything.

## The 10 rules (quality checklist ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â run BEFORE first draft)

Every short-form build. Run this list during authoring, not after.

1. **No dead frames.** Every 100ms has an animating element.
2. **Scene payoff ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¥ 1s hold.** Budget by reveal time, not total time.
3. **Face is a character.** Grade + Ken Burns + side vignette.
4. **No hard seams.** Feather y=960 with gradient + scan line.
5. **One jaw-dropper per 5s.** Typography slam, glitch, whip-pan, audio slam.
6. **Audio reactivity non-negotiable.** 3ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“6% text, 10ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“30% background.
7. **Rotate transition flavors.** No two consecutive the same.
8. **Captions pop, don't politely label.** Stroke not pill. Scale + color on active word.
9. **Motion through full scene duration.** Secondary motion if entrances land early.
10. **Background is a layer, not a color.** Radial + noise + particles + vignette minimum.
11. **Slam/stamp overlays land AFTER target text is fully visible.** Reveal logic > word-sync. Stamp `t` ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¥ target-visible `t` + 0.10ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“0.25s. Otherwise the punchline lands before the setup.

## Project structure (every short-form project)

```
video-projects/<slug>/
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ hyperframes.json
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ meta.json                    (id, name, dimensions 1080x1920, fps 30)
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ index.html                   (root composition, the 4-layer scaffold)
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ compositions/
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ ambient-bg.html
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ seam-treatment.html
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ captions.html            (with shift() function if retiming)
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ scene1-<label>.html
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ scene2-<label>.html
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬ÂÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ ...
ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ assets/
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ <name>.mp4               (original recording)
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ <name>-edit.mp4          (edited ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â cuts removed ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â this is what the comp uses)
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ transcript.json          (whisper output)
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬Å¡   ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬ÂÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ brand assets (logo, brand-tokens.css, background music)
ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬ÂÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ renders/
    ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ <slug>-v1-draft.mp4
    ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ frames-v1/
    ÃƒÂ¢Ã¢â‚¬ÂÃ…â€œÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ <slug>-v1.mp4
    ÃƒÂ¢Ã¢â‚¬ÂÃ¢â‚¬ÂÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ÃƒÂ¢Ã¢â‚¬ÂÃ¢â€šÂ¬ ...
```

## Retime protocol (when audio is re-edited or timestamps drift)

1. Measure old and new edited audio durations with `ffprobe`. Delta = total cut time.
2. Identify cut window(s): which seconds were removed, from where.
3. Write the Plan table: every scene `data-start`, `data-duration`, every face-mode transition `t`, any scene whose internal offsets straddle a cut.
4. For each scene that straddles a cut, both its parent duration AND its internal offsets change. Scenes entirely on one side of the cut just need parent `data-start` shifted.
5. Lint ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ draft render ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ word-exact frame verify ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ final render. No shortcuts.

## What NOT to do in short-form

- Don't animate `<video>` element dimensions ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â freezes frames. Animate wrapper div.
- Don't use `repeat: -1` on any timeline ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â breaks the capture engine. Finite counts only.
- Don't use `Math.random()` or `Date.now()` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â breaks determinism. Seeded PRNG if pseudo-random needed.
- Don't use `<br>` inside captions ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â natural wrapping + `<br>` produces extra unwanted breaks.
- Don't skip the frame verification gate. Lint exit code is not visual truth.
- Don't author in original-time if the audio is edited. Edited-time or nothing.
- Don't leave `background: #07121c` flat. Layer it.
- Don't hard-cut between scenes. Rotate transition flavors.
- Don't polite-caption. Pop them.
- Don't let the face sit still. Grade + Ken Burns always.

## Lessons from may-shorts-18 (v1 ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ v2)

Distilled from the 4 concrete problems the v1 render had and what fixed them in v2. Apply these on every new short.

### 1. Slam/stamp timing ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â reveal logic beats word-sync

A SLAM/STAMP overlay (KILLED, DEAD, STOP, etc.) lands AFTER its target text is fully visible, **not** during the spoken word. In may-shorts-18 v1 scene 1, CLAUDE and CHATGPT were pitched as opponents ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â KILLED fired at local 0.46s while CHATGPT didn't appear until 0.66s, so viewers saw "Claude ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ KILLED" with no visible target. The joke collapsed.

**Rule:** `stamp_t ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¥ target-text-visible_t + 0.10ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“0.25s`. The "visible" timestamp is the END of the target's entrance animation, not its start. Word-sync is a guideline; visual reveal order is the constraint.

### 2. BOTTOM face-mode scale ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â don't ship the default

Default `BOTTOM = { x: 0, y: 1136, scale: 0.5625 }` (exact horizontal fit for a 1920ÃƒÆ’Ã¢â‚¬â€1080 source) leaves empty studio background flanking the speaker if they occupy <70% of the source frame. This is the default in may-shorts-19 and was copied into may-shorts-18 v1 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â both videos had visible dead space left and right of the speaker in every BOTTOM scene.

**Rule:** prefer `BOTTOM = { x: -180, y: 1110, scale: 0.75 }` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â crops 180px each side, bottom-anchors to y=1920. Preview ONE frame of BOTTOM mode against the actual source video before committing the constant. If the source speaker is tight-framed already, scale 0.65 may be enough; if the source is wide studio framing, push to scale 0.80 and re-tune x.

Always keep HIDDEN's `x`, `y`, `scale` identical to BOTTOM ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â they only differ in `opacity` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â so the opacity-fade scenes don't drift geometrically mid-fade.

### 3. Face-mode transitions ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â three things at once, not one

When the face changes mode between adjacent scenes, a bare 0.15s pre-roll + 0.32s duration `expo.inOut` on just the face wrapper reads as rigid ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â the outgoing scene's panels are still fully opaque behind the morphing face, so the eye sees two things fighting instead of a crossfade.

**Rule:** for any "hero" scene-to-scene face-mode change (especially BOTTOM ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬Â FULLSCREEN), do all three:
1. Extend that specific transition's duration to 0.45ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“0.55s (not the default 0.32s)
2. Start it 0.25ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“0.30s before the new scene's `data-start` (not the default 0.15s)
3. Fade + blur the outgoing scene's panel wrapper to `opacity: 0, filter: blur(6px)` over 0.20ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“0.25s, starting 0.25s before scene end

Implementation-wise, promote the face-mode transition array to per-entry `dur` so one transition can be longer than the others:
```js
[ { t: 2.06, mode: FULLSCREEN, dur: 0.50 }, { t: 3.71, mode: HIDDEN, dur: 0.32 }, ... ]
  .forEach(({ t, mode, dur }) => mainTl.to("#face-wrapper", { ...mode, duration: dur, ease: "expo.inOut" }, t));
```

Three simultaneous changes = "a real editor edited this." Any one alone = rigid.

### 4. Data-feel scenes beat decoration scenes mid-video

For scenes 3ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“5 of a 15ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“20s short (the "middle grind" where attention drops the hardest), lean on visuals that read as information ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â bar races, stat grids with counting numbers, heatmaps, sparklines, flowcharts, dashboard chrome with telemetry ticking, pain-point grids that flash red in sequence. the v1 build of a legacy short in scene 4 was a radar-rings + terminal-chip + sparks combo ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â functional but decorative, and the first review called it "bland." v2 replaced it with a 3ÃƒÆ’Ã¢â‚¬â€3 pain-point grid lighting up red-orange in sequence + a sparkline stroke-drawing with a YOU-ARE-HERE marker + the payoff slam ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â same time budget, much higher engagement.

**Rule:** pure typography-plus-icon scenes feel like slides. Data-feel scenes feel like evidence. When a middle scene feels bland, replace the decoration with something that reads as *information*: a small number ticking up, a bar filling, a chart stroking in, a grid flashing in sequence.

## Reference compositions

- `video-projects/may-shorts-19/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â the canonical short-form example (18.84s, 1080x1920, 7 scenes, face-mode choreography, karaoke captions with shift(), ambient bg + seam treatment). Read `index.html` and any `compositions/scene*.html` before authoring a new short.
- `video-projects/may-shorts-18/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â secondary reference with the 4 lessons above baked in: BOTTOM scale=0.75, KILLED stamp timed after CHATGPT reveal, scene-1ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢2 fluid fade, scene 4 data-dashboard "THE PATTERN" grid.

## Related skills (invoke in addition)

- `/hyperframes` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â framework rules (always first)
- `/hyperframes-cli` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â CLI commands (init, lint, preview, render)
- `/gsap` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â animation library reference
- `/hyperframes-registry` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â installing transition blocks
- `/seedance-loop-prompt` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â if the short needs an AI-generated looping background video

## Memory pointers (relevant feedback entries)

- `feedback_short_form_principles.md` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â the 10 rules, full rationale
- `feedback_contrast_technique.md` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â glow localization + text-shadow halos + brightening dim text
- `feedback_techy_background_layers.md` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 6-layer control-room background stack
- `feedback_visual_verification.md` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â the verification gate
- `project_brand_specs.md` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â if the short is brand-specific (hex codes, fonts, logo glow)
