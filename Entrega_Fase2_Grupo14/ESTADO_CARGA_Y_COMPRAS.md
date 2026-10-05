# Estado de la carga masiva y del ciclo de compras

**Responsable: Alberto Josué Hernández Armas, carné 201903553 · 5 de octubre de 2026**

Puntos 12.1 (parte masiva) y 12.2 del enunciado. Esta nota es para que el resto del equipo
sepa exactamente qué hay en la instancia antes de seguir con lo suyo.

> Las credenciales de la instancia y la dirección pública **no van en el repositorio**, porque
> es público. Se pasan por el chat del grupo.

---

## 1. Lo que quedó cargado y verificado

| Comprobación | Esperado (hoja «Cuadre») | En Odoo |
|---|---|---|
| Productos de la carga masiva | 30 | 30 |
| Inventario al costo de lo importado | Q 38,096.00 | Q 38,096.00 |
| Proveedores y sus contactos | 5 y 5 | 5 y 5 |
| Líneas de lista de precios de proveedor | 30 | 30 |
| Reglas de reabastecimiento | 30 | 30 |
| Clientes por segmento | 12 · 11 · 7 · 5 | 12 · 11 · 7 · 5 |
| Talleres marcados como empresa | 7 | 7 |
| Productos bajo el mínimo al terminar la carga | 4 | LUB-004, FRE-001, ELE-002 y LLA-002 |

Productos adicionales creados desde el sistema: **LUB-007**, lubricante de cadena en aerosol
400 ml (Q 65 / Q 38), y **ELE-007**, bombillo LED de stop 1157 (Q 40 / Q 22).

| Compra | Proveedor | Productos | Número | Estado |
|---|---|---|---|---|
| 1 | Frenos y Transmisiones de Guatemala | FRE-001 × 44 | P00001 | Recibida en RMT/IN/00001, Q 2,420 |
| 2 | Importadora Centroamericana de Repuestos | LUB-004 × 72 · LUB-007 × 24 | P00002 | Recibida en RMT/IN/00002, Q 2,280 |
| 3 | Grupo Eléctrico Moto GT | ELE-007 × 30 | P00003 | Recibida en RMT/IN/00003, Q 660 |
| 4 | Distribuidora Llantera del Sur | LLA-002 × 16 | P00004 | Confirmada, sin recibir, Q 4,400 |
| 5 | Grupo Eléctrico Moto GT | ELE-002 × 88 | P00005 | Solicitud enviada, sin confirmar, Q 1,584 |

Inventario al costo después de las tres recepciones: **Q 43,456.00**.

---

## 2. Cuatro reglas para no romper los números

1. **No cerrar las compras 4 y 5.** Son las órdenes pendientes de proveedores que pide el
   informe de inventario de la 12.4. Si se cierran, ese reporte queda vacío.
2. **No agregar compras ni ventas fuera del plan.** Cada movimiento cambia el inventario
   valorizado del informe, que hoy cuadra al centavo contra el archivo de datos maestros.
3. **El Excel de datos maestros no se modificó.** Su columna «Ubicación» dice `WH/Existencias`
   y la ubicación real de la instancia es `RMT/Existencias`, porque la bodega se llama «Bodega
   Central RutaMoto» y su código corto es RMT desde la Fase 1. Se resolvió dejando esa columna
   en «No importar»: con una sola bodega, Odoo asigna la ubicación por omisión, que es la
   correcta. Está documentado en el MU-01 y en la sección 6.2 del informe.
4. **Las 32 reglas de reabastecimiento quedaron con disparador manual**, a propósito, para que
   el planificador nocturno no genere órdenes por su cuenta y altere el estado de las compras
   antes de la demostración.

---

## 3. Qué se agregó al repositorio

| Ruta | Qué es |
|---|---|
| `2_Manuales_Usuario/MU-01_Carga_masiva_y_compras.docx` y `.pdf` | Manual terminado: 9 capítulos, 30 figuras, tablas de validación llenas |
| `2_Manuales_Usuario/capturas_MU-01/` | Las 28 capturas originales |
| `1_Informe/informe_fase2_secciones_Alberto_Hernandez.docx` | Secciones 5, 6.2, 6.4 y 7 con sus 8 tablas llenas, en el formato de la plantilla, para pegar en el informe unificado |
| `3_Archivos_Datos/RutaMoto_demo_en_vivo_Fase2.xlsx` | Producto que no existe en la base (LUB-008), para la demostración en vivo del sábado sin tocar ningún número del informe |
| `4_Videos/guion_video_carga_y_compras.md` | Guion de nueve minutos del video de carga y compras |
| `5_Presentacion/manual_demo_en_vivo_fase2.md` | Paso a paso de los dos bloques de la demostración del sábado |
| `_Referencia/scripts_instancia/` | Scripts de PowerShell: capturas, conducción de pantalla del video y túnel público |

---

## 4. Lo que falta, y de quién es

| Pendiente | Responsable |
|---|---|
| Carga manual: categoría Accesorios y equipaje (6 productos), proveedor AccesoRuta y 5 clientes. Con eso el catálogo llega a 36 y el inventario a Q 45,000 | Jemima |
| Tarifa Talleres B2B, las 4 cotizaciones y el informe de inventario | Jemima |
| Servidor de correo, 2 plantillas, campaña al segmento Repartidor y pipeline con 5 oportunidades | Brayan |
| Unir informe y manuales, PDF, ZIP y subir la entrega | Santiago |
| Video de carga y compras | Alberto |

La hoja `NO_IMPORTAR_carga_manual` del Excel trae exactamente lo que va a mano, con sus
precios, costos, existencias, mínimos y máximos. Esos números no se cambian.

---

## 5. Cosas que conviene saber antes de la defensa

- **No se tomó respaldo antes de la primera importación.** No hubo que restaurar nada porque
  la validación previa de cada hoja pasó limpia, pero queda anotado como problema encontrado
  en el capítulo 6.1 del MU-01.
- **La pantalla de alertas de reabastecimiento se capturó después del ciclo de compras**, así
  que ya no muestra las cuatro alertas activas: Odoo descuenta de la cantidad a ordenar lo que
  viene en camino, incluso lo que está en una solicitud sin confirmar. La evidencia equivalente
  son las reglas con su mínimo y el documento de origen de cada orden.
- **En la base siguen los documentos de la demostración de la Fase 1**: los pedidos S00001 a
  S00003 con sus entregas y facturas, a cuatro clientes de prueba archivados. No afectan los
  números de la carga, pero por eso las cotizaciones de esta fase empiezan a numerar en S00004.
