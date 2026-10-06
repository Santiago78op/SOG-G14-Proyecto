# Guion de los videos y de la demo: Fase 2

El enunciado pide *"videos alojados en Google Drive que evidencien [...] la ejecución de los puntos clave (Cadena de Suministros, Campañas CRM [...])"*. Son **tres videos**, uno por rol técnico, para que ninguno espere al otro para grabar. Al final está el orden de la **demo en vivo** del sábado (20 puntos).

| Video | Quién graba | Duración | Archivo |
|---|---|---|---|
| Cadena de suministros: carga y compras | Rol 3 | 8 a 10 min | `Fase2_Video_Carga_Compras_Grupo14.mp4` |
| Cotizaciones e informe de inventario | Rol 2 | 6 a 8 min | `Fase2_Video_Cotizaciones_Inventario_Grupo14.mp4` |
| CRM: plantillas, campaña y pipeline | Rol 4 | 6 a 8 min | `Fase2_Video_CRM_Grupo14.mp4` |

## Reglas para los tres (las mismas de la Fase 1)

- Grabá la pantalla (OBS o `Win + G`), a 1080p, y que el texto se lea.
- **Narrá mientras hacés.** Un video mudo no demuestra dominio.
- Al inicio decí tu nombre, tu carné y qué vas a mostrar.
- Una sola toma alcanza. Si algo falla, explicá el error y cómo lo resolvés: eso suma.
- **Grabá lo que ya hiciste, sobre datos reales.** No repitas la carga para el video: mostrá el resultado y rehacé en cámara solo un ejemplo pequeño (una fila, un producto). Si repetís la importación completa, se duplican los productos.
- Subí el video a la carpeta del grupo en Drive y probá el enlace en una ventana de incógnito.

---

## Video 1: carga y compras (rol 3)

**0:00. Presentación.**
> "Soy [nombre], carné [número], del Grupo 14. Muestro la carga de datos maestros de RutaMoto en Odoo y el ciclo completo de compras a proveedores."

**0:30. El Excel.** Abrí `RutaMoto_datos_maestros_Fase2.xlsx`. Mostrá las hojas y explicá por qué van en ese orden: los productos antes que las existencias, los proveedores antes que la lista de qué provee cada uno. Mostrá la hoja *Cuadre*: el inventario al costo suma Q 45,000, igual que el presupuesto de la Fase 1.

**1:30. La importación.** Mostrá el importador con una hoja cargada, el mapeo de columnas y el botón *Probar*. Explicá qué pasa si hay un error: no se importa nada y la base queda limpia. Después mostrá el resultado: productos agrupados por categoría, una ficha completa y los clientes agrupados por segmento.

**4:00. La alerta.** En Reabastecimiento se ven los cuatro productos bajo el mínimo. Explicá que el stock se diseñó así a propósito.
> "Odoo no tiene un documento llamado requisición. En nuestro diseño, la requisición es esta alerta: la regla detecta que FRE-001 tiene 6 unidades con un mínimo de 15 y propone comprar hasta el máximo."

**5:00. El ciclo.** Mostrá la compra de FRE-001 completa: la solicitud de cotización al proveedor correcto, la orden confirmada, la recepción validada y FRE-001 que pasa de 6 a 50 en el historial de movimientos.

**7:30. Productos adicionales y compras abiertas.** Mostrá LUB-007 y ELE-007, creados desde el sistema, y la lista de las cinco compras con sus estados. Explicá por qué la 4 y la 5 quedan abiertas.

**9:00. Cierre.**
> "La base queda con 38 productos, 6 proveedores y 40 clientes, y con el ciclo de compras demostrado de la alerta a la recepción."

---

## Video 2: cotizaciones e inventario (rol 2)

**0:00. Presentación.**

**0:30. La carga manual.** Mostrá la categoría Accesorios y explicá por qué se cargó a mano: el enunciado pide las dos modalidades, y cargar a mano una categoría completa demuestra el formulario sin repetir lo importado. En cámara, creá o editá un campo de un producto.

**2:00. El flujo para talleres.** La tarifa *Talleres B2B*: qué descuento tiene, a quién se le asignó y por qué los talleres cotizan antes de comprar.

**3:00. De la cotización a la venta.** Seguí la cotización 1 completa: cotización con la tarifa aplicada, envío al cliente, confirmación como pedido, entrega validada (FRE-004 baja de 8 a 4) y factura. Después mostrá la lista de las cuatro cotizaciones con sus estados.

**5:30. Informe de inventario.** Existencias por categoría, las dos órdenes pendientes de proveedores y las alertas que quedan, cada una con su compra en curso.

**7:00. Medición.**
> "El quiebre de stock, que en la Fase 1 era una meta, hoy se mide: 1 SKU en cero de 38 es 2.6 %, dentro del 5 %."

---

## Video 3: CRM (rol 4)

**0:00. Presentación.**

**0:30. Servidor de correo.** La configuración y la prueba de conexión. Explicá por qué elegiste Mailpit o Gmail.

**1:30. Las dos plantillas.** Mostrá cada una en el editor y señalá los cuatro elementos que exige el enunciado: logo y nombre, banner, texto breve y llamado a la acción.

**3:00. La campaña.** El filtro del segmento Repartidor con sus 13 destinatarios, el envío, las estadísticas y un correo abierto en la bandeja.

**5:00. El pipeline.** Las cinco etapas y qué significa cada una en RutaMoto. Las cinco oportunidades. Mové una tarjeta en cámara y abrí el historial de la que llegó a Ganado, donde se ve cada cambio de etapa con su fecha y su usuario.

---

## La demo en vivo del sábado (20 puntos)

La rúbrica dice *"Se demuestra el funcionamiento correcto del ERP y CRM de forma fluida"*. Fluida quiere decir **sin buscar en los menús frente al catedrático.** Ensáyenla el viernes, completa, con cronómetro.

| Orden | Quién | Qué se muestra | Minutos |
|---|---|---|---|
| 1 | Rol 1 | Qué pedía la fase, cómo se repartió y el Excel con su cuadre | 2 |
| 2 | Rol 3 | Carga masiva: importar **una fila nueva** en vivo con *Probar* | 3 |
| 3 | Rol 2 | Carga manual: crear un producto en vivo | 2 |
| 4 | Rol 3 | Alerta → solicitud → orden → recepción, con un producto | 4 |
| 5 | Rol 2 | Cotización → pedido → entrega → factura | 3 |
| 6 | Rol 2 | Informe de inventario y quiebre de stock medido | 2 |
| 7 | Rol 4 | Plantilla, campaña y correo recibido | 3 |
| 8 | Rol 4 | Pipeline: mover una oportunidad y mostrar su historial | 2 |

**Antes de entrar:**

- La laptop del rol 3 cargada, con Odoo arriba y **sin depender del túnel**. En la demo se usa `localhost`.
- Un respaldo del cierre de fase restaurado en una segunda laptop, por si la primera falla.
- Datos de demo preparados: la fila del Excel, el producto a crear en vivo y el producto para el ciclo de compras. Que no sean los mismos que ya están en la base.
- Todos deben poder hacer cualquier paso de la tabla. El catedrático elige a quién preguntarle.
