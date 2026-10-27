# postprocessing — Mesa de Publicación

Paquete de despegue de cada pieza antes de dispararlo con Zernio. Una carpeta por pieza:

```text
postprocessing/<slug>/
├── caption.md     # copy final: hook, desarrollo, CTA
├── funnel.md      # keyword DM, mensaje, recurso entregado
├── post.json      # plataformas, fecha, hashtags (primer comentario)
└── media-url.txt  # URL pública del MP4 final o los PNGs
```

Aquí desembarcan las piezas terminadas de los motores:
- Video 9:16: `final.mp4` desde `video-studio/video-projects/<slug>/`
- Carrusel 3:4: slides PNG desde `carousel-studio/batches/<vuelta>/<slug>/slides/`

## Disparo

```bash
python helper/zernio.py post-package postprocessing/<slug>   # desde Content Manager/
```

> **SOP completo:** `../../vault/SOPs/funnels_publicacion.md` · **Guía operativa:** `../../AGENTS.md` (apartado *Motores del Sistema*)
