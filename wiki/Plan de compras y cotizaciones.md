---
tags: [fase2, compras, cotizaciones, plan]
aliases: [Compras, Cotizaciones, Plan de compras]
---

# Plan de compras y cotizaciones

Las cantidades están elegidas para que ninguna venta deje un producto en cero y para que la 12.4 tenga órdenes pendientes que mostrar. **No improvisar compras ni ventas extra en la base.**

## Compras (rol 3, punto 12.2)

| # | Proveedor | Productos | Estado al entregar |
|---|---|---|---|
| 1 | Frenos y Transmisiones de Guatemala, S.A. | FRE-001 × 44 | Recibida (6 → 50) |
| 2 | Importadora Centroamericana de Repuestos, S.A. | LUB-004 × 72 · LUB-007 × 24 | Recibida |
| 3 | Grupo Eléctrico Moto GT | ELE-007 × 30 | Recibida |
| 4 | Distribuidora Llantera del Sur | LLA-002 × 16 | **Confirmada, sin recibir** |
| 5 | Grupo Eléctrico Moto GT | ELE-002 × 88 | **Solicitud enviada, sin confirmar** |

LUB-007 (Q 65 / Q 38) y ELE-007 (Q 40 / Q 22) son los **productos adicionales** que se crean desde el sistema con existencia cero. Su existencia entra por las compras 2 y 3.

**La «requisición»:** Odoo 18 Community no tiene un documento con ese nombre. En este proyecto la requisición es la **alerta de reabastecimiento**: la regla detecta FRE-001 en 6 con mínimo 15, y «Ordenar una vez» genera la solicitud de cotización. Se defiende como decisión de diseño. Opcional: *Acuerdos de compra* para una licitación. No se verificó que ese módulo venga en Community 18.

## Cotizaciones (rol 2, punto 12.3)

Tarifa **Talleres B2B** con descuento (se propone 10 %), asignada a los 9 talleres.

| # | Cliente | Productos | Estado al entregar |
|---|---|---|---|
| 1 | Servicio Técnico El Pistón | FRE-004 × 4 · LUB-001 × 6 | Facturada (FRE-004 baja de 8 a 4) |
| 2 | MotoClínica Villa Nueva | LLA-001 × 5 · LLA-006 × 10 | Entregada |
| 3 | Alejandro Javier Lainfiesta Ruiz | CAS-003 × 1 · CAS-004 × 1 | Enviada |
| 4 | Taller Dos Ruedas Mixco | FRE-003 × 3 | Cancelada |

## CRM (rol 4, puntos 14 y 15)

- **Campaña** al segmento Repartidor: 13 destinatarios.
- **Pipeline** con 5 etapas: Nuevo lead → Contactado → Cotización enviada → Negociación → Ganado. Perdido es una acción, no una columna.
- **5 oportunidades sugeridas:** Taller Moto Express Zona 7 (la que recorre todas las etapas), Moto Servicio La Florida, Taller Hermanos Cutzal, Centro de Servicio Motoaventura y Mónica Isabel Arévalo Soto.

Relacionado: [[Datos maestros y cuadre]] · [[Reparto y calendario Fase 2]]
