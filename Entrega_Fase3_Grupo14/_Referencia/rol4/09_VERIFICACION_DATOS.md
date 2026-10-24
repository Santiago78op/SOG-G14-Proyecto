# Verificación de datos del informe · 23-10, 23:00

> Lo que está comprobado contra Odoo y lo que todavía falta llenar. Si el BI se capturó
> después de las 19:29, los valores de stock y top 5 pueden cambiar: se actualizan con la
> captura final.

## Comprobado

| Dato | Valor | Fuente |
|---|---|---|
| Historia | 45 pedidos · **Q 14,679.50 con IVA** · Q 13,106.67 sin IVA | Script `05_VERIFICAR_BI.py` |
| Margen de la historia | **Q 3,781.67** | Script / `ESTADO_SITIO_Y_HISTORIA.md` |
| Pedido WEB-09 | **S00055** · Q 860.00 con IVA | Script |
| Factura WEB-09 | **INV/2026/00054** · pagada | Script |
| Entrega WEB-09 | **RMT/OUT/00053** · hecha | Script |
| Pedido WEB-11 | **S00056** · Q 364.50 con IVA | Script |
| Factura WEB-11 | **INV/2026/00056** · pagada | Script |
| Entrega WEB-11 | **RMT/OUT/00054** · hecha | Script |
| Productos publicados | 38 · 0 en cero | `ESTADO_SITIO_Y_HISTORIA.md` |
| Categorías | 6 | `ESTADO_SITIO_Y_HISTORIA.md` |
| Stock bajo al corte | **CAS-005 (1/2)** y **ELE-002 (12/30)** | Script final |
| Top 5 al corte | LUB-001 52 · LUB-004 21 · ELE-007 13 · FRE-001 12 · ELE-003 11 (sin Delivery_007) | Script final |
| Equipo del sitio | Website · Q 4,571.50 con IVA · Q 4,081.69 sin IVA · margen Q 1,217.69 | Script final |
| Origen del lead | **vacío**; no se inventa “Sitio web” | CRM |
| Pedidos de la Fase 2 en el período | S00004 y S00005 (Q 1,710.00) | Script |
| Pedidos del sitio | 13 confirmados (11 directos + 2 CRM) · Q 4,571.50 con IVA | Script final |
| Total historia + sitio | 58 pedidos · Q 19,251.00 con IVA | 14,679.50 + 4,571.50 |

## Falta llenar en el informe

| Dónde | Qué falta |
|---|---|
| 10.2 | Insertar la captura de barras (figura 2) |
| 10.3 | Insertar la captura de pastel (figura 3) |
| 10.4 | Insertar la captura de stock bajo (figura 4) |
| 10.5 | Insertar las capturas de líneas (figura 5); los números ya están (58 / Q 19,251.00) |
| 10.6 | Insertar el pivote top 5 (figura 6); los números ya están (52/21/13/12/11, sin Delivery_007) |
| 10.7 | Insertar el gráfico de margen (figura 7); los totales/margen ya están en el texto |
| 10.8 | Insertar el tablero (figura 8) o declarar que no se incluyó |
| Tabla de validación | Solo “Tablero” queda pendiente; Evolución y Canales ya están |

## Ojo con los números

- **Q 14,679.50** es con IVA; el informe de ventas de Odoo muestra **Q 13,106.67 sin IVA** por omisión. Decir cuál se usa.
- **Q 19,111.00** es el total del plan (historia + 11 pedidos del sitio). Si el BI incluye los pedidos de la Fase 2 o faltan pedidos del sitio, el total real es otro. No forzar el número.
- **Top 5**: el plan era 45/21/13/12/11; al corte es 52/21/13/12/11. Excluir `Delivery_007` (flete).
- **Stock bajo**: el plan era 4; al corte son 2 (CAS-005 y ELE-002). Explicar la diferencia por los mínimos y las entradas.
- **Pedidos del sitio**: hay 13 confirmados (11 directos + 2 CRM), no 11; la diferencia son 2 pedidos extra y Q 140 de fletes/ajustes.
- **Origen**: el lead no tiene “Sitio web”; se documenta como límite.

## Archivos

- Informe formateado: `1_Informe/informe_fase3_secciones_Brayan_FORMATO.docx`.
- Capturas: `_Referencia/rol4/capturas_seleccionadas/`.
- Manual visual: `_Referencia/rol4/03_BORRADOR_MU-06_CON_IMAGENES.docx`.
