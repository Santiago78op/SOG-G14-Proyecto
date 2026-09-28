# Validación: la Fase 2 contra el enunciado

Revisión del 2026-09-28. Cada requisito del enunciado (`2S2026_Proyecto_1.pdf`) que aplica a la Fase 2, dónde quedó cubierto en esta carpeta y en qué estado está.

- **Preparado:** el material está hecho y listo para usarse.
- **Pendiente:** depende de que alguien lo ejecute en Odoo. Nada de esto se puede adelantar sin el sistema.

## 1. Rúbrica de la Fase 2 (sección 8.2.2)

| Criterio | Pts | Dónde se cubre | Estado |
|---|---|---|---|
| Documentación técnica: manuales de instalación y configuración con capturas | 10 | `2_Manuales_Usuario/` MU-00 (instalación, de la Fase 1) y MU-01 a MU-03 (configuración) | Preparado · capturas pendientes |
| Cumplimiento de entregables: estructura, formato y empaquetado | 10 | Misma estructura de carpetas que la Fase 1 + LEEME con lista de comprobación | Preparado · ZIP final pendiente (rol 1) |
| Presentación técnica: demostración de la carga y los procesos | 20 | `5_Presentacion/` + orden de la demo en `4_Videos/guion_videos_fase2.md` | Preparado · ensayo pendiente |
| Carga de productos, clientes y proveedores, manual y masiva | 30 | Excel (hojas 1 a 7 + carga manual), MU-01 caps. 1–6, MU-02 cap. 1, informe sección 6 | Preparado · carga pendiente (roles 2 y 3) |
| Procesos de compras y cotizaciones | 15 | MU-01 caps. 7–9, MU-02 caps. 2–3, informe secciones 7 y 8 | Preparado · ejecución pendiente |
| Envío de correos desde el CRM | 10 | MU-03 caps. 1–3, informe secciones 10 y 11, logo y banners en `3_Archivos_Datos/marca` | Preparado · ejecución pendiente (rol 4) |
| Medición de logros | 5 | Informe sección 13 (6 indicadores + validación de punta a punta), MU-02 cap. 5 | Preparado · cálculo pendiente (rol 2) |

## 2. Metodología de la Fase 2 (sección 9)

| Punto del enunciado | Dónde | Estado |
|---|---|---|
| 1. Carga de datos maestros: productos, clientes y proveedores | Excel + MU-01 + MU-02 | Preparado |
| 2. Cadena de suministros y procesos transaccionales de ventas y cotizaciones | MU-01 (compras) y MU-02 (cotización → pedido → entrega → factura) | Preparado |
| 3. Módulo de compras completo, de la requisición a la recepción | MU-01 caps. 8–9. La requisición es la alerta de reabastecimiento; ver límite 1 | Preparado |
| 4. Plantillas de correo, pipeline de ventas y pruebas de envío de campañas segmentadas | MU-03 caps. 2–4 | Preparado |

## 3. Punto 12: cadena de suministros

| Requisito | Dónde | Estado |
|---|---|---|
| **12.1** Excel de **productos**: código, nombre, categoría, precio, costo, stock inicial, imagen | Hoja `1_Productos` (con stock inicial informativo e imagen por URL) + hoja `2_Existencias_iniciales` | Preparado |
| Excel de **clientes**: nombre, correo, teléfono, dirección, segmento | Hoja `7_Clientes` (el segmento va como etiqueta) | Preparado |
| Excel de **proveedores**: nombre, contacto, productos que proveen, condiciones de pago | Hoja `4_Proveedores` (con contacto y productos) + hojas 5 y 6 para importarlos | Preparado |
| Importar el archivo al ERP | MU-01 caps. 2–6 | **Pendiente (rol 3)** |
| Realizar también la carga manual | Hoja `NO_IMPORTAR_carga_manual` + MU-02 cap. 1 | **Pendiente (rol 2)** |
| Manual de usuario paso a paso con capturas | MU-01 y MU-02 | Plantilla lista |
| **12.2** Crear productos adicionales desde el sistema | LUB-007 y ELE-007 (MU-01 cap. 7) | Preparado |
| Registrar órdenes de compra a proveedores | 5 compras planificadas (informe, página «Premisa») | Preparado |
| Verificar el movimiento en inventario | MU-01 cap. 9, paso 3 + tabla del informe 7.3 | Preparado |
| **12.3** Flujo de cotización para clientes específicos | Tarifa Talleres B2B (MU-02 cap. 2) | Preparado |
| Cotizaciones personalizadas | 4 cotizaciones planificadas | Preparado |
| Convertir la cotización en pedido o venta | MU-02 cap. 3, pasos 3 a 5 | Preparado |
| **12.4** Reporte de existencias actuales | MU-02 cap. 4, paso 1 | Preparado |
| Reporte de órdenes pendientes de proveedores | Compras 4 y 5, dejadas abiertas a propósito | Preparado |
| Reporte de alertas de stock bajo | Reglas de reabastecimiento (hoja 3); 4 productos bajo el mínimo por diseño | Preparado |

## 4. Puntos 13, 14 y 15: CRM

| Requisito | Dónde | Estado |
|---|---|---|
| **13** Plantilla 1: promoción especial | MU-03 cap. 2, paso 3 + `banner_promocion.png` | Preparado |
| Plantilla 2: fidelización o recordatorio | MU-03 cap. 2, paso 5 + `banner_fidelizacion.png` | Preparado |
| Cada plantilla con logo y nombre, imagen o banner, y texto con llamado a la acción | `marca/logo_rutamoto.png` + tabla de validación del MU-03 | Preparado |
| Manual de cómo hacer una plantilla | MU-03 cap. 2 | Plantilla lista |
| **14** Seleccionar al menos un segmento | Repartidor, 13 destinatarios (MU-03 cap. 3) | Preparado |
| Asociar una plantilla a la campaña | MU-03 cap. 3, paso 1 | Preparado |
| Manual con capturas | MU-03 cap. 3 | Plantilla lista |
| **15** Al menos 4 etapas del proceso comercial | 5 etapas: Nuevo lead, Contactado, Cotización enviada, Negociación, Ganado | Preparado |
| Mínimo 5 clientes ficticios en distintas etapas | 5 oportunidades sugeridas (MU-03 cap. 4) | Preparado |
| Mover al menos un cliente por todas las etapas, con trazabilidad | MU-03 cap. 4, pasos 3 y 4 (historial de la oportunidad) | Preparado |
| Manual con capturas | MU-03 cap. 4 | Plantilla lista |

## 5. Entregables de la Fase 2 (sección 4.4)

| Entregable del enunciado | Dónde | Estado |
|---|---|---|
| Informe ejecutivo/técnico (PDF) | `1_Informe/informe_fase2_PLANTILLA.docx`, con las secciones 1 a 4 ya redactadas | Parcial: faltan las secciones de los roles 2, 3 y 4 |
| Manuales de usuario y técnico | `2_Manuales_Usuario/` | Plantillas listas |
| Video demostrativo en Google Drive | Guion de 3 videos en `4_Videos/` | **Pendiente: grabar** |
| Archivos de datos: el Excel de la carga masiva | `3_Archivos_Datos/RutaMoto_datos_maestros_Fase2.xlsx` | **Hecho** |
| Presentación ante el catedrático | `5_Presentacion/` + guion de la demo | Preparado |
| Mapa de flujo de procesos | Solo se entrega en la Fase 1 | No aplica |

## 6. Requisitos para optar a la calificación (sección 8.1)

| Requisito | Situación en la Fase 2 |
|---|---|
| ERP y CRM de la lista permitida | Odoo y Odoo CRM, desde la Fase 1 |
| **Módulo avanzado: ciclo de compras RFQ → PO → Recepción demostrable** | Cubierto por el MU-01. Si no se demuestra en vivo, la nota es **cero** |
| **Manuales con capturas completos** | Hay que llenar todos los recuadros. Si falta uno, la nota es **cero** |
| Entrega con todos los archivos de la fase, comprimidos | Lista de comprobación en el LEEME |
| Evaluación técnica: presentarse y demostrar autoría | Usuarios individuales en Odoo: el historial muestra quién hizo cada cosa |
| Herramienta de BI implementada | Es de la **Fase 3**. No se pide en esta, pero el requisito es general: conviene decirlo si el catedrático pregunta |
| Integración e-commerce y flujo de compra en el sitio | Es de la **Fase 3** |

## Lo que se corrigió en esta revisión

- **Imágenes de producto.** Todas repetían la rueda del logo. Ahora cada una tiene su propia ilustración (llanta, casco, botella de aceite, bujía, disco, etc.).
- **Hoja de proveedores.** No mostraba el contacto que pide el enunciado; se agregó la columna «Contacto».
- **Fase 1 duplicada.** Había dos carpetas: la de trabajo y la entregada, descargada de Drive. Se dejó una sola, `Entrega_Fase1_Grupo14/`, con lo entregado y su referencia. Las plantillas de trabajo se quitaron; siguen en el historial de git (commit `ca8ed69`).

## Límites honestos

1. **La «requisición»** no existe como documento en Odoo 18 Community. Se implementa como la alerta de reabastecimiento que genera la solicitud de cotización. Es una interpretación que hay que defender en la demo, no algo que el enunciado diga así.
2. **Nada se probó todavía en Odoo:** ni la importación del Excel ni las rutas de menú de los manuales.
3. **Las imágenes son ilustraciones referenciales, no fotos.** La fotografía de producto figura en el presupuesto de la empresa, pero no se hizo.
4. **La Fase 1 en el repo son los archivos de trabajo que se bajaron de Drive.** No incluyen el PDF que se subió a UEDI, ni los videos, ni el ZIP de entrega, porque nunca estuvieron en esta máquina.
