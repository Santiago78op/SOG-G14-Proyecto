---
tags: [avance, estado, gerenciales]
aliases: [Estado, Dónde quedamos, Progreso]
---

# AVANCE: dónde quedamos

> Fuente de verdad del progreso. Se actualiza al cerrar cada sesión de trabajo. Fechas siempre absolutas.

## 📌 Último turno — 2026-10-05 (rol 1): informe final armado, manuales unidos y rama de entrega lista

**Próximo paso:** poner el enlace del video del rol 2 en el anexo E de `Informe_Fase2_Grupo14_RutaMoto.docx`, volver a exportar el PDF, comprimir `Entrega_Fase2_Grupo14/` desde la rama `entrega/fase2` y subir a UEDI. Es lo único que falta del informe.

### Qué se hizo

- El rol 2 subió el MU-02 y `informe_fase2_Jemima.docx`, que es el informe completo con sus secciones (6.3, 6.4, 8, 9 y 13) escritas sobre la versión que ya tenía las del rol 3. Se tomó como base.
- El informe final es **`1_Informe/Informe_Fase2_Grupo14_RutaMoto.docx`** y su **`.pdf`** (43 páginas). Sustituye a `informe_fase2_PLANTILLA.docx`, que ya no existe.
- Se borraron las tres páginas de trabajo y todo el texto gris de instrucción. Las franjas grises de rol se dejaron: son la evidencia de autoría por sección.
- Tablas (24) y figuras (14) numeradas; índice con las páginas del PDF.
- **Fecha:** carátula y alcance pasaron del 3 al **5 de octubre de 2026** (decisión del rol 1).
- **4.1:** las cinco actividades con «Cierre el 5 oct» y «Terminada», más una oración que dice que cerraron después de lo planificado. Es lo que respalda el repositorio; no se escribió una causa.
- **4.2:** se quitó la fila vacía. **Anexos:** se quitó la fila G (respaldo), porque nadie dio el nombre del archivo.
- **14 Conclusiones:** cinco párrafos redactados a partir de las secciones del informe. **El rol 1 tiene que leerlos antes de subir.**
- **Capturas del rol 4:** las siete figuras de las secciones 5.1, 10, 11 y 12 estaban como recuadro vacío. Se tomaron del MU-03.
- **Manuales:** `2_Manuales_Usuario/Manuales_Usuario_Fase2_Grupo14.pdf` une MU-00 (exportado ahora desde su `.docx`), MU-01, MU-02 y MU-03: 100 páginas, con marcadores por manual.
- Se quitó del repo `~WRL0364.tmp`, un temporal de Word que entró con el commit del rol 2.

### Correcciones de fondo que hay que conocer

- **La campaña llegó a 12 repartidores, no a 13.** La sección 11 decía 13 destinatarios y 13 / 13 / 0, pero las capturas del propio rol 4 muestran «12 correos enviados», el filtro con 12 registros y 12 mensajes en Mailpit. Se corrigió a 12 / 12 / 0, con la aclaración de que el segmento cerró en 13 al sumarse el repartidor de la carga manual. La hora de envío (5:09 p. m. del 5 de octubre) sale de la misma captura.
- **La captura del pipeline muestra las cinco oportunidades en «Nuevo lead»**, no repartidas por etapa: no hay ninguna captura del tablero con las cinco ya movidas. El pie de la figura lo dice así. La tabla de etapas finales es del rol 4 y no se tocó.
- **13.1:** los dos indicadores que el rol 2 dejó «Pendiente» se llenaron con lo documentado: exactitud de la carga masiva 100 % (165 registros, con la salvedad de LUB-001) y entrega de la campaña 100 % (12 de 12).
- **13.2, paso 6 (CRM):** quedó como «No verificado en esta fase», porque las oportunidades del pipeline son de clientes distintos de los cuatro cotizados.

### Lo que sigue flojo y no se pudo resolver sin el sistema

- **8.2:** las cotizaciones 2, 3 y 4 dicen «No visible en la evidencia» en el número de Odoo, y la 4 dice «se debe comprobar también el estado final». Es texto del rol 2; solo ella o la instancia pueden completarlo.
- **9.2:** la fecha prevista de P00004 dice «No visible en la vista consolidada».
- **MU-03:** sus 18 pies de figura siguen como «Figura __».
- **La presentación** sigue siendo `presentacion_fase2_PLANTILLA.pptx`.
- **El PDF del informe se exportó con LibreOffice**, no con Word (no hay Word en la máquina del rol 1). El escudo de la carátula se dejó como marca de agua dentro de la imagen para que se vea igual en los dos.

## 📌 Turno anterior — 2026-10-05 (rol 1): secciones de Alberto pasadas al informe

**Próximo paso:** sin cambios; sigue faltando todo lo del rol 2. El informe actualizado ya está también en `entrega/fase2`.

- Las secciones **5, 6.2, 6.4 y 7** (con 7.1, 7.2 y 7.3) de `informe_fase2_secciones_Alberto_Hernandez.docx` ya están en `informe_fase2_PLANTILLA.docx`, con sus dos figuras (el error de ubicación de la importación y el historial de movimientos). El `.docx` de Alberto se dejó como está.
- Se conservaron las franjas grises de rol y la 5.1 del rol 4. En esas secciones se borró lo gris de instrucción, **menos en la 6.4**: ahí la columna «Resultado obtenido» solo tiene la parte de la carga masiva (30 productos, Q 38,096.00, 5 proveedores, 12/11/7/5 clientes, 32 reglas) y el rol 2 tiene que completarla con la carga manual.
- Los pies que Alberto numeró (Tabla 1 a 8, Figura 1 y 2) volvieron a «__»: la numeración se hace al final, sobre el informe completo.
- El tamaño de letra se igualó al de la plantilla: su archivo traía el cuerpo a 10 pt y las celdas llenadas a 12 pt, al revés que el resto del informe.

## 📌 Turno anterior — 2026-10-05 (rol 1): rama `entrega/fase2` con solo los entregables

**Próximo paso:** sin cambios. El PDF y el ZIP siguen esperando lo del rol 2; los pendientes del rol 1 son los de la tabla del turno de abajo.

- `feature/201905884_Informe` se unió a `main`.
- Se creó la rama **`entrega/fase2`** a partir de `main`. Contiene solo lo que pide la sección 4.4 del enunciado, en el estado en que está hoy: `1_Informe/` (solo el informe: el `.docx` y el `.pdf` sueltos de Alberto se quitaron de la rama cuando sus secciones entraron en la plantilla, y siguen en `main`), `2_Manuales_Usuario/` (MU-00, MU-01, MU-03 y el MU-02 en plantilla, porque del rol 2 no hay otra versión), `3_Archivos_Datos/` completo, `4_Videos/` con los dos guiones y `5_Presentacion/` con el `.pptx`.
- Quedaron fuera de esa rama: `wiki/`, `CLAUDE.md`, el enunciado, la Fase 1, `_Referencia/`, el LEEME, el manual de la demo, las plantillas ya sustituidas del MU-01 y el MU-03 y la carpeta `capturas_MU-01/` (las capturas ya están dentro del manual). Los videos en sí se entregan como enlace de Drive en los anexos del informe; `4_Videos/` se conserva con los guiones para mantener la misma estructura de carpetas de la Fase 1.
- **Se sigue trabajando en `main`** y en las ramas `feature/`. `entrega/fase2` no se une de vuelta a `main`: borraría el cerebro y la Fase 1. Esa rama tampoco tiene `.gitignore` (se quitó para que el paquete traiga solo la carpeta de entrega), así que ahí hay que cuidar de no agregar `.venv/` ni `_Paquetes_para_integrantes/`. Las imágenes del Excel apuntan a `main`, así que tampoco se puede mover nada de `3_Archivos_Datos/imagenes_productos/` allá.

## 📌 Turno anterior — 2026-10-05 (rol 1): sección 6.1, bibliografía y enlaces de dos videos

**Próximo paso:** el rol 1 sigue bloqueado para armar el PDF y el ZIP hasta que llegue lo del rol 2 (MU-02, secciones 6.3, 8, 9 y 13, y su video). Mientras tanto: pasar las secciones de Alberto a la plantilla del informe y pedir el nombre del respaldo para el anexo G.

### Lo que cambió en `informe_fase2_PLANTILLA.docx`

- **6.1 Archivo de datos maestros**, redactada: estructura del Excel, por qué hay una hoja por modelo de Odoo, columnas importables e informativas, hojas de apoyo y el cuadre de Q 45,000.
- **Bibliografía**, completa: 9 páginas de la documentación de Odoo 18, la de Mailpit y el enunciado. Las URL se comprobaron el 2026-10-05 (todas responden) y esa es la fecha de consulta que quedó escrita. La entrada que ya estaba decía «Import data into Odoo»; la página se llama «Export and import data» y se corrigió.
- **Anexos:** D = video de carga y compras (rol 3), F = video del CRM (rol 4). Los dos enlaces abren sin sesión iniciada.

### Pendiente del rol 1

| Pieza | Estado |
|---|---|
| 4.1 Avance contra el cronograma | 🟡 faltan las columnas Real y Estado |
| 4.2 Correcciones a la Fase 1 | 🟡 borrar la fila vacía o llenarla si llega la nota |
| 14 Conclusiones | ⬜ espera la medición del rol 2 |
| 16 Anexos | 🟡 faltan E (video del rol 2) y G (nombre del respaldo) |
| Pasar a la plantilla las secciones de Alberto (5, 6.2, 6.4 y 7) | ✅ hecho el 2026-10-05; la 6.4 espera la parte del rol 2 |
| Unir manuales, numerar tablas y figuras, borrar lo gris, PDF y ZIP | ⬜ |

### Preguntas abiertas

- **Los videos no tienen el nombre acordado.** En Drive se llaman `geren1_fase2_parte_alberto_hernandez.mp4` y `Screen_Recording_20261005_190311_Gmail.mp4`. El segundo, por el nombre, puede ser solo la grabación del correo recibido y no el recorrido completo del CRM: **nadie lo ha revisado todavía.**
- **La fecha de entrega.** [[CONTEXTO-CLAUDE]] dice sábado 03-10-2026 y el trabajo sigue el 05-10. Si se movió, hay que corregirla ahí y en el alcance del informe, que dice «entre el 21 de septiembre y el 3 de octubre».
- **Del rol 2 no hay nada en el repo.**

## 📌 Turno anterior — 2026-10-05: carga masiva importada y ciclo de compras cerrado

**Próximo paso:** el resto del equipo ya puede trabajar sobre la instancia. Falta la carga manual (Accesorios y equipaje, AccesoRuta y 5 clientes), las cotizaciones, el informe de inventario, las plantillas de correo, la campaña y el pipeline. Entrar por el túnel con el usuario propio, no con `admin`.

### Lo que quedó cargado en Odoo

| Comprobación | Esperado (hoja Cuadre) | En Odoo |
|---|---|---|
| Productos de la carga masiva | 30 | 30 |
| Inventario al costo de lo importado | Q 38,096.00 | Q 38,096.00 |
| Proveedores y sus contactos | 5 y 5 | 5 y 5 |
| Líneas de lista de precios de proveedor | 30 | 30 |
| Reglas de reabastecimiento | 30 | 30 (32 con las de los productos adicionales) |
| Clientes por segmento | 12 · 11 · 7 · 5 | 12 · 11 · 7 · 5 |
| Productos bajo el mínimo al terminar la carga | 4 | 4 (LUB-004, FRE-001, ELE-002, LLA-002) |

Productos adicionales creados desde el sistema: **LUB-007** (Q 65 / Q 38) y **ELE-007** (Q 40 / Q 22).

Las cinco compras, en los estados del plan: **P00001** FRE-001 × 44 recibida (RMT/IN/00001, Q 2,420) · **P00002** LUB-004 × 72 y LUB-007 × 24 recibida (RMT/IN/00002, Q 2,280) · **P00003** ELE-007 × 30 recibida (RMT/IN/00003, Q 660) · **P00004** LLA-002 × 16 confirmada sin recibir (Q 4,400) · **P00005** ELE-002 × 88 solicitud enviada (Q 1,584). Inventario al costo después de las tres recepciones: **Q 43,456.00**.

### Tres defectos del Excel que aparecieron al importar (ninguno rompió nada)

1. **La ubicación.** El archivo dice `WH/Existencias`; la instancia tiene `RMT/Existencias` porque la bodega es «Bodega Central RutaMoto» con código RMT desde la Fase 1. La prueba previa rechazó las 30 filas sin escribir nada. **El archivo no se cambió**: la columna se dejó en «No importar» y Odoo asigna la ubicación por omisión, que es la correcta. La captura del error es evidencia buena para el informe.
2. **Los términos de pago estaban en inglés.** Se renombraron a los nombres del archivo y se creó «50% anticipo, 50% contra entrega». Odoo 18 ya no acepta el tipo de línea «saldo»: las dos líneas son porcentajes de 50.
3. **LUB-001 ya existía** desde la prueba de la Fase 1. Se importaron las 29 filas restantes y se completó la ficha existente, para no dejar dos productos con el mismo código. Su cantidad contada de 60 se aplicó sobre lo que había: quedó en 60, no en 75.

### Lo que hay que saber antes de tocar la base

- **Las reglas de reabastecimiento quedaron con disparador manual.** Es a propósito: con disparador automático el planificador nocturno genera órdenes solo y cambia el estado de las compras que la fase deja preparado.
- **No cierren las compras 4 y 5.** Son las órdenes pendientes de proveedores del informe de inventario.
- **No agreguen compras ni ventas fuera del plan.** Cada movimiento cambia el inventario valorizado del informe.
- Los tres usuarios nuevos existen pero **sin contraseña**: las define el rol 3 desde Ajustes › Usuarios y las pasa por el grupo.

### Estado de la Fase 2

| Pieza | Estado |
|---|---|
| Carga masiva (12.1) | ✅ importada y cuadrada contra la hoja Cuadre |
| Productos adicionales y ciclo de compras (12.2) | ✅ cinco compras en sus estados |
| Manual MU-01 | 🟡 redactado; faltan las capturas |
| Secciones 5, 6.2, 6.4 y 7 del informe | 🟡 redactadas; faltan las dos figuras |
| Guion del video de carga y compras | ✅ con script que conduce la pantalla |
| Carga manual, cotizaciones e informe de inventario | ⬜ |
| Correo, campaña y pipeline del CRM | ⬜ |
| Respaldo posterior a la carga | 🟡 hay que subirlo a Drive |

## 📌 Turno anterior — 2026-09-28: Fase 2 repartida y repo propio

**Próximo paso:** repartir los paquetes (`Entrega_Fase2_Grupo14/_Paquetes_para_integrantes/*.zip`, fuera de git) con los mensajes de `_Referencia/mensajes_whatsapp_fase2.md`. Después, el rol 3 prepara la instancia (respaldo, túnel, usuarios, categorías, etiquetas y términos de pago) para que el **martes 29-09** se haga la carga masiva, que es la ruta crítica.

### Estado de la Fase 2

| Pieza | Estado |
|---|---|
| Excel de datos maestros (7 hojas + carga manual + diccionario + cuadre) | ✅ hecho, **sin importar todavía** |
| 38 imágenes de producto (ilustraciones propias), logo y 2 banners | ✅ hechos; las imágenes se sirven desde el repo público por URL *raw* (verificado: HTTP 200) |
| Plantilla del informe (16 secciones) | 🟡 secciones 1–4 redactadas (rol 1); faltan las de los roles 2, 3 y 4 y el cierre (14–16) |
| Manuales MU-01, MU-02 y MU-03 | 🟡 plantillas con cada paso, ruta sugerida y recuadro de captura; **rutas de menú no probadas** |
| MU-00 (instalación de la Fase 1) | 🟡 faltan las capturas de los pasos 1, 2 y 4 del CRM (rol 4) |
| Carga, compras, cotizaciones, campaña y pipeline en Odoo | ⬜ no empezados |
| 3 videos | ⬜ guion listo, sin grabar |
| Presentación (12 diapositivas) y guion de la demo | ✅ listos; falta el ensayo |
| PDF y ZIP de entrega | ⬜ rol 1, al final |

### Decisiones de este turno

Ver [[Decisiones y límites]]. En corto: una sola base de Odoo con túnel y un usuario por integrante; la carga se partió por datos (masiva = 5 categorías, manual = Accesorios completa); la «requisición» es la alerta de reabastecimiento; Mailpit como servidor de correo recomendado; el repo quedó separado de `SO2_MT`.

### Defectos de este turno (contados, no tapados)

- Las primeras imágenes de producto repetían la rueda del logo en todos los productos. El usuario lo notó («ni los logos están de las llantas») y se rehicieron con una ilustración por producto.
- Hubo dos carpetas de Fase 1: la de trabajo y la entregada, bajada de Drive. Se dejó solo la entregada.
- Los primeros commits salieron con el trailer `Co-Authored-By` de Claude, contra la regla del dueño del repo. Se corrigieron con `--amend` + `--force-with-lease`.

### Preguntas abiertas

- ¿Servidor de correo: Mailpit o Gmail del grupo? Decide el rol 4 con el rol 3.
- ¿Porcentaje de la tarifa de talleres? Se propone 10 %; decide el rol 2.
- ¿Llegaron observaciones de la calificación de la Fase 1? Si llegan, van a la sección 4.2 del informe.
- No están en el repo el PDF subido a UEDI, los videos ni el ZIP de la Fase 1: nunca estuvieron en la máquina del rol 1.
