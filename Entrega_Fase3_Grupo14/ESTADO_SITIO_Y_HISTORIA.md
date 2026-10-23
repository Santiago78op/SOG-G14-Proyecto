# Estado del sitio, la configuración y la historia de ventas

Fase 3, Grupo 14. Alberto Josué Hernández Armas, carné 201903553. Al 23-10-2026.

Esto es lo que ya está en la instancia y lo que entrego, para que el informe final se arme sin volver a
verificar cada número. Todas las cifras de abajo están leídas de Odoo, no del Excel del plan.

## Lo que quedó montado

| Pieza | Estado |
|---|---|
| Respaldo antes de instalar | `respaldos/rutamoto_2026-10-23_1440.zip` (10 MB) y el volcado `.sql` del mismo momento |
| Módulos | Sitio web, Comercio electrónico, Disponibilidad de producto, Formulario de contacto, Motor de pagos, Portal del cliente y Márgenes en órdenes de venta |
| Categorías del sitio | 6, con 6 o 7 productos cada una |
| Productos publicados | 38 de 38 |
| Precios en la tienda | con impuesto incluido (LUB-001 a Q 45.00) |
| Venta sin existencia | bloqueada en los 38; la existencia se muestra en la ficha pública |
| Registro de clientes | libre, sin invitación |
| Medio de pago | transferencia bancaria, activada y publicada, con instrucciones |
| Factura automática | activada |
| Tarifa Talleres B2B | 10 %, sobre los nueve talleres |
| P00004 | recibida: RMT/IN/00004, LLA-002 de 0 a 16 |
| Historia de ventas | 45 pedidos cargados, entregados y facturados |

## Los números de la historia, leídos de Odoo

| Indicador | Odoo | Plan | Meta de la Fase 1 |
|---|---|---|---|
| Pedidos | 45 | 45 | |
| Clientes distintos | 36 | 36 | |
| Líneas de pedido | 83 | | |
| Venta con impuesto incluido | Q 14,679.50 | Q 14,679.50 | |
| Venta sin impuesto | Q 13,106.67 | | |
| Margen | Q 3,781.67 | | |
| Ticket promedio | Q 326.21 | Q 326.21 | Q 285, se cumple |
| Recompra | 9 de 36, 25.0 % | 9 de 36 | 20 %, se cumple |
| Entregas en menos de 24 h | 40 de 45, 88.9 % | 40 de 45 | 90 %, no se cumple |
| Facturas publicadas | 45, de ellas 42 cobradas | | |
| Productos en quiebre | 0 de 38 | 0 de 38 | ≤ 5 %, se cumple |
| Bajo el mínimo al final | ELE-002 | CAS-005, ELE-002, FRE-004, LUB-001 | |

**Ojo con las dos cifras de venta.** El plan está calculado con el impuesto incluido, que es como se publican
los precios en la tienda. El informe de ventas de Odoo agrupa por omisión el importe **sin** impuesto, que es
Q 13,106.67. No son dos resultados distintos, es la misma venta con y sin IVA, y por eso la historia cuadra con
el plan al centavo. Para el BI y las conclusiones conviene decir siempre cuál de las dos se está usando.

Top 5 por unidades, de Odoo: LUB-001 (37), LUB-004 (13), ELE-007 (13), ELE-003 (10), FRE-001 (8).

## Trazabilidad de ejemplo

Pedido **S00013**, de Mónica Isabel Arévalo Soto, 07-10-2026, un FRE-004 a Q 395.00 con impuesto incluido.
Generó la entrega **RMT/OUT/00013**, validada el 08-10, y la factura **INV/2026/00015**, publicada y cobrada,
las dos con S00013 en el campo de origen. Sirve de ejemplo para la sección de integración.

## Lo que entrego

- `2_Manuales_Usuario/MU-04_Sitio_web_ecommerce.docx` y su PDF: 19 páginas, 4 capítulos, 15 pasos.
- `1_Informe/informe_fase3_secciones_Alberto_Hernandez.docx`: el apartado del sitio web completo, la
  introducción del apartado de integración con su tabla, la arquitectura, del sitio al ERP y la historia de
  ventas.
- `4_Videos/guion_video1_sitio_y_configuracion.md` y el script que conduce la pantalla,
  `odoo-docker/scripts/17_video_fase3.ps1`.
- Capturas en `capturas_fase3/`.

## Lo que falta y de quién depende

1. **La última columna de la tabla «Qué registro crea cada evento del sitio»**. Las tres filas que se pueden
   comprobar con la historia ya están llenas. Las otras seis dicen que se comprueban con los pedidos del sitio
   o con el flujo del CRM, y hay que completarlas cuando esos pedidos existan. Hoy no hay ningún pedido con el
   sitio web como origen, ni ningún usuario de portal.
2. **Las subsecciones de carrito, pago, facturación y cotizaciones** del apartado del sitio están escritas
   desde la configuración, que es lo que pide la plantilla. La evidencia del recorrido completo desde el
   navegador va en el apartado de pruebas de flujo completo, no en el mío.
3. **El respaldo de cierre** se hace cuando todos terminen de escribir en la base. Comando:
   `powershell -ExecutionPolicy Bypass -File .\odoo-docker\scripts\02_respaldo.ps1`.
4. **La numeración de los títulos** del archivo de secciones empieza en 1 porque es un documento suelto. Al
   pegarlo en el informe completo Word la renumera sola.
