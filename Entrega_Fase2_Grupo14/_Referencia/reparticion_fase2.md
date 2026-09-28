# Repartición: Proyecto 1, Fase 2 (Grupo 14)

Alcance: **solo la Fase 2**, que se entrega el **sábado 3 de octubre de 2026**, el mismo día de la presentación técnica. Hoy es lunes 28: quedan cinco días.

Según la metodología del enunciado, la Fase 2 es *Configuración, desarrollo de módulos y operación base*. Deja el ERP y el CRM con datos reales, con los procesos de compra, cotización y campaña funcionando. La Fase 1 dejó Odoo instalado; ahora hay que hacerlo operar.

---

## La rúbrica de la Fase 2

| Área | Criterio | Puntos |
|---|---|---|
| Habilidades (40) | Documentación técnica: manuales de instalación y configuración con capturas | 10 |
| | Cumplimiento de entregables: estructura, formato y empaquetado | 10 |
| | Presentación técnica: demostración funcional de carga de datos y procesos ERP/CRM | 20 |
| Conocimiento (60) | Carga de productos, clientes y proveedores: importación masiva y manual, validación en sistema | **30** |
| | Procesos de compras y cotizaciones: flujo funcional completo en el ERP | 15 |
| | Envío de correos desde el CRM: plantillas y ejecución de campaña | 10 |
| | Medición de logros: indicadores de rendimiento y validación del flujo | 5 |

Hay dos diferencias con la Fase 1:

1. **Ya no son cuatro bloques de 15.** Los 60 puntos vienen en 30 + 15 + 10 + 5, así que el reparto no puede ser un bloque por persona. Los dos bloques grandes se parten en mitades que no se pisan.
2. **La presentación es una demo en vivo** (20 puntos). No alcanza con diapositivas: el catedrático va a pedir que le muestren el sistema funcionando.

Y hay dos **requisitos de calificación** que vuelven a aplicar: el *Módulo Avanzado Implementado* (el ciclo de compras RFQ → PO → Recepción tiene que ser demostrable) y la *Documentación Obligatoria* (manuales con capturas completos). Si falla uno, la nota del proyecto es cero.

## Los cuatro roles

| # | Integrante | Qué hace | Bloque que responde | Manual |
|---|---|---|---|---|
| 1 | Santiago Julián Barrera Reyes | Excel de datos maestros (ya armado), secciones de marco del informe (1–4, 14–16), une los manuales, PDF y ZIP | Entregables (10) · coherencia de la documentación (10) | — |
| 2 | Jemima Solmaira Chavajay | 12.1 **carga manual** · 12.3 cotización a clientes · 12.4 informe de inventario · medición | Carga, parte manual (de 30) · Cotizaciones (de 15) · Medición (5) | MU-02 |
| 3 | Alberto Josué Hernández Armas | Administra la instancia · 12.1 **carga masiva** · 12.2 almacén y ciclo de compras | Carga, parte masiva (de 30) · Compras (de 15) | MU-01 |
| 4 | Brayan Emanuel García | Servidor de correo · 13 plantillas · 14 campaña · 15 pipeline · completa capturas del MU-00 | Correos del CRM (10) | MU-03 y MU-00 |

La presentación técnica (20) es de los cuatro: cada quien demuestra lo que configuró.

### Por qué así

- **La carga (30 puntos) se parte por datos, no por tarea.** El rol 3 importa el Excel: 30 productos de cinco categorías, 5 proveedores, 35 clientes. El rol 2 carga a mano lo que el Excel **no trae**: la categoría *Accesorios y equipaje* completa (6 productos), su proveedor AccesoRuta y 5 clientes. Así la carga manual no es una repetición de la masiva, los dos pueden trabajar al mismo tiempo sin pisarse y entre los dos completan el catálogo de 36.
- **Compras y cotizaciones (15) se parten por módulo.** Compras al rol 3, que ya administra el ERP y tiene el ciclo avanzado, que es requisito. Cotizaciones al rol 2, que ya tiene los clientes en la cabeza desde los beneficiarios y los segmentos de la Fase 1.
- **El CRM completo es del rol 4**, que lo instaló en la Fase 1. El pipeline no tiene puntos propios en la rúbrica de la Fase 2, pero la metodología lo pone en esta fase y el catedrático lo va a pedir en la demo.
- **El rol 1 no toca Odoo.** Prepara el Excel antes y arma la entrega después. Un quinto par de manos sobre la misma base solo agrega riesgo de que alguien mueva un número.

## Lo que ya está hecho

| Qué | Dónde | Detalle |
|---|---|---|
| **Excel de datos maestros** | `3_Archivos_Datos/RutaMoto_datos_maestros_Fase2.xlsx` | Una hoja por modelo de Odoo, en orden de importación, más un diccionario de campos, la hoja de carga manual y un cuadre |
| 38 imágenes de producto | `3_Archivos_Datos/imagenes_productos/` | Referenciales (código, nombre y categoría). Una por producto, incluidos los 2 adicionales |
| Logo y dos banners | `3_Archivos_Datos/marca/` | Propuesta, en la paleta de la presentación de la Fase 1 (azul `#1F3A5F`, ámbar `#D79B00`) |
| Plantilla del informe | `1_Informe/informe_fase2_PLANTILLA.docx` | 16 secciones, franja gris por rol, tablas de validación con el resultado esperado ya puesto |
| Manuales por rol | `2_Manuales_Usuario/MU-01…MU-03` | Cada paso con su título, ruta sugerida, recuadro de captura y resultado esperado |
| MU-00 | `2_Manuales_Usuario/MU-00_Manual_Instalacion_ERP_CRM.docx` | El manual de instalación de la Fase 1, copiado tal cual. Al rol 4 le toca agregar las capturas que faltaban |
| Guion de videos y demo | `4_Videos/guion_videos_fase2.md` | Tres videos y el orden de la demo del sábado |
| Presentación | `5_Presentacion/presentacion_fase2_PLANTILLA.pptx` | Diapositivas de apoyo a la demo |

### Los números están diseñados para cuadrar

- El inventario inicial de los 36 productos, valorizado al costo, suma **exactamente Q 45,000.00**, que es el rubro *Inventario inicial* del presupuesto de la Fase 1. Q 38,096 entran por importación y Q 6,904 a mano.
- Cuatro productos quedan **bajo su mínimo** a propósito (LUB-004, FRE-001, ELE-002, LLA-002) y uno en **cero** (LLA-002). Son los que disparan las alertas de stock bajo y las compras de la 12.2. Sin eso, la 12.4 no tendría alertas que mostrar.
- Quiebre de stock al terminar la carga: 1 de 36 = **2.8 %**, dentro de la meta ≤ 5 % del KPI 5. Por primera vez un KPI de la Fase 1 se mide con datos reales.
- **Plan de compras (rol 3):** tres recibidas (FRE-001; LUB-004 + LUB-007; ELE-007), una confirmada sin recibir (LLA-002) y una solicitud sin confirmar (ELE-002). Las dos últimas son las *órdenes pendientes de proveedores* de la 12.4.
- **Plan de cotizaciones (rol 2):** cuatro, con cantidades elegidas para que ninguna venta deje un producto en cero. Una facturada, una entregada, una enviada y una cancelada.
- 40 clientes: 13 repartidores, 12 particulares, 9 talleres, 6 entusiastas. La campaña del rol 4 va al segmento repartidor (13 destinatarios).

## Una sola instancia de Odoo

Odoo sigue en la laptop del rol 3. **Trabajamos todos sobre esa misma base**, no sobre copias restauradas: con cuatro copias, el sábado habría cuatro bases distintas y ninguna completa.

- El rol 3 abre un túnel de Cloudflare (`cloudflared tunnel --url http://localhost:8069`, gratis y sin cuenta) que da una URL pública temporal. Conviene agregar `proxy_mode = True` al `odoo.conf`.
- Un usuario por integrante. El historial de cada registro dice quién hizo qué, y eso es evidencia de autoría para la evaluación técnica.
- Respaldos a Drive antes de la carga, después de la carga y al cierre.
- **Plan B** si el túnel falla: relevo de respaldos en orden de dependencia (3 → 2 → 4). Es más lento y solo trabaja uno a la vez.

## Calendario

| Día | Rol 1 | Rol 2 | Rol 3 | Rol 4 |
|---|---|---|---|---|
| Lun 28 | Reparte | Lee MU-02 y el Excel | Respaldo, túnel, usuarios, categorías, etiquetas, términos de pago | Servidor de correo y plantillas |
| Mar 29 | Revisa la carga contra «Cuadre» | Carga manual | **Carga masiva** y respaldo | Plantillas; capturas del MU-00 |
| Mié 30 | Secciones 1–4 | Tarifa de talleres y 4 cotizaciones | Productos adicionales y compras 1–5 | Campaña y pipeline |
| Jue 1 | Une manuales | Informe de inventario y medición | MU-01 y video | MU-03 y video |
| Vie 2 | PDF y ZIP | MU-02 y video | Ensayo de la demo | Ensayo de la demo |
| Sáb 3 | **Entrega** | Presentación | Presentación | Presentación |

**Ruta crítica:** la carga masiva del martes. La campaña necesita clientes con segmento, el pipeline necesita talleres, las cotizaciones necesitan productos, y el informe de inventario necesita las compras. Un día de atraso en la carga es un día de atraso en todo.

## Lo que se entrega el 3

| # | Entregable | Formato | Responsable |
|---|---|---|---|
| 1 | Informe de avance | PDF | Rol 1 arma; escriben los cuatro |
| 2 | Manuales de usuario MU-00 a MU-03 | Un solo PDF | Cada rol el suyo, el rol 1 los une |
| 3 | Archivo de datos (Excel de la carga masiva) | XLSX | Rol 1 |
| 4 | Videos demostrativos | Enlaces de Drive | Roles 2, 3 y 4 |
| 5 | Todo comprimido | ZIP | Rol 1 |
| 6 | Presentación técnica | Demo en vivo | Los cuatro |

Igual que en la Fase 1, el enunciado dice *"en el formato y la estructura comprimida solicitada"* y nunca dice cuál es. Se repite la estructura de carpetas de la Fase 1, que ya se entregó así.

---

## Límites honestos (lo que no se probó)

- **Las rutas de menú de los manuales no se probaron sobre nuestra instancia.** Están escritas para Odoo 18 Community en español; los nombres exactos pueden variar. Cada manual lo advierte y pide escribir lo que diga la pantalla.
- **El Excel no se importó todavía.** Está armado según los campos de Odoo 18 (en la hoja *Diccionario*), pero la primera prueba real la hace el rol 3 el martes con el botón *Probar*. Hay tres puntos frágiles, y cada uno tiene su plan: el nombre de la ubicación (`WH/Existencias`), los nombres de los términos de pago según el idioma, y que las categorías existan **sin categoría padre**.
- **La importación de imágenes por URL** necesita que las imágenes estén en un sitio público (se propone un repo de GitHub). Si no se hace, las imágenes se suben a mano.
- **"Requisición" no existe como documento en Odoo 18 Community.** Se implementa como la alerta de reabastecimiento que genera la solicitud de cotización. Hay que explicarlo así en el informe y en la demo, como decisión de diseño. Opcional: *Acuerdos de compra* para una licitación entre dos proveedores. No verifiqué que ese módulo venga en la edición Community 18.
- **Mailpit no envía correos reales**: los captura. Es la evidencia más limpia, pero si el catedrático quiere ver un correo en un buzón de verdad, hace falta la opción B (Gmail del grupo).
- **El túnel depende de que la laptop del rol 3 esté encendida.** Es el mismo punto único de falla que ya se señaló en la Fase 1, y sigue abierto.

_Repartición Fase 2: Proyecto 1, Sistemas Organizacionales y Gerenciales 1, 2S 2026._
