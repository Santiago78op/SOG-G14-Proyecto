# Guion de videos y demo final: Fase 3 (Grupo 14)

Los videos van a Drive y su enlace al anexo del informe. La demo del sábado 24-10 vale 20 puntos y el enunciado
dice que la integración es «el aspecto más valorado»: la demo se arma alrededor de **un solo pedido que se sigue
por todos los módulos**.

## Video 1 · Rol 3 · Sitio y configuración (6–8 min)

| Min | Qué se ve |
|---|---|
| 0:00 | Aplicaciones: Comercio electrónico y Sitio web instalados sobre la base de la Fase 2 |
| 1:00 | Tienda: las 6 categorías y los 38 productos con imagen y precio |
| 2:30 | Ajustes: registro gratuito, facturación automática, proveedor de pago de prueba |
| 4:00 | Tarifa Talleres B2B y «no vender sin existencia» |
| 5:00 | P00004 recibida: LLA-002 pasa de 0 a 16 y aparece disponible en la tienda |
| 6:00 | La historia cargada: Ventas › Informes por día, del 05 al 20-10 |

## Video 2 · Rol 2 · Compra de punta a punta (6–8 min)

Un pedido del flujo A, sin cortes:

| Min | Qué se ve |
|---|---|
| 0:00 | Registro de un cliente nuevo en el sitio |
| 1:00 | Catálogo → carrito → pago de prueba → confirmación |
| 2:30 | Backend: el mismo número de pedido en Ventas (equipo «Sitio web») |
| 3:30 | La factura publicada y pagada, sin que nadie la haya creado |
| 4:30 | Inventario: la entrega reservada; se valida y baja la existencia |
| 5:30 | Portal del cliente: pedido entregado y factura en PDF |
| 6:30 | Taller con tarifa B2B (flujo C) |

## Video 3 · Rol 4 · CRM en el sitio y BI (8–10 min)

| Min | Qué se ve |
|---|---|
| 0:00 | Formulario de contacto del sitio → lead en el CRM (flujo B) |
| 1:30 | Oportunidad → cotización → correo en Mailpit → el cliente acepta y paga en el portal |
| 3:30 | Inventario: barras por producto, pastel por categoría, tabla de stock bajo |
| 5:30 | Ventas: líneas por día, semana y mes; top 5; ventas y margen por canal |
| 7:30 | Tablero con todo junto y un filtro aplicado en vivo |

## Demo en vivo del sábado (orden sugerido, ~15 min)

1. **Rol 1 (1 min):** qué es RutaMoto y qué se cierra en esta fase.
2. **Rol 2 (4 min):** compra en vivo por el sitio, con un cliente nuevo y desde un celular si se puede.
3. **Rol 3 (3 min):** el mismo pedido en Ventas, Facturación e Inventario. Validar la entrega en vivo.
4. **Rol 2 (1 min):** el portal muestra el pedido entregado y la factura.
5. **Rol 4 (4 min):** el BI se actualiza con la venta recién hecha: el pedido aparece en la línea de hoy y el
   producto baja en las barras. Es la prueba más fuerte de la integración.
6. **Rol 1 (2 min):** KPIs contra metas, conclusiones y escalabilidad.

**Antes de la demo:** respaldo restaurado en una segunda laptop, `localhost` en vez del túnel, un producto con
existencia de sobra para la compra en vivo (no uno del top 5, para no mover los números del informe).
