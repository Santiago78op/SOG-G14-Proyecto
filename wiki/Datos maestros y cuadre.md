---
tags: [fase2, datos, excel, cuadre, inventario]
aliases: [Excel, Datos maestros, Cuadre, Carga]
---

# Datos maestros y cuadre

Archivo: `Entrega_Fase2_Grupo14/3_Archivos_Datos/RutaMoto_datos_maestros_Fase2.xlsx`. **Importado el 2026-10-05.** Los siete bloques entraron sin errores y los conteos cuadran contra la hoja «Cuadre».

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

## Lo frágil, ya resuelto (2026-10-05)

1. Las 6 categorías se crearon **sin categoría padre**. Confirmado: si cuelgan de «All» el nombre completo deja de coincidir.
2. Las 4 etiquetas y el término «50% anticipo, 50% contra entrega» existen. Ese término lleva **dos líneas porcentuales de 50**: Odoo 18 ya no acepta el tipo de línea «saldo».
3. **La ubicación del Excel no coincide.** El archivo dice `WH/Existencias` y la instancia tiene `RMT/Existencias`. La columna se dejó en **«No importar»** y Odoo asigna la ubicación por omisión del almacén, que es la correcta. El archivo no se modificó.
4. Los términos de pago venían en inglés y se renombraron a los nombres del archivo.
5. **Probar antes de Importar**: así apareció el problema de la ubicación, sin escribir nada en la base.
6. LUB-001 ya existía desde la Fase 1. Se importaron 29 filas y se completó la ficha existente; su cantidad contada de 60 se aplicó sobre lo que había y quedó en **60**.
7. Después de importar la hoja 2 hay que pulsar **Aplicar**, o las cantidades quedan contadas y el inventario sigue en cero.

## Imágenes

38 PNG en `imagenes_productos/`: ilustraciones propias por producto, marcadas como «Ilustración referencial», no fotos. La columna *Imagen* apunta a `raw.githubusercontent.com/Santiago78op/SOG-G14-Proyecto/main/...`, así que **el repo tiene que seguir siendo público** para que Odoo las descargue.

Relacionado: [[Plan de compras y cotizaciones]] · [[Caso RutaMoto]]
