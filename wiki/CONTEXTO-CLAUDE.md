# Proyecto 1 — RutaMoto · Contexto para Claude Code

> Archivo de contexto **portable y versionado**. Viaja con el repo dentro de `wiki/` y lo importa `CLAUDE.md` con la línea `@wiki/CONTEXTO-CLAUDE.md`. Así, cualquier integrante del grupo que abra la carpeta con Claude Code arranca con el mismo contexto, en cualquier máquina y sin instalar nada.

## Quién y qué

- **Curso:** Sistemas Organizacionales y Gerenciales 1, USAC, Facultad de Ingeniería, 2S-2026, sección A. Catedrático: Ing. Fernando José Paz González. Tutor académico: Josué Daniel Caal Torres.
- **Proyecto:** *Transformación Digital en E-Commerce con ERP, CRM y BI*. Vale 60 pts y se evalúa en 3 fases de 100 puntos cada una. **No entregar una fase anula el proyecto completo.**
- **Enunciado:** `2S2026_Proyecto_1.pdf`, en la raíz del repo. Análisis por fase en [[Rúbrica y requisitos]].
- **Repo:** github.com/Santiago78op/SOG-G14-Proyecto (público).

## Grupo 14

| Rol | Integrante | Carné | Fase 2 |
|---|---|---|---|
| 1 | Santiago Julián Barrera Reyes | 201905884 | Excel de datos maestros, secciones de marco del informe (1–4 y 14–16), unir los manuales, PDF y ZIP |
| 2 | Jemima Solmaira Chavajay | 201801521 | Carga manual (12.1), cotizaciones (12.3), informe de inventario (12.4) y medición |
| 3 | Alberto Josué Hernández Armas | 201903553 | Instancia de Odoo, carga masiva (12.1) y ciclo de compras (12.2) |
| 4 | Brayan Emanuel García | 202300848 | Servidor de correo, plantillas (13), campaña (14), pipeline (15) y capturas faltantes del MU-00 |

**Si sos uno de ellos, empezá por tu fila** y por tu manual en `Entrega_Fase2_Grupo14/2_Manuales_Usuario/`. El reparto completo, con su justificación, está en [[Reparto y calendario Fase 2]].

## Fechas

| Fase | Contenido | Entrega |
|---|---|---|
| 1 | Planificación, diseño y diagnóstico | **Entregada** el 19-09-2026 |
| 2 | Carga de datos, cadena de suministros y CRM | **Sábado 03-10-2026**, con demo técnica en vivo ese mismo día |
| 3 | Sitio e-commerce, integración, portal y BI | 24-10-2026 |

## El caso, en una línea

**RutaMoto**: tienda en línea de repuestos y accesorios para motocicleta en Guatemala, Mixco y Villa Nueva. Catálogo de 36 productos en 6 categorías, 4 segmentos de cliente (repartidor, particular, taller, entusiasta) y 6 proveedores. Detalle en [[Caso RutaMoto]].

## Stack (decidido en la Fase 1, no se cambia)

Odoo 18.0 Community como ERP y CRM, con eCommerce, sobre PostgreSQL 16, en Docker. Power BI Desktop en la Fase 3. La instancia vive en la **laptop del rol 3** y los demás entran por un túnel. Ver [[Ambiente Odoo]].

## Reglas que no se negocian

- **Los números salen del Excel y de su hoja «Cuadre».** Inventario inicial = **Q 45,000** exacto (el rubro del presupuesto de la Fase 1). Nadie cambia un precio, una cantidad ni un nombre sin avisar en el grupo. Ver [[Datos maestros y cuadre]].
- **Una sola base de Odoo para los cuatro.** Nada de copias: con cuatro copias, el sábado no cuadra nada.
- **No improvisar movimientos en la base.** Las compras y las cotizaciones siguen un plan fijo ([[Plan de compras y cotizaciones]]): cada movimiento extra cambia el informe de inventario.
- **Capturas mientras se hace el paso**, no después.
- **Gris y cursiva = instrucción.** Se borra antes de entregar.
- **Lo que no se probó se dice.** Las rutas de menú de los manuales y el Excel **no se han probado todavía en Odoo**. Si la pantalla dice otra cosa, gana la pantalla: se corrige el manual y se anota en [[AVANCE]].
- **Commits sin trailer `Co-Authored-By` ni menciones a Claude.** Es regla del dueño del repo (rol 1).
- **Dos condiciones que dan cero:** el ciclo de compras (RFQ → PO → Recepción) tiene que ser demostrable en vivo, y los manuales tienen que tener captura en cada paso crítico.

## Dónde está cada cosa

| Qué | Ruta |
|---|---|
| Fase 1 entregada | `Entrega_Fase1_Grupo14/` (+ `_Referencia/concepto_empresa.md`, la premisa del caso) |
| Fase 2: guía del equipo | `Entrega_Fase2_Grupo14/LEEME_PRIMERO.docx` |
| Fase 2: informe | `Entrega_Fase2_Grupo14/1_Informe/informe_fase2_PLANTILLA.docx` (secciones 1–4 ya redactadas) |
| Fase 2: manuales | `Entrega_Fase2_Grupo14/2_Manuales_Usuario/` MU-00 a MU-03 |
| Fase 2: Excel, imágenes y marca | `Entrega_Fase2_Grupo14/3_Archivos_Datos/` |
| Fase 2: guion de videos y demo | `Entrega_Fase2_Grupo14/4_Videos/guion_videos_fase2.md` |
| Fase 2: validación contra el enunciado | `Entrega_Fase2_Grupo14/_Referencia/validacion_enunciado_fase2.md` |
| Estado y próximo paso | [[AVANCE]] |
