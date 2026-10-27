# SOP: Video Studio (Edición Shortform)

> **Propósito:** Flujo paso a paso para editar videos verticales con ritmo cinematográfico, cortes quirúrgicos y la estética de {{NOMBRE_MARCA}}.  
> **Stack canónico:** el Video Studio — HyperFrames + GSAP + ffmpeg (transcripción: **Whisper local gratis por defecto**; ElevenLabs Scribe opcional de pago).

---

## 1. Principios de Edición

1. **Ritmo acelerado pero legible:** cero silencios, cero retomas. Duración típica 30–75 s.
2. **Zooms dinámicos:** punch-in 1.15×–1.25× en cada cambio de idea; la cámara nunca queda estática > 3–4 s.
3. **Identidad visual:** overlays según `Conceptos/visual_identity.md` §6 (colores, tipografías, sombras, acento).
4. **Leer antes de editar:** `Content Manager/video-studio/MOTION_PHILOSOPHY.md` + DESIGN.md del proyecto.

---

## 2. Flujo Operativo

```
[1 PROYECTO] ➔ [2 TRANSCRIBIR] ➔ [3 CORTAR SILENCIOS] ➔ [4 CORTAR ERRORES] ➔ [5 OVERLAYS] ➔ [6 PREFLIGHT & EXPORT]
```

1. **Crear proyecto:** `npm run new-video -- <slug>` desde `Content Manager/video-studio/`.
2. **Transcripción:** Whisper local gratis → `hyperframes transcribe` → `transcript.json` con timestamps por palabra. Opcional de pago: ElevenLabs Scribe → `npm run transcribe` (requiere key en `video-studio/.env`).
3. **Cortar silencios:** usar skill `/cut-silences` → genera video editado + transcripción retimeada.
4. **Cortar errores:** usar skill `/cut-mistakes` con el video y transcript del paso anterior (nunca mezclar timestamps originales con metraje editado).
5. **Overlays de marca:**
   - *Takeover* full-frame en quiebres de sección o tesis.
   - *Badge* flotante (`[REGLA 01]`, `[ERROR COMÚN]`).
   - *Stat* numérico monumental en `--accent`.
   - Validar sincronía con el beat de la voz.
6. **Preflight y render:** `npm run preflight -- <slug>` → revisar audio joins, contraste y safe areas → `final.mp4`. Guardar evidencia en `VERIFY.md`.

---

## 3. Conexión con el Funnel

1. Mover `final.mp4` a `Content Manager/postprocessing/<slug>/`.
2. Crear `caption.md` con CTA y keyword.
3. Activar el funnel → `SOPs/funnels_publicacion.md`.
