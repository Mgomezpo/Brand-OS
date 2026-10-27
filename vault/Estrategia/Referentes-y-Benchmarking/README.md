---
tags: [estrategia, referentes, benchmarking]
status: vacia-por-diseno
---

# 📚 Biblioteca de Creadores Referentes

> **Propósito:** Aquí va la información de los **creadores y cuentas de referencia** que esta marca quiere decodificar. Es la carpeta de ingeniería inversa: cada referente se desmonta en patrones visuales, narrativos y de conversión para alimentar los frameworks de `Estrategia/` y las reglas de `SOPs/`.

Esta carpeta se entrega **vacía intencionalmente** en la plantilla: cada usuario monta su propio roster con los creadores de su nicho (el SOP del roster está en [[SOPs/ritual_ingesta_semanal|Ritual Semanal de Ingesta]]).

> 🗺️ **Evolución planificada:** estandarizar la ingesta de referentes vía scraping (Apify). Mientras ese conector no exista, la carpeta se puebla con el proceso manual de abajo y queda vacía de perfiles.

---

## 📁 Qué va aquí (estructura por referente)

```text
Referentes-y-Benchmarking/
├── README.md                          # este hub
└── <slug-referente>/                  # 1 carpeta por creador
    ├── perfil.md                      # ficha del creador (duplica Templates/referente_perfil.md)
    ├── analisis-<formato>.md          # deconstrucción por formato (carruseles, reels, etc.)
    └── digest_semanal_W{{SEMANA}}.md  # fichas de ingesta periódica (opcional)
```

---

## 🔄 Cómo poblarla

1. Elegir el referente (4–6 máximo, ver SOP de ingesta).
2. Duplicar [[Templates/referente_perfil|la plantilla de perfil de referente]] → guardarla como `Referentes-y-Benchmarking/<slug-referente>/perfil.md`.
3. Añadir los análisis de deconstrucción de sus piezas (estructura, ángulos, hooks, mecánicas de conversión).
4. Enlazar cada perfil desde el [[Estrategia/README|índice de Estrategia]].

Cada estudio concluye con **3 Semillas de Producción** traducidas a la voz de `Conceptos/tone_of_voice.md` y al stack real de `Conceptos/proof_bank.md`.

---

## 🧠 Ejemplo de referencia (teoría ya extraída)

Las deconstrucciones maestras que dieron origen a los frameworks de esta plantilla viven en `Estrategia/Carruseles-y-Prompting/analisis-referencias-maestras.md` (Grow with Alex, Chase H, Helder). Estúdialas como muestra del nivel de análisis esperado: son la teoría destilada, no perfiles de biblioteca.

---

## 📏 Reglas

- Un referente = una carpeta = un `perfil.md` (más análisis auxiliares si aplica).
- Los patrones descubiertos se convierten en reglas en `SOPs/` o frameworks en `Estrategia/Frameworks-de-Guionizacion/`, no quedan solo como notas.
- **Nunca copiar copy:** se decodifican *mecanismos* (estructura, ángulo, hook, CTA), no textos. Los copies completos de otros creadores no se archivan aquí.
