# SOP: Funnels Comment-to-DM & Publicación Multicanal

> **Propósito:** Vincular cualquier pieza (Reel o Carrusel) a un embudo automatizado de DM y programar su publicación.
> **Herramienta canónica:** Zernio (automatización de DM y distribución multicanal). Reemplazable por {{HERRAMIENTA_DM}}.

---

## 1. Arquitectura del Funnel

```
[PIEZA] (Reel o Carrusel)
   ▼
[CTA EN EL COPY]  "Comentá {{KEYWORD}} y te envío {{RECURSO}}"
   ▼
[LISTENER]        detecta el comentario con la keyword
   ▼
[DM AUTOMÁTICO]   envía el link / PDF / recurso
   ▼
[NURTURE]         {{SECUENCIA_POSTERIOR}} (email, agenda, oferta de entrada)
```

Keywords y recursos: `Conceptos/identity/offer.md` §2.

---

## 2. Paquete de Postprocesado

`Content Manager/pipeline/40_postprocessing/<slug>/`

| Archivo | Contenido |
| :--- | :--- |
| `caption.md` | Copy final: hook, desarrollo, CTA |
| `funnel.md` | Keyword, mensaje DM, recurso entregado |
| `post.json` | Plataformas, fecha, hashtags (primer comentario) |
| `media-url.txt` | URL pública del MP4 o PNGs |

---

## 3. Plantillas de Configuración

```json
// funnel trigger
{
  "name": "Funnel <slug>",
  "trigger": "comment",
  "keyword": "{{KEYWORD}}",
  "response_dm": "{{MENSAJE_DM}} {{URL_RECURSO}}"
}
```

```json
// post.json
{
  "text": "<caption.md>",
  "media": ["<media-url>"],
  "networks": ["instagram", "tiktok", "linkedin"],
  "firstCommentText": "{{HASHTAGS}}",
  "publishDate": "YYYY-MM-DDTHH:MM:SS"
}
```

---

## 4. Gobernanza

- **Modo Copiloto:** nada se publica sin aprobación humana explícita.
- **Modo Autónomo:** publica si pasa checklist del SOP + filtro de voz.
- Modo activo de esta marca: `{{MODO_GOBERNANZA}}`.
