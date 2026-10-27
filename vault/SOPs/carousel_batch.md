# SOP: Batch Semanal de Carruseles (1 por Línea)

> **Propósito:** Producción secuencial por lotes ("Vueltas") con 1 carrusel por línea de diseño, separando estrictamente **Research → Copy → Prompts**.

---

## 1. Ciclo Secuencial (3 Fases Obligatorias)

> [!IMPORTANT]
> Prohibido generar prompts en paralelo al research o antes de aprobar el copy.

```
[FASE 1 · RESEARCH]
1. Leer el puntero de rotación en content_pillars.md.
2. Proponer al humano 1 ÁNGULO por línea.
3. 🛑 ESPERAR APROBACIÓN.
4. Investigar con fuentes fechadas, datos y frameworks.
5. Guardar en Content Manager/carousel-studio/batches/<vuelta>/<slug>/research.md.
            │
            ▼
[FASE 2 · NARRATIVA Y COPY]
1. Tesis + estructura slide a slide (SOP carousels.md).
2. Redactar copy.md con one-liners ≤ 12 palabras.
3. 1 acento por slide y CTA con keyword en MAYÚSCULAS.
            │
            ▼
[FASE 3 · DISEÑO & PROMPTS]
1. Prompts anclados al medio visual de cada línea (design_lines/line-*.md).
2. Ley del Hero Cover en slide 01.
3. Crear carpeta del proyecto + carousel.html con tokens.
4. Generar fondos bg_0X → auditoría → compilación a PNG.
```

---

## 2. Anatomía de Cada Slide del Batch

1. **One-liner monumental (≤ 12 palabras).**
2. **1 palabra de acento** con el token de la línea.
3. **Prompt de fondo (Clean Canvas):**
   - Proporción 3:4 vertical.
   - Sujeto en el 35–40 % inferior o lateral; 55–65 % superior limpio.
   - Sintaxis: `[SCENE]` `[SUBJECT]` `[LIGHTING]` `[CINEMATOGRAPHY & OPTICS]`.
   - Prompt negativo canónico (`visual_identity.md`).

---

## 3. Estructura de Archivos

```text
Content Manager/carousel-studio/batches/<vuelta>/<slug>/
├── research.md       # investigación de Fase 1
├── copy.md           # one-liners, jerarquía y prompts
├── assets/           # bg_01.jpg … bg_0N.jpg (fondos IA 3:4)
├── carousel.html     # lienzo con tokens de la línea
└── slides/           # PNG compilados con Playwright (slide-01.png …)
```

---

## 4. Criterios de Aprobación

1. Todos los fondos presentes.
2. Texto sobre espacio negativo sin pisar elementos complejos.
3. 1 acento por lámina + CTA claro.
4. Cadencia: {{HORARIO}} con 1–2 días de separación entre piezas de la rotación.
