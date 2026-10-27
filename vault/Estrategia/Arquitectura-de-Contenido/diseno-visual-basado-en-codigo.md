# Sistemas de Diseño Visual Basados en Código (Zero-Template)

En **Brand OS Engine**, cada marca posee un lenguaje visual y tipográfico único, implementado algorítmicamente en `core/renderer/generative-composer.mjs`. No existen plantillas estáticas; el motor genera el DOM HTML y los estilos CSS necesarios según el contenido de cada diapositiva.

Todas las diapositivas se configuran con dimensiones exactas para carruseles verticales en redes sociales: **1080 × 1440 px (relación de aspecto 3:4)**.

---

## 1. {{MARCA_B2B}} — Sistema de Diseño Suizo High-End

Diseñado originalmente en Claude para reflejar la sofisticación de un Chief Operating Officer (COO) técnico de $5,000 USD/mes.

* **Filosofía:** Precisión suiza, contrastes oscuros de alta gama, sobriedad matemática y elegancia financiera.
* **Paleta Cromática:**
  - Fondo Base: `#090D14` (Obsidiana Profunda)
  - Gradiente Dual de Iluminación:
    - `radial-gradient(circle at 85% 15%, rgba(191, 161, 117, 0.08) 0%, transparent 45%)` (Bronce Cálido)
    - `radial-gradient(circle at 15% 85%, rgba(37, 99, 235, 0.06) 0%, transparent 50%)` (Cobalto Tecnológico)
  - Acento Principal: `#BFA175` (Bronce Champagne Metálico)
  - Color de Acento Brillante: `#D1B892`
  - Tarjeta de Métrica: Fondo `#161D2B` con borde izquierdo `4px solid #BFA175`
  - Textos: Blanco editorial `#F9FAFB` y gris técnico `#D1D5DB`
* **Grilla Técnica de Ingeniería:**
  - Inyectada mediante pseudo-elemento `.slide::before`
  - Grilla de líneas milimétricas de `60px × 60px` con opacidad sutil al 2% (`rgba(255, 255, 255, 0.02)`).
* **Tipografía:**
  - **Titulares (`.slide-title`):** `Fraunces`, Serif Display, 58px a 64px, font-weight 700, line-height 1.12, letter-spacing -0.02em.
  - **Headers, Badges, Números y Métricas:** `Space Grotesk`, sans-serif geométrica monospaced, font-weight 600 a 700, letter-spacing 0.12em a 0.18em.
  - **Cuerpo de Texto (`.slide-body`):** `Inter`, sans-serif suiza, 26px, font-weight 300, line-height 1.55.
* **Detalles Perimetrales Inmutables:**
  - Header: Punto brillante de marca `.brand-dot` (ámbar con resplandor) + `{{NOMBRE_MARCA}} / OPERATIONAL SYSTEMS` + Contador `01 / 05`.
  - Divisor: Barra horizontal de 100px con gradiente de `#BFA175` a transparente.
  - Footer: `FIJA: $5,000 USD / MES • ZERO HUMAN-IN-THE-LOOP` + `DESLIZA PARA ANÁLISIS →` (o `SESIÓN DE DIAGNÓSTICO EN BIO` en la última lámina).

---

## 2. {{MARCA_APP}} — Sistema de Cuaderno Analógico Creativo

Inspirado en la filosofía de {{AGENTE_ESTUDIO}} Rubin, el minimalismo de Apple y los cuadernos físicos de notas creativas.

* **Filosofía:** Calidez editorial, táctil, honesta, anti-corporativa y centrada en resolver el caos mental del creador.
* **Paleta Cromática:**
  - Fondo Base: `#0B0B0B` (Tinta Carbón Mate)
  - Iluminación Perimetral: Radial crimson profundo (`rgba(159, 21, 34, 0.18)` al 90% 10% y `rgba(110, 11, 20, 0.12)` al 10% 90%).
  - Acento Principal: `#9F1522` (Carmesí Editorial / Sello de Cera)
  - Color de Badge: `#E27B86` sobre fondo `rgba(159, 21, 34, 0.15)`
  - Textos: Papel marfil `#F8F6F1` y gris cálido `#D6D3CD`
* **Textura de Grano Analógico:**
  - Inyectada en `.slide::before` mediante un filtro SVG vectorial en línea (`feTurbulence` con `fractalNoise` al 4% de opacidad) para dar la textura de una libreta de bocetos.
* **Tipografía:**
  - **Titulares (`.saas-title`):** `Fraunces`, Serif Humanista (300 a 400), 58px / 64px, letter-spacing -0.025em.
  - **Cuerpo de Texto (`.saas-body`):** `Outfit`, sans-serif moderna cálida a 26px.
  - **Kickers, Sellos y Datos (`.saas-seal-badge`):** `JetBrains Mono` con `letter-spacing: 0.32em` estricto en mayúsculas.
  - **Anotación Manuscrita de {{AGENTE_ESTUDIO}} (`.handwritten-note`):** `Reenie Beanie`, cursive a 30px en tono amarillo de nota adhesiva (`#F2D77B`).
* **Paneles y Superficies:**
  - Paneles planos con radio 0px (`border-radius: 0px` estricto según DESIGN.md).
  - Borde izquierdo de 4px en carmesí `#9F1522`.
* **Detalles Perimetrales:**
  - Header: Punto de cera carmesí + `{{MARCA_APP}} / EL DESPACHO DE {{AGENTE_ESTUDIO}}` + `EDICIÓN 01 / 05` en JetBrains Mono.
  - Footer: `DE LA IDEA AL CALENDARIO EN MINUTOS • NOTAS CREATIVAS CON IA` + `LEER DESPACHO →` (o `CREA TU CUADERNO EN BIO`).

---

## 3. {{NOMBRE_CREADOR}} {{APELLIDO_CREADOR}} — Sistema Cel-Shaded Terminal (Build in Public)

Diseñado a partir de `PRODUCT.md` y `voice.md` en `{{NOMBRE_MARCA}} (Marca Personal)`: una estética que fusiona la consola de ingeniería de software con sombras duras tipo cómic/cel-shaded.

* **Filosofía:** Transparencia de ingeniería, sin adornos vacíos, dinámico, directo y narrado en primera persona con vos.
* **Paleta Cromática:**
  - Fondo Base: `#0D1117` (Consola de código)
  - Resplandor: `radial-gradient` cian (`rgba(56, 189, 248, 0.08)`) y azul cobalto
  - Acento Principal: `#38BDF8` (Cian Eléctrico de Terminal)
  - Barra de Terminal: `#0D1117` con tres puntos de ventana (`#FF5F56`, `#FFBD2E`, `#27C93F`)
  - Tarjetas: `#161B22` con borde de `1.5px solid #30363D`, borde izquierdo de `5px solid #38BDF8` y sombra dura proyectada (`box-shadow: 6px 6px 0px rgba(0, 0, 0, 0.7)`)
  - Textos: `#F0F6FC` y `#C9D1D9`
* **Tipografía:**
  - **Titulares (`.personal-title`):** `Inter` 900 Black masivo y rotundo a 58px / 64px, letter-spacing -0.035em.
  - **Cuerpo (`.personal-body`):** `Inter` 300 / 400 a 26px.
  - **Terminal, Comandos y Métricas:** `JetBrains Mono` con prompt de shell `❯`.
* **Detalles Perimetrales:**
  - Header: Prompt de consola `❯ brand.log --build-in-public` + `[01/05]`.
  - Footer: `ARQUITECTURA DE SISTEMAS & LECCIONES DE FUNDADOR` + `DESLIZA EL POST →` (o `DEJAME TU OPINIÓN ABAJO ↓`).

---

## 4. Tipos de Diapositiva y Layouts Automáticos

El generador analiza las propiedades de cada slide (`badge`, `metric`, `body`) y selecciona el layout más adecuado:

1. **`hook` (Slide 1):** Titular masivo a 64px, badge de diagnóstico y espacio abierto para atrapar la mirada en el feed.
2. **`editorial` (Slide estándar):** Titular a 54px, divisor estilizado, párrafo explicativo de hasta 900px de ancho y métrica contextual en píldora.
3. **`metric` (Slide de impacto cuantitativo):** Genera la **Tarjeta de Métrica Operativa** (`.metric-card`), con borde vertical de acento, etiqueta monospaced de 12px y número grande a 38-40px.
4. **`procedural` (Slide de flujo/código):** Caja oscura con estilo de terminal o arquitectura de sistema para desglosar flujos de paso a paso.
5. **`cta` (Slide final):** Caja de llamado a la acción con flecha directriz y mensaje de conversión sobrio.
