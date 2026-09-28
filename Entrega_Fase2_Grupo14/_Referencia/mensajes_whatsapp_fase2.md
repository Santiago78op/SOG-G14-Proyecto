# Mensajes para el grupo: Fase 2 (Grupo 14)

Listos para copiar y pegar. Van con los asteriscos de WhatsApp (`*negrita*`). Primero el mensaje general, después uno por persona, cada uno con su paquete adjunto (carpeta `_Paquetes_para_integrantes`).

---

## 1) Mensaje general

> Buenas. Va la repartición de la *Fase 2*. Se entrega el *sábado 3 de octubre* y ese mismo día es la presentación, que esta vez es una *demo en vivo* del sistema: 20 puntos. Quedan cinco días.
>
> Ya está todo armado: la plantilla del informe, un manual por rol con cada paso y su recuadro de captura, y el *Excel de datos maestros listo para importar* (36 productos, 6 proveedores, 40 clientes, existencias y mínimos). Nadie arranca de cero.
>
> 👉 [PEGAR AQUÍ EL ENLACE DE LA CARPETA]
>
> Abran primero *LEEME_PRIMERO*. A cada uno le mando aparte su paquete con solo lo suyo.
>
> *Dónde se escribe:* el *manual* es uno por persona, así que lo trabaja cada quien en su archivo y me lo devuelve. El *informe* es uno solo: lo subo a Drive y cada quien escribe en las secciones con su franja gris. La copia del informe que viene en el paquete es solo para verlo sin internet.
>
> *El reparto:*
> • *Jemima (rol 2):* carga manual, cotizaciones a clientes, informe de inventario y medición.
> • *Alberto (rol 3):* carga masiva del Excel y el ciclo completo de compras.
> • *Brayan (rol 4):* servidor de correo, plantillas, campaña y pipeline del CRM.
> • *Yo (rol 1):* el Excel, las secciones de marco, unir los manuales y armar el PDF y el ZIP.
>
> *Una sola base de Odoo para los cuatro:* la de la laptop de Alberto, con acceso remoto por un túnel y un usuario para cada quien. Nada de copias: si cada uno carga en la suya, el sábado no cuadra nada.
>
> *Ojo con el orden:* la carga masiva del *martes* es la ruta crítica. La campaña, el pipeline, las cotizaciones y el inventario dependen de que esa carga esté hecha.
>
> Dos cosas que son requisito y no rúbrica, o sea que si fallan la nota es cero: el *ciclo de compras* tiene que poder demostrarse en vivo, y los *manuales tienen que tener captura* en cada paso.

---

## 2) Rol 2: Jemima

> *ROL 2 · Jemima: carga manual, cotizaciones, inventario y medición*
>
> Te toca la mitad manual de la carga (de 30 puntos), las cotizaciones (de 15) y la medición (5). Tu manual es el *MU-02*.
>
> *Qué hacés en Odoo*
> • *12.1 Carga manual (martes).* A mano, desde los formularios, lo que el Excel NO trae: la categoría *Accesorios y equipaje* completa (6 productos con precio, costo, imagen y existencia), su proveedor *AccesoRuta Importaciones* y 5 clientes. Los datos exactos están en la hoja *NO_IMPORTAR_carga_manual* del Excel. Podés hacerlo al mismo tiempo que Alberto importa, porque son datos distintos.
> • *12.3 Cotizaciones (miércoles).* Creás la tarifa *Talleres B2B* con descuento y hacés las 4 cotizaciones del plan: una facturada, una entregada, una enviada y una cancelada. Las cantidades ya están elegidas para no dejar ningún producto en cero; no las cambies sin avisar.
> • *12.4 Informe de inventario (jueves).* Existencias actuales, órdenes pendientes de proveedores y alertas de stock bajo. Va al final porque necesita las compras de Alberto terminadas.
>
> *Qué escribís en el informe:* secciones 6.3, 8, 9 y 13. En la 13, por primera vez el KPI de quiebre de stock de la Fase 1 se mide con datos reales. Tiene que dar 2.6 %, dentro de la meta del 5 %.
>
> *Video:* cotizaciones e informe de inventario, de 6 a 8 minutos. El guion está en 4_Videos.

---

## 3) Rol 3: Alberto

> *ROL 3 · Alberto: carga masiva y ciclo de compras*
>
> Sos la ruta crítica de la fase, igual que en la Fase 1. La instancia vive en tu laptop y la carga masiva desbloquea a los otros tres. Te toca la mitad masiva de la carga (de 30) y las compras (de 15). Tu manual es el *MU-01*.
>
> *Hoy lunes*
> • *Respaldo* de la base antes de tocar nada.
> • *Túnel* para que entremos: `cloudflared tunnel --url http://localhost:8069` (se instala con `winget install Cloudflare.cloudflared`). Agregá `proxy_mode = True` al odoo.conf. Pasá la URL por el grupo.
> • *Un usuario por integrante*, con su nombre.
> • Las *6 categorías sin categoría padre*, las *4 etiquetas* de segmento y el término de pago *50 % anticipo, 50 % contra entrega*. Sin eso la importación falla.
>
> *Martes: la carga masiva.* Siete hojas del Excel, en el orden del LEEME. Siempre *Probar* antes de *Importar* y capturá el mensaje de validación. Tres cosas frágiles: el nombre de la ubicación (WH/Existencias o como se llame en tu Odoo), los nombres de los términos de pago, y que las categorías no tengan padre. Al terminar, respaldo y *avisá en el grupo*.
>
> *Miércoles: compras.* Creás a mano los 2 productos adicionales (LUB-007 y ELE-007). Después el ciclo completo: la alerta de stock bajo de FRE-001 genera la solicitud de cotización, se confirma como orden y se recibe. Son 5 compras: 3 recibidas, 1 confirmada sin recibir y 1 solo enviada. *Las dos últimas se dejan abiertas a propósito*, porque son las órdenes pendientes del informe de Jemima.
>
> Odoo no tiene un documento que se llame "requisición". En nuestro diseño, la requisición es la alerta de reabastecimiento. Explicalo así, como decisión, en el manual y en la demo.
>
> *En el informe:* secciones 5, 6.2, 6.4 (con Jemima) y 7. *Video:* carga y compras, de 8 a 10 minutos.

---

## 4) Rol 4: Brayan

> *ROL 4 · Brayan: CRM, correo, campañas y pipeline*
>
> Todo el CRM es tuyo: los 10 puntos de correos, más el pipeline. Tu manual es el *MU-03*.
>
> *Lo que no depende de nadie (lunes y martes)*
> • *Servidor de correo.* Sin él la campaña queda en error. Te recomiendo *Mailpit*: un contenedor que se agrega al docker-compose de Alberto, captura todos los correos y los muestra con su diseño en una página, sin credenciales. Coordinalo con él. La opción B es un Gmail del grupo con contraseña de aplicación.
> • *Las 2 plantillas:* una de promoción especial y otra de fidelización. Cada una con logo y nombre, banner y un texto corto con llamado a la acción. En 3_Archivos_Datos/marca ya hay un logo y dos banners de propuesta.
> • *MU-00:* el manual de instalación del CRM de la Fase 1 no tenía captura en los pasos 1, 2 y 4. Completalas, que la rúbrica de esta fase vuelve a evaluar esos manuales.
>
> *Cuando esté la carga (miércoles)*
> • *Campaña* al segmento *Repartidor* (13 destinatarios) con una de tus plantillas. Capturá el filtro, las estadísticas y los correos recibidos.
> • *Pipeline* con 5 etapas (Nuevo lead, Contactado, Cotización enviada, Negociación, Ganado), 5 oportunidades con talleres y entusiastas de la base, y *una movida por todas las etapas*. La trazabilidad se muestra con el historial de la oportunidad.
>
> *En el informe:* secciones 5.1, 10, 11 y 12. *Video:* plantillas, campaña y pipeline, de 6 a 8 minutos.
