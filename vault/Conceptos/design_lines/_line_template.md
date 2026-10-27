# Línea {{LINE_ID}} — {{NOMBRE_LINEA}}

> **Identificador CSS:** `[data-line="{{LINE_ID}}"]`
> **Arquetipo:** *{{ARQUETIPO_EDITORIAL}}*
> **Objeto / metáfora visual:** {{METAFORA_VISUAL}}
> **Rol en el Funnel:** **{{TOF / MOF / BOF}} — {{OBJETIVO}}**

---

## 1. Narrativa & Filosofía

{{DESCRIPCION_DE_LA_VOZ_DE_ESTA_LINEA}}

- **Tono:** {{TONO}}
- **Mensaje central:** "{{MENSAJE_CENTRAL}}"
- **Métrica clave:** {{GUARDADOS / COMPARTIDOS / DMs / COMENTARIOS}}
- **Regla inmutable de la línea:** {{REGLA}} (ej: "cero computadores en esta línea")

---

## 2. Anatomía Editorial (5–7 slides)

- **Estructura del cuerpo:** {{ESTRUCTURA}}
- **Elementos gráficos nativos:** {{GRAFICOS}}
- **Slide 1 · Hero Cover:** {{CONCEPTO_PORTADA}} (cumple la Ley del Hero Cover)
- **Slide final · CTA:** "{{CTA}}" con keyword `{{KEYWORD}}`

---

## 3. Tokens CSS

```css
[data-line="{{LINE_ID}}"] {
  --font-display: "{{FUENTE_DISPLAY}}", sans-serif;
  --tracking-display: {{TRACKING}};

  --surface-page:   {{HEX}};
  --surface-raised: {{HEX}};
  --border:         {{HEX}};

  --text-strong:    {{HEX}};
  --text-body:      {{HEX}};
  --text-muted:     {{HEX}};

  --accent:         {{HEX}};
  --line-1:         {{HEX}};
  --line-2:         {{HEX}};

  --radius-sm: {{PX}};
  --radius-md: {{PX}};
}
```

---

## 4. Prompting para Fondos IA

- **Medio visual nativo:** {{MEDIO}}
- **Sujetos permitidos:** {{SUJETOS}}
- **Sujetos prohibidos:** {{PROHIBIDOS}}
- **Encuadre (3:4 vertical):** sujeto en el {{35}} % inferior; {{65}} % superior limpio ({{HEX_FONDO}}).
- **Sintaxis:** `[SCENE]` · `[SUBJECT]` · `[LIGHTING]` · `[CINEMATOGRAPHY & OPTICS]` + prompt negativo canónico.

---

## 5. Proyectos Producidos en esta Línea
- [[Content Manager/pipeline/20_carruseles/{{slug}}/copy|{{slug}}]] — {{descripcion}}
