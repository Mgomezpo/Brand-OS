---
name: brand-onboard
description: Use on Day 1 of a Brand OS install, or when someone says "configura mi marca", "onboard me", "iniciar marca", "set up my brand", or wants to populate the Brand Brain. Runs a 7-block interactive interview and scaffolds the canonical Brand Brain in vault/Conceptos/.
---

## What this skill does

Conducts an interactive, structured 7-block interview to extract the complete Brand Brain of the user or client. As each block is answered, it updates `vault/Conceptos/00_brand_intake.md` and generates or updates the 7 core Brand Brain files in `vault/Conceptos/`:

1. `brand_core.md` (Mission, archetype, contrarian beliefs, brand narrative)
2. `user_persona.md` (Target audience, the daily scene of pain, micro-frustrations)
3. `positioning.md` (Category, enemy, unique mechanism, unfair advantage)
4. `offer.md` (Core offer, deliverables, pricing tier, DM funnel keyword)
5. `tone_of_voice.md` (Communication registers, vocabulary rules, forbidden AI-slop blacklist)
6. `content_pillars.md` (The 4 content lines, weekly rotation schedule, ratio)
7. `proof_bank.md` (Verified metrics, client case studies, data points, testimonials)

It also replaces all generic `{{NOMBRE_MARCA}}` and `{{NOMBRE_CREADOR}}` placeholders with the user's authentic brand and creator name.

## The Interview Process (7 Blocks)

Ask **one question at a time**. Never overwhelm the user by dumping all 7 blocks at once. Checkpoint answers into `vault/Conceptos/00_brand_intake.md` as you progress.

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

### Block 7: Banco de Pruebas (Proof Bank)
- ¿Qué métricas reales, números verificables o casos de estudio concretos puedes compartir? (Cero cifras inventadas).
- Ejemplos: "Facturación de $X", "Retención del Y%", "Caso de [Cliente] que redujo su tiempo de Z a W horas".

---

## Scaffolding Phase (At completion)

When all 7 blocks are confirmed:

1. Write the full answers into `vault/Conceptos/00_brand_intake.md`.
2. Populate each individual markdown file in `vault/Conceptos/`:
   - `brand_core.md`
   - `user_persona.md`
   - `positioning.md`
   - `offer.md`
   - `tone_of_voice.md`
   - `content_pillars.md`
   - `proof_bank.md`
3. Update `AGENTS.md` and `CLAUDE.md` replacing `{{NOMBRE_MARCA}}` with the real brand name.
4. **The Wow Moment:** Prompt the user:
   > *"Tu Brand Brain está completamente configurado y blindado contra AI-slop. ¿Listo para producir? Escribe `/carousel-batch` para compilar tus primeros 5 carruseles 3:4 o `/script-shortform` para redactar tu primer guion 9:16."*
