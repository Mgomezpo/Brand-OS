---
tags: [brand-brain, visual]
status: pendiente
---

# 🎨 Identidad Visual y Dirección de Arte

> **Propósito:** Estándares visuales, tokens, tipografía y dirección óptica para todas las piezas de {{NOMBRE_MARCA}}.
> **Tokens técnicos:** `design-system/tokens.css` · **Líneas de diseño:** [[design_lines/index]]

---

## 1. Concepto Visual

- **Nombre del sistema visual:** {{SISTEMA_VISUAL}}
- **Atmósfera en 1 frase:** {{ATMOSFERA}}
- **Referencias que amamos:** {{REFERENCIAS}}
- **Referencias prohibidas:** {{ANTI_REFERENCIAS}}

---

## 2. Sistema de Color (Regla de 3 Roles)

| Rol | Token | HEX | Uso |
| :--- | :--- | :--- | :--- |
| **Lienzo** | `--surface-page` | {{HEX_FONDO}} | Fondo dominante |
| **Lectura** | `--text-strong` | {{HEX_TEXTO}} | Tipografía principal |
| **Acento** | `--accent` | {{HEX_ACENTO}} | **Un solo elemento focal por pieza** (keyword o CTA) |
| Secundario (opcional) | `--line-1` | {{HEX}} | Gráficos / datos |

---

## 3. Tipografía (Regla de 2 Familias)

| Rol | Familia | Uso |
| :--- | :--- | :--- |
| **Grita (Display)** | {{FUENTE_DISPLAY}} | Titulares, números monumentales |
| **Susurra (Lectura)** | {{FUENTE_TEXTO}} | Cuerpo, eyebrows, subtítulos |
| Mono (opcional) | {{FUENTE_MONO}} | Badges técnicos, datos |

---

## 4. Principios de Composición (universales)

1. **Tipografía desnuda:** el texto descansa sobre espacio negativo, no dentro de cajas tipo SaaS.
2. **Espacio negativo ≥ 45 %** del encuadre.
3. **Márgenes seguros ≥ 96 px** (interfaces de IG/TikTok).
4. **Cero texto dentro de imágenes generadas por IA:** el texto se estampa en código.
5. **Hero Cover:** la slide 1 / frame 1 es un hecho visual extraordinario, nunca un fondo pasivo.

---

## 5. Dirección Óptica para IA Generativa

- **Medio visual nativo de la marca:** {{FOTO / ILUSTRACION / 3D / COMIC / COLLAGE}}
- **Lentes preferidos:** {{35mm / 50mm / 85mm}}
- **Iluminación:** {{ILUMINACION}}
- **Composición:** sujeto en tercio inferior/lateral, 55–65 % superior limpio para tipografía.
- **Prompt negativo canónico:** `text, letters, numbers, logos, watermark, UI, buttons, {{EXTRA}}`

> Guía completa de prompting: `Estrategia/Carruseles-y-Prompting/guias-de-prompting.md` y `libreria-prompts-fondos.md`.

---

## 6. Video

- **Estilo de overlays:** {{ESTILO_OVERLAYS}}
- **Subtítulos:** máx. 4 palabras/línea, palabra activa en `--accent`.
- **Logo / intro / outro:** {{ASSETS}}
