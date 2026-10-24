# Checklist de capturas · Rol 4

> **13 figuras para el MU-06, ~20 tomas.** La misma captura se usa en el manual, en el
> informe y en la diapositiva: no se repite el trabajo.
> Si la pantalla dice otra cosa que la ruta escrita, **gana la pantalla** y se anota la ruta
> real en el manual.
>
> **Prioridad:** las figuras **1 a 11** son las que pide el enunciado (flujo B + los 5 reportes
> obligatorios: barras, pastel, stock bajo, líneas por día/semana/mes y top 5). Las figuras
> **12** (margen por canal) y **13** (tablero) son extras del plan del grupo: suman, pero no son
> requisito. Si el tiempo aprieta, primero 1-11 y después 12-13.
>
> **Ojo con la instancia real del 23-10** (leído de Odoo, no del plan):
> - Los precios de la tienda son **con IVA incluido**. La historia da **Q 14,679.50 con IVA** y
>   **Q 13,106.67 sin IVA**. El informe de ventas de Odoo muestra **sin IVA** por omisión: hay que
>   decir siempre cuál se está usando.
> - Ya hay **5 pedidos de la Fase 2** además de la historia: la base tiene **50 pedidos por
>   Q 16,794.50**. El informe de ventas los va a incluir. Decidir si se excluyen o se explican;
>   no borrarlos.
> - Al corte, Odoo reporta **CAS-005 (1/2) y ELE-002 (12/30)** bajo el mínimo; el plan preveía
>   cuatro (CAS-005, ELE-002, FRE-004, LUB-001). Usar lo que muestre Odoo y explicar la diferencia.
> - El top 5 de la **historia sola** es LUB-001 (37), LUB-004 (13), ELE-007 (13), ELE-003 (10),
>   FRE-001 (8); con los pedidos del sitio cambia. Anotar el top 5 real.

## Antes de empezar (30 minutos)

- [ ] URL del **servidor en la nube** y usuario propio (no `admin`): `http://54.167.23.144:8069`.
- [ ] Tienda: `http://54.167.23.144:8069/shop`; Mailpit: `http://54.167.23.144:8025`.
- [ ] Sitio publicado: 38 productos, 6 categorías, registro gratuito.
- [ ] Medio de pago publicado (transferencia o Demo) y factura automática activa. **Si es
  transferencia, el pago no se confirma solo: hay que registrar el pago a mano.**
- [ ] P00004 recibida: **LLA-002 en 16**.
- [ ] Historia cargada: **45 pedidos, Q 14,679.50 con IVA (Q 13,106.67 sin IVA)**, fechas del 05 al 20.
- [ ] Mailpit arriba; la bandeja arranca vacía y los correos nuevos sí se capturan.
- [ ] Mónica y Taller Hermanos Cutzal con acceso al portal (o sabes cómo invitarlos).
- [ ] Equipo del sitio creado (por defecto **Website Sales**) y **Márgenes** activos en Ventas.
- [ ] Módulo **Dashboards** (`board`) instalado; si no, Aplicaciones › buscar «Dashboards».
- [ ] Confirmado que **WEB-12 todavía no está hecha**: el BI final se captura después.

## Convenciones

- Captura de **ventana completa del navegador**, con la URL y el menú visibles. No recortes solo la tabla.
- Zoom al 100 %, resolución 1920×1080 o mayor.
- **Nunca** captures una contraseña, el correo del administrador ni datos personales reales.
- Guarda en `capturas_rol4/` con el nombre exacto de la tabla de abajo.
- Captura **en el momento**: primero haces el paso, luego capturas el resultado; no reconstruyas después.
- Para el portal, usa una **sesión de incógnito** como cliente, no la sesión de administrador.

## Mapa de figuras

| Figura | Capítulo | Tomas | Archivo | Se reutiliza en |
|---|---|---|---|---|
| 1 | Formulario del sitio | 1 | `01_formulario.png` | — |
| 2 | Lead en el CRM | 2 | `02_lead_lista.png`, `03_lead_ficha.png` | Informe 6.2, diapositiva 6 |
| 3 | Oportunidad y cotización | 2 | `04_oportunidad.png`, `05_cotizacion.png` | Diapositiva 6 |
| 4 | Correo en Mailpit | 1 | `06_correo_mailpit.png` | — |
| 5 | Portal: aceptar y pagar | 3 | `07_portal_cotizacion.png`, `08_portal_pago.png`, `09_pedido_confirmado.png` | Diapositiva 6 |
| 6 | Entrega y factura | 2 | `10_entrega_validada.png`, `11_factura_pagada.png` | — |
| 7 | Existencias por producto | 1 | `12_inv_barras.png` | Informe 10, diapositiva 10 |
| 8 | Inventario por categoría | 1 | `13_inv_pastel.png` | Informe 10, diapositiva 10 |
| 9 | Stock bajo | 1 | `14_stock_bajo.png` | Informe 10, diapositiva 10 |
| 10 | Ventas por día/semana/mes | 3 | `15_ventas_dia.png`, `16_ventas_semana.png`, `17_ventas_mes.png` | Informe 10 (tres), diapositiva 11 (día) |
| 11 | Top 5 | 1 | `18_top5.png` | Informe 10, diapositiva 11 |
| 12 | Ventas y margen por canal | 1 | `19_margen_canal.png` | Informe 10 |
| 13 | Tablero | 1 | `20_tablero.png` | Informe 10 |

---

## Flujo B · Figuras 1 a 6

### Figura 1 · Formulario de contacto del sitio

- **Pantalla:** `Sitio › Contáctanos` (sesión sin iniciar).
- **Antes:** llena el formulario con Mónica Isabel Arévalo Soto, `monica.arevalo@example.com`,
  y pide cotización por **CAS-005 (chaqueta) y CAS-006 (rodilleras)**.
- **Qué debe verse:** el formulario lleno, con el nombre, el correo y el mensaje; si ya se envió,
  el aviso de confirmación.
- **Dato que hay que anotar:** fecha y hora del envío; nombre exacto con el que entró el lead.
- **Ojo:** no uses la cuenta de administrador; el formulario debe crear un lead, no una ficha interna.

### Figura 2 · El lead en el CRM

- **Pantalla:** `CRM › Pipeline` (o `Iniciativas`), y luego la ficha del lead.
- **Qué debe verse:** la tarjeta del lead con el nombre de Mónica, el correo y el mensaje; en la
  ficha, el teléfono y el texto que venían del formulario. El campo **Origen** puede estar vacío;
  no es bloqueante, se anota como diferencia.
- **Dato:** nombre del lead, etapa y fecha; si el origen está vacío, anotarlo.
- **Si no aparece:** revisa que el módulo `website_crm` esté instalado y que el formulario
  esté configurado para crear un lead. Anótalo como problema del capítulo 1.

### Figura 3 · Oportunidad y cotización

- **Pantalla:** la oportunidad (desde el lead, botón **Convertir a oportunidad**) y
  `Oportunidad › Nueva cotización`.
- **Qué debe verse:** la oportunidad vinculada a Mónica y la cotización con **CAS-005 ×1** y
  **CAS-006 ×1**, precio de lista **Q 680 + Q 180 = Q 860**.
- **Dato:** número de la oportunidad, número de la cotización, subtotal, impuestos y total.
- **Ojo:** si el precio no es Q 860, revisa la lista de precios del cliente y los impuestos.
  No inventes el número: anota lo que muestra Odoo.

### Figura 4 · Correo en Mailpit

- **Pantalla:** Mailpit (la URL que te dé Alberto), bandeja de entrada.
- **Qué debe verse:** el correo de la cotización con el asunto, el destinatario
  `monica.arevalo@example.com` y el **enlace al portal**.
- **Dato:** asunto, hora de envío, nombre del remitente.
- **Ojo:** no captures la configuración del servidor ni contraseñas. Si el correo no llega,
  revisa que Mailpit esté arriba y que Odoo tenga el servidor saliente; anótalo.

### Figura 5 · El cliente acepta y paga en el portal

- **Pantalla:** abre el enlace del correo en una **sesión de incógnito**.
- **Qué debe verse:** la cotización en el portal, el botón **Aceptar**, la pantalla del medio de
  pago (transferencia o Demo) y la confirmación del pedido. Si es transferencia, el pago se
  registra a mano después; no se confirma solo.
- **Dato:** número de pedido que asigna Odoo, fecha, total y estado del pago.
- **Ojo:** si Mónica no tiene usuario de portal, invítala desde
  `Contactos › Mónica › Acción › Conceder acceso al portal`; el correo de invitación también
  llega a Mailpit. Hazlo **antes** de la captura, no en medio del flujo.

### Figura 6 · Entrega validada y factura pagada

- **Pantalla 1:** `Inventario › Entregas`, abrir la entrega del pedido, **Validar**.
- **Pantalla 2:** `Facturación › Facturas de clientes`, abrir la factura del pedido.
- **Qué debe verse:** la entrega en estado **Hecho** y la factura en estado **Pagada** (o con el
  pago registrado a mano si es transferencia); el mismo pedido en las dos.
- **Dato:** número de entrega, número de factura, fecha, cantidad entregada y existencia antes y
  después. Anotar los valores reales: pueden cambiar por los pedidos de la Fase 2.
- **Ojo:** el inventario baja cuando **validas la entrega**, no cuando se paga la factura. Si la
  factura queda pendiente, el pedido existe pero el pago no está registrado; no lo confundas con un
  error de stock. Valida la entrega y registra el pago (o documenta que quedó pendiente).

### Cierre del capítulo 1

- [ ] Repetir el flujo con **WEB-11** (Taller Hermanos Cutzal, LUB-004 ×6 y LUB-007 ×3,
  tarifa B2B, total esperado **Q 364.50**).
- [ ] Validar la entrega de WEB-11 y comprobar la factura pagada.
- [ ] Anotar los números de Odoo de los dos pedidos en la hoja de datos.

---

## BI · Figuras 7 a 13

> **No captures el BI final hasta que Jemima avise que WEB-12 está hecha y que validó sus
> entregas.** Antes de capturar, corre `05_VERIFICAR_BI.py`.

### Figura 7 · Existencias por producto (barras)

- **Ruta:** `Inventario › Informes › Existencias` › vista **Gráfico** › **Barras**, agrupado
  por **Producto**.
- **Filtro:** productos almacenables; si la gráfica sale ilegible, limita a los 15 con más
  existencia y dilo en el pie.
- **Qué debe verse:** las barras de los productos; los de existencia baja se ven al final.
- **Dato:** cantidad de productos mostrados, existencia de LUB-004, FRE-001 y LUB-002.
- **Esperado:** 38 productos; LUB-004 59, FRE-001 38, LUB-002 35.

### Figura 8 · Inventario por categoría (pastel)

- **Ruta:** la misma vista › **Pastel**, agrupado por **Categoría de producto**.
- **Qué debe verse:** las 6 categorías con su participación.
- **Dato:** categoría con más unidades y con menos.
- **Esperado:** Lubricantes y filtros es la mayor (178 unidades); Cascos y protección, la menor (40).

### Figura 9 · Productos con stock bajo (tabla)

- **Ruta:** `Inventario › Operaciones › Reabastecimiento` (reglas de reorden), filtro
  **bajo el mínimo** o `qty_to_order > 0`.
- **Qué debe verse:** la tabla con producto, mínimo, existencia y cantidad a pedir.
- **Dato:** lista exacta y valores.
- **Esperado al corte:** **CAS-005 (1/2) y ELE-002 (12/30)**; el plan preveía CAS-005, ELE-002, FRE-004 y LUB-001. Si salen otros, revisa que Jemima
  haya validado sus entregas y que P00004 esté recibida.

### Figura 10 · Evolución de las ventas (tres capturas)

- **Ruta:** `Ventas › Informes › Ventas` › **Gráfico** › **Líneas**, eje de fecha **Día**.
- **Filtro:** pedidos confirmados (`Ventas`), no cotizaciones. Excluye WEB-07.
- **Tres tomas:** día, semana y mes. La misma vista, cambiando la agrupación de fecha.
- **Dato:** número de pedidos, total vendido, fecha inicial y final.
- **Esperado:** 56 pedidos, **Q 19,111.00**; la historia del 05 al 20 se ve como una serie
  continua y los pedidos del sitio del 21 al 23 como la cola reciente.

### Figura 11 · Top 5 de productos

- **Ruta:** `Ventas › Informes › Ventas` › **Pivote** › filas **Producto**, medida
  **Cantidad**, orden descendente.
- **Qué debe verse:** los cinco primeros con su cantidad.
- **Dato:** los cinco códigos y cantidades.
- **Esperado:** LUB-001 (45), LUB-004 (21), ELE-007 (13), FRE-001 (12), ELE-003 (11);
  entre los cinco, 102 de 179 unidades (57 %).

### Figura 12 · Ventas y margen por canal

- **Ruta:** `Ventas › Informes › Ventas` › **Gráfico** o **Pivote**, agrupado por
  **Equipo de ventas**, medida **Margen** (y **Total**).
- **Qué debe verse:** **Ventas directas (WhatsApp y teléfono)** y **Website Sales** (o el
  nombre que tenga el equipo del sitio).
- **Dato:** total y margen de cada canal.
- **Esperado:** directo **Q 14,679.50**; sitio **Q 4,431.50**; total **Q 19,111.00**.
- **Ojo:** si no aparece la medida **Margen**, activa `Ventas › Configuración › Ajustes ›
  Márgenes` o instala el módulo `sale_margin`. Sin costos cargados, el margen sale 100 %.

### Figura 13 · Tablero

- **Ruta:** en cada vista, icono de engranaje (**Acciones**) junto al nombre de la vista ›
  **Dashboard** › **Add to my Dashboard**. Luego abre la app **Dashboards**.
- **Qué debe verse:** el tablero con los reportes de inventario y ventas juntos.
- **Dato:** cuántos widgets tiene y qué reportes incluye.
- **Ojo:** el módulo **Dashboards** (`board`) es de Odoo 18 Community; si no está, se instala
  desde Aplicaciones. La ruta «Favoritos › Agregar a mi tablero» del MU-06 **no es la de
  Odoo 18**; corrígela en el manual.
- **Plan B:** si el tablero no funciona, guarda los 7 reportes como favoritos y muestra
  **Mis favoritos**; anótalo como límite en el capítulo 3.

---

## Hoja de datos (llénala mientras capturas)

| Dato | Dónde se lee | Valor |
|---|---|---|
| Nº de pedido WEB-09 | Ventas › Pedidos | |
| Factura WEB-09 | Facturación › Facturas | |
| Entrega WEB-09 | Inventario › Entregas | |
| Total WEB-09 | Pedido / factura | |
| Nº de pedido WEB-11 | Ventas › Pedidos | |
| Factura WEB-11 | Facturación › Facturas | |
| Entrega WEB-11 | Inventario › Entregas | |
| Total WEB-11 | Pedido / factura | |
| Pedidos de historia | Ventas › Informes | 45 |
| Venta de historia | Ventas › Informes | Q 14,679.50 |
| Pedidos del sitio | Ventas › Informes | 11 |
| Venta del sitio | Ventas › Informes | Q 4,431.50 |
| Total confirmado | Ventas › Informes | Q 19,111.00 |
| Top 5 | Pivote | |
| Bajo el mínimo | Reabastecimiento | |
| Productos en cero | Existencias | 0 |
| Margen por canal | Informe de ventas | |

## Después de capturar

- [ ] Cada figura tiene su archivo y su pie.
- [ ] Los números de Odoo están anotados, no deducidos.
- [ ] Las rutas del manual coinciden con la pantalla; si no, se corrigieron.
- [ ] No hay contraseñas ni datos personales en las capturas.
- [ ] Las capturas 12 a 20 se hicieron **después** de WEB-12 y con las entregas validadas.
- [ ] Se corrió `05_VERIFICAR_BI.py` y no quedan fallos críticos.
