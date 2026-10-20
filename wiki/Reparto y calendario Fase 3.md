---
tags: [fase3, reparto, calendario, roles, ventas, bi]
aliases: [Fase 3, Reparto Fase 3, Plan de ventas, Historia simulada]
---

# Reparto y calendario de la Fase 3

Entrega y presentación final: **sábado 24-10-2026**. Repartida el **martes 20-10**, con los mismos roles de la Fase 2.
Todo el material está en `Entrega_Fase3_Grupo14/`; la guía del equipo es `LEEME_PRIMERO_Fase3.docx`.

## Qué pide (rúbrica)

Sitio (15) · Integración ERP/CRM/web (15) · BI (10) · Conclusiones con datos (20) · Documentación (10) · Entregables
(10) · Presentación (20). Puntos 16 (sitio), 17 (BI) y 19 (conclusiones) del enunciado; detalle en
[[Rúbrica y requisitos]].

## Reparto

| Rol | Qué hace | Manual | Secciones del informe | Video |
|---|---|---|---|---|
| 3 · Alberto | Sitio y configuración, 38 productos publicados, P00004 recibida, carga de la historia, respaldos (antes de la historia y al cierre) | MU-04 | 5, 6.1, 6.3, 9 (con el rol 1) | Sitio y configuración |
| 2 · Jemima | Pedidos WEB-01 a 08, 10 y 12 por el sitio (flujos A, C, D, E), entregas y portal; **avisa en el grupo al terminar WEB-12** | MU-05 | 7, 8 | Compra de punta a punta |
| 4 · Brayan | Flujo B (formulario → lead → cotización → portal: WEB-09 y 11) **y la entrega de esos dos**; reportes BI con tablero después del aviso de WEB-12 | MU-06 | 6.2, 10 | CRM en el sitio y BI |
| 1 · Santiago | Plan de ventas, informe, KPIs, SMART, escalabilidad, conclusiones, presentación, PDF y ZIP | — | 1–4, 9, 11–16 | — |

## Calendario

| Día | Qué pasa |
|---|---|
| Mar 20-10 | Reparto; respaldo de la base |
| **Mié 21-10** | **Ruta crítica (rol 3):** sitio publicado, pago de prueba, factura automática, P00004 e historia cargada |
| Jue 22-10 | Pedidos por el sitio y flujo del CRM; empieza el BI |
| Vie 23-10 | Últimos pedidos, BI, manuales, videos; informe, PDF y ZIP; ensayo |
| **Sáb 24-10** | **Entrega y presentación final** |

## El plan de ventas

Archivo: `3_Archivos_Datos/RutaMoto_ventas_Fase3.xlsx` (legible) y `historial_ventas_fase3.json` (lo que lee el
script). Los genera `_Referencia/generadores/generar_ventas.py` con semilla fija, a partir del Excel de la Fase 2.

- **Historia simulada:** 45 pedidos del 05-10 al 20-10, canal «Ventas directas (WhatsApp y teléfono)», 36 clientes de
  los 40 y 9 que repiten. La carga `_Referencia/scripts_instancia/cargar_historial_ventas.py` por XML-RPC: crea,
  confirma, entrega, factura, paga y reescribe las fechas. Tiene modo `--probar` y es reanudable (se salta los
  `HIST-nnn` completos).
- **Pedidos por el sitio:** 12 (WEB-01 a WEB-12) entre el 21 y el 23-10, cada uno prueba un flujo: A compra directa,
  B cotización desde el sitio vía CRM, C taller con tarifa B2B, D quiebre resuelto (LLA-002 tras P00004), E carrito
  abandonado.
- **Lo que debería dar el BI** (hoja «4_Cuadre», calculado a precio de lista con 10 % a talleres):

| Indicador | Plan | Meta Fase 1 |
|---|---|---|
| Venta simulada | Q 14,679.50 | — |
| Ticket promedio de la historia | Q 326.21 | Q 285 |
| Recompra | 9 de 36 = 25.0 % | 20 % |
| Entregas en < 24 h | 40 de 45 = 88.9 % | 90 % |
| Top 5 por unidades | LUB-001 (45), LUB-004 (21), ELE-007 (13), FRE-001 (12), ELE-003 (11) | — |
| Bajo el mínimo al final | CAS-005, ELE-002, FRE-004, LUB-001 | — |
| Quiebre de stock | 0 de 38 | ≤ 5 % |

**Ojo:** estos números son *del plan*. Las conclusiones salen de lo que muestre Odoo; si no coincide, se explica.
Las entregas en < 24 h quedan por debajo de la meta porque así salió la semilla, no porque se buscara: en el informe
se presenta como dato de una historia simulada, no como hallazgo de la operación.

## Existencia de partida que asume el plan

Excel de la Fase 2 + compras recibidas (P00001–P00003) − cotizaciones entregadas (S00004 y S00005 del plan:
FRE-004 −4, LUB-001 −6, LLA-001 −5, LLA-006 −10). **No se verificó contra la instancia**: el script lo comprueba
con `qty_available` antes de escribir y se detiene si algo no alcanza.

Relacionado: [[Reparto y calendario Fase 2]] · [[Datos maestros y cuadre]] · [[Decisiones y límites]] · [[AVANCE]]
