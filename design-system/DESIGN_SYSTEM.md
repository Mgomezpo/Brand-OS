# Sistema de Diseño Canónico — {{NOMBRE_MARCA}}

> **Propósito:** Especificación de tokens de diseño, geometría, paleta cromática y tipografías para la generación determinista de activos gráficos.
> **Formatos Canónicos Oficiales:**
> - **Carruseles de Redes:** **Proporción 3:4** (1080 × 1440 px).
> - **Video Vertical (Reels / TikTok / Shorts):** **Proporción 9:16** (1080 × 1920 px).

---

## 🎨 1. Sistema de Color (Regla de los 3 Roles)

`css
:root {
  /* 1. Fondo (Canvas) */
  --surface-page:    #000000;  /* Fondo base del lienzo */
  --surface-raised:  #161513;  /* Superficies elevadas */
  --surface-sunken:  #0a0a0a;  /* Superficies hundidas */
  --border:          #262626;  /* Bordes estructurales */

  /* 2. Lectura (Tipografía) */
  --text-strong:     #ffffff;  /* Titulares y alto contraste */
  --text-body:       #e8e0d0;  /* Cuerpo de lectura */
  --text-muted:      #8c877d;  /* Eyebrows y notas */

  /* 3. Acento Focal (Un solo elemento focal por pieza) */
  --accent:          #ffd60a;  /* Color de impacto, payoffs y CTA */
}
`

---

## 🔤 2. Tipografía (Regla de las 2 Familias)

| Rol | Token | Ejemplo de Fuente | Uso Exclusivo |
| :--- | :--- | :--- | :--- |
| **Grita (Display)** | --font-display | Anton, Space Grotesk, Newsreader | Titulares de portada, números monumentales |
| **Susurra (Lectura)** | --font-body | Hanken Grotesk, Inter | Cuerpo de texto, eyebrows, subtítulos |
| **Mono (Técnico)** | --font-mono | Space Mono, JetBrains Mono | Badges, timestamps, código y specs |

---

## 📐 3. Dimensiones y Grillas

- **Carruseles (3:4):** 1080 × 1440 px (renderizado a 2× DPI: 2160 × 2880 px).
- **Video Vertical (9:16):** 1080 × 1920 px.
- **Margen de seguridad perimetral:** Mínimo 96 px en todos los bordes.
- **Espacio negativo obligatorio:** Al menos el 45% del encuadre limpio de texto.

---

## 🔋 4. Pesos, Tracking y Escala de Video

- **Pesos** (`--wt-*`): `400` regular · `500` medio · `700` bold · `900` black. El contraste extremo de peso es parte de la voz de la marca.
- **Tracking** (`--track-*`): `--track-tight` (-0.02em) para display; `--track-wide` (0.16em) para labels en mayúsculas.
- **Escala de video 9:16** (`--size-*`): `mega 240px` (número monumental) → `display 110px` → `title 72px` → `headline 48px` → `body 32px` → `label 22px` → `tiny 18px`. Todo tamaño se lee en ≤2 segundos.

## 🎞️ 5. Movimiento (Firma)

Ritmo **pop snappy con settle rápido** — cero rebotes blandos estilo SaaS, cero blur de entrada.

- **Easings CSS** (`--ease-*`): `--ease-snap` es el default (expo-out con settle).
- **Eases GSAP** (`--gsap-*`): `--gsap-pop: back.out(2.4)` para pops con anticipación; `--gsap-punch: power4.out` para punch-ins de cámara en keywords.
- **Duraciones**: `--dur-in: 0.35s` · `--dur-out: 0.25s`.

## 🌗 6. Texturas Deterministas

Toda textura es un SVG/gradiente **con semilla fija** — el render es 100% reproducible (sin `Math.random()`, sin `Date.now()`).

- `--tex-halftone` + `--tex-halftone-size`: puntos para sombreado cel-shaded.
- `--tex-grain`: grano de impresión (feTurbulence, seed=7).
- Sombras duras `--shadow-hard-sm/md/lg`: siempre `Npx Npx 0px`, nunca con blur.

## 🔌 7. Conexión con la Style-Library (Primacía)

`design-system/tokens.css` es la **fuente primaria**. La style-library del video-studio vive en dos modos:

| Modo | `"scope"` en style.json | Regla |
| :--- | :--- | :--- |
| **Brand** | `brand` | Importa `../../../design-system/tokens.css` y deriva acento, tipografías, tamaños y movimiento de aquí. Solo añade su variación de lienzo/forma. Ej.: `03-pop-comic`. |
| **Generic** | `generic` | Archivo de estilo autocontenido (vestuario de referencia). No importa tokens de marca. Ej.: `01-vox-explainer`, `02-youtube-influencer`. |

**Contrato común** que todo estilo debe exponer (ya satisfecho por este archivo): `--bg`, `--fg`, `--accent`, `--muted`, `--font-display`, `--font-body`, `--font-mono`. Al regenerar la marca en el Bloque 8, los estilos brand heredan automáticamente los nuevos valores.