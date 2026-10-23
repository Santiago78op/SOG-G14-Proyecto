# Video 1 · Sitio web y configuración

**RutaMoto, Fase 3, Grupo 14.** Alberto Josué Hernández Armas, carné 201903553.
Duración: 7 minutos y 30 segundos.

La pantalla la conduce el script `odoo-docker/scripts/17_video_fase3.ps1`, que abre cada vista en su minuto.
Durante la grabación solo hay que hablar. Con `-Manual` espera ENTER entre bloque y bloque, para ensayar.

Antes de grabar: contenedores arriba, sesión iniciada en Odoo con `admin@rutamoto.gt` y las demás ventanas de
Chrome cerradas. La grabación se hace con la barra de tareas oculta y el navegador en pantalla completa.

---

## 0:00 · Presentación

> Buenas. Soy Alberto Hernández, carné 201903553, del Grupo 14. En este video muestro el sitio de comercio
> electrónico de RutaMoto y cómo quedó configurado. RutaMoto es la tienda de repuestos y accesorios para
> motocicleta del caso, y hasta la fase anterior solo tenía el ERP: catálogo, inventario, compras y clientes.
> Lo que se agrega en esta fase es el canal de venta en línea, y la idea que quiero dejar clara desde el
> principio es que no se agregó un sistema aparte. El sitio corre sobre la misma base de datos del ERP.

## 0:30 · El respaldo previo

> Lo primero fue respaldar. Instalar módulos modifica el esquema de la base, así que antes de tocar nada se
> generó este archivo, rutamoto dos mil veintiséis, diez, veintitrés, de diez megas, más un volcado SQL del
> mismo momento. Si algo hubiera salido mal, este es el punto de retorno. No es una formalidad: es la única
> forma de deshacer una instalación.

## 1:00 · Los módulos instalados

> Desde Aplicaciones se instaló Comercio electrónico. Odoo arrastró consigo lo que el caso necesita: Sitio
> web, Portal del cliente y Motor de pagos. Se agregaron dos módulos más: Disponibilidad de producto, que
> hace que la tienda lea las existencias reales del almacén, y Formulario de contacto, que convierte en
> iniciativa del CRM lo que un visitante escribe en Contáctanos.
>
> Quiero detenerme en cómo se comprueba que un módulo está instalado, porque la pantalla de aplicaciones
> puede mostrar una tarjeta en caché. La prueba es la ficha: cuando está instalado ofrece Actualizar y
> Desinstalar. Si ofreciera Activar, no lo estaría.

*(1:35, módulo de márgenes)*

> Este otro es Márgenes en órdenes de venta. Sin él, el informe de ventas de Odoo dice cuánto se vendió pero
> no cuánto se ganó, y el enunciado pide reportes de ventas y de ganancias. Con él, cada línea de pedido
> calcula la diferencia entre el precio de venta y el costo del producto, y esa columna queda disponible para
> los reportes de inteligencia de negocios.

## 2:00 · El catálogo publicado

> Estas son las categorías del sitio. No son las mismas que las categorías internas de producto: las
> internas sirven para la contabilidad y los informes, estas arman el menú que ve el cliente. Se crearon seis
> con los mismos nombres que las internas, para que el catálogo publicado y el del ERP se lean igual, y cada
> uno de los 38 productos quedó en la suya, entre seis y siete por categoría.

*(2:30, lista de productos publicados)*

> Acá están los 38 productos publicados. Un producto existe en el ERP aunque no esté publicado; publicarlo es
> lo que lo vuelve visible y comprable. En esta lista se ve, para cada uno, la dirección con la que aparece en
> el sitio, su precio y las unidades a la mano, que es el dato que viene del almacén, no un número escrito
> aparte para la tienda.

## 3:10 · La tienda vista por un cliente

> Esto es lo que ve alguien que entra sin haber iniciado sesión. Está en una ventana de incógnito a propósito,
> para que no aparezca la barra de edición del administrador. El logotipo de RutaMoto, el menú de categorías,
> el buscador, el filtro por rango de precio y los productos con su ilustración y su precio en quetzales.
>
> Acá hubo una corrección que vale la pena contar. La tienda mostraba los precios sin impuesto, así que el
> aceite aparecía en cuarenta con dieciocho en lugar de los cuarenta y cinco del catálogo. Se cambió a precio
> con impuesto incluido, que es como se publican los precios al consumidor en Guatemala y como están en el
> archivo de datos maestros.

*(3:50, ficha de LUB-001)*

> Esta es la ficha del producto en la tienda: el precio con impuesto incluido, la existencia a la vista y el
> botón de agregar al carrito. En los 38 productos se desactivó la casilla de seguir vendiendo cuando no hay
> existencia. La consecuencia es que la tienda deja de vender un producto en cuanto el almacén llega a cero,
> sin que nadie lo marque a mano. Para mí esa es la prueba más directa de que el sitio y el ERP comparten los
> datos: no hay dos inventarios que sincronizar, hay uno solo.

## 4:20 · El registro de clientes

> El enunciado pide que el sitio permita registrar clientes. La privacidad quedó en registro libre, así que
> cualquier visitante crea su cuenta desde la tienda sin que nadie lo invite. Odoo crea el contacto en la
> misma tabla donde viven los 40 clientes que se cargaron en la fase anterior y le asocia un usuario de
> portal. Desde ese momento la persona ve sus pedidos y sus facturas en Mi cuenta.

## 4:45 · Pago y facturación automática

> Estos son los ajustes del sitio. Dos cosas importan acá. La primera es el proceso de pago. La segunda es
> esta casilla, factura automática: con ella, cuando el cliente confirma el pago, el sistema crea y publica la
> factura solo, sin que nadie la escriba. Eso es lo que cierra el ciclo que pide la rúbrica: el sitio genera
> el pedido, el inventario reserva y descuenta la mercadería y la facturación emite el documento, los tres
> sobre el mismo registro.

*(5:20, proveedores de pago)*

> Como medio de pago se activó y publicó la transferencia bancaria, con las instrucciones que el cliente lee
> al terminar la compra: el número de cuenta y la indicación de poner el número de pedido como referencia. El
> enunciado declara opcional la pasarela de pago real, y contratar una exige datos bancarios de una empresa
> que no existe, así que esta configuración cubre el requisito sin inventar una integración que después no se
> podría comprobar. Los demás proveedores quedaron deshabilitados.

## 5:45 · La tarifa de talleres

> Estas son las listas de precios: la predeterminada y Talleres B2B, con diez por ciento de descuento, que se
> creó en la fase anterior y está asignada a los nueve talleres del catálogo de clientes. Como el sitio lee la
> misma lista de precios que el ERP, un taller que entra con su cuenta ve el precio con descuento y un
> particular ve el precio de lista. No hay dos catálogos ni dos tiendas.

## 6:05 · P00004 recibida

> Esta es la recepción de la compra cuatro, que la fase anterior dejó confirmada y sin recibir a propósito,
> para que el informe de inventario tuviera una orden pendiente. En esta fase se recibe, porque la llanta
> trasera estaba en cero y, con el sitio configurado para no vender sin existencia, ese producto no se podría
> comprar en línea. Al validar, la llanta pasa de cero a dieciséis unidades y el catálogo queda sin ningún
> producto en quiebre.

## 6:30 · La historia de ventas cargada

> Por último, la historia de ventas que alimenta los reportes. Son 45 pedidos entre el 5 y el 20 de octubre,
> generados con un plan y cargados con un script que, por cada pedido, crea la orden, la confirma, valida la
> entrega, publica la factura, registra el pago y reescribe las fechas con las del plan. El script tiene un
> modo de solo lectura que comprueba clientes, productos y existencias antes de escribir, y esa validación
> pasó limpia a la primera.
>
> Lo que muestra el informe de ventas de Odoo, que lee la base y no la salida del script: 45 pedidos, 36
> clientes distintos, catorce mil seiscientos setenta y nueve con cincuenta de venta con impuesto incluido y
> un ticket promedio de trescientos veintiséis con veintiuno, por encima de la meta de doscientos ochenta y
> cinco que se fijó en la primera fase.

*(7:05, existencias)*

> Y así quedó el almacén después de que la historia sacara la mercadería: ningún producto en quiebre y solo
> una bujía por debajo de su mínimo de reabastecimiento.

## 7:30 · Cierre

> Eso es el sitio y su configuración. Queda publicado sobre la misma base del ERP, con 38 productos, registro
> libre de clientes, pago por transferencia, factura automática y la tarifa de talleres aplicándose sola. La
> compra de punta a punta por el sitio y los reportes de inteligencia de negocios van en los otros dos videos.
> Gracias.
