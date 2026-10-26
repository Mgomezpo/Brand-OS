# Ingesta de Temas, Memoria Vectorial y Filtros Deterministas

Este documento explica de dónde sale el contenido, cómo se procesa y qué mecanismos matemáticos y algorítmicos evitan la repetición temática o la emisión de contenido de baja calidad.

---

## 1. Fuentes de Ingesta de Contenido

El motor soporta dos modalidades complementarias de ingesta:

### A. Ontología Editorial Estructurada (`brands/[brand]/topics.mjs`)
Cada marca dispone de una matriz de temas diseñada de acuerdo con su audiencia. Cada tema contiene:
- `vertical`: Subsegmento o industria objetivo (ej. *Agencias de Branding*, *Creadores de Contenido*, *Builders Tech*).
- `pillar`: Pilar de pensamiento o problema a resolver.
- `hook`: Gancho de alta tensión con datos cuantitativos o contraste directo.
- `coreThesis`: Fundamento del razonamiento.
- `slides`: Array de entre 4 y 8 objetos con `{ title, body, badge, metric }`.
- `caption`: Copy extendido para el pie de foto en redes sociales.
- `cta`: Llamado a la acción sobrio y directo.

### B. Ingesta Reactiva por Repurposing (`core/repurposer/cross-pollinate.mjs`)
Permite introducir un evento técnico real de la vida diaria de desarrollo o negocio mediante el comando:

```bash
npm run repurpose -- --event "Ayer desplegamos un worker en Node que genera carruseles en 8 segundos"
```

El modelo `DeepSeek V4 Flash` (o su fallback determinista) toma este único hecho y deriva 3 perspectivas simultáneas:
1. **{{MARCA_B2B}}:** Lo enfoca en el ahorro mensual de horas no facturables en agencias.
2. **{{MARCA_APP}}:** Lo enfoca en la fluidez de pasar de notas desordenadas a un calendario.
3. **{{NOMBRE_CREADOR}} {{APELLIDO_CREADOR}}:** Lo narra como una lección de arquitectura técnica en primera persona con vos.

---

## 2. Memoria Semántica y Deduplicación Vectorial (90 Días)

Para asegurar que una marca no repita el mismo ángulo o mensaje en semanas consecutivas, `core/memory/vector-memory.mjs` implementa un sistema de memoria vectorial local con ventana deslizante de **90 días**:

### Algoritmo de Hashing de Características (1536 Dimensiones)
En lugar de depender de APIs externas de embeddings lentas y con coste recurrente, se utiliza una técnica de hashing determinista sobre el espacio léxico:
1. Se limpia y tokeniza el texto del gancho y la tesis.
2. Cada palabra se proyecta sobre un vector de 1536 dimensiones mediante una función de dispersión por desplazamiento de bits (Bitwise Hash Trick).
3. El vector resultante se normaliza a norma unitaria ($L_2$):
   $$\|v\| = \sqrt{\sum_{i=1}^{1536} v_i^2}, \quad \hat{v} = \frac{v}{\|v\|}$$

### Similitud Coseno y Regla de Rechazo
Al evaluar un nuevo tema candidato, se calcula la similitud coseno contra todos los posts publicados en los últimos 90 días:
$$\text{Similitud}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$

* **Umbral de Duplicidad:** Si $\text{Similitud} \ge 0.82$, el tema se marca como duplicado y el orquestador busca automáticamente el siguiente tema disponible en la ontología.

---

## 3. Tier 1: Linter Determinista por Expresiones Regulares

Antes de llamar a cualquier LLM, el borrador se somete a `core/linter/deterministic.mjs`. Si existe una sola violación, el proceso se interrumpe en $0\text{ ms}$:

### A. Lista Negra Universal de Humo y Clichés
* `snakeOilHype`: Palabras como *automatización mágica*, *ahorra tiempo*, *revoluciona*, *game-changer*, *fórmula secreta*, *ingresos pasivos*, *despega tu negocio*.
* `corporateAbstract`: Jerga como *sinergia*, *holístico*, *innovación disruptiva*, *paradigma*, *optimización 360*, *valor añadido*.
* `vanityMetrics`: Peticiones de interacción como *comenta abajo*, *dale like*, *sígueme para más*, *comparte este post*.

### B. Prohibición de Preguntas Retóricas en el Gancho
Queda prohibido comenzar el gancho con preguntas amateur tipo:
* *¿Sabías que...?*
* *¿Te has preguntado alguna vez...?*
* *¿Quieres saber cómo...?*
Todo gancho debe ser una **afirmación contundente con tensión**, respaldada por una métrica o un hecho.

### C. Validación Estructural
Se verifica que el número de diapositivas sea estrictamente entre **4 y 8 láminas**, evitando carruseles incompletos o excesivamente densos.
