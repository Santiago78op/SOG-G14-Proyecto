# Guion del video y de la demo · Rol 4

> Video de 8-10 minutos y 4 minutos de demo en vivo. Se graba **después** de WEB-12 y de las
> capturas del BI. Las mismas capturas del checklist sirven para el video y las diapositivas.

## Antes de grabar

- [ ] WEB-12 hecha y avisada por Jemima.
- [ ] Entregas de Jemima validadas (si no, el stock no baja en el video).
- [ ] `05_VERIFICAR_BI.py` sin fallos críticos.
- [ ] Mailpit arriba y el correo de la cotización a mano.
- [ ] Sesión de incógnito lista como Mónica (para el portal).
- [ ] Navegador a 100 %, notificaciones silenciadas, ninguna contraseña visible.
- [ ] Guion impreso o en otra pantalla; una sola toma si se puede.

## Video · 8-10 minutos

### 0:00-1:30 · El formulario crea el lead

**Qué se ve:** el sitio, `Contáctanos`, el formulario lleno con Mónica y el mensaje por CAS-005 y
CAS-006. Luego, el cambio al backend: `CRM › Pipeline`, la tarjeta del lead con origen **Sitio web**
y la ficha con el mensaje.

**Qué decir:**
> «Este es el flujo B: una cotización que nace en el sitio. El cliente no compra de inmediato,
> pide una cotización. Al enviar el formulario, el lead entra al CRM con el origen del sitio y con
> los datos que escribió el cliente. No hay una exportación ni un conector: el sitio y el CRM son
> la misma base.»

**No mostrar:** la cuenta de administrador ni la configuración del servidor de correo.

### 1:30-3:30 · Oportunidad, cotización y correo

**Qué se ve:** convertir el lead en oportunidad, crear la cotización con CAS-005 ×1 y CAS-006 ×1,
el total **Q 860.00**, enviar por correo y el correo en Mailpit con el enlace al portal.

**Qué decir:**
> «La oportunidad queda vinculada a la clienta. La cotización sale del CRM, no de una hoja aparte.
> El correo lo genera Odoo y llega a Mailpit, que es el servidor de pruebas; el enlace lleva al
> portal del cliente.»

### 3:30-5:30 · El portal cierra la venta

**Qué se ve:** abrir el enlace en incógnito, la cotización en el portal, **Aceptar**, el pago de
prueba, la confirmación del pedido. Luego, en el backend: el pedido confirmado, la entrega validada
y la factura pagada.

**Qué decir:**
> «El cliente acepta y paga en el portal. El pedido se confirma solo en Ventas, la factura se
> publica y la entrega se reserva. Cuando la bodega valida la entrega, baja la existencia. El mismo
> pedido se puede seguir en Ventas, Inventario y Facturación.»

**Ojo:** si el pago no queda pagado, no sigas: el inventario no baja y el BI no cuadra.

### 5:30-7:30 · BI de inventario y ventas

**Qué se ve:** las tres vistas de inventario (barras, pastel, stock bajo) y las tres de ventas
(líneas por día/semana/mes, top 5, margen por canal). Cambia una agrupación en vivo: de día a
semana, o el filtro de fecha.

**Qué decir:**
> «Los reportes salen de la misma base. Este es el inventario por producto, por categoría y los
> cuatro productos bajo el mínimo. En ventas, la historia del 05 al 20 se ve como una serie y los
> pedidos del sitio del 21 al 23 como la cola. El top 5 por unidades y el margen por canal salen
> del mismo informe.»

**No decir:** «Esto lo hice en Power BI». Es Odoo, y esa es la decisión que se defiende.

### 7:30-9:00 · Tablero y cierre

**Qué se ve:** el tablero con los siete reportes y un filtro aplicado en vivo.

**Qué decir:**
> «Los siete reportes están guardados como favoritos y reunidos en el tablero. El tablero se abre
> con el dato del momento. Esto es lo que permite que la gerencia vea inventario y ventas sin
> exportar nada.»

**Cierre:** «Con esto se cierra el flujo B: del formulario al portal, y del portal al reporte.»

## Demo en vivo · 4 minutos

| Min | Qué haces | Qué dices |
|---|---|---|
| 0:00 | Muestras el sitio y el formulario | «El cliente pide una cotización desde el sitio.» |
| 0:40 | Envías el formulario y abres el lead en el CRM | «El lead entra solo, con origen del sitio.» |
| 1:20 | Conviertes a oportunidad y muestras la cotización | «La cotización sale del CRM, con el precio de lista.» |
| 1:50 | Abres Mailpit y el portal | «El correo lleva al portal; el cliente acepta y paga.» |
| 2:30 | Muestras el pedido, la entrega y la factura | «El mismo pedido en Ventas, Inventario y Facturación.» |
| 3:10 | Abres el tablero y cambias un filtro | «El BI se actualiza con la venta recién hecha.» |

**Si el túnel falla:** usa las capturas del checklist y di que el respaldo está en la segunda
laptop. No improvises una base nueva.

## Diapositivas 6, 10 y 11

### Diapositiva 6 · Del sitio al CRM

- Título: «Del sitio al CRM».
- Subtítulo: «Flujo B: de un formulario a una venta aceptada en el portal».
- Tres pasos: **Formulario** (Contáctanos) → **Oportunidad y cotización** (CRM) → **Portal**
  (acepta y paga).
- Captura: el lead con origen Sitio web y la cotización aceptada.
- Frase: «El lead no se copia: nace en la misma base.»

### Diapositiva 10 · BI de inventario

- Título: «BI · Inventario».
- Tres capturas: barras por producto, pastel por categoría, tabla de stock bajo.
- Frase: «38 productos, 4 bajo el mínimo y 0 en cero; el dato sale de la misma base.»

### Diapositiva 11 · BI de ventas

- Título: «BI · Ventas».
- Dos capturas: líneas por día (y el cambio a semana/mes) y top 5.
- Frase: «56 pedidos y Q 19,111.00; el top 5 concentra el 57 % de las unidades.»
- Si el número real difiere, se dice: «el plan preveía... y Odoo mostró...».

## Reglas de la grabación

- Una toma por bloque; si algo falla, se corta y se repite el bloque, no todo el video.
- No muestres contraseñas, correos de administrador ni datos personales reales.
- El video se sube a Drive y el enlace va al anexo del informe; no se commitea el archivo.
- El video no reemplaza las capturas del manual: el manual necesita las figuras, no el video.
