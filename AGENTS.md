# {{NOMBRE_MARCA}} — Brand OS · Guía de Operación para Agentes de IA

> **Centro de Operaciones y Sistema Operativo de Contenidos de {{NOMBRE_MARCA}}**  
> Este documento establece la arquitectura canónica definitiva del workspace. Cualquier agente de IA (Antigravity, Claude, Codex, Gemini) debe seguir estrictamente estas definiciones para evitar duplicidad y mantener un estándar de calidad **tope de gama**.

---

## 🏛️ Los 4 Pilares del Workspace

El workspace está estructurado con Obsidian en la cima comandando la fábrica de contenidos:

```
Brand OS/
│
├── 🧠 vault/                  → OBSIDIAN ARRIBA (Torre de Control & Araña de Instrucciones MD)
│   ├── 00_Dashboard.md        → Centro de comando con visión 360° del ecosistema
│   ├── Board.md               → Tablero Kanban unificado (Ideas ➔ Producción ➔ Funnel ➔ Publicado)
│   ├── Findings.md            → Bitácora de aprendizajes de contenido y retención
│   ├── Repos.md               → Banco de herramientas y descubrimientos técnicos
│   ├── Conceptos/             → Brand Brain (intake, núcleo, audiencia, voz, visual, pilares, pruebas)
│   ├── Estrategia/            → Frameworks de guionización + Research empírico + Referentes UNIFICADOS
│   ├── SOPs/                  → Procedimientos maestros (hooks, guiones, carruseles 3:4, video, funnels)
│   └── Templates/             → Plantillas estandarizadas de notas de proyecto, guiones y lotes
│
├── 🎨 design-system/          → LA FUENTE CANÓNICA DE MARCA (Tokens CSS, SVG, Grillas 3:4 y 9:16)
│   ├── DESIGN_SYSTEM.md       → Especificación de proporciones, colores y tipografías
│   ├── tokens.css             → Variables de superficies, lectura y acento focal
│   ├── index.css              → Estilos deterministas de diapositivas 3:4 (1080 × 1440 px)
│   └── svg/                   → Gráficos vectoriales limpios
│
├── 🚀 Content Manager/         → LA FÁBRICA DE CONTENIDOS (Engines y Software Determinista)
│   ├── carousel-studio/       → Estudio de carruseles 3:4 (Playwright + batch_manager.py)
│   ├── video-studio/          → Estudio de video 9:16 (HyperFrames + GSAP + ElevenLabs)
│   ├── pipeline/              → Mesa de ensamblaje transversal (40_postprocessing)
│   └── helper/                → Embudos transversales (Zernio comment-to-DM)
│
├── ⚙️ connections.md          → Registro de motores, APIs y renderizadores alcanzables
├── 📈 EXPANSIONS.md           → Guía de escala: qué agregar, cadencias y anti-patrones
└── 🤖 AGENTS.md / CLAUDE.md   → Esta guía operativa
```

---

## ⚡ Skills Integradas (Built-in Skills)

Ejecuta estas skills en Claude Code, Codex o Antigravity:

| Skill | Descripción | Cuándo ejecutar |
|---|---|---|
| `/brand-onboard` | Asistente de intake de marca en 7 bloques | Día 1, o al pivotar el posicionamiento. Puebla `vault/Conceptos/`. |
| `/brand-audit` | Auditoría de integridad, ratios y márgenes | Tras el setup, semanalmente o antes de compilar. Verifica 3:4, 9:16, márgenes de 96px, pruebas reales y enlaces wiki. |
| `/carousel-batch` | Motor de producción de carruseles 3:4 en 3 fases | Producción semanal. Genera 5 carruseles 3:4 deterministas (1080 × 1440 px). |
| `/script-shortform` | Generador de guiones de video 9:16 de alta retención | Para Reels/TikTok/Shorts. 4 movimientos (hook <12 palabras, tensión, mecanismo, CTA) con direcciones visuales. |
| `/grill-me` | Entrevista adversarial de contexto | Antes de redactar contenido. Pone a prueba ángulos y creencias contrarias contra el Brand Core. |
| `/level-up` | Loop de calibración semanal y aprendizajes | Retro semanal. Actualiza `vault/Findings.md` con retención y `vault/Repos.md` con hallazgos técnicos. |

---

## 🧠 Orden de Lectura Obligatorio para Agentes

Antes de proponer o escribir cualquier contenido:

1. `vault/Conceptos/brand_core.md` → Quién es la marca (misión, arquetipo, creencias contrarias).
2. `vault/Conceptos/user_persona.md` → A quién le habla (la escena del dolor cotidiana).
3. `vault/Conceptos/positioning.md` + `offer.md` → Qué vende, mecanismo único y keywords de DM.
4. `vault/Conceptos/tone_of_voice.md` → Cómo habla (registros y lista negra anti-AI-slop).
5. `vault/Conceptos/content_pillars.md` → De qué habla y cuál es la línea activa en la rotación.
6. `vault/Conceptos/visual_identity.md` → Cómo se ve (carruseles 3:4, video 9:16).
7. `vault/Conceptos/proof_bank.md` → Qué datos y métricas reales puede citar (cero cifras inventadas).

---

## 🚫 Reglas Inmutables para Agentes (Guardrails)

1. **El Vault es 100% Markdown de Instrucciones:** Nunca colocar archivos de salida pesados (MP4s, renders masivos de PNGs) en `vault/`.
2. **Estudios por fuera del Pipeline:** El video se edita en `video-studio/` y los carruseles se compilan en `carousel-studio/`. El `pipeline/` es solo la mesa de trabajo y postprocesamiento.
3. **Formato Canónico de Carruseles: Proporción 3:4 (1080 × 1440 px).** Prohibido usar 4:5 o formatos cuadrados.
4. **Formato Canónico de Video: Proporción 9:16 (1080 × 1920 px).**
5. **Cero Texto en Imágenes de IA:** Los fondos generados por IA se solicitan 100% limpios de letras, logos y botones. La tipografía se estampa en código HTML/CSS determinista.
6. **Separación de Fases en Batches:** Research puro ➔ Aprobación ➔ Copy de One-Liners ➔ Prompts visuales. Prohibido redactar prompts antes de aprobar el copy.
7. **Regla de 3 Colores:** Fondo (`--surface-page`), Lectura (`--text-strong`), Acento (`--accent`). Solo **1 palabra resaltada por pantalla** y el CTA.
