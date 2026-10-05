---
tags: [avance, estado, gerenciales]
aliases: [Estado, Dónde quedamos, Progreso]
---

# AVANCE: dónde quedamos

> Fuente de verdad del progreso. Se actualiza al cerrar cada sesión de trabajo. Fechas siempre absolutas.

## 📌 Último turno — 2026-10-05: carga masiva importada y ciclo de compras cerrado

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
