# Design System — Fuente Canónica de Marca

Una sola verdad visual. Todo carrusel y video debe estampar `design-system/tokens.css` directamente o a través de `index.css` — cualquier otra fuente de color o tipografía es una divergencia que se corrige.

## Anatomía

| Archivo | Papel |
| :--- | :--- |
| `tokens.css` | Los ~20 tokens canónicos: `--surface-page`, `--text-strong`, `--accent`, `--font-display`, margen de 96px, radios. **Consumidos por los dos motores.** |
| `index.css` | Estilos deterministas de las diapositivas 3:4 (1080×1440): `.slide-frame`, `.slide-bg`, `.slide-content`. Importa `tokens.css` y consume todo vía `var(--token)`. |
| `DESIGN_SYSTEM.md` | Especificación textual del sistema: Regla de 3 Roles, familias tipográficas, grillas y negativo obligatorio. |
| `svg/` | Gráficos vectoriales limpios de la marca (logo, iconografía de línea). |

## Cómo fluyen los tokens hacia el resto

> ⚠️ Los **nombres de variables son API estable**: los dos motores dependen de ellos. Al regenerar la marca, cambia SOLO los valores; jamás renombres una variable.

```text
design-system/tokens.css
├─→ carousel-studio: <slug>/carousel.html → carga ../../design-system/index.css (3:4 · slides/*.png)
├─→ video-studio:    su AGENTS.md indica mapear tokens → variables CSS por composición (9:16)
├─→ vault/Conceptos/visual_identity.md   (tablas HEX/fuentes = espejo legible de tokens.css)
└─→ vault/Conceptos/design_lines/        (tokens y prompts por línea de diseño)
```

## Contrato de regeneración (`/brand-onboard` Bloque 8)

1. Los tokens **solo se regeneran vía el Bloque 8** de `/brand-onboard`: se diseñan a punta de preguntas de *vibe* (lienzo, energía del acento, voz tipográfica, geometría, referencias) — nunca pidiendo HEX ni nombres de fuente, salvo que la persona ya los tenga y los dé.
2. No editar `tokens.css` a mano para "probar un color": la regeneración determinista necesita un paso por el Bloque 8, y `/brand-audit` detectará cualquier divergencia.
3. Después de regenerar, correr `/brand-audit` para confirmar: 0 placeholders, ratios 3:4/9:16 respetados, wiki-links vivos.
