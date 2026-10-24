# Entrega de la Fase 3

**Transformación Digital en E-Commerce con ERP, CRM y BI · Caso RutaMoto**
Sistemas Organizacionales y Gerenciales 1, Sección A · Grupo 14 · 24 de octubre de 2026

| Integrante | Carné | Responsabilidad en esta fase |
|---|---|---|
| Santiago Julián Barrera Reyes | 201905884 | Consolidación, análisis y conclusiones |
| Jemima Solmaira Chavajay | 201801521 | Pruebas de flujo completo y portal del cliente |
| Alberto Josué Hernández Armas | 201903553 | Sitio web e integración con el ERP |
| Brayan Emanuel García | 202300848 | CRM en el sitio y reportes de inteligencia de negocios |

## Qué hay en cada carpeta

| Carpeta | Contenido |
|---|---|
| `1_Informe` | Informe final, 55 páginas, en PDF y en Word. Es el documento principal: integra las 16 secciones, 39 figuras y 9 tablas |
| `2_Manuales_Usuario` | MU-04 sitio web, MU-05 compra en línea y portal, MU-06 CRM y reportes. Cada uno en Word y PDF, más los tres unidos en `Manuales_Usuario_Fase3_Grupo14.pdf` |
| `3_Archivos_Datos` | Plan de ventas de la fase en Excel y el archivo JSON que leyó el script de carga |
| `4_Videos` | Qué muestra cada video y los guiones. Los enlaces de Drive se entregan junto con este paquete |
| `5_Presentacion` | Presentación de la fase, 14 diapositivas, en PowerPoint y PDF |
| `6_Reportes_BI` | Las seis capturas de los reportes de inventario y ventas, con el filtro que genera cada una |
| `7_Prototipo` | Dónde está el prototipo funcional, cómo se levanta y el diagrama de la arquitectura |

## El prototipo funcional

El sistema no es una maqueta: está en línea y se puede abrir durante la calificación.

| Qué | Dónde |
|---|---|
| Odoo (ERP, CRM y administración) | http://54.167.23.144:8069 |
| Tienda en línea | http://54.167.23.144:8069/shop |
| Mailpit, el correo de prueba del entorno | http://54.167.23.144:8025 |
| Repositorio del proyecto | https://github.com/Santiago78op/SOG-G14-Proyecto |

Odoo 18.0 Community sobre PostgreSQL 16, en tres contenedores Docker, en un servidor de Amazon Web
Services. El detalle está en `7_Prototipo/ENTORNO_EN_LA_NUBE.md`.

## Qué se hizo en esta fase, en una página

El sitio de comercio electrónico se levantó sobre la misma base que ya operaba desde la Fase 2:
38 productos publicados en 6 categorías, registro libre de clientes, carrito, pago por
transferencia bancaria y factura automática. No hay un catálogo para la tienda y otro para el ERP.

Se cargó una historia de 45 pedidos entre el 5 y el 20 de octubre para que los reportes tuvieran
volumen, y se ejecutaron 12 pedidos reales por el sitio, WEB-01 a WEB-12, que prueban cinco flujos:
compra directa, cotización desde el CRM, taller con tarifa B2B, producto que vuelve al catálogo
tras una reposición, y carrito abandonado.

Al cierre, la instancia tiene 63 pedidos confirmados por Q 21,366.00 con impuesto incluido, 64
facturas publicadas, 51 entregas validadas y ningún producto en quiebre. Cuatro de los seis
indicadores de la Fase 1 cumplen su meta; los dos que no se pueden medir se declaran como no
medidos y se explica qué haría falta para medirlos.

## Por dónde empezar a revisar

1. `1_Informe/Informe_Fase3_Grupo14_RutaMoto.pdf`, apartado 6, que es la integración.
2. El apartado 8, con los doce casos de prueba y su número de pedido en Odoo.
3. El apartado 10, con los seis reportes, y el 11 con los indicadores contra la meta.
4. El prototipo en línea, para comprobar que lo anterior está vivo.
