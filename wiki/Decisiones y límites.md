---
tags: [decisiones, limites, riesgos]
aliases: [Decisiones, Límites honestos, Riesgos]
---

# Decisiones y límites

## Decisiones tomadas (con su porqué)

| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-09 (Fase 1) | Odoo 18 Community para ERP y CRM, en Docker, instalación local | Una sola base para las tres piezas; cero integración que construir; el enunciado admite ambiente local |
| 2026-09-28 | Una sola instancia para los cuatro, con túnel y un usuario por integrante | Con copias no cuadra nada; los usuarios individuales dan evidencia de autoría |
| 2026-09-28 | La carga se parte por datos: masiva = 5 categorías, manual = Accesorios completa | Los dos roles trabajan en paralelo y la manual no repite la masiva |
| 2026-09-28 | Inventario diseñado para cuadrar en Q 45,000 y con 4 SKU bajo el mínimo | Coherencia con el presupuesto de la Fase 1, y alertas reales para la 12.4 |
| 2026-09-28 | Requisición = alerta de reabastecimiento | No existe el documento en Odoo 18 Community |
| 2026-09-28 | Mailpit como servidor de correo recomendado | Evidencia completa sin credenciales; la decisión final es del rol 4 |
| 2026-09-28 | Correos de clientes y proveedores en `@example.com` | Dominio reservado: no le llega nada a nadie real |
| 2026-09-28 | Repo propio y público, separado de `SO2_MT` | Las imágenes se sirven por URL *raw* para la importación |
| 2026-09-28 | Una sola carpeta de Fase 1, con lo entregado | La copia de trabajo duplicaba lo entregado y confundía |
| 2026-10-05 | La columna «Ubicación» de la hoja 2 se deja en «No importar» en vez de corregir el Excel | Con una sola bodega, Odoo asigna la ubicación por omisión, que es la correcta. Cambiar el archivo repartido habría abierto la puerta a cuatro versiones distintas |
| 2026-10-05 | LUB-001 no se reimporta: se completa la ficha que ya existía | Importar la fila habría dejado dos productos con el mismo código, porque el importador no reconoce registros existentes sin identificador externo |
| 2026-10-05 | Las 32 reglas de reabastecimiento quedan con disparador **manual** | Con disparador automático el planificador nocturno genera órdenes solo y altera el estado de compras diseñado para la demostración |
| 2026-10-05 | Los productos adicionales reciben su regla de mínimo **después** de las compras | Creada antes, la regla habría propuesto 40 unidades de cada uno en lugar de las cantidades del plan |

## Límites honestos (lo que no se sabe o no se probó)

- **El Excel ya se importó** (2026-10-05) y los siete bloques cuadran contra la hoja «Cuadre».
- **Las rutas de menú de los manuales no se probaron una por una**: el MU-01 las lleva corregidas donde la pantalla real decía otra cosa.
- **No se tomó respaldo antes de la primera importación.** Quedó anotado en el MU-01; se respaldó al cerrar la carga, después de verificar los números.
- **La pantalla de alertas de reabastecimiento se capturó después del ciclo de compras**, así que ya no muestra las cuatro alertas activas: Odoo descuenta lo que viene en camino. La evidencia equivalente son las reglas con su mínimo y el documento de origen de cada orden.
- **No se verificó que *Acuerdos de compra* venga en Community 18.**
- **Las imágenes son ilustraciones, no fotos.**
- **Mailpit no envía correos reales**, solo los captura.
- **Todo depende de la laptop del rol 3** (punto único de falla, abierto desde la Fase 1).
- **Del PDF de la Fase 1 que se subió a UEDI, de los videos y del ZIP no hay copia** en el repo.
- **Los generadores** de los Word, el Excel, las imágenes y el pptx (python-docx, xlsxwriter, python-pptx y PIL) no están en el repo: quedaron en una carpeta temporal de la sesión del 2026-09-28. Si hay que regenerar algo, se edita el archivo a mano o se reescribe el generador.

Relacionado: [[AVANCE]] · [[Ambiente Odoo]]
