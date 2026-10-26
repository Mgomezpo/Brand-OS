# Reglas de Métricas, Diagnóstico e Iteración de Contenido

---
**Pilar:** `brain/03_studio/feedback/`  
**Propósito:** Cuantificar el desempeño del contenido publicado, diagnosticar anomalías de retención y aplicar iteraciones algorítmicas precisas al siguiente lote de guiones.  
---

## 1. Métricas de Control y Umbrales Clave

| Métrica | Objetivo Aceptable | Objetivo Alto Rendimiento | Qué mide realmente |
| :--- | :--- | :--- | :--- |
| **Retención al Segundo 3 (Hook Rate)** | **> 60%** | **> 72%** | La potencia del gancho verbal y del estímulo visual inicial. |
| **Porcentaje Medio Visto (APV)** | **> 65%** | **> 80%** (en videos ≤ 50s) | El ritmo narrativo, la ausencia de relleno y el valor del desarrollo. |
| **Tasa de Guardados (Saves)** | **> 3%** del alcance | **> 6%** del alcance | La **utilidad práctica** (recursos, repositorios, comandos que guardan para usar). |
| **Tasa de Compartidos (Shares)** | **> 1.5%** del alcance | **> 4%** del alcance | El valor de **estatus y novedad** (hace ver inteligente a quien lo comparte). |

---

## 2. Diagnóstico de Caídas (Drops) y Cómo Iterar el Guion

```
SÍNTOMA 1: Retención al Seg 3 cae por debajo del 55%
  ├── Causa: Apertura blanda, preámbulo innecesario o falta de texto/estímulo visual inicial.
  └── Solución de Guion: Reescribir el hook verbal a menos de 10 palabras e iniciar directamente sobre la pantalla de la herramienta.

SÍNTOMA 2: Caída brusca entre el segundo 10 y el 25
  ├── Causa: Bloque de "cabeza parlante" prolongado sin cambio de plano, o jerga teórica abstracta.
  └── Solución de Guion: Reducir la explicación hablada e insertar demostración en Cursor o terminal en el segundo 10.

SÍNTOMA 3: Caída pronunciada en el segundo 35-45 antes del cierre
  ├── Causa: La audiencia percibió que la lección terminó; CTA largo o despedida ceremonial.
  └── Solución de Guion: Recortar la transición al CTA a una sola frase: "Comenta [BUILD] y te paso el código". Fin seco.
```

---

## 3. El Bucle de Feedback Semanal

Al cierre de cada ciclo semanal:
1. **Auditoría del Top 20%:** Identificar el video con mayor ratio de retención y comentarios. Extraer su estructura a `frameworks/` como nueva variante.
2. **Auditoría del Bottom 20%:** Detectar la causa de fricción y agregar el patrón a la lista de prohibiciones.
3. **Calibración de Teleprompter:** Si una palabra provocó tropiezos repetidos durante el rodaje del Creador, registrarla para sustitución léxica.
