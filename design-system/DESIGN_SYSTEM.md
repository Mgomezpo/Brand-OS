# Sistema de DiseÃ±o CanÃ³nico â€” {{NOMBRE_MARCA}}

> **PropÃ³sito:** EspecificaciÃ³n de tokens de diseÃ±o, geometrÃ­a, paleta cromÃ¡tica y tipografÃ­as para la generaciÃ³n determinista de activos grÃ¡ficos.
> **Formatos CanÃ³nicos Oficiales:**
> - **Carruseles de Redes:** **ProporciÃ³n 3:4** (1080 Ã— 1440 px).
> - **Video Vertical (Reels / TikTok / Shorts):** **ProporciÃ³n 9:16** (1080 Ã— 1920 px).

---

## ðŸŽ¨ 1. Sistema de Color (Regla de los 3 Roles)

`css
:root {
  /* 1. Fondo (Canvas) */
  --surface-page:    #000000;  /* Fondo base del lienzo */
  --surface-raised:  #161513;  /* Superficies elevadas */
  --surface-sunken:  #0a0a0a;  /* Superficies hundidas */
  --border:          #262626;  /* Bordes estructurales */

  /* 2. Lectura (TipografÃ­a) */
  --text-strong:     #ffffff;  /* Titulares y alto contraste */
  --text-body:       #e8e0d0;  /* Cuerpo de lectura */
  --text-muted:      #8c877d;  /* Eyebrows y notas */

  /* 3. Acento Focal (Un solo elemento focal por pieza) */
  --accent:          #ffd60a;  /* Color de impacto, payoffs y CTA */
}
`

---

## ðŸ”¤ 2. TipografÃ­a (Regla de las 2 Familias)

| Rol | Token | Ejemplo de Fuente | Uso Exclusivo |
| :--- | :--- | :--- | :--- |
| **Grita (Display)** | --font-display | Anton, Space Grotesk, Newsreader | Titulares de portada, nÃºmeros monumentales |
| **Susurra (Lectura)** | --font-body | Hanken Grotesk, Inter | Cuerpo de texto, eyebrows, subtÃ­tulos |
| **Mono (TÃ©cnico)** | --font-mono | Space Mono, JetBrains Mono | Badges, timestamps, cÃ³digo y specs |

---

## ðŸ“ 3. Dimensiones y Grillas

- **Carruseles (3:4):** 1080 Ã— 1440 px (renderizado a 2Ã— DPI: 2160 Ã— 2880 px).
- **Video Vertical (9:16):** 1080 Ã— 1920 px.
- **Margen de seguridad perimetral:** MÃ­nimo 96 px en todos los bordes.
- **Espacio negativo obligatorio:** Al menos el 45% del encuadre limpio de texto.