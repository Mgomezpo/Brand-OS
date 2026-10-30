---
tags: [brand-brain, intake]
status: pendiente
---

# 📝 Brand Intake — Entrevista de Arranque (8 Bloques)

> **Propósito:** Cuestionario maestro para poblar el Brand Brain de una marca nueva. El agente lo conduce **una pregunta a la vez** (skill `/brand-onboard`) y vuelca cada respuesta en el documento destino indicado.
> **Regla:** No inventar respuestas. Si el humano no sabe, marcar `⚠️ HIPÓTESIS` y validar con datos en 30 días.
> **Espejo:** Este archivo es el gemelo operativo de `.claude/skills/brand-onboard/SKILL.md` — si cambia una pregunta, cambian ambos.

---

## Bloque 1 · Identidad y Misión → `Conceptos/brand_core.md`
1. Nombre de la marca y quién está detrás (persona, empresa, producto)?
2. Misión principal: el problema del mundo que la indigna.
3. Creencia contraria (lo que el nicho acepta y la marca rechaza): 2–3.
4. Arquetipo (Sabio, Rebelde, Creador, Explorador, Cuidador, Héroe, Mago, Bufón, Amante, Gobernante, Inocente, Persona Común).
5. Anti-identidad: ¿qué NO es la marca?

## Bloque 2 · Audiencia → `Conceptos/user_persona.md` + `Conceptos/jtbd_forces.md`
6. ICP: rol, contexto, momento de vida/negocio.
7. Escena exacta del dolor (lugar, hora, herramienta, emoción).
8. Qué solucionó antes y por qué falló.
9. Qué lo frena a comprar (ansiedades y hábitos).
10. ¿Cómo se ve su "después" ideal?

## Bloque 3 · Posicionamiento → `Conceptos/positioning.md`
11. Categoría donde juega y enemigo común (mentalidad obsoleta, práctica tóxica, falso gurú).
12. Mecanismo único con nombre memorable (el "cómo" propietario).
13. Contra qué alternativas compite (incluida "no hacer nada").

## Bloque 4 · Oferta → `Conceptos/offer.md`
14. Qué vende exactamente (producto/servicio, formato de entrega).
15. Entregable principal y rango de precio o nivel de la oferta.
16. Qué incluye y qué NO incluye la oferta.

## Bloque 5 · Voz → `Conceptos/tone_of_voice.md`
17. Idioma, país/región y trato (tú / vos / usted).
18. Pega 1–2 textos reales tuyos que representen tu tono natural.
19. 3 adjetivos de cómo suena · 3 de cómo NUNCA suena.
20. Palabras propias (léxico canónico) y expresiones prohibidas (lista negra anti-AI-slop).

## Bloque 6 · Banco de Pruebas → `Conceptos/proof_bank.md`
21. Métricas reales verificables (facturación, retención, horas ahorradas) — cero cifras inventadas.
22. Casos de estudio y testimonios con nombre/situación concretos.

## Bloque 7 · Contenido y Rotación → `Conceptos/content_pillars.md`
23. Plataformas y cadencia realista (ej. 5 piezas semanales, 1–2 días de separación).
24. 3–4 pilares temáticos y cuál arranca el primer lote.
25. Referentes admirados → `Estrategia/Referentes-y-Benchmarking/`.

## Bloque 8 · Sistema de Diseño → `Conceptos/visual_identity.md` + `design-system/` + `design_lines/`

> **Nunca pedir HEX ni tipografías.** Se diseña a punta de preguntas de *vibe* y el agente deriva los tokens. Si la persona ya tiene colores/fuentes exactas y las ofrece, se honran tal cual.

26. Lienzo: noche de estudio (oscuro) / editorial de papel (claro) / lienzo vivo saturado.
27. Energía del acento: amarillo-ámbar (ganancia), rojo (rebeldía/alarma), cian (tech), dorado (premium), verde (orgánico) — 1–2 opciones.
28. Voz tipográfica: MAYÚSCULAS monumentales / serif editorial / mono técnico / sans humanista.
29. Geometría: esquinas duras o suaves; sombras duras estilo sticker ¿sí o no?
30. Referencias que ama y anti-referencias prohibidas.
31. ¿Cuántas líneas de diseño rotar (recomendado 3–5) y mapa funnel por línea (BOF/MOF/TOF)?

**Salidas del Bloque 8** (contrato de enchufado): `design-system/tokens.css` + `DESIGN_SYSTEM.md` regenerados con los tokens de marca, `visual_identity.md` lleno (`status: completo`), `design_lines/index.md` + `line-<id>.md` por línea, y `{{NOMBRE_MARCA}}` reemplazado en `AGENTS.md`, `CLAUDE.md` y `README.md`.
