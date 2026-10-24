# Paquete de trabajo · Rol 4 (Brayan)

> Preparado el **jueves 22-10-2026** y actualizado el **viernes 23-10-2026, 17:00**, cuando la instancia ya está en la nube. Para el plan de cierre, abrí `07_GUIA_CONTINUAR_23OCT.md`.
> No son archivos de entrega: son borradores y herramientas para que el trabajo real sea
> **clickear, capturar y pegar**.

## Archivos

| Archivo | Para qué |
|---|---|
| `01_CHECKLIST_CAPTURAS.md` | Las 13 figuras del MU-06 y las ~20 tomas, en orden, con lo que hay que anotar en cada una. |
| `02_MENSAJES.md` | Mensajes listos para Alberto, Jemima y Santiago, con las horas límite. |
| `03_BORRADOR_MU-06.docx` | Textos, tablas y pies del manual, listos para pasar al MU-06 de entrega. |
| `03_BORRADOR_MU-06_CON_IMAGENES.docx` | El mismo borrador con las figuras 1-6 y las dos entregas insertadas; sirve para revisar el armado. |
| `04_BORRADOR_INFORME_6.2_10.docx` | Secciones 6.2 y 10 del informe, con la justificación del BI y los pies de figura. |
| `04_BORRADOR_INFORME_6.2_10_CON_IMAGENES.docx` | Igual, con el lead insertado en 6.2. |
| `05_VERIFICAR_BI.py` | Script de solo lectura que compara Odoo contra la hoja `4_Cuadre` antes de capturar. |
| `06_GUION_VIDEO_Y_DEMO_ROL4.md` | Guion del video de 8-10 min, la demo de 4 min y el texto de las diapositivas 6, 10 y 11. |
| `07_GUIA_CONTINUAR_23OCT.md` | Plan de cierre del viernes 23: orden de ataque, corte del BI y mínimo viable. |
| `08_PENDIENTES_ROL4.md` | Estado de cada entregable y lo que falta, con horarios. |
| `09_VERIFICACION_DATOS.md` | Datos comprobados contra Odoo y lo que falta llenar en el informe. |
| `capturas_seleccionadas/` | 13 capturas depuradas y su `MANIFEST.md`; el resto de la carpeta `images/` no se usa. |

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
| Historia simulada | 45 pedidos, **Q 14,679.50 con IVA** (Q 13,106.67 sin IVA) |
| Pedidos del sitio (sin WEB-07) | 11 pedidos, **Q 4,431.50 con IVA** |
| Total confirmado del plan | 56 pedidos, **Q 19,111.00 con IVA** |
| Top 5 por unidades | LUB-001 (45), LUB-004 (21), ELE-007 (13), FRE-001 (12), ELE-003 (11) |
| Bajo el mínimo al final | CAS-005, ELE-002, FRE-004, LUB-001 |
| Productos en cero | 0 de 38 |

**Corrección importante:** en una respuesta anterior se dijo que el sitio daba Q 3,146.00. Ese
cálculo se comió las segundas líneas de los pedidos. El total correcto, con las cantidades y
precios del Excel y el 10 % a los dos talleres, es **Q 4,431.50 con IVA**. El total del plan es
**Q 19,111.00 con IVA**.

**Ojo:** estos números son del plan. La instancia real al 23-10 ya tiene **50 pedidos
(Q 16,794.50 con IVA)**: 45 de la historia y 5 de la Fase 2. El BI verá esos 5 si no los filtra.
El detalle y el plan de cierre están en `07_GUIA_CONTINUAR_23OCT.md`.

## Orden de hoy

Seguí `07_GUIA_CONTINUAR_23OCT.md`. En corto:

1. Entrar a la nube con tu usuario y correr `05_VERIFICAR_BI.py`; si dice **NO CAPTURAR**, revisar.
2. Invitar al portal a Mónica y Taller; hacer WEB-09 y WEB-11 con `01_CHECKLIST_CAPTURAS.md`.
3. Esperar WEB-12 (corte 21:00) y capturar el BI; primero los 5 reportes obligatorios.
4. Pasar 6.2/10 y el MU-06 a Santiago; grabar el video y llenar las diapositivas 6, 10 y 11.

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
