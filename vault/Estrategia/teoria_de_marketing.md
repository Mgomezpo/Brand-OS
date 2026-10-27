# Teoría de Marketing — Frameworks Estratégicos

> **Propósito:** Marcos conceptuales universales que sustentan la psicología del contenido y la ingeniería del pipeline. Independientes de la marca.

---

## 1. El Bucle de 4 Capas (Operating Loop)

```
[1. RAW] ➔ [2. WIKI] ➔ [3. RULES & SKILLS] ➔ [4. VERIFICATION]
```

1. **Raw:** ingesta inmutable de notas, transcripciones, ideas de voz, referencias. Nunca se edita.
2. **Wiki:** síntesis en SOPs, conceptos y guías interconectadas. Fuente única de verdad (`Conceptos/`, `SOPs/`).
3. **Rules & Skills:** reglas de calidad, prompts y agentes que consultan la Wiki.
4. **Verification:** revisión humana o algorítmica (linter de copy, checklist de diseño, métricas) antes de publicar.

---

## 2. Jobs to Be Done (Christensen & Moesta)

- La gente no compra productos: **contrata** una solución para progresar en una circunstancia.
- La demografía no explica la compra. La explican las **4 fuerzas**: Push (dolor) + Pull (atracción) vs Ansiedad + Hábito.
- El contenido más efectivo describe con precisión quirúrgica **el momento** en que se siente la fricción.
- Plantilla de marca: `Conceptos/audience/jtbd_forces.md`.

---

## 3. Sistema 1 y Sistema 2 (Kahneman)

- **Sistema 1** (rápido, emocional) controla el pulgar. Hook y portada deben procesarse en **< 0.8 s**: contraste, rostros, ruptura de expectativa.
- **Sistema 2** (lento, analítico) se activa solo si el 1 se detuvo. Exige lógica, datos, pasos numerados.
- **Regla:** *Atrapá con el Sistema 1, convencé con el Sistema 2 y cerrá facilitando la decisión al Sistema 1 (keyword por DM).*

---

## 4. Niveles de Consciencia (Eugene Schwartz)

| Nivel | El usuario… | El contenido debe… | Funnel |
| :--- | :--- | :--- | :--- |
| Inconsciente | No sabe que tiene el problema | Despertar alerta con contraste | TOF |
| Consciente del problema | Siente el dolor, no conoce soluciones | Diagnosticar causa raíz | TOF/MOF |
| Consciente de la solución | Conoce opciones | Comparar, mostrar mecanismo | MOF |
| Consciente del producto | Conoce la marca | Prueba, oferta, urgencia | BOF |
| Totalmente consciente | Listo | CTA directo | BOF |

---

## 5. Sistema de Producción de 30 Activos (Backtracking)

- Sustituir inspiración esporádica por una línea de montaje predecible.
- **Paquete mensual:** 10 TOF (Reels) · 12 MOF (Carruseles/guías) · 8 BOF (casos, comparativas, oferta).
- **Backtracking:** diseñar primero la conversión final y trabajar hacia atrás los contenidos que educan y desarman objeciones.

---

## 6. Principios Psicológicos Obligatorios

1. **Brecha de información (Loewenstein):** abrir una incógnita que solo se cierra viendo el desarrollo.
2. **Aversión a la pérdida (Kahneman):** formular el problema desde el coste del error (pesa ~2× más que la ganancia).
3. **Heurística de especificidad:** nombres exactos, cifras concretas; cero abstracciones ("herramientas", "productividad").
4. **Doble codificación (Paivio):** el texto en pantalla complementa o contradice la voz, nunca la repite.

---

## 7. Arquitectura Híbrida Zero-Template

- **Trampa del HTML puro:** LLMs maquetando sin dirección de arte producen "developer mockups" (cajas grises, botones web).
- **Modelo híbrido:**
  - **IA (no determinista):** concepto, copy, fotografía/ilustración de fondo con espacio negativo.
  - **Código (determinista):** HTML + tokens CSS + navegador headless (Playwright / HyperFrames) renderizan tipografía al píxel (1080 × 1440 / 1080×1920).
- Profundización: `Estrategia/arquitectura_contenido/manifiesto-ia-vs-determinismo.md`.
