# Frontera Arquitectónica: Inteligencia Artificial vs. Código Determinista

Uno de los errores más comunes en sistemas de marketing automatizado modernos es confiarle a los LLMs la generación de imágenes completas (mediante difusión tipo Midjourney/DALL-E) o permitir que la IA decida la posición absoluta de los elementos gráficos en un canvas. Esto produce alucinaciones visuales, textos deformados, inconsistencia de marca y pérdida del estándar tipográfico.

En **Brand OS Engine**, la frontera entre **Inteligencia Artificial** y **Código Determinista** está trazada con precisión matemática:

---

## 1. Matriz de Responsabilidad Técnica

| Componente del Sistema | Tecnología Utilizada | ¿Usa IA? | Justificación Técnica |
| :--- | :--- | :---: | :--- |
| **Ingesta de Ontologías** | Arrays y Objetos ECMAScript (`topics.mjs`) | **NO** | Las tesis y ganchos base están estructurados en código para garantizar veracidad técnica. |
| **Repurposing de Eventos** | `DeepSeek V4 Flash` (NVIDIA NIM API, Temp 0.3) | **SÍ** | Transforma 1 evento crudo de desarrollo en 3 perspectivas editoriales diferenciadas. |
| **Deduplicación Semántica** | Hashing de Palabras Normalizado (1536 dims) + Coseno | **NO** | Algoritmo determinista local de bolsa de palabras en Cero-Latencia sin costes de tokens. |
| **Tier 1: Filtro Determinista** | Expresiones Regulares compiladas (Regex) | **NO** | Bloqueo inmutable en 0 ms de clichés de marketing, humo y preguntas retóricas. |
| **Tier 2: Linter Semántico** | `DeepSeek V4 Flash` (LLM-as-a-Judge, Temp 0.0) | **SÍ** | Auditor implacable que evalúa voz, especificidad y outcome con rúbrica estricta (>= 8.5). |
| **Composición de Layouts** | HTML5 semántico + CSS3 moderno (Flexbox/Grid) | **NO** | Los márgenes, tipografías, badges y cajas se calculan matemáticamente con CSS. |
| **Renderizado de Activos** | Playwright (Chromium Headless, 1080 × 1440 @ 2x DPI) | **NO** | Compilación determinista a nivel de píxel idéntica al render de un navegador. |
| **Composición de Video** | GreenSock Animation Platform (GSAP) + HyperFrames | **NO** | Curvas Bézier y transiciones temporales calculadas en código a 60 fps (sin Remotion). |
| **Gateway de Publicación** | Fetch API + Zernio REST Endpoints | **NO** | Subida multipart al CDN y despacho programado con aislamiento de cuentas. |

---

## 2. Los Modelos de IA en Detalle

### A. Tier 2: Linter Semántico (LLM-as-a-Judge)
* **Archivo:** `core/linter/semantic-judge.mjs`
* **Modelo:** `deepseek-ai/deepseek-v4-flash-0731`
* **Proveedor:** NVIDIA NIM API (`https://integrate.api.nvidia.com/v1`)
* **Parámetros:** `temperature: 0.0`, `response_format: { type: "json_object" }`, `max_tokens: 300`, `timeout: 30000ms`.
* **Misión:** Actuar como Director Editorial despiadado. No escribe contenido; solo audita y califica el borrador contra el archivo `brand.json` de la marca.
* **Rúbrica Ponderada:**
  $$\text{Score} = (0.25 \times \text{Tono}) + (0.25 \times \text{AntiCliché}) + (0.25 \times \text{Especificidad}) + (0.25 \times \text{Outcome})$$
* **Umbral de Aprobación:** $\text{Score} \ge 8.5 / 10$. Si el score es inferior, el pipeline aborta la compilación.

### B. Repurposing Cruzado (Cross-Pollination)
* **Archivo:** `core/repurposer/cross-pollinate.mjs`
* **Modelo:** `deepseek-ai/deepseek-v4-flash-0731`
* **Parámetros:** `temperature: 0.3`, `response_format: { type: "json_object" }`.
* **Misión:** Recibir un hecho operativo de la ingeniería (ej. *"Hoy desplegamos un worker en Node que reduce la latencia de render a 8 segundos"*) y proyectarlo simultáneamente en:
  1. {{MARCA_B2B}}: Enfoque de costo financiero y margen de agencia.
  2. {{MARCA_APP}}: Enfoque de cómo ordenar notas caóticas hacia el calendario.
  3. {{NOMBRE_CREADOR}} {{APELLIDO_CREADOR}}: Enfoque en primera persona con vos (*"Mirá, me cansé de..."*).
* **Fallback:** Si la API no responde, el sistema cuenta con un fallback determinista curado para no interrumpir el pipeline.

---

## 3. Por Qué el Diseño Visual es 100% Código Determinista

1. **Nitidez Tipográfica Absoluta:** Las fuentes Google Fonts (`Fraunces`, `Space Grotesk`, `Inter`, `Outfit`, `JetBrains Mono`) se renderizan como curvas vectoriales nativas en Chromium, evitando la rasterización borrosa de los modelos generativos de imágenes.
2. **Jerarquía Visual Inmutable:** Las distancias (padding de 85px, divisores de 100px, tarjetas de métrica con padding de 36px y bordes de 4px) son invariantes y respetan las proporciones áureas y la grilla suiza.
3. **Consistencia de Identidad:** El color `#BFA175` de {{MARCA_B2B}} o el `#9F1522` de {{MARCA_APP}} nunca sufren alteraciones de matiz o tono entre una diapositiva y otra.
4. **Cero Dependencia de Herramientas Externas:** No se requiere abrir Figma, exportar SVGs manualmente ni pagar suscripciones de Canva o software de plantillas.
