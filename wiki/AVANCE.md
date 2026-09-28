---
tags: [avance, estado, gerenciales]
aliases: [Estado, Dónde quedamos, Progreso]
---

# AVANCE: dónde quedamos

> Fuente de verdad del progreso. Se actualiza al cerrar cada sesión de trabajo. Fechas siempre absolutas.

## 📌 Último turno — 2026-09-28: Fase 2 repartida y repo propio

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
