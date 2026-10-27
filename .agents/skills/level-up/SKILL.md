---
name: level-up
description: Weekly calibration and learning loop skill. Evaluates published content performance, audience feedback, retention drop-offs, and technical discoveries, cleanly appending verified lessons to vault/Findings.md and vault/Repos.md.
---

## What this skill does

Transforms raw weekly publishing outcomes into compounding brand intelligence. It prevents the brand from repeating underperforming hooks and ensures that every technical or editorial breakthrough is captured permanently in the Obsidian vault.

## The 3-Step Calibration Loop

### Step 1: Content & Retention Review
Ask the user:
1. "¿Qué pieza (carrusel 3:4 o video 9:16) tuvo el mejor desempeño esta semana y qué métrica lo respalda (guardados, comentarios con la keyword, visualizaciones completas)?"
2. "¿Qué pieza no funcionó como esperabas y en qué segundo o slide se cayó la audiencia?"
3. "¿Qué objeción, duda recurrente o pregunta surgió en los comentarios o en los DMs?"

### Step 2: Extract the Compounding Finding
Synthesize the answers into an actionable rule following the format in `vault/Findings.md`:

```markdown
### [YYYY-MM-DD] Aprendizaje: [Título Corto del Hallazgo]
- **Observación:** [Qué pasó en los datos o en los comentarios]
- **Causa Raíz:** [Por qué ocurrió esto según el comportamiento del usuario]
- **Regla Operativa:** [Qué haremos a partir de ahora en los guiones/carruseles]
```

Append this finding to `vault/Findings.md`.

### Step 3: Tool & Engine Calibration (Machine Layer)
Ask:
"¿Descubrimos o ajustamos alguna herramienta técnica esta semana (ej. nuevo flag de Playwright, mejora en la transcripción ElevenLabs/Whisper, prompt de IA visual con mejor textura, conector de Zernio)?"

If yes:
- Update `vault/Repos.md` with the tool details, code snippet, and link.
- Update `connections.md` if a new service or engine status changed.
- If relevant, adjust `design-system/tokens.css` or the rendering scripts in `Content Manager/`.
