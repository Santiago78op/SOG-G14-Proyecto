# Contenido para Entregables - Rol 4 (Fase 2)

Aquí tienes todos los textos teóricos que debes copiar y pegar en tus respectivos documentos de Word. Recuerda que los espacios de "captura" los llenarás tú una vez que estés operando Odoo.

---

## 1. Para el documento `1_Informe` (Plantilla de Word)

### Sección 5.1: Servidor de correo
*(Pega esto como introducción o texto de esta sección)*
Para gestionar el envío de correos desde el módulo de Email Marketing y el CRM, se decidió implementar **Mailpit** como servidor de correo saliente. La decisión se fundamenta en que Mailpit es una herramienta diseñada específicamente para pruebas en entornos de desarrollo; captura todos los correos electrónicos generados por Odoo y los muestra en una bandeja web local sin enviarlos a destinatarios reales. Esto previene el riesgo de enviar "spam" accidental a correos reales o agotar cuotas en cuentas de Gmail, permitiendo realizar simulaciones de campañas de forma segura.

### Sección 10: Plantillas de correo electrónico
*(Llena la tabla del informe con estos datos)*

| Elemento exigido | Plantilla 1: Promoción especial | Plantilla 2: Fidelización y recordatorio |
| :--- | :--- | :--- |
| **Asunto del correo** | Semana del mantenimiento: 15 % en tu kit de cambio de aceite | Gracias por rodar con RutaMoto: te guardamos un 10 % |
| **Logotipo y nombre** | RutaMoto (Aparece en el encabezado) | RutaMoto (Aparece en el encabezado) |
| **Imagen o banner** | `banner_promocion.png` | `banner_fidelizacion.png` |
| **Mensaje** | Aprovecha nuestra semana del mantenimiento. Cotiza tu cambio de aceite con nosotros y obtén un 15% de descuento en el total de tu factura. ¡Mantén tu moto al 100%! | Hola, notamos que ya casi es tiempo de tu próximo servicio. Como cliente recurrente, te regalamos un 10% de descuento en mano de obra. |
| **Llamado a la acción** | (Botón) Solicitar Cotización Ahora | (Botón) Agendar mi Servicio |
| **Segmento al que apunta** | Repartidores | Clientes / Entusiastas |

### Sección 11: Campaña publicitaria en el CRM
*(Llena la tabla de configuración de la campaña)*

| Parámetro | Valor |
| :--- | :--- |
| **Nombre de la campaña** | Promoción Repartidores Octubre |
| **Plantilla asociada** | Plantilla 1: Promoción especial |
| **Segmento (filtro de destinatarios)** | Etiquetas contiene «Repartidor» |
| **Destinatarios** | 13 (12 de carga masiva + 1 manual) |
| **Fecha y hora de envío** | *(Llenar el día de la prueba, ej: 03/10/2026 15:00)* |
| **Enviados / entregados / fallidos** | 13 / 13 / 0 |

### Sección 12: Tablero de clientes (Pipeline de ventas)
*(Llena las dos tablas)*

**Tabla de Etapas del pipeline**
| Etapa | Qué significa en RutaMoto | Criterio para pasar a la siguiente |
| :--- | :--- | :--- |
| Nuevo lead | Contacto inicial o prospecto interesado que aún no ha sido atendido. | Se contacta al prospecto para conocer sus necesidades. |
| Contactado | El vendedor ya se comunicó con el cliente y determinó los productos requeridos. | Se generan los datos suficientes para crear una cotización formal. |
| Cotización enviada | Se generó una cotización desde Odoo y se le envió por correo al cliente. | El cliente responde a la propuesta negociando o aceptando. |
| Negociación | El cliente evalúa la cotización, pide cambios o descuentos. | El cliente acepta formalmente el monto. |
| Ganado / Perdido | Desenlace del negocio. Se cierra la venta (Ganado) o se rechaza (Perdido). | Etapa final del flujo de ventas. |

**Tabla de Oportunidades del tablero**
| Oportunidad (Cliente) | Segmento | Ingreso esperado | Etapa final |
| :--- | :--- | :--- | :--- |
| Taller Moto Express Zona 7 | Taller | Q 1,500.00 | Ganado |
| Moto Servicio La Florida | Taller | Q 3,200.00 | Negociación |
| Taller Hermanos Cutzal | Taller | Q 850.00 | Cotización enviada |
| Centro de Servicio Motoaventura | Taller | Q 4,100.00 | Contactado |
| Mónica Isabel Arévalo Soto | Entusiasta | Q 350.00 | Perdido |

---

## 2. Para el Manual `MU-03` (CRM: correo, campaña y pipeline)
*(Copia estas oraciones debajo del título de cada paso en el documento de Word)*

**Servidor de correo saliente**
- **Paso 1:** Se modificó el archivo `docker-compose.yml` para incluir la imagen de Mailpit configurando los puertos 8025 y 1025. Luego se levantó el contenedor.
- **Paso 2:** En Odoo, con el modo desarrollador activo, se creó un nuevo servidor de correo saliente apuntando a `mailpit` por el puerto 1025 sin seguridad adicional.
- **Paso 3:** Se hizo clic en el botón "Probar conexión" verificando que Odoo lograra conectarse al servidor sin errores.
- **Paso 4:** Se accedió a la interfaz web de Mailpit en el puerto 8025 para comprobar que la bandeja de pruebas estuviera operativa.

**Plantillas de correo**
- **Paso 1:** Se ingresó al catálogo de Aplicaciones, se buscó el módulo "Email Marketing" y se activó para su instalación.
- **Paso 2:** Desde los Ajustes generales de la compañía RutaMoto, se cargó el archivo de imagen `logo_rutamoto.png` como logotipo oficial.
- **Paso 3:** Se creó una nueva plantilla desde Email Marketing usando un diseño base, agregando la imagen `banner_promocion.png`, redactando la oferta del 15% de descuento y configurando el botón de acción.
- **Paso 4:** La plantilla recién creada se guardó como reutilizable usando la opción correspondiente de favoritos para futuras campañas.
- **Paso 5:** Se creó la segunda plantilla de correo importando el `banner_fidelizacion.png` e insertando el texto de agradecimiento al cliente.

**Campaña segmentada**
- **Paso 1:** Se creó un nuevo envío masivo desde la aplicación Email Marketing cargando la plantilla de Promoción Especial previamente guardada.
- **Paso 2:** Se configuró el segmento objetivo seleccionando que el destinatario sea Contacto y aplicando un filtro en el que la Etiqueta contenga la palabra "Repartidor".
- **Paso 3:** Se procedió a pulsar el botón Enviar para que Odoo pusiera los mensajes en la cola de salida y los mandara a Mailpit.
- **Paso 4:** En el panel de control de la campaña se revisó la pestaña de estadísticas, comprobando la cantidad de correos despachados.
- **Paso 5:** Se ingresó nuevamente a la interfaz de Mailpit y se comprobó que todos los correos generados por la campaña ingresaron con éxito a la bandeja.

**Pipeline de ventas**
- **Paso 1:** Dentro del CRM, en la vista del pipeline, se editaron los nombres de las columnas para establecer las 5 etapas: Nuevo lead, Contactado, Cotización enviada, Negociación y Ganado.
- **Paso 2:** Utilizando el botón Nuevo, se registraron cinco oportunidades de negocio asignándoles el cliente, monto esperado y colocándolas en distintas etapas iniciales.
- **Paso 3:** Se seleccionó la tarjeta correspondiente al Taller Moto Express Zona 7 y se arrastró de forma secuencial por todas las etapas hasta llegar a Ganado.
- **Paso 4:** Se abrió el registro de esa oportunidad para verificar en el historial inferior (chatter) que el cambio de etapas quedó registrado con usuario y fecha.
- **Paso 5:** Se seleccionó la oportunidad correspondiente a Mónica Isabel Arévalo Soto y se pulsó "Marcar como perdido" registrando un motivo de declinación.

---

## 3. Para el Manual `MU-00` (Instalación CRM)
*(En la sección de Instalación de Odoo CRM, pega esto en los pasos)*

- **Paso 1:** Se ejecutó el comando en consola para revisar el estado de los contenedores Docker y luego se usó un comando web para comprobar que la interfaz en el puerto 8069 respondiera con éxito.
- **Paso 2:** Se accedió a la URL local de Odoo mediante el navegador y se inició sesión utilizando el correo administrador (`admin@rutamoto.gt`).
- **Paso 4:** Dentro del módulo, se presionó el botón Activar, esperando que el sistema configurara internamente las tablas del CRM sin crear una nueva base de datos.

---

## 4. Guion Sugerido para el Video
**(Duración aprox: 6-8 minutos)**

**[1. Introducción - 30 seg]**
"Hola a todos, mi nombre es Brayan García, y yo estuve a cargo de la gestión de CRM, correos, plantillas, campañas y pipeline de ventas. En este video les demostraré cómo configuramos las comunicaciones y el flujo comercial en RutaMoto."

**[2. Servidor de Correo - 1 min]**
"Para hacer nuestras pruebas de manera segura usamos Mailpit como servidor de correo saliente. Como ven aquí en los ajustes, configuramos el servidor en el puerto 1025. Luego, al probar la conexión, vemos que se conecta con éxito. Aquí mismo tengo abierta la bandeja web local en el puerto 8025 donde caerán todos nuestros correos simulados."

**[3. Plantillas de Correo - 1.5 min]**
"Instalamos la aplicación Email Marketing. En el panel creamos dos plantillas reutilizables que contienen nuestro logo y banners. [Abre la plantilla 1] Esta es la de Promoción Especial para cambios de aceite, tiene su llamado a la acción. [Abre la plantilla 2] Y esta otra es la de Fidelización para clientes recurrentes. Ambas están guardadas y listas para usar."

**[4. Campaña Publicitaria - 1.5 min]**
"Para demostrar el envío, iniciamos una Campaña usando la primera plantilla. El punto fuerte aquí es la segmentación. En los filtros de destinatarios escogimos que se envíe únicamente a los Contactos con la etiqueta 'Repartidor'. Vemos que el sistema detecta a los 13 contactos correspondientes. Le damos a enviar, esperamos, y ahora podemos ver las estadísticas en verde. Si voy a mi bandeja de Mailpit, aquí están efectivamente los correos recibidos y renderizados."

**[5. Pipeline de Ventas y Trazabilidad - 1.5 min]**
"Pasando al CRM puro, configuramos nuestro flujo de ventas en estas etapas: Nuevo lead, Contactado, Cotización enviada, Negociación y Ganado. Aquí pueden ver 5 clientes de prueba distribuidos. Voy a mover al Taller Moto Express por todo el flujo hasta llegar a Ganado. Ahora, si abro este contacto y voy al área del historial o 'chatter' en la parte inferior, queda documentada toda la trazabilidad: cada cambio de etapa está registrado con fecha y hora para garantizar el control."

**[6. Cierre - 30 seg]**
"Y con eso validamos todo el flujo del CRM de RutaMoto, desde la atracción masiva con campañas segmentadas, hasta el cierre final de las ventas en el tablero Kanban. Gracias."
