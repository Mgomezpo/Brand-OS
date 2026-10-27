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