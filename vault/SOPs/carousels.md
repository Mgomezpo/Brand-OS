# SOP: Carruseles Editoriales (3:4)

> **Propósito:** Estándar de estructura, copy y dirección de arte para carruseles de alto valor en Instagram / LinkedIn.
> **Inputs:** línea de diseño (`Conceptos/design_lines/`), pilar y keyword (`strategy/content_pillars.md`).

---

## 1. Reglas de Dirección de Arte

1. **Formato:** 1080 × 1440 px (3:4).
2. **Tipografía desnuda** sobre espacio negativo; nada de tarjetas grises tipo SaaS.
3. **Modelo híbrido:** fondo generado por IA (limpio, sin texto) + tipografía estampada en código (HTML/CSS → PNG).
4. **Cero texto en IA:** fondos sin letras, números, logos ni botones.

### Regla de 3 colores
1. **Fondo:** `--surface-page` de la línea.
2. **Lectura:** `--text-strong` / `--text-body`.
3. **Acento:** `--accent` → **una sola palabra por slide** + CTA.

### Ley del Hero Cover (Slide 01)
1. Nunca un fondo pasivo: hecho visual extraordinario (ángulo dramático, despiece flotante, pedestal, choque de materiales).
2. **One-liner monumental ≤ 12 palabras**, tono formativo ("Cómo lograr X", "El método de 3 pasos").
3. Doble registro tipográfico: display de la línea + acento serif itálica.

### Protocolo de rostros (`[CHARACTER SHEET INJECTION]`)
Cuando aparece el vocero o un referente: slot explícito en el prompt con imagen de referencia, descripción fisionómica idéntica entre slides.

---

## 2. Fórmula Canónica de 7 Slides

```
[1 Cover/Hook] ➔ [2 Dolor] ➔ [3 Giro] ➔ [4 Tesis/Oferta] ➔ [5 Mecanismo 1-2-3] ➔ [6 Prueba] ➔ [7 CTA]
```

| # | Slide | Función | Componentes |
| :-: | :--- | :--- | :--- |
| 1 | **Portada** | Pattern interrupt | Eyebrow (`{{CATEGORIA}} · 01/07`) + titular 2 líneas + subtítulo que derriba una creencia |
| 2 | **Dolor** | Conectar con Sistema 1 | Header de contraste crudo + escena de `user_persona.md` |
| 3 | **Giro cognitivo** | Cambiar el marco mental | El problema real no es el síntoma sino la arquitectura |
| 4 | **Tesis** | Nuevo vehículo | Declaración de principio, sin infocomercial |
| 5 | **Mecanismo** | Predictibilidad | 3 pasos numerados (`Step 01/02/03`) |
| 6 | **Prueba** | Validación empírica | Métrica gigante de `proof_bank.md` + explicación sobria |
| 7 | **CTA** | Conversión DM | Punchline + "Escribí `{{KEYWORD}}`…" |

> Variantes por arquetipo editorial (Datos, Mito vs Realidad, Kit, Historia): ver `design_lines/index.md`.

---

## 3. Caption en 4 Bloques (Fórmula Helder Peñaloza)

```
[1 · El alma del proyecto]  → 1–2 líneas coloquiales: marca, caso o fricción cotidiana.
[2 · El flujo técnico]      → qué insumos exactos se le dieron al sistema.
[3 · La prueba tangible]    → qué devolvió, sin vueltas.
[4 · CTA automatizado]      → "Comentá {{KEYWORD}} y te paso…"
```
- **Hashtags:** siempre en el primer comentario.
- Análisis completo: `Estrategia/referentes_ejemplo/helder-penaloza/`.

---

## 4. Checklist Pre-Render

- [ ] 1080 × 1440 px verificado
- [ ] Sin "developer mockup trap"
- [ ] Regla de 3 colores con tokens de la línea
- [ ] Regla de 2 tipografías
- [ ] Márgenes ≥ 96 px
- [ ] 1 acento por slide · keyword del funnel activo en MAYÚSCULAS
- [ ] Cifras presentes en `proof_bank.md`
- [ ] Copy pasa la lista negra de `tone_of_voice.md`
