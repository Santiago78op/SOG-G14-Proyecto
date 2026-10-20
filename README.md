# SOG-G14-Proyecto

Proyecto 1 de **Sistemas Organizacionales y Gerenciales 1** (USAC, 2S 2026, sección A): *Transformación Digital en E-Commerce con ERP, CRM y BI*. Caso **RutaMoto**, una tienda en línea de repuestos y accesorios para motocicleta, montada sobre Odoo 18 Community.

## 👉 Fase 3: empezá acá

**Entrega y presentación final: sábado 24 de octubre de 2026.** Mismos roles que en la Fase 2. Buscá tu fila:

| Quién | Qué hacés | Abrí esto | Cuándo |
|---|---|---|---|
| **Alberto (rol 3)** | Instalás y configurás el sitio (Comercio electrónico), publicás los 38 productos, recibís P00004 y cargás la historia de ventas con el script, **primero con `--probar`**. Respaldos: antes de la historia y al cierre, cuando Jemima avisa | `Entrega_Fase3_Grupo14/2_Manuales_Usuario/MU-04_...` y [`cargar_historial_ventas.py`](Entrega_Fase3_Grupo14/_Referencia/scripts_instancia/cargar_historial_ventas.py) (instrucciones arriba del archivo) | **Miércoles 21: ruta crítica.** Nadie puede comprar hasta que el sitio esté publicado |
| **Jemima (rol 2)** | Hacés en el sitio los pedidos WEB-01 a 08, WEB-10 y WEB-12, validás sus entregas y probás el portal del cliente. **Avisás en el grupo al terminar WEB-12** | `MU-05_...` y la hoja `2_Pedidos_sitio` de [`RutaMoto_ventas_Fase3.xlsx`](Entrega_Fase3_Grupo14/3_Archivos_Datos/RutaMoto_ventas_Fase3.xlsx) | Jueves 22 y viernes 23, cuando Alberto avise que el sitio está publicado |
| **Brayan (rol 4)** | Formulario del sitio → lead → cotización → portal (WEB-09 y WEB-11), **validás esas dos entregas**, y los reportes BI con los informes de Odoo | `MU-06_...` y la hoja `4_Cuadre` del Excel de ventas (lo que tiene que dar el BI) | CRM el jueves 22; capturas del BI después del aviso de WEB-12 |
| **Santiago (rol 1)** | Informe, KPIs, objetivos SMART, escalabilidad, conclusiones, presentación, PDF y ZIP | `1_Informe/informe_fase3_PLANTILLA.docx` | Viernes 23 |

Detalle completo (rúbrica, reglas y lista de configuración del sitio): `Entrega_Fase3_Grupo14/LEEME_PRIMERO_Fase3.docx`. Para leerlo hay que **descargarlo**, porque GitHub no muestra los Word. Las secciones del informe que te tocan llevan una franja gris con tu rol. Lo gris en cursiva es instrucción y se borra antes de entregar. El guion de tu video está en [`4_Videos/guion_videos_fase3.md`](Entrega_Fase3_Grupo14/4_Videos/guion_videos_fase3.md).

**Tres reglas:**
1. Solo se compran por el sitio los pedidos del plan: cada compra de más cambia los números del BI.
2. Capturas mientras hacés el paso, no después.
3. El repo es público: ninguna contraseña en documentos ni commits.

Las rutas de menú de los manuales **no están probadas**: si tu pantalla dice otra cosa, gana la pantalla y lo corregís en el manual.

## Grupo 14

| Rol | Integrante |
|---|---|
| 1. Consolidación, análisis y conclusiones | Santiago Julián Barrera Reyes |
| 2. Pruebas de flujo y portal del cliente | Jemima Solmaira Chavajay |
| 3. Sitio web e integración (ERP) | Alberto Josué Hernández Armas |
| 4. CRM en el sitio y reportes BI | Brayan Emanuel García |

## Contenido

| Carpeta | Qué es |
|---|---|
| `2S2026_Proyecto_1.pdf` | Enunciado |
| `Entrega_Fase1_Grupo14/` | **Fase 1 entregada** el 19-09-2026: informe, manual de instalación, mapa de procesos, guion de videos y presentación, más la referencia del caso (`_Referencia/concepto_empresa.md`) |
| `Entrega_Fase2_Grupo14/` | **Fase 2 entregada** el 05-10-2026: informe, manuales MU-00 a MU-03, datos maestros en Excel, imágenes, videos y presentación. Lo entregado tal cual está en la rama `entrega/fase2` |
| `Entrega_Fase3_Grupo14/` | **Fase 3, en curso**: guía del equipo, plantilla del informe, manuales MU-04 a MU-06, plan de ventas, script de la historia y guion de videos |
| `wiki/` | El cerebro del proyecto (Obsidian): estado en `wiki/AVANCE.md`, decisiones en `wiki/Decisiones y límites.md` |

Si abrís el repo con Claude Code, `CLAUDE.md` le da todo el contexto del proyecto.

## Nota sobre las imágenes

La columna *Imagen* de `Entrega_Fase2_Grupo14/3_Archivos_Datos/RutaMoto_datos_maestros_Fase2.xlsx` apunta a los archivos de `imagenes_productos/` de este repositorio. Odoo los descarga al importar mientras el repositorio siga siendo público.

Los clientes, proveedores, correos (`@example.com`) y teléfonos del caso son ficticios.
