# Guías de Generación Visual por Sistema de Diseño (Prompting Framework)

> **Principio Rector:** El **Sistema de Diseño manda**. El *Manual Cinematográfico* o las técnicas de captura física no son una plantilla única para todo; son herramientas que se activan **únicamente** cuando la línea de diseño lo exige. Para cada línea, primero se define el **medio visual nativo** y luego se parametriza el prompt.

---

## Matriz de Líneas de Diseño vs. Medio Visual

| Línea | Sistema de Diseño | Medio Visual Nativo | ¿Usa Manual Cinematográfico? | Elementos Clave del Prompt |
| :--- | :--- | :--- | :--- | :--- |
| **`default`** | **{{SISTEMA_VISUAL}} Canonical Comic** | **Ilustración Cómic / Hard Cel-Shaded** | ❌ NO (Cero foto realista, cero lentes/Hasselblad) | Trazos gruesos de tinta negra (`heavy ink linework 2px-4px`), sombras duras de un solo tono (`1-step hard cel-shading`, cero blur), colores planos saturados (`flat fills`), pared crema mate (`#fdfaf1`) en 65% superior, escritorio {{SISTEMA_VISUAL}} (lámpara cálida, IDE glowing, gorra roja, verde jersey). |
| **`spec`** | **Vintage Technical Engineering (Rally / DTM Spec Sheet)** | **Fotomecánica Monocromática / Halftone Risograph Screen Print** | ❌ NO (Cero fotorrealismo o 3D; imprenta de medios tonos analógica) | Estética de póster técnico de competición 80s/90s, trama gruesa halftone (`coarse monochrome halftone screen print`), papel prensa técnico cálido (`#f3f2ef`), tinta carbón densa (`#1a1a1e`), acento de homologación rojo (`#b5342a`), **sujeto de manufactura física, despiece ortogonal de producto y patronaje técnico (patrones de corte de indumentaria, despiece de calzado/suelas, troqueles de packaging, calibradores mecánicos — ESTRICTAMENTE PROHIBIDO computación, chips, placas o servidores)** en tercio inferior, 65% superior de papel vacío para titulares duales Space Grotesk + Serif cursiva. |
| **`orion`** | **Classic Cosmic Comic (Agent Clone Protocol)** | **Ilustración de Cómic Cósmico Clásico (Bronze Age / Kirby Space)** | ❌ NO (Cero fotorrealismo o 3D; ilustración heroica de cómic) | Arte de portada de cómic cósmico (Jack Kirby / Marvel Bronze Age / Invincible), entintado dinámico y cel-shading, fondo cósmico de estrellas y nebulosa carbón/rosa/azul (`#33323a`, `#c98fb0`, `#6f9fd8`), destellos de energía ámbar (`#e8b45f`) y Kirby krackle, personaje célebre retratado como superhéroe cósmico de operaciones/IA, **con protocolo de inyección de Character Sheet (`--cref`)**, tercio superior despejado para Trade Dress ("CLAUDE CODE COMICS GROUP"), titular 3D extruido y burst badges de giveaway. |
| **`caps`** | **Clean Product Showcase & Design Sheet Framework** | **Fotografía Comercial de Producto en Estudio / Catalog Lookbook** | ✅ SÍ (Fotografía comercial de estudio para productos físicos) | Fotografía comercial de alta gama para productos de marca (indumentaria, calzado, accesorios, packaging), cámara Sony A7R V a f/8, luz difusa balanceada 5000K, texturas táctiles auténticas (lona, cuero, sarga, costuras de precisión), encuadre en marco Caps sobre fondo de lona cruda (`#ece5da`) o marfil (`#f7f1e8`), 40% superior despejado para titulares Oswald mayúsculas y metadatos de Design Sheet. |
| **`bunny`** | **Low-Poly Isometric Diorama (Client Stories & Case Studies)** | **Render 3D Low-Poly Isométrico / Dioramas de Arcilla Pastel** | ❌ NO (Cero fotorrealismo humano; render 3D estilizado low-poly) | Diorama arquitectónico isométrico en baja poligonización (*low-poly clay render*), casitas de dirección, pequeños estudios y entornos de trabajo en tonos pastel, tejados periwinkle (`#7385c8`), paredes crema y rosa suave (`#ef9ac2`), árboles geométricos facetados, iluminación cenital cálida de maqueta con sombras suaves, fondo limpio lila-crema pastel (`#f8f0f4`) en el 65% superior para narrativa de casos reales y anécdotas de consultoría ("Me senté con una marca..."). |

---

## 1. Línea `default` ({{SISTEMA_VISUAL}} Cel-Shaded Comic) — Especificación de Prompting

La marca personal en su línea central vive dentro de una **novela gráfica / cómic europeo**: un creador/desarrollador en su habitación con paredes crema, iluminado por una lámpara de escritorio, rodeado de monitores de código y un escritorio de cristal teal o madera cálida.

### Sintaxis Canónica para `default`:
* **Estilo Artístico Obligatorio:** `Graphic novel comic illustration, modern European ligne claire style, authentic cel-shaded vector art`.
* **Entintado & Sombras:** `Bold, confident black ink linework with uniform 3px stroke weight. Pure hard-edged cel-shading with zero gradient blur, zero airbrushing. Flat saturated color fills`.
* **Composición Clean Canvas (3:4 vertical):**
  - **Tercio inferior (35%):** El escritorio de trabajo {{SISTEMA_VISUAL}} (lámpara de escritorio de latón encendida, monitor panorámico oscuro con sintaxis de código brillante en verde/blanco, taza de café humeante sobre desk mat verde azulado / roble, gorra roja descansando).
  - **Zona superior (65%):** Pared plana de papel crema cálido {{SISTEMA_VISUAL}} (`#fdfaf1` / `#f6efdd`) completamente limpia de objetos, sirviendo de espacio negativo puro para los titulares en Anton y amarillo.
* **Tokens de Color en el Prompt:**
  - Lienzo / Pared: Warm cream matte paper `#fdfaf1` / `#f6efdd`.
  - Tinta: Dense carbon ink `#100f0d`.
  - Acentos de escena: Desk teal `#1f7a63`, Jersey green `#1f6b48`, Ballcap red `#c8252b`, Signal yellow glow `#ffd60a`.
* **Prompt Negativo para `default`:**
  ```text
  photorealistic, realistic photo, 3D render, octane render, airbrushed, blurred gradient shadows, photorealism, glossy plastic, corporate suit, corporate office, glass skyscraper, text, letters, numerals, words, watermark, speech bubbles.
  ```

---

## 2. Línea `spec` (Data Storytelling, Benchmarks & Métricas de Producto Físico) — Especificación de Prompting

Inspirada en las fichas técnicas de homologación de ingeniería y competición de los años 80 y 90 (estilo fichas Group B / DTM / despieces de taller de manufactura). Traduce la física de la **producción física, el patronaje y el despiece de producto comercial** a una estética gráfica de imprenta fotomecánica de alto contraste, trama de medios tonos (*halftone*) y maquetación técnica sobre papel prensa.

> 🚫 **REGLA ABSOLUTA Y NO NEGOCIABLE: CERO COMPUTACIÓN / CERO SILICIO EN `SPEC`**
> 
> {{NOMBRE_CREADOR}} {{APELLIDO_CREADOR}} está posicionado como **Product Marketing AI Specialist** para marcas de **producto físico, e-commerce, moda y manufactura** — NO como ingeniero de sistemas, técnico de telecomunicaciones o divulgador de hardware.
> 
> Queda **TERMINANTEMENTE PROHIBIDO** incluir en los prompts o visuales de `spec`:
> - ❌ Computadores, portátiles, laptops, pantallas de código, monitores, terminales o interfaces digitales.
> - ❌ Racks de servidores, centros de datos, cables ethernet o placas madre.
> - ❌ Microchips, CPUs, GPUs, obleas de silicio, circuitos integrados, soldaduras electrónicas o PCBs.
> - ❌ Osciloscopios, testers digitales o diales electrónicos.
>
> **¿Qué SÍ ES el sujeto de `spec`?**
> La **física tangible del producto comercial y las herramientas tradicionales de manufactura de taller**:
> 1. **Indumentaria & Textil:** Patrones de corte de prendas, líneas de tiza de sastre, reglas curvas de patronaje, cizallas industriales de corte pesado, densidades de tejido e hilos técnicos.
> 2. **Calzado & Sneakers:** Despiece ortogonal de capas de suela (outsole, midsole, insole, amortiguación), hormas de zapatero, costuras de cerco y cortes de cuero.
> 3. **Packaging & Cajas:** Planos desplegados de troquelado (die-cut blueprints), líneas de hendido, solapas de pegado, matrices de estampado en caliente (hot-stamping dies) y sellos de cera o inspección de control de calidad.
> 4. **Herramientas de Precisión Mecánica:** Calibradores Vernier analógicos de acero, micrómetros de tornillo manuales, comparadores de cuadrante mecánicos (dial gauges) y compases de punta seca.

### Sintaxis Canónica para `spec`:
* **Estilo Artístico & Medio:** `Vintage 1980s-1990s technical engineering poster aesthetic, coarse monochrome halftone screen print, risograph dot-matrix dither, authentic high-contrast darkroom lithography on archival newsprint`.
* **Sujeto de Inmersión (Física de Producto y Manufactura):** `Physical product manufacturing blueprint, exploded technical diagram of sneaker sole layers, unfolded packaging die-cut template layout, garment patternmaker cutting lines, mechanical vernier caliper measuring fabric thickness, precision industrial tailoring shears resting on technical spec paper`.
* **Tratamiento Gráfico & Tinta:** `Dense carbon ink (#1a1a1e) dots over aged technical paper (#f3f2ef), heavy ink bleed, extreme macro mechanical contrast, 1-bit rasterized texture, subtle technical red inspection stamp or arrow (#b5342a)`.
* **Composición Clean Canvas (3:4 vertical):**
  - **Tercio inferior (35%):** El despiece técnico del producto físico o herramienta de manufactura en perspectiva ortogonal o vista de taller, renderizado enteramente en trama halftone de puntos gruesos, desvaneciéndose hacia arriba con viñeta de medios tonos.
  - **Zona superior (65%):** Fondo de papel técnico cálido (`#f3f2ef`) completamente vacío y limpio, con textura sutil de fibra vegetal y cero objetos, listo para recibir los bloques de texto HTML en Space Grotesk y cursiva.
* **Tokens de Color en el Prompt:**
  - Base: Warm archival technical newsprint `#f3f2ef`.
  - Tinta principal: Dense carbon ink `#1a1a1e`.
  - Acento técnico: Homologation spec red `#b5342a` o Navy `#33435e`.
* **Prompt Negativo Obligatorio para `spec`:**
  ```text
  computer, server, rack, silicon wafer, microchip, motherboard, cpu, gpu, microcircuit, circuit board, pcb, oscilloscope, electronic display, digital screen, monitor, laptop, code terminal, cables, wire harness, car, automobile, vehicle, 3D render, octane render, smooth airbrushed gradient, photorealism, glossy plastic, modern neon UI, text, letters, numerals, words, watermark.
  ```

---

## 3. Línea `orion` (Classic Cosmic Comic / Agent Clone Protocol) — Especificación de Prompting

Inspirada en las portadas de cómic cósmico clásico de la Edad de Bronce (Jack Kirby, Jim Starlin) y el impacto visual moderno de portadas como *Invincible* y *Cosmic Ghost Rider*. Diseñada para carruseles de **Giveaways de Clones de Agentes en Claude Code**, donde figuras históricas o personajes célebres de Product Marketing (April Dunford, Seth Godin, David Ogilvy, Brian Chesky) son retratados como superhéroes cósmicos que lideran operaciones de IA.

### Sintaxis Canónica para `orion`:
* **Estilo Artístico Obligatorio:** `Vintage cosmic superhero comic book cover art, classic Bronze Age Marvel comic illustration, bold dynamic ink linework, Kirby krackle cosmic energy dots, dramatic celestial lighting, vibrant pulp comic print aesthetic`.
* **Inyección Obligatoria de Referencia:** `[CHARACTER SHEET INJECTION: <URL_OR_IMAGE_PATH>]` al inicio de cada prompt que contenga un personaje o clon.
* **Sujeto Central (Personaje Clonado):** `[Nombre del Personaje célebre] illustrated as a powerful comic book cosmic hero, dynamic confident heroic pose, determined expression, radiating glowing amber and blue cosmic energy from hands and chest, iconic stylized clothing adapted into retro-futuristic agent hero attire`.
* **Atmósfera & Entorno Cósmico:** `Deep charcoal space starfield (#33323a), swirling celestial nebula in cosmic pink (#c98fb0) and stellar blue (#6f9fd8), glowing starburst rays, celestial planets in background, black ink crosshatching and solid comic shadows`.
* **Composición Clean Canvas (3:4 vertical):**
  - **Zona superior (35-40%):** Espacio superior despejado de elementos del sujeto para montar el Trade Dress ("CLAUDE CODE COMICS GROUP"), el titular monumental 3D extruido y los burst badges de giveaway en HTML.
  - **Zona central e inferior (60-65%):** El personaje heroico en plano medio o cuerpo entero dinámico emergiendo del cosmos hacia el espectador.
* **Tokens de Color en el Prompt:**
  - Fondo espacial: Charcoal starfield `#33323a`.
  - Energía y rayos: Cosmic amber `#e8b45f` and neon yellow `#ffd60a`.
  - Nebulosa: Nebula pink `#c98fb0` and cosmic blue `#6f9fd8`.
  - Sombras y tinta: Pure carbon ink `#100f0d`.
* **Prompt Negativo para `orion`:**
  ```text
  photorealistic, realistic 3D human photo, octane render, smooth airbrushing, corporate stock photography, modern flat SaaS gradient, blurry realistic background, plain business suit stock photo, real skin pores, text, letters, numerals, words, watermark.
  ```

---

## 4. Línea `caps` (Clean Product Showcase & Design Sheet Framework) — Especificación de Prompting

Inspirada en catálogos comerciales de producto de alta gama, dirección de arte para marcas de moda/accesorios y hojas de especificación técnica (*Product Design Sheets*). Diseñada para carruseles educativos que enseñan a **mantener consistencia visual de producto de marca en IA**.

### Sintaxis Canónica para `caps`:
* **Estilo Artístico & Medio:** `High-end commercial product photography, studio catalog lookbook aesthetic, pristine tactile material focus, sharp edge-to-edge product clarity, clean modern e-commerce campaign visual`.
* **Sujeto Central de Producto:** `[Prenda / Gorra / Calzado / Accesorio / Packaging de marca] isolated on neutral warm tone studio surface, visible authentic material textures (washed cotton twill, wide-wale corduroy, full-grain leather, brass hardware, precision stitching), exact brand color adherence`.
* **Óptica & Cámara:** `Sony A7R V with 90mm macro prime at f/8, ultra-high resolution product sharpness, zero lens distortion, crisp depth of field keeping entire product in critical focus`.
* **Iluminación:** `Diffused 5000K balanced softbox studio daylight, subtle wrap-around ambient contact shadow on surface, zero harsh blown-out specular highlights`.
* **Composición Clean Canvas (3:4 vertical):**
  - **Zona de Producto (50-60% central/inferior):** El producto centrado o en ángulo cenital 90° / perspectiva de catálogo de 3/4, rodeado de un fondo neutro cálido de lona o papel kraft limpio (`#f7f1e8` / `#ece5da`), listo para incrustarse en el "Marco Caps".
  - **Zona superior (40%):** Fondo neutro despejado para titulares en Oswald mayúsculas y etiquetas de metadatos de la Design Sheet.
* **Tokens de Color en el Prompt:**
  - Base de estudio: Unbleached raw cotton canvas `#ece5da` / light studio surface `#f7f1e8`.
  - Tonalidades de producto: Worn rust `#b5342a`, washed olive `#58634f`, vintage navy `#2c3b4d`, natural leather `#a06d48`.
* **Prompt Negativo para `caps`:**
  ```text
  blurry background, deformed product geometry, asymmetrical logos, messy studio, plastic sheen, oversaturated neon, chromatic aberration, human face, full body model distraction, low-resolution textures, watermark, text, numerals.
  ```

---

## 5. Línea `bunny` (Low-Poly Isometric Diorama / Client Stories & Case Studies) — Especificación de Prompting

Inspirada en dioramas arquitectónicos en miniatura 3D de baja poligonización (*low-poly*) con acabado de arcilla mate y paleta pastel cálida. Diseñada para carruseles de **Storytelling con Clientes, Casos de Estudio y Lecciones de Dirección en Product Marketing con IA** (*"Me senté con una marca que quería..."*).

### Sintaxis Canónica para `bunny`:
* **Estilo Artístico & Medio:** `Isometric 3D low-poly miniature diorama, stylized pastel clay render, low-poly faceted architectural model, soft ambient occlusion, toy-like tactile aesthetic, Blender Cycles soft studio lighting`.
* **Sujeto Central (El Escenario Narrativo):** `Charming miniature low-poly cozy headquarters building on wooden stilts with deck, pastel pink (#ef9ac2) and cream wooden plank walls, soft periwinkle blue (#7385c8) roof with round attic window, small wooden lantern post, geometric faceted low-poly trees and bushes, clean stepping stones`.
* **Atmósfera & Iluminación:** `Warm gentle morning pastel daylight, soft lilac-tinted diffuse ambient contact shadows, clean pristine matte surfaces with zero gloss or plastic shine`.
* **Composición Clean Canvas (3:4 vertical):**
  - **Tercio inferior (35-40%):** El diorama isométrico flotando centrado con sus elementos en miniatura, asentado sobre una base sutil de terreno facetado.
  - **Zona superior (60-65%):** Fondo liso y limpio en suave rosa crema pastel (`#f8f0f4`), completamente libre de elementos, reservado para los titulares en Baloo 2 y el texto narrativo del caso de estudio en HTML.
* **Tokens de Color en el Prompt:**
  - Fondo limpio: Soft pastel lilac-cream `#f8f0f4`.
  - Arquitectura y acentos: Bubblegum pink `#ef9ac2`, Periwinkle blue `#7385c8`, Soft cornflower `#aab6e2`, Warm wooden tones `#c48c68`, Mint green foliage `#96c5a8`.
* **Prompt Negativo para `bunny`:**
  ```text
  photorealistic, realistic human photo, gritty dark photography, horror, hyperrealistic skin, dirty textures, corporate glass skyscraper, neon glow, chromatic aberration, text, words, watermark, deformed geometry.
  ```

---

## 6. Lógica de Portadas Heroicas (Slide 01) y Protocolo de Inyección de Rostros

### 6.1. La Ley del Hero Cover (Slide 01 es un Hecho Visual Extraordinario, NO un fondo pasivo)

La portada de un carrusel representa el **80% del éxito en retención y guardados** (patrón validado en referentes como Helder Peñaloza y Alan Villagrán). Detener el pulgar en el feed exige un impacto visual inmediato en menos de 0.5 segundos.

* **El Cover NUNCA puede estar al mismo nivel visual que las slides interiores:**
  - ❌ **Prohibido:** Un fondo de escritorio pasivo idéntico al de las demás slides, una textura plana repetitiva o una composición tímida.
  - ✅ **Obligatorio:** Un **Hecho Visual Extraordinario ("Volada" / Scroll-Stopper Monumental)** que genere curiosidad inmediata, magnetismo táctil o asombro estético.

* **Técnicas Canónicas para Construir un Hero Cover Extraordinario:**
  1. **Perspectiva o Ángulo Dramático:**
     - Plano cenital 90° perfecto (vista ortogonal pura o desde dron) que ordene el caos de forma hipnótica.
     - Perspectiva de gusano / contrapicado heroico con producto elevado sobre pedestal monolítico bañado por un haz de luz focal divino.
  2. **Contraste de Escala o Despiece Espectacular:**
     - Macro extremo de textura táctil (sarga de algodón, costura gruesa, cuero graneado) contrastado contra la forma pura del producto.
     - Despiece físico monumental (las 12 capas de una zapatilla o los troqueles de una caja flotando en perfecta alineación isométrica).
  3. **Choque Tangible de Materiales:**
     - Tiza sobre pizarra de taller, herramientas de latón pulido junto a tejidos gastados, sellos de cera roja sobre papel técnico milimetrado.
  4. **Instalación Conceptual:**
     - Un diorama 3D colosalmente detallado (en `bunny`), o un superhéroe cósmico emergiendo de una supernova con energía crepitante (en `orion`).

* **Jerarquía Tipográfica Monumental (HTML Overlay sobre Cover):**
  - **One-Liner de Portada:** Máximo **10 a 12 palabras**. Contundente, directo y de valor evidente.
  - **Tono 100% Positivo y Formativo:** Formatos de *"Cómo lograr X"*, *"El método exacto para Y"*, *"Los números detrás de Z"*. Cero amarillismo ("está muerto", "perderás todo") y cero cifras trilladas ("$10K").
  - **Doble Registro Tipográfico Obligatorio:** Contraste dinámico entre la Display principal de la línea (`Anton`, `Space Grotesk`, `Oswald`, `Baloo 2`) y un acento editorial en **cursiva itálica serif** (`font-serif italic text-accent`) o un número colosal de color de impacto (`#ffd60a`, `#b5342a`, `#e8b45f`).
  - **Clean Canvas Estricto (3:4 Vertical):** El sujeto heroico vive en el tercio inferior (35-40%), dejando el **60% a 65% superior completamente inmaculado** (pared crema, papel técnico, lona cruda, vacío cósmico limpio) para albergar la tipografía en HTML sin solapamientos.

---

### 6.2. Protocolo de Inyección de Rostros y Character Sheets (Personajes & Creador)

Cuando un carrusel incluye la imagen de un referente real (April Dunford, Seth Godin, David Ogilvy, Brian Chesky, etc.) o del propio creador ({{NOMBRE_CREADOR}} {{APELLIDO_CREADOR}}), el pipeline exige **consistencia fisionómica absoluta** para evitar alucinaciones, mutaciones o rostros irreconocibles entre slides:

1. **Slot Explícito de Inyección en el Prompt:**
   Todo prompt que incluya al personaje debe encabezar obligatoriamente la directiva:
   ```text
   [CHARACTER SHEET INJECTION: <URL_OR_LOCAL_FILE_PATH>]
   ```
2. **Mapeo por Motor de Generación:**
   - **En Midjourney v6:**
     - Se agrega al final del prompt: `--cref <URL> --cw 80` (Character Weight 80 fija los rasgos fisionómicos del rostro mientras permite adaptar la vestimenta y pose al estilo de cómic cósmico o atelier).
     - Si se requiere identidad fotográfica 1:1 estricta, usar `--cw 100`.
   - **En Gemini Flow / Nano Banana / Imagen 3:**
     - Se pasa la imagen de referencia en el slot de entrada como `Subject Reference Image` con afinidad alta.
   - **En ComfyUI / Flux / Stable Diffusion:**
     - Se conecta vía **IP-Adapter Face / InstantID / PuLID** con un peso de fijación entre `0.75` y `0.85`.

3. **Tokens Fisionómicos Fijos e Inmutables:**
   La imagen de referencia NO sustituye la descripción textual; trabajan en conjunto. El prompt DEBE describir siempre los mismos rasgos distintivos invariantes:
   - *Estructura facial y edad estimada.*
   - *Peinado exacto, corte, longitud y color del cabello.*
   - *Expresión característica (estratega resuelto, mirada penetrante, sonrisa cálida de artesano).*
   - *Rasgos identificatorios (gafas específicas, barba recortada o afeitado limpio).*
   
   *Ejemplo Canónico (April Dunford en `orion`):*
   > `[CHARACTER SHEET INJECTION: assets/ref_april_dunford.jpg] April Dunford, renowned product positioning strategist, authentic facial likeness, short blonde textured haircut, sharp confident and analytical expression, illustrated as a classic cosmic superhero in Bronze Age comic book style...`

4. **Persistencia Multi-Slide:**
   Si el personaje aparece en la Slide 01 (Cover) y en la Slide 06 (Cierre), ambas prompts DEBEN compartir la misma imagen de referencia (`--cref`) y la misma cadena fisionómica inmutable, variando únicamente la acción, la pose y el encuadre.

