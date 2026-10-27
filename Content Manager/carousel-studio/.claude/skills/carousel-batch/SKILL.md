---
name: carousel-batch
description: Resident operator skill of carousel-studio — runs the weekly 3:4 carousel batch (1 carousel per design line, canvas 1080 × 1440 px, PNG export 2× = 2160 × 2880). Thin operator of the canon — vault SOPs and this studio's README prevail over this file. Strictly separates research, human approval, one-liner copy, per-line AI visual prompts, and deterministic Playwright compilation.
---

## What this skill does

Runs the weekly carousel batch: **1 carrusel por cada línea de diseño activa** (rotación pentagonal). Este skill es el **operador** del estudio; el canon vive en el vault y prevalece sobre este archivo:

- **Protocolo y fases:** `../../vault/SOPs/carousel_batch.md`
- **Fórmula de slides y dirección de arte:** `../../vault/SOPs/carousels.md`
- **Comandos y anatomía de archivos:** `README.md` de este estudio

Nunca inventes reglas nuevas: si algún número de este archivo choca con los SOPs o con el README del estudio, ganan ellos.

## Fase 0 — Contexto del batch

1. Lee `../../vault/Conceptos/content_pillars.md` (§4): el puntero de rotación (vuelta activa y líneas que tocan).
2. El batch produce **5 carruseles** (1 por línea). La **publicación** se dosifica 1–2 carruseles/semana según `../../vault/Estrategia/Frameworks-de-Guionizacion/matriz_de_formatos.md` (reels: TOFU; carrusel: MOFU de guardados).

## Fase 1 — Ángulo + Research (aprobación antes que todo)

1. Lee `../../vault/Conceptos/content_pillars.md` (pilar activo por línea) y cruza la escena de dolor de `../../vault/Conceptos/user_persona.md`.
2. Selecciona el ángulo con el router `../../vault/Estrategia/Frameworks-de-Guionizacion/decision_tree.md` (8 frameworks reales en 4 ramas).
3. Propón **1 ángulo por línea con 2–3 variantes de hook** (≤ 12 palabras, ideal 8–10).
4. 🛑 **ESPERAR APROBACIÓN HUMANA** — prohibido redactar slides ni prompts con hooks no aprobados.
5. Con el ángulo aprobado: investiga con **fuentes fechadas**, datos y frameworks → guarda `batches/<vuelta>/<slug>/research.md`. Toda cifra citada debe existir en `../../vault/Conceptos/proof_bank.md`.

## Fase 2 — Copy (Fórmula Canónica de 7 Slides)

Estructura pegada al canon (`../../vault/SOPs/carousels.md` §2): `[1 Cover] → [2 Dolor] → [3 Giro] → [4 Tesis] → [5 Mecanismo 1-2-3] → [6 Prueba] → [7 CTA]` — variantes por arquetipo editorial en `../../vault/Conceptos/design_lines/line-<id>.md`.

Escribe `batches/<vuelta>/<slug>/copy.md`:

- **One-liner monumental por slide ≤ 12 palabras** (incluido el Hero Cover). `copy.md` es la fuente del texto.
- Máximo 25 palabras por slide; los bullets son one-liners (nunca párrafos).
- **Regla de 3 colores** con tokens de la línea: `--surface-page` (fondo) · `--text-strong`/`--text-body` (lectura) · `--accent` — **1 sola palabra en acento por slide**.
- Slide 7 (CTA): acción explícita con la keyword de DM de `../../vault/Conceptos/offer.md` en MAYÚSCULAS.
- Hero Cover según la Ley del Hero Cover (`../../vault/SOPs/carousels.md` §1).
- Doble registro tipográfico: display de la línea + acento serif itálica donde aplique.

Marca el gate de copy en la conversación: 🛑 **sin copy aprobado por el dueño, Fase 3 no arranca** (el TRACKER refleja solo el estado de fondos/compilado que calcula `batch_manager.py status`).

## Fase 3 — Prompts Visuales (por línea) + Compilación

**RULE: prohibido escribir prompts antes de que el copy esté aprobado.**

1. Los prompts de fondo se **anclan a la línea** (`../../vault/Conceptos/design_lines/line-<id>.md` §4): medio visual nativo, sujetos permitidos/prohibidos, sintaxis `[SCENE]` · `[SUBJECT]` · `[LIGHTING]` · `[CINEMATOGRAPHY & OPTICS]`, **prompt negativo canónico** de `../../vault/Conceptos/visual_identity.md`, encuadre 3:4 con sujeto en el 35–40% inferior/lateral y 55–65% superior limpio.
2. Genera `batches/<vuelta>/<slug>/assets/bg_01.jpg … bg_0N.jpg` (IA **100% limpia** de texto: sin letras, números, logos ni botones) → mini-auditoría visual de limpieza → guarda bajo el slug.
3. Construye `batches/<vuelta>/<slug>/carousel.html` cargando el sistema de diseño — desde el HTML son **5 niveles de subida** hacia la raíz: `@import "../../../../../design-system/index.css";` (que a su vez importa `tokens.css`) — más los tokens de la línea de este carrusel. Márgenes de 96 px en todos los bordes.
4. Compila (desde la raíz de este estudio):
   ```bash
   python batch_manager.py compile <slug>   # pieza del batch: carousel.html → slides/*.png
   npm run capture -- <slug>/carousel.html  # compilación de una pieza suelta
   ```
   Canvas **1080 × 1440 px** (3:4); el motor exporta a **2× DPI (PNG 2160 × 2880)**.
5. Checklist pre-render (`../../vault/SOPs/carousels.md` §4): ratio verificado, sin "developer mockup trap", 3 colores, 2 tipografías, ≥96 px, 1 acento por slide, cifras en `../../vault/Conceptos/proof_bank.md`, copy pasa la lista negra de `../../vault/Conceptos/tone_of_voice.md`.
6. Corre `python batch_manager.py status` tras compilar para verificar el lote (el estado vive en la consola del gestor, no en tableros persistidos) y avanza el puntero de la vuelta en `../../vault/Conceptos/content_pillars.md` (§4); el paquete final sale por `../postprocessing/<slug>/` (SOP: `../../vault/SOPs/funnels_publicacion.md`, caption en 4 bloques según `../../vault/SOPs/carousels.md` §3).

## Mantenimiento

Espejo de este skill a `.agents/`: desde la **raíz del workspace** corre `python scripts/sync-skills.py` (también sincroniza las skills de marca y tiene modo `--check`).
