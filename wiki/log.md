# Log — gerenciales

Bitácora append-only. Cada entrada: `## [YYYY-MM-DD] op | título` (op = ingest/query/lint). Consulta: `grep "^## \[" log.md | tail -5`. Index: [[00 - 📊 Cerebro Gerenciales (MOC)]].

## [2026-09-28] schema | Creado el cerebro del proyecto
Cerebro versionado dentro del repo `SOG-G14-Proyecto` (`wiki/`), con el mismo patrón que el de Redes: `CLAUDE.md` en la raíz importa `wiki/CONTEXTO-CLAUDE.md`, así cualquier integrante que use Claude Code arranca con el mismo contexto. Registrado en diamon como `gerenciales`. Notas iniciales: [[CONTEXTO-CLAUDE]], [[AVANCE]], [[Caso RutaMoto]], [[Ambiente Odoo]], [[Reparto y calendario Fase 2]], [[Datos maestros y cuadre]], [[Plan de compras y cotizaciones]], [[Rúbrica y requisitos]], [[Decisiones y límites]] y [[Glosario]].

## [2026-10-05] ingest | Carga masiva importada y ciclo de compras cerrado
Las siete hojas del Excel entraron en Odoo en orden de dependencia: 30 productos con imagen, 30 líneas de existencia aplicadas por Q 38,096.00, 30 reglas de reabastecimiento, 5 proveedores con sus 5 contactos, 30 líneas de lista de precios de proveedor y 35 clientes segmentados 12/11/7/5. Todo cuadra contra [[Datos maestros y cuadre]]. Se crearon LUB-007 y ELE-007 desde el sistema y las cinco compras de [[Plan de compras y cotizaciones]] quedaron en sus estados: P00001, P00002 y P00003 recibidas, P00004 confirmada sin recibir y P00005 como solicitud enviada. Tres defectos del archivo aparecieron en la validación previa y están documentados en [[AVANCE]] y [[Decisiones y límites]]: la ubicación `WH/Existencias`, los términos de pago en inglés y LUB-001 duplicado.


## [2026-10-05] ingest | Sección 6.1, bibliografía y enlaces de dos videos en el informe
El rol 1 redactó la 6.1 (estructura del Excel y cuadre de Q 45,000, tomados de [[Datos maestros y cuadre]]) y completó la bibliografía con 9 páginas de la documentación de Odoo 18, la de Mailpit y el enunciado, todas comprobadas ese día. En los anexos quedaron los enlaces de Drive de los videos del rol 3 (D) y del rol 4 (F). Faltan el video del rol 2 y el nombre del respaldo. Pendientes y preguntas abiertas en [[AVANCE]].

## [2026-10-05] schema | Rama `entrega/fase2` con solo los entregables
`feature/201905884_Informe` se unió a `main` y de ahí salió `entrega/fase2`, que conserva únicamente el informe, los manuales, los archivos de datos y la presentación de la Fase 2 (sección 4.4 del enunciado). No se une de vuelta a `main`. Qué entró y qué quedó fuera, en [[AVANCE]].

## [2026-10-05] ingest | Secciones del rol 3 pasadas al informe
Las secciones 5, 6.2, 6.4 y 7 de Alberto se pasaron de su `.docx` a `informe_fase2_PLANTILLA.docx`, con sus dos figuras. La tabla de la 6.4 quedó con la parte de la carga masiva y espera la del rol 2. Detalle en [[AVANCE]].

## [2026-10-05] ingest | Informe final de la Fase 2 armado y manuales unidos
Con lo del rol 2 en el repo, el informe quedó como `Informe_Fase2_Grupo14_RutaMoto` (`.docx` y `.pdf`, 43 páginas): sin páginas de trabajo ni texto gris, con tablas y figuras numeradas, conclusiones redactadas y las capturas del rol 4 tomadas del MU-03. Los cuatro manuales se unieron en `Manuales_Usuario_Fase2_Grupo14.pdf`. La campaña se corrigió a 12 destinatarios, que es lo que muestran las capturas. Falta solo el enlace del video del rol 2 en el anexo E. Detalle y puntos flojos en [[AVANCE]].
