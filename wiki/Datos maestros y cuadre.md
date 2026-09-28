---
tags: [fase2, datos, excel, cuadre, inventario]
aliases: [Excel, Datos maestros, Cuadre, Carga]
---

# Datos maestros y cuadre

Archivo: `Entrega_Fase2_Grupo14/3_Archivos_Datos/RutaMoto_datos_maestros_Fase2.xlsx`. **No se ha importado todavía** (al 2026-09-28).

## Hojas, en orden de importación

| Hoja | Registros | Qué crea en Odoo |
|---|---|---|
| 1_Productos | 30 | productos almacenables (`is_storable`) con categoría, precio, costo e imagen por URL |
| 2_Existencias_iniciales | 30 | inventario físico: **hay que pulsar Aplicar** |
| 3_Reglas_reabastecimiento | 30 | mínimos y máximos: generan las alertas de stock bajo |
| 4_Proveedores | 5 | empresas con su plazo de pago (y su contacto, como columna informativa) |
| 5_Contactos_proveedores | 5 | personas de contacto, hijas del proveedor |
| 6_Productos_por_proveedor | 30 | qué provee cada uno, a qué costo y en cuántos días |
| 7_Clientes | 35 | clientes con su segmento como etiqueta |
| NO_IMPORTAR_carga_manual | 6 productos + 1 proveedor + 5 clientes | lo que el rol 2 carga **a mano** |

Además: `LEEME` (instrucciones), `Diccionario` (encabezado → campo técnico de Odoo) y `Cuadre`.

## Los números que tienen que dar

| Concepto | Masiva | Manual | Total |
|---|---|---|---|
| Productos del catálogo base | 30 | 6 | 36 |
| Proveedores | 5 | 1 | 6 |
| Clientes | 35 | 5 | 40 (13 repartidores, 12 particulares, 9 talleres, 6 entusiastas) |
| Inventario al costo | Q 38,096 | Q 6,904 | **Q 45,000** |

**Estado diseñado a propósito al terminar la carga:** LUB-004, FRE-001 y ELE-002 quedan bajo su mínimo, y LLA-002 en cero. Son los que disparan las alertas y las compras de la 12.2. Quiebre de stock: 1 de 36 = **2.8 %**. Al cierre de la fase, con 38 SKU y LLA-002 todavía en cero, da **2.6 %**. Ambos dentro de la meta ≤ 5 %.

## Antes de importar (lo frágil)

1. Crear las 6 categorías **sin categoría padre**: si cuelgan de «All», el nombre deja de coincidir.
2. Crear las 4 etiquetas de segmento y el término de pago «50% anticipo, 50% contra entrega».
3. Comprobar el nombre de la ubicación: el Excel dice `WH/Existencias`.
4. Comprobar cómo se llaman los términos de pago en el idioma de la base.
5. **Probar antes de Importar** siempre, y respaldar antes de la primera importación.
6. LUB-001 ya tiene 24 unidades de la prueba de la Fase 1. El inventario físico importa cantidades **contadas**, así que debería quedar en 60 y no en 84. Verificarlo.

## Imágenes

38 PNG en `imagenes_productos/`: ilustraciones propias por producto, marcadas como «Ilustración referencial», no fotos. La columna *Imagen* apunta a `raw.githubusercontent.com/Santiago78op/SOG-G14-Proyecto/main/...`, así que **el repo tiene que seguir siendo público** para que Odoo las descargue.

Relacionado: [[Plan de compras y cotizaciones]] · [[Caso RutaMoto]]
