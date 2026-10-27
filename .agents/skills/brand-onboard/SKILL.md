---
name: brand-onboard
description: Use on Day 1 of a Brand OS install, or when someone says "configura mi marca", "onboard me", "iniciar marca", "set up my brand", or wants to populate the Brand Brain. Runs an 8-block interactive interview and scaffolds the canonical Brand Brain in vault/Conceptos/ PLUS a connected design-system (tokens.css, DESIGN_SYSTEM.md, design_lines) fully wired to both engines.
---

## What this skill does

Conducts an interactive, structured 8-block interview to extract the complete Brand Brain of the user or client. As each block is answered, it updates `vault/Conceptos/00_brand_intake.md` and generates or updates the 7 core Brand Brain files in `vault/Conceptos/`:

1. `brand_core.md` (Mission, archetype, contrarian beliefs, brand narrative)
2. `user_persona.md` (Target audience, the daily scene of pain, micro-frustrations)
3. `positioning.md` (Category, enemy, unique mechanism, unfair advantage)
4. `offer.md` (Core offer, deliverables, pricing tier, DM funnel keyword)
5. `tone_of_voice.md` (Communication registers, vocabulary rules, forbidden AI-slop blacklist)
6. `content_pillars.md` (The 4 content lines, weekly rotation schedule, ratio)
7. `proof_bank.md` (Verified metrics, client case studies, data points, testimonials)

Block 8 designs the **Sistema de Diseño** and wires the whole workspace: `design-system/tokens.css`, `design-system/DESIGN_SYSTEM.md`, `vault/Conceptos/visual_identity.md`, the `design_lines/` and the carousel tracker. Both engines (carousel 3:4 and video 9:16) read from those tokens, so at the end of the interview the mount is 100% connected.

It also replaces all generic `{{NOMBRE_MARCA}}` and `{{NOMBRE_CREADOR}}` placeholders with the user's authentic brand and creator name.

## The Interview Process (8 Blocks)

Ask **one question at a time**. Never overwhelm the user by dumping all blocks at once. Checkpoint answers into `vault/Conceptos/00_brand_intake.md` as you progress.

### Block 1: Identidad y Misión de Marca
- ¿Cuál es el nombre de tu marca y quién es el creador/fundador?
- ¿Cuál es la misión principal y cuál es la creencia contraria (lo que todos en tu nicho aceptan pero tú rechazas categóricamente)?
- ¿Cuál es tu arquetipo de marca (ej. El Sabio, El Rebelde, El Arquitecto, El Mentor Pragmático)?

### Block 2: User Persona y Escena de Dolor Cotidiana
- ¿A quién le hablas exactamente (ICP)?
- Describe una escena cotidiana y ultra-específica donde experimentan su mayor dolor o frustración profesional/personal.
- ¿Qué soluciones ya intentaron y por qué fallaron?

### Block 3: Posicionamiento y Mecanismo Único
- ¿En qué categoría juegas y quién es tu "enemigo común" (una mentalidad obsoleta, una práctica tóxica de la industria o un falso gurú)?
- ¿Cuál es tu Mecanismo Único (el método, sistema o framework propio con nombre memorable que resuelve el problema)?

### Block 4: Oferta y Embudo de Conversión
- ¿Qué vendes concretamente (mentoría, consultoría, software, curso, producto de alta gama)?
- ¿Cuál es tu palabra clave para el embudo de comentarios a DM (ej. "SISTEMA", "AUDITORIA", "GROWTH")?
- ¿Qué lead magnet o activo de alto valor reciben al enviar esa palabra?

### Block 5: Tono de Voz y Lista Negra Anti-AI-Slop
- Pega 1 o 2 textos reales que hayas escrito (posts, emails o guiones) que representen tu tono natural.
- ¿Qué palabras o clichés odias y quedan terminantemente prohibidos (ej. "En el vertiginoso mundo digital", "desbloquear", "game-changer", "adéntrate", "revolucionario")?
- ¿Cómo se describe tu registro (ej. directo, quirúrgico, socrático, irónico, pedagógico)?

### Block 6: Pilares de Contenido y Rotación
- ¿Cuáles son tus 3 o 4 pilares temáticos de contenido (ej. Educación Técnica, Casos de Estudio/Prueba, Creencias Contrarias/Mentalidad, Estilo de Vida/Detrás de Cámaras)?
- ¿Cuál es el pilar prioritario para el primer lote de contenidos?
- ¿Qué cadencia realista puedes sostener (ej. 5 piezas semanales con 1–2 días de separación)?

### Block 7: Banco de Pruebas (Proof Bank)
- ¿Qué métricas reales, números verificables o casos de estudio concretos puedes compartir? (Cero cifras inventadas).
- Ejemplos: "Facturación de $X", "Retención del Y%", "Caso de [Cliente] que redujo su tiempo de Z a W horas".

### Block 8: Sistema de Diseño (sin HEX, sin nombres de fuente)

> **Regla de oro:** nunca pidas códigos HEX ni nombres de tipografía. El diseño se diseña a punta de preguntas de *vibe* y el agente deriva los tokens. Si la persona ya tiene HEX o fuentes y las ofrece, se honran tal cual y se saltan la derivación.

1. **Lienzo:** ¿Tu contenido se siente más a… noche de estudio (fondo oscuro tipo cine), editorial sobre papel (fondo claro), o un lienzo vivo de color saturado?
2. **Energía del acento:** ¿Qué emoción debe disparar el color de impacto: urgencia y ganancia (amarillo/ámbar), rebeldía o alarma (rojo), tech y precisión (cian eléctrico), premium calibrado (oro/dorado), orgánico y calma (verde)? Una o dos opciones.
3. **Voz tipográfica:** ¿Tu marca GRITA EN MAYÚSCULAS monumentales, susurra con serif editorial elegante, habla como terminal técnico mono, o conversa con sans humanista redonda?
4. **Geometría:** esquinas duras (radical, brutalista) o suaves (accesible, moderno)? Sombras duras estilo sticker, ¿sí o no?
5. **Referencias:** ¿qué cuentas o piezas físicas/visuales amas, y cuáles son anti-referencias prohibidas?
6. **Líneas de diseño:** ¿cuántas líneas de diseño quieres rotar (recomendado 3–5) y qué mapa funnel prefieres por línea (BOF/MOF/TOF)?

### Derivar los tokens (Bloque 8 ejecución)

Con las respuestas + `tone_of_voice.md` + el arquetipo de `brand_core.md`, el agente decide y **declara el resultado antes de escribir** (tabla de Lienzo/Lectura/Acento + 2 familias tipográficas + geometría) para aprobación en una línea. Después escribe:

- `design-system/tokens.css` — regenerado con los tokens de marca (mismos nombres de variables, los dos motores dependen de ellos).
- `design-system/DESIGN_SYSTEM.md` — secciones Color y Tipografía actualizadas con la paleta derivada y el nombre de la marca.
- `vault/Conceptos/visual_identity.md` — placeholders `{{SISTEMA_VISUAL}}`, `{{ATMOSFERA}}`, tablas HEX/fuentes llenas; `status: completo`.
- `vault/Conceptos/design_lines/` — duplica `_line_template.md` por cada línea elegida (`line-<id>.md` con arquetipo, pilar, funnel, tokens derivados de la paleta y posible variación de medio) y completa la tabla de `index.md`.
- `vault/00_Dashboard.md` — filas de estado (`pendiente` → `completo` para intake y visual).

---

## Scaffolding Phase (At completion)

When all 8 blocks are confirmed:

1. Write the full answers into `vault/Conceptos/00_brand_intake.md` (status `completo`).
2. Populate each individual markdown file in `vault/Conceptos/` (the 7 Brand Brain files above).
3. Execute Block 8: derive, declare, and write the design system + design lines (see Derivation above) — this is the step that "enchufa" los dos motores: los carruseles leen `design-system/tokens.css` vía `index.css` y el video mapea los tokens a variables CSS por composición.
4. Update `AGENTS.md`, `CLAUDE.md` and `README.md` replacing `{{NOMBRE_MARCA}}` with the real brand name.
5. Offer the final verification: run `/brand-audit` (placeholders 0, ratios 3:4/9:16, wiki-links vivos).

**The Wow Moment:** Prompt the user:

> *"Tu Brand Brain está completo, tu sistema de diseño es tuyo y único, y cada carrusel 3:4 y cada video 9:16 ya saldrá con tu paleta y tus fuentes. ¿Listo para producir? Abre sesión en `Content Manager/carousel-studio/` y usa su skill residente `/carousel-batch` para compilar tus primeros 5 carruseles 3:4, o escribe `/script-shortform` para redactar tu primer guion 9:16."*
