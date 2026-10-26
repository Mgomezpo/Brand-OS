# SOP: Video Studio (Edición Shortform)

> **Propósito:** Flujo paso a paso para editar videos verticales con ritmo cinematográfico, cortes quirúrgicos y la estética de {{NOMBRE_MARCA}}.
> **Stack de referencia:** HyperFrames + GSAP + Whisper local + ffmpeg (reemplazable por {{STACK_VIDEO}}).

---

## 1. Principios de Edición

1. **Ritmo acelerado pero legible:** cero silencios, cero retomas. Duración típica 30–75 s.
2. **Zooms dinámicos:** punch-in 1.15×–1.25× en cada cambio de idea; la cámara nunca queda estática > 3–4 s.
3. **Identidad visual:** overlays según `Conceptos/visual/visual_identity.md` §6 (colores, tipografías, sombras, acento).

---

## 2. Flujo Operativo

```
[1 INGESTA] ➔ [2 TRANSCRIBIR] ➔ [3 CORTES] ➔ [4 OVERLAYS] ➔ [5 PREFLIGHT & EXPORT]
```

1. **Ingesta:** crear proyecto `AI Content Manager/pipeline/30_video/<slug>/` y copiar `source.mp4`.
2. **Transcripción:** Whisper → `transcript.json` con timestamps por palabra.
3. **Cortes:** silencios muertos + errores/retakes (inicios falsos, frases repetidas).
4. **Overlays de marca:**
   - *Takeover* full-frame en quiebres de sección o tesis.
   - *Badge* flotante (`[REGLA 01]`, `[ERROR COMÚN]`).
   - *Stat* numérico monumental en `--accent`.
   - Validar sincronía con el beat de la voz.
5. **Preflight y render:** revisar audio joins, contraste y safe areas → `final.mp4`.

---

## 3. Conexión con el Funnel

1. Mover `final.mp4` a `AI Content Manager/pipeline/40_postprocessing/<slug>/`.
2. Crear `caption.md` con CTA y keyword.
3. Activar el funnel → `SOPs/funnels_publicacion.md`.
