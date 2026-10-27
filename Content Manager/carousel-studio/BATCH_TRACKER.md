# BATCH TRACKER — Semana Actual

> **Este tablero lo reescribe por completo el motor** (`python batch_manager.py status`) cuando existe `CURRENT_BATCH.json` — antes de eso persiste esta plantilla. No lo edites a mano: el estado real lo calcula el motor (fondos detectados en `batches/<vuelta>/<slug>/assets/` y slides compiladas).
> **Sin batch activo:** crea `CURRENT_BATCH.json` con 5 carruseles (1 por línea — puntero de rotación: `../../vault/Conceptos/content_pillars.md` §4). El motor `status` imprime la estructura exacta si lo corres sin lote.

| # | Línea | Tema / Slug | Fondos Listos | Estado | Acción Inmediata |
| :-: | :--- | :--- | :---: | :---: | :--- |
| 1 | `{{line_1}}` | `{{slug_1}}` | 0/7 | ⏳ Pendiente | Pegar `bg_01.jpg` en `assets/` |
| 2 | `{{line_2}}` | `{{slug_2}}` | 0/7 | ⏳ Pendiente | Pegar `bg_01.jpg` en `assets/` |
| 3 | `{{line_3}}` | `{{slug_3}}` | 0/7 | ⏳ Pendiente | Pegar `bg_01.jpg` en `assets/` |
| 4 | `{{line_4}}` | `{{slug_4}}` | 0/7 | ⏳ Pendiente | Pegar `bg_01.jpg` en `assets/` |
| 5 | `{{line_5}}` | `{{slug_5}}` | 0/7 | ⏳ Pendiente | Pegar `bg_01.jpg` en `assets/` |

> 💡 La aprobación de copy (gate research → 🛑 → copy → prompts) es de proceso, no de motor: vive en la skill `carousel-batch` y los SOPs del vault, no en este tablero.
