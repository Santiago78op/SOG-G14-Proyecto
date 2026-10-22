# Paquete de trabajo · Rol 4 (Brayan)

> Preparado el **jueves 22-10-2026, 11:20** para que el rol 4 no arranque desde cero.
> No son archivos de entrega: son borradores y herramientas para que el trabajo real sea
> **clickear, capturar y pegar**.

## Archivos

| Archivo | Para qué |
|---|---|
| `01_CHECKLIST_CAPTURAS.md` | Las 13 figuras del MU-06 y las ~20 tomas, en orden, con lo que hay que anotar en cada una. |
| `02_MENSAJES.md` | Mensajes listos para Alberto, Jemima y Santiago, con las horas límite. |
| `03_BORRADOR_MU-06.docx` | Textos, tablas y pies del manual, listos para pasar al MU-06 de entrega. |
| `04_BORRADOR_INFORME_6.2_10.docx` | Secciones 6.2 y 10 del informe, con la justificación del BI y los pies de figura. |
| `05_VERIFICAR_BI.py` | Script de solo lectura que compara Odoo contra la hoja `4_Cuadre` antes de capturar. |
| `06_GUION_VIDEO_Y_DEMO_ROL4.md` | Guion del video de 8-10 min, la demo de 4 min y el texto de las diapositivas 6, 10 y 11. |

## Qué es obligatorio y qué es extra

El enunciado (punto 17) pide **cinco reportes**: barras por producto, pastel por categoría, tabla
de stock bajo, líneas por día/semana/mes y tabla del top 5. Eso es lo que se evalúa en los 10
puntos del BI. El **margen por canal** y el **tablero** son extras del plan del grupo: suman para
la demostración, pero no son requisito. Si el tiempo aprieta, se hacen primero los cinco y después
los dos extras.

Del punto 16 (sitio), lo tuyo es solo el **flujo B**: formulario → lead → cotización → portal
(WEB-09 y WEB-11). El catálogo, el carrito, el registro y el manual del sitio son de Alberto y
Jemima. Del punto 19 (conclusiones), lo tuyo son **los números y las capturas**; el texto lo
escribe Santiago.

## Los números del plan (para no improvisar)

| Dato | Valor |
|---|---|
| Historia simulada | 45 pedidos, **Q 14,679.50** |
| Pedidos del sitio (sin WEB-07) | 11 pedidos, **Q 4,431.50** |
| Total confirmado del plan | 56 pedidos, **Q 19,111.00** |
| Top 5 por unidades | LUB-001 (45), LUB-004 (21), ELE-007 (13), FRE-001 (12), ELE-003 (11) |
| Bajo el mínimo al final | CAS-005, ELE-002, FRE-004, LUB-001 |
| Productos en cero | 0 de 38 |

**Corrección importante:** en una respuesta anterior se dijo que el sitio daba Q 3,146.00. Ese
cálculo se comió las segundas líneas de los pedidos. El total correcto, con las cantidades y
precios del Excel y el 10 % a los dos talleres, es **Q 4,431.50**. El total del plan es
**Q 19,111.00**.

## Orden de hoy

1. Mandar el mensaje a Alberto (está en `02_MENSAJES.md`). Sin URL, sitio e historia no hay capturas.
2. Correr `05_VERIFICAR_BI.py` en cuanto haya URL. Si dice **NO CAPTURAR**, no se captura: se corrige.
3. Hacer WEB-09 y WEB-11 con las capturas de `01_CHECKLIST_CAPTURAS.md`.
4. Mañana, después del aviso de WEB-12, correr el script otra vez y hacer las capturas del BI.

## Regla de trabajo con Santiago

El informe y el MU-06 salen de `_Referencia/generadores/generar_documentos.py`. Si se edita el
`.docx` de entrega a mano y después alguien corre el generador, se pierde el texto. Por eso:

- Los borradores de este paquete van **aparte**; no se toca el `.docx` de entrega hasta que
  Santiago confirme que ya no va a regenerar.
- Si Santiago prefiere, el texto se pasa al generador en una rama y él hace el merge.
- El MU-06 se puede llenar a mano; en ese caso, **no volver a correr el generador** sobre ese archivo.

## Horas límite

| Qué | Quién | Cuándo |
|---|---|---|
| URL del túnel + sitio + historia | Alberto | **Hoy 18:00** |
| WEB-12 + entregas validadas | Jemima | **Viernes 12:00** |
| Secciones 6.2 y 10 + capturas | Brayan | **Viernes 18:00** |
| Ensayo de los 4 minutos | Brayan | **Sábado 09:00** |

Si una hora límite no se cumple, se avisa a Santiago ese mismo día; no se espera al sábado.
