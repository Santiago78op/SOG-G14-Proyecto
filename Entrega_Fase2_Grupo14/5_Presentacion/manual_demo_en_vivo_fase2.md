# Demostración en vivo del sábado: tu parte

**Alberto Josué Hernández Armas, 201903553 · Grupo 14 · RutaMoto · Fase 2**

Te tocan dos bloques de la demostración: la carga masiva (3 minutos) y el ciclo de compras
(4 minutos). Los dos se hacen con **un producto que no existe en la base**, así que nada de lo
que muestres cambia un número del informe ni cierra una compra que el informe declara
pendiente.

El archivo es `RutaMoto_demo_en_vivo_Fase2.xlsx`. Tenelo abierto en una pestaña y en el
escritorio, listo para seleccionarlo en el importador.

**En la demostración se usa `localhost:8069`, no el túnel.**

---

## Antes de entrar

1. `09_reanudar.ps1` y entrá a Odoo como `admin@rutamoto.gt`. Esperá a que cargue una vez:
   la primera carga después de levantar los contenedores es lenta y en vivo se siente eterna.
2. Dejá abiertas estas cuatro pestañas, en este orden, para no buscar en los menús:
   - Inventario › Productos › Productos
   - Inventario › Operaciones › Inventario físico
   - Inventario › Operaciones › Reabastecimiento
   - Compras › Órdenes › Solicitudes de presupuesto
3. Ensayá la corrida completa el viernes, con cronómetro. Son siete minutos tuyos.
4. Si ya ensayaste una vez, **archivá el LUB-008 anterior** antes de volver a empezar: ficha
   del producto › Acción › Archivar. Si no, vas a terminar con varios productos del mismo
   código.

---

## Bloque 2 de la demostración: carga masiva (3 minutos)

### Qué decir al empezar

> Los datos maestros se cargaron desde un archivo de Excel, una hoja por cada cosa que se
> importa y en orden de dependencia. Voy a importar en vivo un producto nuevo para que se vea
> el procedimiento completo.

### Qué hacer

| # | Dónde | Qué hacés | Qué señalás |
|---|---|---|---|
| 1 | Inventario › Productos › Productos | Engranaje › Importar registros › Subir archivo › `RutaMoto_demo_en_vivo_Fase2.xlsx` | Que arriba aparece el selector de hoja: se importa una hoja a la vez |
| 2 | misma pantalla | Elegís la hoja **1_Demo_Producto** | El mapeo de columnas, y la última columna en «No importar» |
| 3 | misma pantalla | Pulsás **Probar** | «Esto valida el archivo contra la base y después deshace todo. Si algo falla, no se escribe nada» |
| 4 | misma pantalla | Pulsás **Importar** | El producto aparece en la lista con su código |
| 5 | Inventario › Operaciones › Inventario físico | Engranaje › Importar registros › mismo archivo › hoja **2_Demo_Existencia** › Probar › Importar | Que la cantidad queda **contada**, no aplicada |
| 6 | misma pantalla | Seleccionás la línea y pulsás **Aplicar** | «Sin este paso el inventario sigue en cero: es el error más común» |

### Si preguntan algo

**«¿Y si el archivo trae un error?»**
Esa es la razón de «Probar». Pasó de verdad en esta carga: la columna de ubicación del archivo
decía `WH/Existencias` y nuestra bodega tiene `RMT/Existencias`, porque se llama Bodega Central
RutaMoto y su código corto es RMT. La validación rechazó las treinta filas sin escribir nada.
Está documentado en el manual MU-01 y en la sección 6.2 del informe.

**«¿Cómo entraron las imágenes?»**
La columna Imagen trae la dirección pública de cada archivo en el repositorio del grupo, y Odoo
las descarga durante la importación. Por eso el repositorio tiene que seguir siendo público.

**«¿Cuántos registros se importaron?»**
30 productos, 30 líneas de existencia por Q 38,096 al costo, 30 reglas de reabastecimiento,
5 proveedores con sus 5 contactos, 30 líneas de lista de precios de proveedor y 35 clientes.

---

## Bloque 4 de la demostración: ciclo de compras (4 minutos)

### Qué decir al empezar

> Odoo 18 Community no tiene un documento que se llame requisición. En nuestro diseño la
> requisición es la alerta de la regla de reabastecimiento, y el botón «Ordenar una vez» es el
> acto de requerir. Voy a recorrer el ciclo completo con el producto que acabo de crear.

### Qué hacer

| # | Dónde | Qué hacés | Qué señalás |
|---|---|---|---|
| 1 | Inventario › Productos › LUB-008 | Pestaña **Compra**: importás la hoja 3, o agregás a mano a la Importadora Centroamericana con precio 52 y plazo 5 | «Esto es lo que hace que la orden se llene sola» |
| 2 | Inventario › Operaciones › Reabastecimiento | Importás la hoja **4_Demo_Regla** (mínimo 10, máximo 40) | El producto aparece con 2 unidades y propuesta de 38 |
| 3 | misma pantalla | Pulsás **Ordenar una vez** | «Esta es la requisición: nace de una regla, no de un formulario» |
| 4 | Compras › Solicitudes de presupuesto | Abrís la solicitud recién creada | Proveedor, precio y fecha prevista **no se escribieron**: salieron de la lista de precios |
| 5 | misma pantalla | **Confirmar pedido** | Aparece el botón de Recepción: el ERP generó solo el movimiento |
| 6 | misma pantalla | Botón **Recepción** › **Validar** | Estado Hecho |
| 7 | Inventario › Productos › LUB-008 | Mirás la existencia | De 2 a 40 unidades. Y el producto desapareció de la lista de reabastecimiento |

Si el tiempo aprieta, los pasos 1 y 2 se pueden dejar hechos de antemano y la demostración
empieza en el 3. Decilo en voz alta si lo hacés: «la regla y el proveedor ya están puestos».

### Si preguntan algo

**«¿Dónde está la requisición?»**
Es la línea de reabastecimiento. Y queda trazable: cada orden de compra conserva como documento
de origen la regla que la disparó. Se puede abrir cualquiera de las cinco compras reales y
mostrar ese campo.

**«¿Por qué hay órdenes sin recibir?»**
A propósito. La compra 4 está confirmada sin recibir y la compra 5 quedó como solicitud enviada:
son las órdenes pendientes de proveedores que pide el informe de inventario. Si las cerráramos,
ese reporte quedaría vacío.

**«¿Qué pasó con el inventario después de las compras?»**
Pasó de Q 38,096 a Q 43,456, que es exactamente el costo de las tres compras recibidas:
2,420 más 2,280 más 660. Que esa suma cierre al quetzal es la prueba de que el movimiento se
registró una sola vez y los módulos lo comparten.

**«¿Y los productos adicionales?»**
LUB-007 y ELE-007, creados desde el formulario con existencia cero. Su inventario entró por las
compras 2 y 3, así que el mismo producto demuestra la creación desde el sistema y el ciclo de
compras completo.

---

## Si algo falla en vivo

| Síntoma | Qué hacer |
|---|---|
| El navegador no carga `localhost:8069` | En la consola: `docker compose ps`; si algo está caído, `docker compose up -d` |
| Odoo va lento en la primera pantalla | Normal tras levantar los contenedores. Seguí hablando |
| «Ordenar una vez» no aparece | La regla no se importó o el producto está por encima del mínimo. Mostralo y explicalo: es parte del mecanismo |
| Se te duplicó LUB-008 de un ensayo anterior | Archivá el viejo desde su ficha, Acción › Archivar, y seguí |

No cortes ni pidas disculpas si algo falla: explicá qué pasó y cómo se resuelve. En una
evaluación técnica eso demuestra dominio mejor que una corrida perfecta.
