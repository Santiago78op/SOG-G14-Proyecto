# Log — gerenciales

Bitácora append-only. Cada entrada: `## [YYYY-MM-DD] op | título` (op = ingest/query/lint). Consulta: `grep "^## \[" log.md | tail -5`. Index: [[00 - 📊 Cerebro Gerenciales (MOC)]].

## [2026-09-28] schema | Creado el cerebro del proyecto
Cerebro versionado dentro del repo `SOG-G14-Proyecto` (`wiki/`), con el mismo patrón que el de Redes: `CLAUDE.md` en la raíz importa `wiki/CONTEXTO-CLAUDE.md`, así cualquier integrante que use Claude Code arranca con el mismo contexto. Registrado en diamon como `gerenciales`. Notas iniciales: [[CONTEXTO-CLAUDE]], [[AVANCE]], [[Caso RutaMoto]], [[Ambiente Odoo]], [[Reparto y calendario Fase 2]], [[Datos maestros y cuadre]], [[Plan de compras y cotizaciones]], [[Rúbrica y requisitos]], [[Decisiones y límites]] y [[Glosario]].

## [2026-10-05] ingest | Carga masiva importada y ciclo de compras cerrado
Las siete hojas del Excel entraron en Odoo en orden de dependencia: 30 productos con imagen, 30 líneas de existencia aplicadas por Q 38,096.00, 30 reglas de reabastecimiento, 5 proveedores con sus 5 contactos, 30 líneas de lista de precios de proveedor y 35 clientes segmentados 12/11/7/5. Todo cuadra contra [[Datos maestros y cuadre]]. Se crearon LUB-007 y ELE-007 desde el sistema y las cinco compras de [[Plan de compras y cotizaciones]] quedaron en sus estados: P00001, P00002 y P00003 recibidas, P00004 confirmada sin recibir y P00005 como solicitud enviada. Tres defectos del archivo aparecieron en la validación previa y están documentados en [[AVANCE]] y [[Decisiones y límites]]: la ubicación `WH/Existencias`, los términos de pago en inglés y LUB-001 duplicado.

