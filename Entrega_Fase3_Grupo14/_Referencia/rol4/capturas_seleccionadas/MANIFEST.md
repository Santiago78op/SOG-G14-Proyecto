# Capturas seleccionadas · Rol 4

> Depuradas de `2_Manuales_Usuario/images/` el **23-10, 19:35**. Son las que sirven para el
> MU-06, las secciones 6.2/10 y las diapositivas. Las demás son intentos, filtros, la orden vieja
> **S00052**, o la terminal: no se usan.

## Mapa

| Archivo | Qué muestra | Manual | Informe | Diapositiva |
|---|---|---|---|---|
| `01_formulario_monica.png` | Formulario de Contáctanos lleno con Mónica, asunto y pregunta | Figura 1 | — | 6 |
| `02_lead_monica.png` | Lead/oportunidad de Mónica con correo, teléfono y mensaje; etapa Nuevo lead. **El origen está vacío** | Figura 2 | 6.2 | 6 |
| `03_cotizacion_monica.png` | Pedido/cotización **S00055**, líneas CAS-005 y CAS-006, total **Q 860.00** | Figura 3 | 6.2 (tabla) | 6 |
| `04_correo_monica.png` | Mailpit con el correo **Cotización S00055** y el enlace al portal | Figura 4 | — | — |
| `05_portal_monica.png` | Portal del cliente con la cotización S00055 y el botón Aceptar y firmar | Figura 5 | — | 6 |
| `05b_firma_monica.png` | Firma de Mónica en el portal | Figura 5 | — | — |
| `06_factura_monica.png` | Factura **INV/2026/00054** pagada, Q 860.00 | Figura 6 | 6.2 (tabla) | — |
| `06b_pago_monica.png` | Registrar pago de la factura de Mónica (transferencia) | Figura 6 (apoyo) | — | — |
| `06c_entrega_monica.png` | Entrega **RMT/OUT/00053** de Mónica en estado Hecho | Figura 6 | 6.2 | — |
| `web11_entrega.png` | Entrega **RMT/OUT/00054** del Taller en estado Hecho | — | 6.2 (apoyo) | — |
| `web11_formulario.png` | Formulario de Contáctanos lleno con el Taller | — | 6.2 (apoyo) | — |
| `web11_pedido.png` | Pedido **S00056** del Taller, LUB-004 ×6 y LUB-007 ×3, **Q 364.50** | — | 6.2 (tabla) | — |
| `web11_portal.png` | Portal del Taller con la cotización S00056, Q 364.50 | — | — | — |
| `web11_portal_confirmado.png` | Portal con el pedido S00056 confirmado y la firma del Taller | — | — | — |
| `web11_factura.png` | Factura **INV/2026/00056** del Taller, Q 364.50, con el pago manual | — | 6.2 (tabla) | — |

## Lo que falta capturar

| Falta | Dónde | Para qué |
|---|---|---|
| **BI · inventario** (barras, pastel, stock bajo) | `Inventario › Informes › Ubicaciones` (barras/pastel) y `Operaciones › Reabastecimiento` (stock bajo) | Figuras 7-9 del manual y 10.2-10.4 del informe |
| **BI · ventas** (líneas día/semana/mes, top 5) | `Ventas › Informes` | Figuras 10-11 del manual y 10.5-10.6 del informe |
| **BI · margen por canal** (extra) | `Ventas › Informes` | Figura 12 |
| **BI · tablero** (extra) | `Dashboards` | Figura 13 |

## Reglas

- No uses **S00052**: es el intento viejo de Mónica, sin factura; se canceló. El pedido bueno es
  **S00055**.
- El **origen** del lead quedó vacío. No inventes “Sitio web”: en el manual y en 6.2 se dice que
  el lead llegó con los datos del formulario y que el campo Origen no quedó registrado.
- Las capturas del BI se toman **después** de WEB-12 o del corte de las 21:00. Si se toman antes,
  el stock y el top 5 cambian.
- La captura del portal de Mónica muestra “Su contacto: Brayan” porque se abrió con la sesión del
  asesor. La firma es de Mónica; si se puede, recapturar en incógnito como Mónica. Si no, usarla
  y no resaltar esa línea.
- Para WEB-11 no se repiten las 13 figuras: el manual usa las de Mónica. Las capturas del Taller
  son respaldo y datos para la tabla.
