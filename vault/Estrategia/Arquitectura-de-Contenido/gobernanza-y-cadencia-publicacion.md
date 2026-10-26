# Cadencia Semanal y Modelo de Gobernanza

Este documento detalla el calendario de publicación, los niveles de autonomía por marca y las reglas estrictas de seguridad e integración con la API de **Zernio**.

---

## 1. Cadencia Semanal de Publicación

El orquestador (`engine.mjs`) mapea cada día hábil central a una marca y audiencia específica, con publicación fijada a las **14:00 UTC (9:00 AM COT / Hora Colombia)**:

```
          MARTES                    MIÉRCOLES                   JUEVES
   ┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
   │         {{MARCA_B2B}}         │    │        {{MARCA_APP}}        │    │    {{NOMBRE_MARCA}}     │
   │   B2B Alto Ticket   │    │  Creadores de Cont. │    │  Fundador / Builder │
   │   Target: COO/CEOs  │    │  Cuaderno Mágico    │    │  Build in Public    │
   │                     │    │                     │    │                     │
   │  100% AUTÓNOMO      │    │  100% AUTÓNOMO      │    │  COPILOTO (HITL)    │
   │  @brand_enterprise  │    │  @brand_saas             │    │  @brand_personal    │
   └─────────────────────┘    └─────────────────────┘    └─────────────────────┘
```

### Cálculo Dinámico de Fecha
La función `calculateNextDaySlot(dayName, hourUtc)` calcula de forma determinista la fecha ISO del próximo día de la semana correspondiente. Si hoy es el mismo día y la hora ya pasó, o si es un día previo, programa automáticamente para la siguiente iteración semanal garantizando timestamps en el futuro.

---

## 2. Niveles de Gobernanza y Aprobación

| Marca | Nivel de Gobernanza | Comportamiento del Motor | Publicación en Vivo |
| :--- | :--- | :--- | :---: |
| **{{MARCA_B2B}}** | `AUTONOMOUS` (Zero-HITL) | Ejecuta deduplicación, linter bicameral, renderiza láminas, sube a CDN y programa directamente en Zernio. | **Automática** |
| **{{MARCA_APP}}** | `AUTONOMOUS` (Zero-HITL) | Mismo flujo que {{MARCA_B2B}}. Si la cuenta `@brand_saas` no está conectada en Zernio, resguarda los activos en local sin interferir con otras marcas. | **Automática** (al conectar cuenta) |
| **{{NOMBRE_MARCA}}** | `COPILOT_ONLY` (Strict HITL) | **Regla de oro de seguridad:** NUNCA programa ni publica en vivo de forma autónoma. Genera el borrador completo en local y en Zernio como `draft`. Requiere el flag manual `--approve` o confirmación humana. | **Requiere Aprobación** |

---

## 3. Aislamiento Estricto de Cuentas en Zernio API

Para evitar que una marca publique por error en los perfiles de otra (por ejemplo, que contenido de {{MARCA_APP}} termine en `@brand_enterprise` o `@brand_personal`), el gateway `core/publisher/zernio.mjs` implementa una política de **cero tolerancia a fallbacks cruzados**:

```javascript
// 1. Obtener cuentas conectadas en el workspace de Zernio
const targetUsername = brandConfig.targetAccount?.instagram;

// 2. Mapeo ESTRICTO sin fallbacks a cuentas de terceros
const igAccount = targetUsername 
  ? accounts.find(a => a.platform === 'instagram' && a.username === targetUsername)
  : null;

// 3. Si la cuenta no está conectada, se aíslan los activos en local
if (!igAccount && platforms.length === 0) {
  return {
    status: 'STAGED_NO_CONNECTED_ACCOUNT',
    message: `No se encontró cuenta conectada en Zernio para '${targetUsername}'. Activos guardados localmente.`
  };
}
```

### Cuentas Registradas Actualmente en Zernio
- `@brand_enterprise` (Instagram) -> Asignada exclusivamente a **{{MARCA_B2B}}**.
- `@brand_personal` (Instagram) -> Asignada exclusivamente a **{{NOMBRE_CREADOR}} {{APELLIDO_CREADOR}}**.
- `@brand_saas` (Instagram) -> Pendiente de vinculación en el panel de Zernio. El motor compila todo y lo deja listo localmente (`dist/brand-saas/`) esperando la conexión.
