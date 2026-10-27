---
name: carousel-batch
description: Guided 3-phase production engine for weekly 3:4 carousels (1080 x 1440 px). Strictly separates research, copywriting of punchy one-liners, text-free AI visual prompts, and deterministic HTML/CSS compilation.
---

## What this skill does

Guides the creation of high-converting, authority-building carousels in the canonical **3:4 aspect ratio (1080 × 1440 px)**. It enforces the immutable rule of separating cognitive copywriting from visual asset generation.

## The 3-Phase Batch Protocol

### Phase 1: Research & Angle Selection
1. Read `vault/Conceptos/content_pillars.md` to identify the active pillar for the batch.
2. Cross-reference `vault/Conceptos/user_persona.md` to select a specific scene of pain or micro-frustration.
3. Select the angle with the router `vault/Estrategia/Frameworks-de-Guionizacion/decision_tree.md`, which routes to the real framework library:
   - **Quiebre Cognitivo:** `quiebre_de_creencia` (desmantelar una creencia falsa) · `fuga_invisible` (exponer el coste oculto).
   - **Autoridad y Sistemas:** `demostracion_de_mecanismo` (prueba en vivo del sistema propio) · `desglose_paso_a_paso` (metodología replicable).
   - **Storytelling y Lore:** `arco_tres_actos` (vivencia propia) · `leccion_de_trinchera` (principio aprendido en batalla).
   - **Conversión y Cierre:** `activacion_lead_magnet` (recurso a cambio de interacción) · `polarizacion_cualificada` (filtrar del grupo ideal).
4. Propose 3 hook variations (≤ 12 words each, ideally 8–10) for user approval before drafting slides.

### Phase 2: Copywriting of One-Liners (5 to 8 Slides)
Once the hook is approved, write the slide-by-slide copy strictly adhering to these rules:
- **Slide 1 (Cover / Hook):** Maximum 12 words (ideally 8–10). High tension. 1 highlighted word in `--accent`.
- **Slide 2 (The Villain / The Flawed Premise):** Validate the pain. Call out the flawed industry practice.
- **Slide 3 (The Reframe / Shift):** Introduce the brand's contrarian belief.
- **Slides 4-6 (The Mechanism / Proof):** 1 actionable concept per slide. Bullet points must be one-liners (no paragraphs). Cite verified metrics from `vault/Conceptos/proof_bank.md`.
- **Slide 7 (Summary / Takeaway):** The single mental model to remember.
- **Slide 8 (Call to Action):** Explicit action with the DM keyword from `vault/Conceptos/offer.md` (e.g., "Comenta `SISTEMA` y te envío la plantilla en PDF por DM").

**Copy Constraints:**
- Maximum 25 words per slide.
- Strict 3-color rule: background (`--surface-page`), text (`--text-strong`), accent (`--accent`).
- Only **1 single word highlighted** in `--accent` per slide.

### Phase 3: AI Prompts & Deterministic Compilation
**RULE: Prohibited to write prompts before Phase 2 copy is signed off.**

1. **AI Background Prompts:**
   - Prompts must generate background imagery ONLY.
   - Every prompt MUST include: `"pure background texture, minimalist, architectural, ultra high resolution, cinematic lighting, absolutely no text, no letters, no logos, no typography, clean negative space"`.
2. **HTML/CSS Assembly:**
   - Build `<slug>/carousel.html` loading `design-system/index.css` (which imports `design-system/tokens.css`) and applying the design line tokens of this carousel.
   - Ensure 96px padding safe margins on top, bottom, and sides.
3. **Deterministic Render:**
   ```bash
   cd "Content Manager/carousel-studio"
   python batch_manager.py compile <slug>   # pieza del batch: carousel.html → slides/*.png
   npm run capture -- <slug>/carousel.html  # compilación de una pieza suelta
   ```
   - Exporta PNG pixel-perfect a exactamente 1080 × 1440 px.
