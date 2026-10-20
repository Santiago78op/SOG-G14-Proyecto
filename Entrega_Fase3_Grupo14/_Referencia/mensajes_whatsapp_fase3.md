# Mensajes para el grupo: Fase 3 (Grupo 14)

Listos para copiar y pegar, con los asteriscos de WhatsApp (`*negrita*`). Primero el mensaje general y después uno
por persona, cada uno con su paquete adjunto (`Entrega_Fase3_Grupo14/_Paquetes_para_integrantes/`).

---

## 1) Mensaje general

> Buenas. Va la repartición de la *Fase 3*, la última. Se entrega el *sábado 24 de octubre* y ese día es la
> presentación final en vivo (20 puntos). Quedan cuatro días.
>
> Lo que pide: el *sitio de e-commerce* (catálogo, carrito, registro, cotizaciones y facturación), la *integración*
> con el ERP y el CRM, el *portal del cliente* y los *reportes BI* de inventario y ventas. El enunciado dice que la
> integración es lo que más pesa.
>
> Ya está armado: un manual por rol, la plantilla del informe y el *plan de ventas* con los pedidos exactos que
> cada uno hace en el sitio. Todo está en el repo (`git pull`) y les mando su paquete aparte.
>
> *Decisiones:*
> • El sitio es el Comercio electrónico de *Odoo*, en la misma base de la Fase 2. Por eso la integración es real:
> la compra crea sola el pedido, la factura y el movimiento de inventario.
> • El BI se hace con los *informes de Odoo* (gráficos, pivote y tablero), no con Power BI.
> • Para que la gráfica de ventas por día, semana y mes tenga datos, Alberto carga con un script una *historia
> simulada* de 45 pedidos (del 5 al 20 de octubre). El informe lo dice así. Las compras del 21 al 23 las hacemos
> nosotros en el sitio.
>
> *El reparto:*
> • *Alberto (rol 3):* sitio, configuración, P00004 y la carga de la historia. *Miércoles: ruta crítica.*
> • *Jemima (rol 2):* compras de prueba en el sitio y portal del cliente.
> • *Brayan (rol 4):* flujo del CRM desde el sitio y los reportes BI.
> • *Yo (rol 1):* plan de ventas, informe, KPIs, conclusiones, presentación, PDF y ZIP.
>
> *Ojo:* solo se compran por el sitio los pedidos del plan. Cada compra de más cambia los números del BI.

---

## 2) Rol 3: Alberto

> *ROL 3 · Alberto: sitio e-commerce e integración*
>
> Sos la ruta crítica: hasta que el sitio no esté publicado nadie puede comprar. La meta es tenerlo listo el
> *miércoles 21*. Tu manual es el *MU-04*.
>
> *En orden:*
> 1. *Respaldo* de la base.
> 2. Instalá *Comercio electrónico* y activá *Márgenes* en Ventas.
> 3. Registro gratuito, *pago de prueba* (Demo o Transferencia en modo de prueba) y *facturación automática*.
> 4. Las 6 categorías del sitio y los *38 productos publicados*. Que no se venda sin existencia.
> 5. Recibí *P00004* (LLA-002 × 16).
> 6. *La historia:* `cargar_historial_ventas.py`, *primero con --probar*. Si dice PROBLEMAS, pará y mandame la
> salida. Instrucciones arriba del script; corre dentro del contenedor, no hay que instalar nada.
> 7. Pasá la URL del túnel al grupo.
>
> La lista completa con las rutas está en el LEEME, sección «Configuración del sitio». Las rutas no están probadas:
> si la pantalla dice otra cosa, gana la pantalla y lo anotás en el manual.
>
> En el informe: secciones *5, 6.1 y 6.3*, y la *9* conmigo. Video: sitio y configuración (6–8 min).

---

## 3) Rol 2: Jemima

> *ROL 2 · Jemima: compras de prueba y portal del cliente*
>
> Sos la clienta: hacés las compras del plan *en el sitio*, como lo haría alguien de verdad. Tu manual es el *MU-05*.
>
> *Tus pedidos* (hoja *2_Pedidos_sitio* del Excel de ventas): WEB-01 a 08, WEB-10 y WEB-12. Cada uno prueba algo
> distinto: cliente nuevo, cliente con portal, taller con tarifa B2B, LLA-002 que vuelve al catálogo y un carrito
> abandonado a propósito (WEB-07, *no lo pagués*).
>
> Por cada pedido: el número que le da Odoo, la factura, *validar la entrega* en Inventario y revisar el *portal*.
> Para los clientes nuevos usá correos tuyos con +1, +2… (`tucorreo+1@gmail.com`) o `@example.com` si el correo
> sale por Mailpit.
>
> Capturas mientras lo hacés. Lo que falle va a «Defectos encontrados»: vale más que lo que sí funcionó.
>
> En el informe: secciones *7 y 8*. Video: una compra de punta a punta (6–8 min). *Jueves 22* empezás, apenas
> Alberto avise que el sitio está publicado.

---

## 4) Rol 4: Brayan

> *ROL 4 · Brayan: CRM en el sitio y reportes BI*
>
> Dos partes. Tu manual es el *MU-06*.
>
> *1. Del sitio al CRM (WEB-09 y WEB-11, flujo B):* formulario de contacto del sitio → lead en el CRM → oportunidad →
> cotización → enviada por correo (Mailpit) → el cliente la acepta y paga en el portal.
>
> *2. BI con los informes de Odoo:*
> • Inventario: *barras* de existencias por producto, *pastel* por categoría y *tabla* de productos bajo el mínimo.
> • Ventas: *líneas* por día, semana y mes, el *top 5* de productos y ventas con *margen* por canal.
> • Guardalos como favoritos y armá un *tablero*.
>
> El BI se termina *después del último pedido del viernes*, para que las capturas tengan todo. Lo que tiene que dar
> está en la hoja *4_Cuadre* del Excel de ventas: si Odoo da otra cosa, avisame antes de capturar.
>
> En el informe: secciones *6.2 y 10*. Video: CRM en el sitio y BI (8–10 min).
