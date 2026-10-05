# Guion del video: cadena de suministros, carga de datos y ciclo de compras

**Alberto Josué Hernández Armas, carné 201903553 · Grupo 14 · Caso RutaMoto · Fase 2**

Duración objetivo: 9 minutos. El script `odoo-docker\scripts\12_video_fase2.ps1` abre cada
pantalla con estos mismos tiempos, así que durante la grabación solo tenés que hablar.

---

## Antes de grabar

1. Contenedores arriba: `09_reanudar.ps1`. Sesión iniciada en Odoo como `admin@rutamoto.gt`.
2. Cerrá WhatsApp, el correo y todo lo que pueda lanzar una notificación.
3. Tené abierto el Excel `RutaMoto_datos_maestros_Fase2.xlsx` en una ventana aparte: el
   primer bloque es sobre él.
4. Grabá pantalla completa a 1080p, micrófono activado, audio del sistema desactivado.
5. Hacé una corrida en seco del script antes de grabar. Son nueve minutos y te deja ver
   exactamente qué aparece en cada momento.
6. Empezá a grabar, esperá dos segundos y recién ahí ejecutá el script.

```powershell
cd "$env:USERPROFILE\OneDrive\Escritorio\cys\geren1fase1proyecto\odoo-docker\scripts"
powershell -ExecutionPolicy Bypass -File .\12_video_fase2.ps1
```

El script es automático de punta a punta: no tenés que hacer un solo clic. Con `-Manual` espera
un ENTER entre bloque y bloque, por si preferís controlar vos el ritmo, y con `-SinExcel` no
abre el archivo de datos maestros.

---

## El guion

### 0:00 — Presentación

> Buenas. Soy Alberto Josué Hernández Armas, carné 201903553, del Grupo 14. En este video
> muestro la carga de los datos maestros de RutaMoto en Odoo y el ciclo completo de compras
> a proveedores, desde la alerta de existencias hasta la recepción de la mercadería.
>
> RutaMoto es nuestra tienda en línea de repuestos y accesorios para motocicleta. El sistema
> es Odoo Community 18 sobre PostgreSQL 16, el mismo que quedó instalado y documentado en la
> Fase 1.

### 0:30 — El archivo de datos maestros

> Este es el archivo que se importa. Tiene una hoja por cada cosa que se carga, y el orden
> no es arbitrario: cada hoja apunta a registros que crea la anterior. Los productos tienen
> que existir antes que sus existencias, los proveedores antes que la lista de qué provee
> cada uno, y las categorías y las etiquetas antes que todo.
>
> Las columnas azules se importan. Las grises en cursiva son informativas: están para que se
> pueda leer el archivo y para cuadrar los números, y en la importación se dejan en
> «No importar».
>
> Esta es la hoja Cuadre, y es la que manda. El inventario inicial de los 36 productos del
> catálogo base, valorizado al costo, suma exactamente cuarenta y cinco mil quetzales: la
> misma cifra del rubro de inventario inicial del presupuesto de la Fase 1. De esos, treinta
> y ocho mil noventa y seis corresponden a lo que se carga por importación.

### 1:30 — Lo que hay que preparar antes de importar

> Antes de tocar el archivo hay que dejar listas tres cosas en Odoo, porque si no existen la
> importación falla fila por fila.
>
> Las seis categorías de producto, creadas sin categoría padre. Esto es importante: si una
> categoría cuelga de «All», su nombre completo pasa a ser «All barra Lubricantes y filtros»
> y deja de coincidir con el texto del Excel.
>
> Las cuatro etiquetas de contacto, que son los segmentos de clientes del caso: repartidor,
> motociclista particular, taller mecánico y entusiasta.
>
> Y los términos de pago. La base está en español, así que los que trae Odoo por omisión se
> renombraron para que coincidan con el archivo, y se creó el que faltaba: cincuenta por
> ciento de anticipo y cincuenta por ciento contra entrega, con dos líneas de cincuenta por
> ciento cada una.

### 2:30 — El asistente de importación y la validación previa

En pantalla aparecen dos capturas del importador, las mismas que están en el manual. No se
repite la importación en cámara a propósito: volver a importar duplicaría el catálogo.

> Este es el asistente de importación. Se sube el archivo, se elige la hoja, y Odoo propone un
> campo de la base para cada columna. Donde no acierta se elige a mano, con la ayuda de la hoja
> Diccionario del propio archivo, que trae el nombre técnico de cada campo.
>
> Y este es el botón que de verdad importa: **Probar**. Ejecuta la importación completa contra
> la base y después deshace la transacción, así que si algo está mal no se escribe nada y la
> base queda limpia. Es la diferencia entre corregir una columna y restaurar un respaldo.
>
> Esta segunda pantalla es un error real de esta carga, y es la razón por la que ese botón
> existe. La hoja de existencias traía la ubicación escrita como WH barra Existencias, que es
> el código por omisión de Odoo. Nuestra bodega se llama Bodega Central RutaMoto y su código es
> RMT desde la Fase 1, así que la ubicación real es RMT barra Existencias. La validación
> rechazó las treinta filas y no escribió nada.
>
> Como la instancia tiene una sola bodega, la columna se dejó en «No importar»: Odoo asigna
> entonces la ubicación por omisión del almacén, que es justamente la correcta. Se prefirió eso
> a editar el archivo, porque el Excel ya estaba repartido entre los cuatro integrantes.

### 3:30 — El resultado de la carga

> Este es el catálogo cargado, agrupado por categoría. Treinta productos en cinco categorías,
> cada uno con su referencia interna, su precio, su costo y su imagen. Las imágenes entraron
> solas: la columna trae la dirección pública de cada archivo en el repositorio del grupo y
> Odoo las descarga durante la importación.
>
> Esta es una ficha completa. Referencia LUB-001, categoría Lubricantes y filtros, precio de
> venta cuarenta y cinco quetzales, costo veintiocho, y la casilla de seguimiento de
> inventario marcada, que es lo que hace que lleve existencias y alertas.
>
> Aquí están las existencias por ubicación. Sesenta unidades de LUB-001 en RMT barra
> Existencias. Y el total del inventario al costo da treinta y ocho mil noventa y seis
> quetzales, que es exactamente la cifra de la hoja Cuadre. Ese es el primer indicador de la
> fase: el descuadre es de cero.

### 4:30 — Proveedores y clientes

> Los cinco proveedores, cada uno con su plazo de pago: treinta días para dos de ellos,
> quince para el eléctrico, cuarenta y cinco para el de cascos, y el de llantas con el
> cincuenta y cincuenta.
>
> Cada proveedor tiene su persona de contacto como contacto hijo, y cada producto tiene en su
> pestaña de Compra el proveedor que lo surte, con su costo y su plazo de entrega en días.
> Eso es lo que después hace que la orden de compra se llene sola.
>
> Y los treinta y cinco clientes importados, agrupados por segmento: doce repartidores, once
> motociclistas particulares, siete talleres y cinco entusiastas. Esos segmentos son los que
> usa la campaña del CRM.

### 5:15 — La requisición: la alerta de reabastecimiento

> Aquí empieza el ciclo de compras. El enunciado pide una requisición, y Odoo 18 Community no
> tiene un documento que se llame así. En este proyecto la requisición es la alerta de la
> regla de reabastecimiento, y lo documentamos como decisión de diseño.
>
> Cada producto tiene su mínimo y su máximo, importados desde la tercera hoja. Cuando la
> existencia cae por debajo del mínimo, el producto aparece aquí con la cantidad que hay que
> pedir para llegar al máximo.
>
> El inventario inicial está diseñado a propósito para que cuatro productos queden bajo el
> mínimo. FRE-001, pastillas de freno delanteras, con seis unidades y un mínimo de quince.
> LUB-004 con ocho y mínimo veinte. ELE-002 con doce y mínimo treinta. Y LLA-002, la llanta
> trasera, en cero con mínimo cuatro.
>
> El botón «Ordenar una vez» toma esa diferencia y genera la solicitud de cotización al
> proveedor que corresponde. Para FRE-001 propone cuarenta y cuatro unidades, que es lo que
> falta para llegar al máximo de cincuenta.

### 6:15 — De la solicitud a la orden

> Esta es la solicitud de presupuesto que se generó: P cero cero cero cero uno, al proveedor
> Frenos y Transmisiones de Guatemala. Cuarenta y cuatro unidades a cincuenta y cinco
> quetzales, dos mil cuatrocientos veinte en total.
>
> Fíjense en que el proveedor, el precio y el plazo de entrega no se escribieron: salieron de
> la lista de precios de proveedor que se importó en la sexta hoja. Esa es la razón de
> importar esa hoja.
>
> Al confirmar, la solicitud se convierte en pedido de compra y aparece el botón de recepción.
> Ese botón existe porque el ERP generó solo el movimiento de entrada al almacén.

### 7:00 — La recepción y el efecto en el inventario

> Esta es la recepción RMT barra IN barra cero cero cero cero uno, validada. Estado Hecho.
>
> Y este es el punto que pide el enunciado: que el movimiento se refleje en el inventario.
> FRE-001 pasó de seis a cincuenta unidades. En el historial de movimientos se ve la entrada
> desde la ubicación de proveedores hacia RMT barra Existencias, con su fecha, su documento de
> origen y el usuario que la validó.
>
> La alerta de FRE-001 desapareció sola: la regla ya no lo propone porque la existencia volvió
> a estar sobre el mínimo.

### 7:45 — Los productos adicionales y las cinco compras

> El enunciado también pide crear productos adicionales directamente desde el sistema. Son
> estos dos, creados desde el formulario y no desde el Excel, con existencia cero: LUB-007,
> lubricante de cadena en aerosol, sesenta y cinco quetzales de venta y treinta y ocho de
> costo; y ELE-007, bombillo LED de stop, cuarenta y veintidós.
>
> Su existencia no se escribió a mano: entró por compra. Así un mismo producto demuestra las
> dos cosas, la creación desde el sistema y el ciclo completo.
>
> Estas son las cinco compras de la fase. Las tres primeras están recibidas. La cuarta, la de
> las llantas, está confirmada pero sin recibir. Y la quinta, la de las bujías, quedó como
> solicitud enviada sin confirmar.
>
> Las dos últimas están abiertas a propósito: son las órdenes pendientes de proveedores que
> pide el informe de inventario de la sección doce punto cuatro. Si las cerráramos, ese
> reporte quedaría vacío.

### 8:45 — Cierre

> Con esto queda demostrado el ciclo de compras completo: requisición, solicitud de
> cotización, orden de compra y recepción, con el movimiento reflejado en el inventario.
>
> La base queda con treinta y dos productos de mi parte, treinta y ocho cuando se sume la
> carga manual de la categoría Accesorios, con cinco proveedores, treinta y cinco clientes
> segmentados y un inventario valorizado que cuadra contra el archivo de origen. El detalle
> paso a paso, con captura en cada paso, está en el manual MU-01. Gracias.

---

## Si algo falla durante la grabación

No cortes. Explicá el error y cómo lo resolvés, y seguí: en un video de operación eso suma,
porque demuestra que entendés el sistema.

## Después de grabar

- Revisá que se lea el texto de las listas de Odoo sin forzar la vista.
- Subilo a la carpeta del grupo en Drive como `Fase2_Video_Carga_Compras_Grupo14.mp4`.
- Abrí el enlace desde una ventana de incógnito antes de pegarlo en el informe.
