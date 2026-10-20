"""Genera los Word de la Fase 3 (RutaMoto, Grupo 14) a partir de la carátula del informe de la Fase 2.

  .venv/Scripts/python.exe Entrega_Fase3_Grupo14/_Referencia/generadores/generar_documentos.py

Salidas:
  Entrega_Fase3_Grupo14/LEEME_PRIMERO_Fase3.docx
  Entrega_Fase3_Grupo14/1_Informe/informe_fase3_PLANTILLA.docx
  Entrega_Fase3_Grupo14/2_Manuales_Usuario/MU-04_..., MU-05_..., MU-06_..._PLANTILLA.docx

Convención de las plantillas (la misma de la Fase 2): la franja gris dice de qué rol es la sección;
lo gris y en cursiva es instrucción y se borra antes de entregar. Las rutas de menú son de Odoo 18
Community y NO se probaron en la instancia: si la pantalla dice otra cosa, gana la pantalla.
"""
import copy
import sys
from pathlib import Path

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, str(Path(__file__).parent))
from generar_ventas import FLUJOS, PEDIDOS_WEB  # noqa: E402

RAIZ = Path(__file__).resolve().parents[3]
BASE = RAIZ / "Entrega_Fase2_Grupo14/1_Informe/Informe_Fase2_Grupo14_RutaMoto.docx"
F3 = RAIZ / "Entrega_Fase3_Grupo14"
GRIS = RGBColor(0x80, 0x80, 0x80)

ROLES = {
    1: ("Consolidación, análisis y conclusiones", "Santiago Julián Barrera"),
    2: ("Pruebas de flujo completo y portal del cliente", "Jemima Solmaira Chavajay"),
    3: ("Sitio web e-commerce e integración con el ERP", "Alberto Josué Hernández Armas"),
    4: ("CRM en el sitio y reportes BI", "Brayan Emanuel García"),
}
ROLES_CARATULA = {
    "1 — Consolidación y datos maestros": "1 — Consolidación, análisis y conclusiones",
    "2 — Carga manual, cotizaciones y medición": "2 — Pruebas de flujo y portal del cliente",
    "3 — Carga masiva y compras (ERP)": "3 — Sitio web e integración (ERP)",
    "4 — CRM: correo, campañas y pipeline": "4 — CRM en el sitio y reportes BI",
}


# ---------------------------------------------------------------- base: carátula de la Fase 2
def documento(subtitulo, titulo="INFORME FINAL", fecha="GUATEMALA, 24 DE OCTUBRE DEL 2,026"):
    d = docx.Document(BASE)
    cuerpo = d.element.body
    hijos = list(cuerpo.iterchildren())
    for t in hijos[8].iter(qn("w:t")):  # el cuadro de texto del escudo
        if t.text == "INFORME DE AVANCE":
            t.text = titulo
    franja = copy.deepcopy(hijos[62])  # «ROL n — ... · Responsable: ...», con su sombreado
    for el in hijos[22:-1]:  # deja la carátula (0-21) y el sectPr final
        cuerpo.remove(el)
    for p in d.paragraphs[:22]:
        if "Caso: RutaMoto" in p.text:
            _texto(p, subtitulo)
        elif p.text.strip().startswith("GUATEMALA"):
            _texto(p, fecha)
    for fila in d.tables[0].rows[2:]:
        c = fila.cells[2]
        if c.text.strip() in ROLES_CARATULA:
            _texto(c.paragraphs[0], ROLES_CARATULA[c.text.strip()])
    d._franja = franja
    return d


def _texto(p, t):
    """Cambia el texto de un párrafo conservando el formato de su primer run."""
    runs = p.runs
    if not runs:
        p.add_run(t)
        return
    runs[0].text = t
    for r in runs[1:]:
        r.text = ""


def salto(d):
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def indice(d):
    p = d.add_paragraph()
    r = p.add_run("Índice")
    r.bold, r.font.size = True, Pt(14)
    p = d.add_paragraph()
    for tipo, txt in (("begin", None), (None, 'TOC \\o "1-2" \\h \\z \\u'), ("separate", None), ("end", None)):
        run = p.add_run()
        if tipo:
            f = OxmlElement("w:fldChar")
            f.set(qn("w:fldCharType"), tipo)
            run._r.append(f)
            if tipo == "separate":
                run2 = p.add_run("Clic derecho › Actualizar campo (o F9) para generar el índice.")
                run2.italic, run2.font.color.rgb = True, GRIS
        else:
            it = OxmlElement("w:instrText")
            it.set(qn("xml:space"), "preserve")
            it.text = txt
            run._r.append(it)
    salto(d)


def franja(d, rol):
    el = copy.deepcopy(d._franja)
    d.element.body.insert(len(d.element.body) - 1, el)
    p = d.paragraphs[-1]
    area, quien = ROLES[rol]
    _texto(p, f"ROL {rol} — {area}   ·   Responsable: {quien}")


def instr(d, t):
    p = d.add_paragraph()
    r = p.add_run(t)
    r.italic, r.font.color.rgb = True, GRIS
    return p


def texto(d, t):
    d.add_paragraph(t)


def pie(d, t):
    p = d.add_paragraph(t)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def captura(d, que, figura):
    instr(d, f"[Captura: {que}]").paragraph_format.keep_with_next = True
    pie(d, f"Figura __. {figura}. Elaboración propia.")


ANCHO_UTIL = Cm(16)


def tabla(d, encabezados, filas, titulo=None):
    if titulo:
        pie(d, f"Tabla __. {titulo}. Elaboración propia.").paragraph_format.keep_with_next = True
    t = d.add_table(rows=1, cols=len(encabezados))
    t.style = "Table Grid"
    t.autofit = False
    # ancho de cada columna según el texto más largo que tiene (con tope), repartido en el ancho útil
    largo = [max(min(max(len(str(x)) for x in [e] + [f[i] for f in filas]), 60), len(e) + 2, 8) + 4 for i, e in enumerate(encabezados)]
    anchos = [int(ANCHO_UTIL * l / sum(largo)) for l in largo]
    for c, e in zip(t.rows[0].cells, encabezados):
        c.text = e
        c.paragraphs[0].runs[0].bold = True
    for f in filas:
        cells = t.add_row().cells
        for c, v in zip(cells, f):
            c.text = str(v)
    for n, fila in enumerate(t.rows):
        trpr = fila._tr.get_or_add_trPr()
        ns = OxmlElement("w:cantSplit")
        trpr.append(ns)
        if n == 0:  # el encabezado se repite si una tabla larga pasa de página
            hd = OxmlElement("w:tblHeader")
            hd.set(qn("w:val"), "true")
            trpr.append(hd)
        for c, w in zip(fila.cells, anchos):
            c.width = w
            for p in c.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                # las tablas cortas no se parten: cada fila se ata a la siguiente
                p.paragraph_format.keep_with_next = n < len(t.rows) - 1 and len(t.rows) <= 12
                for r in p.runs:
                    r.font.size = Pt(10)
    d.add_paragraph()


def h(d, nivel, t):
    d.add_heading(t, level=nivel)


# ---------------------------------------------------------------- LEEME
def leeme():
    d = documento("Caso: RutaMoto  ·  Fase 3", titulo="GUÍA DEL EQUIPO", fecha="GUATEMALA, 20 DE OCTUBRE DEL 2,026")
    salto(d)
    h(d, 1, "Qué pide la Fase 3")
    texto(d, "Se entrega y se presenta el sábado 24 de octubre de 2026. La fase vale 100 puntos y el enunciado "
             "dice que la integración entre el ERP, el CRM y el sitio es «el aspecto más valorado y determinante».")
    tabla(d, ["Criterio", "Puntos", "Qué hay que mostrar"], [
        ["Sitio e-commerce (punto 16)", "15", "Registro de clientes, carrito, catálogo con 30 o más productos, cotizaciones desde el sitio y facturación"],
        ["Integración ERP/CRM/web", "15", "La venta en línea crea sola el pedido, la factura, el movimiento de inventario y el registro en el CRM"],
        ["Reportes BI (punto 17)", "10", "Inventario: barras por producto, pastel por categoría y tabla de stock bajo. Ventas: líneas por día, semana y mes, y top 5"],
        ["Conclusiones (punto 19)", "20", "Al menos 3, basadas en los datos del BI y en los KPIs de las fases 1 y 2, con beneficios, limitaciones y mejoras"],
        ["Documentación final", "10", "Informe consolidado con los resultados del BI"],
        ["Entregables", "10", "Sitio, reportes BI y manuales completos"],
        ["Presentación final", "20", "Demostración en vivo de la integración completa"],
    ], "Rúbrica de la Fase 3")
    h(d, 1, "Decisiones ya tomadas")
    for t in [
        "El sitio es el módulo Comercio electrónico de Odoo 18, en la misma base de la Fase 2. No hay nada que integrar "
        "por fuera: sitio, ventas, inventario, facturación y CRM comparten la base, y eso es lo que se defiende como integración.",
        "El BI se hace con los informes de Odoo (vistas de gráfico, pivote y tablero), no con Power BI. Son dinámicos "
        "(filtros, agrupaciones y cambio de día, semana o mes en vivo) y leen la base al momento, sin exportar nada.",
        "Las ventas del 05 al 20 de octubre son una historia simulada de 45 pedidos, cargada con un script. Sin ella, la "
        "gráfica por día, semana y mes queda con tres puntos. El informe lo declara así. Las ventas del 21 al 23 de octubre "
        "son reales: las hace el grupo en el sitio.",
        "Mismos roles que en la Fase 2.",
    ]:
        d.add_paragraph("•  " + t, style="List Paragraph")
    h(d, 1, "Reparto")
    tabla(d, ["Rol", "Qué hace en Odoo", "Manual", "Secciones del informe", "Video"], [
        ["3 · Alberto", "Instala y configura el sitio, publica los 38 productos, configura el registro, el pago de prueba y la factura automática, recibe P00004, carga la historia con el script y saca los respaldos (antes de la historia y al cierre, cuando Jemima avisa)", "MU-04", "5, 6.1, 6.3 y 9 (con el rol 1)", "Sitio y configuración"],
        ["2 · Jemima", "Hace los pedidos WEB-01 a WEB-08, WEB-10 y WEB-12 en el sitio (flujos A, C, D y E), valida las entregas, prueba el portal y avisa en el grupo al terminar WEB-12", "MU-05", "7 y 8", "Compra de punta a punta"],
        ["4 · Brayan", "Formulario del sitio → lead → cotización → portal (WEB-09 y WEB-11, flujo B), valida esas dos entregas, y los reportes BI con su tablero después del aviso de WEB-12", "MU-06", "6.2 y 10", "CRM en el sitio y BI"],
        ["1 · Santiago", "No toca Odoo: plan de ventas, informe, análisis de KPIs, objetivos SMART, escalabilidad, conclusiones, presentación, PDF y ZIP", "—", "1–4, 9, 11–16", "—"],
    ], "Reparto de la Fase 3")
    h(d, 1, "Calendario")
    tabla(d, ["Día", "Qué pasa"], [
        ["Mar 20-10", "Reparto. Alberto respalda la base"],
        ["Mié 21-10 (ruta crítica)", "Alberto: sitio publicado, pago de prueba, factura automática, P00004 recibida e historia cargada. Sin esto nadie puede comprar"],
        ["Jue 22-10", "Jemima y Brayan: pedidos por el sitio, portal, flujo del CRM. Brayan empieza el BI"],
        ["Vie 23-10", "Últimos pedidos (WEB-10 a WEB-12); Jemima avisa al terminar WEB-12 y Alberto respalda. Después, BI terminado, manuales, videos. Santiago: informe con los números del BI, PDF y ZIP. Ensayo de la demo"],
        ["Sáb 24-10", "Entrega y presentación final en vivo"],
    ], "Calendario de la Fase 3")
    h(d, 1, "Reglas")
    for t in [
        "Respaldos (Alberto): uno antes de correr el script de la historia y otro al cerrar los pedidos por el sitio, cuando Jemima avisa que hizo WEB-12.",
        "El script se corre primero con --probar. Si dice PROBLEMAS, no se sigue: se avisa en el grupo.",
        "Solo se compran por el sitio los pedidos del plan (hoja 2_Pedidos_sitio del Excel de ventas). Cada compra de "
        "más cambia los números del BI y las conclusiones.",
        "Capturas mientras se hace el paso, no después.",
        "El repo es público: ninguna contraseña en los documentos ni en los commits.",
    ]:
        d.add_paragraph("•  " + t, style="List Paragraph")
    h(d, 1, "Configuración del sitio (rol 3, miércoles)")
    instr(d, "Rutas de Odoo 18 Community sin probar en la instancia. Si la pantalla dice otra cosa, gana la pantalla y se anota en el MU-04.")
    tabla(d, ["#", "Qué", "Dónde (ruta sugerida)"], [
        ["1", "Respaldo de la base", "/web/database/manager › Respaldar"],
        ["2", "Instalar Comercio electrónico (instala Sitio web; con CRM ya instalado se agrega solo el formulario que crea leads)", "Aplicaciones › buscar «Comercio electrónico» › Activar"],
        ["3", "Márgenes en ventas (para el reporte de ganancias)", "Ventas › Configuración › Ajustes › Márgenes"],
        ["4", "Registro libre de clientes", "Sitio web › Configuración › Ajustes › Cuentas de cliente: Registro gratuito"],
        ["5", "Proveedor de pago de prueba", "Facturación › Configuración › Proveedores de pago › Demo (o Transferencia bancaria) › Modo de prueba › Publicar"],
        ["6", "Factura automática al pagar", "Sitio web › Configuración › Ajustes › Facturación automática"],
        ["7", "Categorías del sitio (las 6) y asignarlas", "Sitio web › Configuración › Categorías de eCommerce"],
        ["8", "Publicar los 38 productos", "Sitio web › eCommerce › Productos › Publicado"],
        ["9", "No vender sin existencia (para el flujo D)", "Ficha del producto › pestaña Ventas › desmarcar «Vender fuera de stock», o el ajuste equivalente del sitio"],
        ["10", "Tarifa Talleres B2B visible para los talleres", "Ventas › Productos › Listas de precios › Talleres B2B: sin restricción de sitio web"],
        ["11", "Recibir P00004 (LLA-002 × 16)", "Compras › P00004 › Recibir productos › Validar"],
        ["12", "Cargar la historia", "Script cargar_historial_ventas.py: primero --probar"],
        ["13", "Pasar al grupo la URL del túnel", "13_tunel.ps1"],
    ], "Lista de configuración del sitio")
    h(d, 1, "Archivos")
    tabla(d, ["Archivo", "Para qué"], [
        ["3_Archivos_Datos/RutaMoto_ventas_Fase3.xlsx", "El plan: historia, pedidos por el sitio, flujos y cuadre"],
        ["3_Archivos_Datos/historial_ventas_fase3.json", "Lo que lee el script (no se edita a mano)"],
        ["_Referencia/scripts_instancia/cargar_historial_ventas.py", "Carga la historia en la instancia"],
        ["1_Informe/informe_fase3_PLANTILLA.docx", "El informe, con la franja de cada rol"],
        ["2_Manuales_Usuario/MU-04, MU-05 y MU-06", "Un manual por rol, con cada paso y su captura"],
        ["4_Videos/guion_videos_fase3.md", "Guion de los tres videos y orden de la demo"],
    ], "Archivos de la Fase 3")
    d.save(F3 / "LEEME_PRIMERO_Fase3.docx")


# ---------------------------------------------------------------- INFORME
def informe():
    d = documento("Caso: RutaMoto  ·  Fase 3")
    salto(d)
    indice(d)
    S = []  # (nivel, título, rol, función de contenido)

    def sec(nivel, titulo, rol=None, *bloques):
        h(d, nivel, titulo)
        if rol:
            franja(d, rol)
        for b in bloques:
            b(d)

    I = lambda t: (lambda d: instr(d, t))
    C = lambda q, f: (lambda d: captura(d, q, f))
    T = lambda e, f, t: (lambda d: tabla(d, e, f, t))

    sec(1, "Introducción", 1, I("Qué es RutaMoto en dos líneas, qué hizo cada fase y qué cierra esta: el sitio, la integración, "
                                "el BI y la evaluación de los objetivos. Un párrafo por idea, cuatro párrafos como máximo."))
    salto(d)
    sec(1, "Objetivos de la fase", 1)
    sec(2, "Objetivo general", None, I("Una oración: dejar el ciclo comercial de RutaMoto operando de punta a punta en línea y medirlo con BI."))
    sec(2, "Objetivos específicos", None, I("Cuatro, uno por pieza: sitio, integración, BI, evaluación de objetivos y escalabilidad."))
    sec(1, "Alcance de la fase", 1,
        I("Qué entra y qué no. Tiene que decir de forma explícita lo de la historia simulada:"),
        lambda d: texto(d, "Las ventas registradas entre el 5 y el 20 de octubre de 2026 (45 pedidos, canal «Ventas directas "
                           "(WhatsApp y teléfono)») son una historia simulada, cargada con un script sobre la API de Odoo, para que "
                           "los reportes de ventas por día, semana y mes tengan datos que mostrar. Las ventas del 21 al 23 de octubre "
                           "se hicieron en el sitio, como clientes, por los integrantes del grupo. Las conclusiones distinguen "
                           "siempre entre las dos."),
        I("Fuera de alcance (del enunciado, alcance opcional): pasarela de pago real, aplicación móvil, contabilidad completa."))
    salto(d)
    sec(1, "Seguimiento de la Fase 2", 1)
    sec(2, "Avance contra el cronograma", None, T(["Actividad", "Responsable", "Plan", "Real", "Estado"],
        [["Sitio publicado", "Rol 3", "21-10", "", ""], ["Historia cargada", "Rol 3", "21-10", "", ""],
         ["Pedidos por el sitio", "Rol 2 y 4", "22–23-10", "", ""], ["Reportes BI", "Rol 4", "22–23-10", "", ""],
         ["Informe y entrega", "Rol 1", "23-10", "", ""]], "Avance de la Fase 3 contra el cronograma"))
    sec(2, "Observaciones de la calificación de la Fase 2", None,
        I("Lo que dijo el catedrático de la Fase 2 y qué se corrigió. Si no hubo observaciones, decirlo en una oración."))
    salto(d)
    sec(1, "Sitio web e-commerce", 3, I("Punto 16 del enunciado. Cada subsección con su captura."))
    for t, q in [("Instalación de los módulos", "Aplicaciones con Comercio electrónico y Sitio web instalados"),
                 ("Catálogo publicado", "Tienda con las 6 categorías y los 38 productos (pie: «38 productos publicados»)"),
                 ("Registro de clientes", "Pantalla de registro y ajuste de registro gratuito"),
                 ("Carrito y pago", "Carrito con dos productos y la pantalla del pago de prueba"),
                 ("Facturación", "Ajuste de facturación automática y la factura que generó un pedido del sitio"),
                 ("Cotizaciones desde el sitio", "Pedido del sitio que quedó como cotización en Ventas")]:
        sec(2, t, None, I("Qué se configuró, dónde y por qué. Si algo no funcionó a la primera, contarlo."), C(q, t))
    salto(d)
    sec(1, "Integración ERP, CRM y sitio web", 3,
        I("El criterio que más pesa. La tabla de abajo es el diseño: el rol 3 llena la última columna con lo que pasó de verdad."),
        T(["Evento en el sitio", "Registro que se crea", "Módulo", "¿Automático?", "Visto en la prueba"], [
            ["El visitante se registra", "Contacto con usuario de portal", "Contactos", "Sí", ""],
            ["Agrega al carrito y no paga", "Cotización en borrador", "Ventas", "Sí", ""],
            ["Paga el pedido", "Pedido de venta confirmado", "Ventas", "Sí", ""],
            ["Pedido confirmado", "Entrega reservada (baja el pronóstico)", "Inventario", "Sí", ""],
            ["Pago confirmado", "Factura publicada y pagada", "Facturación", "Sí, con facturación automática", ""],
            ["La bodega valida la entrega", "Baja la existencia real", "Inventario", "No: es el paso físico de despacho", ""],
            ["Llena el formulario de contacto", "Lead u oportunidad", "CRM", "Sí", ""],
            ["Cotización enviada desde el CRM", "Correo con enlace al portal", "CRM y Ventas", "Sí", ""],
            ["El cliente acepta en el portal", "Pedido confirmado", "Ventas", "Sí", ""],
        ], "Qué registro crea cada evento del sitio"))
    sec(2, "Arquitectura", 3, I("Por qué una sola base de Odoo es la integración: no hay conectores que fallen ni datos que copiar. "
                                 "Diagrama sencillo: sitio, ventas, inventario, facturación y CRM sobre la misma base de datos."))
    sec(2, "Del sitio al CRM", 4, I("Flujo B: formulario → lead → oportunidad → cotización → portal. Una captura por paso."),
        C("Lead creado desde el formulario del sitio", "Lead generado desde el sitio web"))
    sec(2, "Del sitio al ERP", 3, I("Un pedido real del sitio seguido en Ventas, Inventario y Facturación, con el mismo número."),
        C("El mismo pedido en Ventas, en la entrega y en la factura", "Trazabilidad de un pedido del sitio"))
    salto(d)
    sec(1, "Portal del cliente", 2, I("Qué ve el cliente en «Mi cuenta»: pedidos, estado de la entrega, facturas y su PDF."),
        C("Portal con la lista de pedidos y una factura", "Portal del cliente"))
    salto(d)
    sec(1, "Pruebas de flujo completo", 2,
        I("Cliente compra → inventario se actualiza → CRM registra → portal refleja. Una fila por pedido del plan; "
          "el número de Odoo y el resultado se llenan al hacer la prueba."),
        T(["Pedido", "Día", "Flujo", "Qué prueba", "Número en Odoo", "Resultado"],
          [[w, dia[5:], f, p, "", ""] for w, dia, _, _, _, f, p, _ in PEDIDOS_WEB], "Casos de prueba del sitio"))
    sec(2, "Defectos encontrados", None, I("Todo lo que no salió como se esperaba, con su causa y cómo se resolvió. "
                                            "Este apartado vale más que la lista de lo que sí funcionó."))
    salto(d)
    sec(1, "Historia de ventas para el análisis", 1,
        I("Rol 1 con el rol 3. Cómo se generó el plan (Excel de ventas), cómo se cargó (script, con el resultado de --probar), "
          "cuántos pedidos entraron y qué números del cuadre se verificaron en Odoo."))
    salto(d)
    sec(1, "Reportes de inteligencia de negocios", 4,
        I("Punto 17. Cada gráfica con su captura, el filtro usado y una oración de lo que muestra."))
    sec(2, "Herramienta y justificación", None, I("Por qué los informes de Odoo y no Power BI: leen la base al momento, "
                                                   "son interactivos sin licencia y no hay que exportar ni refrescar nada."))
    for t, q in [("Existencias por producto", "Gráfica de barras de existencias por producto"),
                 ("Inventario por categoría", "Gráfica de pastel por categoría"),
                 ("Productos con stock bajo", "Tabla de reabastecimiento con los productos bajo el mínimo"),
                 ("Evolución de las ventas", "Gráfica de líneas por día, por semana y por mes (tres capturas)"),
                 ("Los cinco productos más vendidos", "Pivote de productos ordenado por cantidad"),
                 ("Ventas y ganancias por canal", "Ventas directas frente a sitio web, con margen"),
                 ("Tablero", "Tablero con los reportes juntos")]:
        sec(2, t, None, C(q, t))
    salto(d)
    sec(1, "Análisis de resultados", 1,
        I("Los números salen del BI, no del Excel de plan. Si no coinciden con la hoja 4_Cuadre, se dice y se explica."),
        T(["KPI (Fase 1)", "Meta", "Resultado", "Fuente en Odoo", "¿Cumple?"], [
            ["Tasa de conversión del sitio", "2.5 %", "", "Visitantes del sitio frente a pedidos del sitio", ""],
            ["Ticket promedio", "Q 285", "", "Ventas › Informes: total / número de pedidos", ""],
            ["Entregas metropolitanas en < 24 h", "90 %", "", "Entregas: fecha del pedido frente a fecha efectiva", ""],
            ["Satisfacción postventa (CSAT)", "≥ 4.3 / 5", "No medido", "No se implementó encuesta: va en escalabilidad", "—"],
            ["Quiebre de stock", "≤ 5 % de los SKU", "", "Inventario › Existencias", ""],
            ["Tasa de recompra", "20 %", "", "Clientes con más de un pedido", ""],
            ["Clientes registrados", "350 en el trimestre", "", "Contactos con segmento", ""],
        ], "Indicadores de la Fase 1 contra los resultados"),
        I("Separar siempre: qué sale de la historia simulada y qué de las ventas reales del sitio. La conversión y los "
          "clientes registrados por el sitio son de las reales, con una muestra muy chica: decirlo."))
    sec(1, "Evaluación de los objetivos SMART", 1, T(["Objetivo", "Meta", "Qué se logró", "Evidencia"], [
        ["O1 · Habilitar el canal de venta en línea", "Sitio con los 36 productos, carrito, registro y cotizaciones antes del 24-10", "", ""],
        ["O2 · Centralizar el control de inventario", "Todos los movimientos en el ERP, quiebre < 5 %", "", ""],
        ["O3 · Base de clientes segmentada", "350 clientes y 15 talleres en el trimestre", "", ""],
        ["O4 · Sostener la promesa de entrega", "90 % en < 24 h, CSAT ≥ 4.3", "", ""],
    ], "Objetivos SMART de la Fase 1 contra lo logrado"))
    sec(1, "Propuesta de escalabilidad", 1,
        I("Qué haría falta para pasar del prototipo a la operación: servidor en la nube en vez de la laptop del rol 3 (el "
          "punto único de falla de todo el proyecto), pasarela de pago real, dominio rutamoto.gt con certificado, correo "
          "real en vez de Mailpit, encuesta postventa para medir el CSAT, BI con histórico (Power BI o Looker Studio sobre "
          "réplica de PostgreSQL), la expansión a Sacatepéquez, Chimaltenango y Escuintla. Con costo estimado donde se pueda."))
    salto(d)
    sec(1, "Conclusiones", 1,
        I("Mínimo 3, cada una atada a un KPI u objetivo y a un número del BI. Después: beneficios, limitaciones (la historia "
          "simulada, la muestra chica del sitio, la laptop única, el CSAT sin medir) y mejoras para otro proyecto."))
    salto(d)
    sec(1, "Bibliografía", 1, I("APA 7. Documentación de Odoo 18 (sitio, comercio electrónico, portal, informes) y lo citado."))
    sec(1, "Anexos", 1, T(["Anexo", "Contenido", "Ubicación"], [
        ["A", "Video: sitio y configuración (rol 3)", "Enlace de Drive"],
        ["B", "Video: compra de punta a punta (rol 2)", "Enlace de Drive"],
        ["C", "Video: CRM en el sitio y BI (rol 4)", "Enlace de Drive"],
        ["D", "Plan de ventas de la fase", "3_Archivos_Datos/RutaMoto_ventas_Fase3.xlsx"],
        ["E", "Manuales MU-04, MU-05 y MU-06", "2_Manuales_Usuario/"],
    ], "Anexos"))
    d.save(F3 / "1_Informe/informe_fase3_PLANTILLA.docx")


# ---------------------------------------------------------------- MANUALES
def manual(codigo, titulo, rol, capitulos, archivo):
    d = documento(f"Caso: RutaMoto  ·  Fase 3  ·  {codigo}: {titulo}", titulo="MANUAL DE USUARIO")
    salto(d)
    indice(d)
    franja(d, rol)
    instr(d, "Cada paso: qué se hace, la ruta exacta que muestra TU pantalla y la captura. Las rutas de abajo son de Odoo 18 "
             "Community y no se probaron en la instancia: si la pantalla dice otra cosa, se corrige aquí.")
    for i, (cap, pasos) in enumerate(capitulos, 1):
        h(d, 1, cap)
        for j, (paso, ruta, captura_de) in enumerate(pasos, 1):
            h(d, 2, paso)
            p = d.add_paragraph()
            p.add_run("Ruta: ").bold = True
            p.add_run(ruta)
            instr(d, "Qué se hace en este paso y qué se ve al terminar.")
            captura(d, captura_de, paso)
        h(d, 2, f"Validación del capítulo {i}")
        tabla(d, ["Comprobación", "Esperado", "Obtenido"], [["", "", ""]] * 2)
        h(d, 2, f"Problemas encontrados en el capítulo {i}")
        instr(d, "Lo que falló y cómo se resolvió. Si no hubo, decirlo.")
    d.save(F3 / "2_Manuales_Usuario" / archivo)


def manuales():
    manual("MU-04", "Sitio web e-commerce", 3, [
        ("Instalación", [
            ("Respaldo de la base", "/web/database/manager › Respaldar", "Respaldo descargado"),
            ("Instalar Comercio electrónico", "Aplicaciones › «Comercio electrónico» › Activar", "Aplicación instalada"),
            ("Activar márgenes", "Ventas › Configuración › Ajustes › Márgenes", "Ajuste activado")]),
        ("Catálogo", [
            ("Categorías del sitio", "Sitio web › Configuración › Categorías de eCommerce", "Las 6 categorías"),
            ("Publicar los productos", "Sitio web › eCommerce › Productos", "Lista con los 38 publicados"),
            ("No vender sin existencia", "Ficha del producto › Ventas", "Opción desmarcada"),
            ("La tienda vista por un cliente", "Sitio web › Ir al sitio › Tienda", "Tienda con imágenes y precios")]),
        ("Clientes, pago y facturación", [
            ("Registro gratuito", "Sitio web › Configuración › Ajustes › Cuentas de cliente", "Ajuste"),
            ("Proveedor de pago de prueba", "Facturación › Configuración › Proveedores de pago", "Proveedor publicado en modo de prueba"),
            ("Facturación automática", "Sitio web › Configuración › Ajustes", "Ajuste activado"),
            ("Tarifa de talleres en el sitio", "Ventas › Productos › Listas de precios", "Talleres B2B")]),
        ("Recepción de P00004 y carga de la historia", [
            ("Recibir P00004", "Compras › P00004 › Recibir productos › Validar", "LLA-002 con 16 unidades"),
            ("Validar el plan con --probar", "Terminal: docker exec ... --probar", "«Validación limpia»"),
            ("Cargar la historia", "Terminal: docker exec ... (sin --probar)", "Los 45 pedidos cargados"),
            ("Verificar en Ventas", "Ventas › Informes › Ventas, por día", "Ventas del 05 al 20-10")]),
    ], "MU-04_Sitio_web_ecommerce_PLANTILLA.docx")
    manual("MU-05", "Compra en línea y portal del cliente", 2, [
        ("Compra de un cliente nuevo (flujo A)", [
            ("Registrarse en el sitio", "Sitio › Iniciar sesión › Registrarse", "Formulario de registro"),
            ("Buscar en el catálogo y agregar al carrito", "Tienda › categoría › producto › Agregar", "Carrito"),
            ("Pagar", "Carrito › Finalizar compra › Pago", "Confirmación del pedido"),
            ("El pedido en Ventas", "Ventas › Pedidos", "Pedido con origen sitio web"),
            ("La factura automática", "Facturación › Facturas de clientes", "Factura pagada"),
            ("Validar la entrega", "Inventario › Entregas › Validar", "Entrega hecha y existencia rebajada")]),
        ("Portal del cliente", [
            ("Dar acceso a un cliente existente", "Contactos › cliente › Acción › Conceder acceso al portal", "Invitación en Mailpit"),
            ("Mis pedidos", "Sitio › Mi cuenta › Pedidos de venta", "Lista con estado"),
            ("Mis facturas", "Sitio › Mi cuenta › Facturas", "Factura y su PDF")]),
        ("Casos especiales", [
            ("Taller con tarifa B2B (flujo C)", "Sitio con la sesión del taller", "Precio con descuento"),
            ("Producto que vuelve al catálogo (flujo D)", "Tienda › LLA-002", "Disponible después de P00004"),
            ("Carrito abandonado (flujo E)", "Ventas › Cotizaciones", "Cotización del sitio sin pagar")]),
    ], "MU-05_Compra_en_linea_y_portal_PLANTILLA.docx")
    manual("MU-06", "CRM en el sitio y reportes BI", 4, [
        ("Del sitio al CRM (flujo B)", [
            ("Formulario de contacto del sitio", "Sitio › Contáctanos", "Formulario lleno"),
            ("El lead en el CRM", "CRM › Iniciativas (o Pipeline)", "Lead con origen sitio web"),
            ("Convertir a oportunidad y cotizar", "Oportunidad › Nueva cotización", "Cotización"),
            ("Enviar por correo", "Cotización › Enviar por correo", "Correo en Mailpit con enlace"),
            ("El cliente acepta y paga en el portal", "Enlace del correo › Aceptar y pagar", "Pedido confirmado"),
            ("Validar la entrega y revisar la factura", "Inventario › Entregas › Validar; Facturación › Facturas de clientes", "Entrega hecha y factura pagada")]),
        ("Reporte de inventario", [
            ("Existencias por producto (barras)", "Inventario › Informes › Existencias › vista Gráfico › Barras, por Producto", "Barras"),
            ("Inventario por categoría (pastel)", "Misma vista › Pastel, por Categoría de producto", "Pastel"),
            ("Productos con stock bajo (tabla)", "Inventario › Operaciones › Reabastecimiento › filtro bajo el mínimo", "Tabla")]),
        ("Reporte de ventas", [
            ("Ventas por día, semana y mes (líneas)", "Ventas › Informes › Ventas › Gráfico › Líneas, Fecha: Día / Semana / Mes", "Líneas"),
            ("Top 5 productos", "Ventas › Informes › Ventas › Pivote › filas Producto, Cantidad descendente", "Pivote"),
            ("Ventas y margen por canal", "Ventas › Informes › Ventas › agrupar por Equipo de ventas, medida Margen", "Gráfico"),
            ("Guardar como favorito y armar el tablero", "Favoritos › Guardar / Agregar a mi tablero", "Tablero")]),
    ], "MU-06_CRM_en_el_sitio_y_BI_PLANTILLA.docx")


if __name__ == "__main__":
    leeme()
    informe()
    manuales()
    print("Listo:", *[p.relative_to(F3) for p in sorted(F3.rglob("*.docx"))], sep="\n  ")
