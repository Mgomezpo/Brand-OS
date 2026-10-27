# EXPANSIONS — Guía de Crecimiento y Escalabilidad

Brand OS se entrega como un núcleo limpio y determinista: un cerebro de marca en Markdown (Obsidian), un sistema de diseño con tokens CSS canónicos (3:4 y 9:16), una fábrica de contenidos automatizada y 6 skills interactivas.

A medida que tu marca escale o que gestiones múltiples marcas clientes, utiliza esta guía para saber qué agregar, cuándo hacerlo y qué trampas evitar.

La estructura de Brand OS debe operar como un estudio de diseño y producción de alta gama: organizado, determinista y libre de desorden.

---

## 📦 Lo que viene en el Kit (No eliminar)

| Carpeta / Archivo | Propósito |
|---|---|
| `vault/` | Torre de control en Obsidian. Contiene el cerebro de marca, tablero Kanban, bitácora de hallazgos, repositorios, estrategias y SOPs. |
| `vault/Conceptos/` | Brand Brain unificado: intake, brand core, persona, posicionamiento, oferta, voz, pilares y banco de pruebas. |
| `design-system/` | Fuente canónica de diseño. Proporciones 3:4 (1080 × 1440 px), tokens CSS, tipografías y vectores limpios. |
| `Content Manager/` | Motores de renderizado y automatización: `carousel-studio/`, `video-studio/`, `pipeline/` y `helper/`. |
| `connections.md` | Registro de motores y servicios integrados (Playwright, Whisper, Zernio). |
| `CLAUDE.md` / `AGENTS.md` | Manuales operativos raíz para Claude Code, Antigravity y Codex. |
| `.claude/skills/` y `.agents/skills/` | Paquetes de skills: `/brand-onboard`, `/brand-audit`, `/carousel-batch`, `/script-shortform`, `/grill-me`, `/level-up`. |

---

## 🚀 Qué agregar a medida que escalas

| Superficie | Cuándo agregar | Por qué |
|---|---|---|
| `vault/Conceptos/design_lines/` | Tienes 2+ sub-estilos visuales (ej. editorial oscuro, high-contrast minimal, infográfico). | Permite al carrusel alternar paletas de tokens sin romper la grilla 3:4 base. |
| `Content Manager/video-studio/style-library/` | Creas nuevos templates de animación en GSAP o HyperFrames. | Reutilización de transiciones y overlays cinemáticos sin reescribir código. |
| `references/case-studies/` | Cierras clientes o acumulas métricas de retención sobresalientes. | Nutre directamente a `vault/Conceptos/proof_bank.md` para respaldar copies con datos duros. |
| `brands/{cliente-id}/` | Operas como agencia gestionando múltiples marcas. | Arquitectura multitenant: cada cliente tiene su propio `vault/` aislado compartiendo los motores de `Content Manager/`. |
| `references/{tool}-api.md` | Integras una nueva API de redes, webhook de ManyChat o conector MCP. | Documentación técnica investigada una sola vez (`vault/Repos.md`). |
| `audits/` | Se generan reportes automáticos al ejecutar `/brand-audit`. | Bitácora de calidad, verificación de márgenes seguros y cumplimiento de ratios. |

---

## ⏱️ Cadencia de Mantenimiento Recomendada

- **Diario / Por Lote:** Mover tarjetas en `vault/Board.md` (`💡 Ideas` ➔ `🎬 Producción` ➔ `🧲 Funnel` ➔ `🚀 Publicado`).
- **Semanal:** Ejecutar `/level-up` para analizar métricas de retención y registrar aprendizajes en `vault/Findings.md`.
- **Mensual:** Ejecutar `/brand-audit` para certificar que ningún archivo contenga placeholders sin rellenar o desviaciones de proporción.
- **Trimestral:** Ejecutar `/grill-me` sobre el Brand Brain para actualizar `user_persona.md`, `offer.md` y refrescar el mecanismo único contra la competencia.

---

## 🚫 Anti-patrones (Qué NO hacer)

- **Prohibido guardar renders pesados en `vault/`:** Los MP4 finales y lotes de PNGs van en `Content Manager/` o almacenamiento en la nube; el vault es 100% Markdown liviano.
- **Prohibido romper la proporción 3:4 en carruseles:** No uses formatos 4:5 (1080 × 1350 px) ni cuadrados. La norma universal de Brand OS es 1080 × 1440 px.
- **Prohibido solicitar texto en imágenes de IA:** Los fondos se generan 100% limpios de letras y logos. La tipografía siempre se estampa en HTML/CSS determinista.
- **Prohibido inventar datos en los guiones:** Todo número citado debe existir previamente en `vault/Conceptos/proof_bank.md`.
- **Prohibido crear carpetas basurero:** Evita carpetas como `varios/`, `temp/` o `notas/`. Si una idea no está lista, entra como tarjeta en `vault/Board.md`.

---

> *Un sistema de marca de alta fidelidad no acumula ruido: estandariza procesos deterministas para que la creatividad humana opere a máxima velocidad con cero fricción.*
