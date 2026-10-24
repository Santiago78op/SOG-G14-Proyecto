#!/usr/bin/env python3
"""Verifica, sin escribir nada, que la instancia de Odoo tenga lo que el BI del rol 4 necesita.

Compara contra la hoja 4_Cuadre del plan de ventas:

  historia:  45 pedidos, Q 14,679.50, fechas del 05 al 20-10
  sitio:     11 pedidos confirmados (sin WEB-07), Q 4,431.50
  total:     56 pedidos, Q 19,111.00
  top 5:     LUB-001 (45), LUB-004 (21), ELE-007 (13), FRE-001 (12), ELE-003 (11)
  bajo mínimo: CAS-005, ELE-002, FRE-004, LUB-001
  en cero:   0 productos

Uso:

  export ODOO_CLAVE='...'          # no la escribas en el repo
  python3 05_VERIFICAR_BI.py --url https://tu-tunel --db rutamoto --usuario tu@correo

  python3 05_VERIFICAR_BI.py --dry-run   # solo muestra el plan, no se conecta

El script es de solo lectura: no crea, no modifica y no borra registros.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import sys
import xmlrpc.client
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# --- Lo que dice el plan (hoja 4_Cuadre) -------------------------------------

HIST_ORDERS = 45
HIST_TOTAL = 14679.50
WEB_ORDERS = 11
WEB_TOTAL = 4431.50          # calculado con las cantidades y precios del Excel
TOTAL_ORDERS = HIST_ORDERS + WEB_ORDERS
TOTAL_SALES = HIST_TOTAL + WEB_TOTAL

TOP5 = {
    "LUB-001": 45,
    "LUB-004": 21,
    "ELE-007": 13,
    "FRE-001": 12,
    "ELE-003": 11,
}

LOW_STOCK = {"CAS-005", "ELE-002", "FRE-004", "LUB-001"}

ROLE4_PARTNERS = ["Mónica Isabel Arévalo Soto", "Taller Hermanos Cutzal"]
ROLE4_EXPECTED = {"Mónica Isabel Arévalo Soto", "Taller Hermanos Cutzal"}

START = "2026-10-05 00:00:00"
WEB_START = "2026-10-21 00:00:00"
ROLE4_START = "2026-10-21 00:00:00"  # por si el flujo se hizo el 21

TOL = 0.60  # colones de tolerancia por redondeos

# --- Infraestructura mínima --------------------------------------------------


class Report:
    def __init__(self) -> None:
        self.fails: list[str] = []
        self.warns: list[str] = []

    def ok(self, title: str, detail: str = "") -> None:
        print(f"[OK]   {title}" + (f" · {detail}" if detail else ""))

    def info(self, title: str, detail: str = "") -> None:
        print(f"[i]    {title}" + (f" · {detail}" if detail else ""))

    def warn(self, title: str, detail: str = "") -> None:
        print(f"[!]    {title}" + (f" · {detail}" if detail else ""))
        self.warns.append(title)

    def fail(self, title: str, detail: str = "") -> None:
        print(f"[FALLA] {title}" + (f" · {detail}" if detail else ""))
        self.fails.append(title)

    def close(self) -> int:
        print("\n" + "=" * 72)
        if self.fails:
            print("NO CAPTURAR TODAVÍA. Fallos críticos:")
            for f in self.fails:
                print(f"  - {f}")
            if self.warns:
                print("Advertencias:")
                for w in self.warns:
                    print(f"  - {w}")
            return 1
        print("Listo para capturar.")
        if self.warns:
            print("Advertencias (revisar antes de escribir el informe):")
            for w in self.warns:
                print(f"  - {w}")
        return 0


def conectar(url: str, db: str, usuario: str, clave: str):
    comun = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", allow_none=True)
    uid = comun.authenticate(db, usuario, clave, {})
    if not uid:
        sys.exit("No se pudo iniciar sesión: revisá URL, base, usuario y clave.")
    modelos = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", allow_none=True)

    def odoo(modelo: str, metodo: str, *args, **kw):
        return modelos.execute_kw(db, uid, clave, modelo, metodo, list(args), kw)

    return odoo


def many2one_id(value) -> int | None:
    """Odoo devuelve un many2one como [id, nombre] o como id."""
    if isinstance(value, (list, tuple)) and value:
        return int(value[0])
    if isinstance(value, int):
        return value
    return None


def money(value) -> float:
    return float(value or 0.0)


def read_codes(odoo, product_ids: set[int]) -> dict[int, str]:
    if not product_ids:
        return {}
    rows = odoo("product.product", "read", sorted(product_ids), fields=["default_code"])
    return {int(r["id"]): (r.get("default_code") or f"id={r['id']}") for r in rows}


def print_dates(hist: list[dict]) -> None:
    days = Counter((o.get("date_order") or "")[:10] for o in hist)
    print("\nPedidos de historia por día:")
    for day in sorted(days):
        print(f"  {day}: {days[day]}")
    if days:
        print(f"  Rango: {min(days)} → {max(days)}")


# --- Comprobaciones ----------------------------------------------------------


def check_recent_leads(odoo, rep: Report) -> None:
    """Lista los leads/oportunidades creados hoy. Sirve para saber si el formulario del sitio
    está creando la iniciativa o si el problema es solo el filtro de la vista."""
    print("\n--- Iniciativas/leads creados hoy (diagnóstico del formulario) ---")
    today = datetime.now().strftime("%Y-%m-%d 00:00:00")
    try:
        leads = odoo(
            "crm.lead", "search_read",
            [["create_date", ">=", today]],
            fields=[
                "name", "contact_name", "email_from", "source_id", "type",
                "stage_id", "create_date", "user_id", "team_id",
            ],
        )
    except xmlrpc.client.Fault as exc:
        rep.warn("No se pudieron leer las iniciativas", str(exc))
        return

    if not leads:
        rep.warn(
            "No hay iniciativas creadas hoy",
            "El formulario no está creando el lead, o se creó antes de hoy. Revisá la acción del "
            "formulario y el módulo «Formulario de contacto».",
        )
        return

    for lead in leads:
        source = lead.get("source_id")
        source = source[1] if isinstance(source, (list, tuple)) and len(source) > 1 else (source or "—")
        stage = lead.get("stage_id")
        stage = stage[1] if isinstance(stage, (list, tuple)) and len(stage) > 1 else (stage or "—")
        user = lead.get("user_id")
        user = user[1] if isinstance(user, (list, tuple)) and len(user) > 1 else (user or "sin asignar")
        print(
            f"  {lead.get('name')} · {lead.get('contact_name') or '—'} · "
            f"{lead.get('email_from') or '—'} · tipo {lead.get('type')} · origen {source} · "
            f"etapa {stage} · {user} · {lead.get('create_date')}"
        )
    rep.info("Iniciativas de hoy", f"{len(leads)}; si no ves la de Mónica, el formulario no la creó")


def check_history(odoo, rep: Report) -> None:
    print("\n--- Historia simulada ---")
    fields = [
        "name", "client_order_ref", "state", "amount_untaxed", "amount_total",
        "date_order", "team_id", "invoice_ids", "picking_ids",
    ]
    hist = odoo("sale.order", "search_read", [["client_order_ref", "like", "HIST-"]], fields=fields)
    confirmed = [o for o in hist if o.get("state") in ("sale", "done")]

    if not hist:
        rep.fail("No hay ningún pedido HIST-nnn: la historia no está cargada.")
        return

    if len(confirmed) == HIST_ORDERS:
        rep.ok(f"Historia: {len(confirmed)} pedidos confirmados")
    else:
        rep.fail(
            f"Historia: se esperaban {HIST_ORDERS} pedidos confirmados y hay {len(confirmed)} "
            f"(totales con referencia HIST: {len(hist)})"
        )

    total = sum(money(o.get("amount_total")) for o in confirmed)
    net = sum(money(o.get("amount_untaxed")) for o in confirmed)
    if abs(total - HIST_TOTAL) <= TOL:
        rep.ok(
            "Venta de la historia (IVA incluido)",
            f"Q {total:,.2f} (esperado Q {HIST_TOTAL:,.2f}); sin IVA Q {net:,.2f}",
        )
    else:
        rep.warn(
            "Venta de la historia distinta del plan",
            f"Odoo Q {total:,.2f} con IVA vs plan Q {HIST_TOTAL:,.2f}. Revisá la tarifa B2B; "
            f"sin IVA Odoo muestra Q {net:,.2f}.",
        )

    days = Counter((o.get("date_order") or "")[:10] for o in confirmed)
    if len(days) >= 10:
        rep.ok("La historia tiene fechas repartidas", f"{len(days)} días distintos")
    elif len(days) > 1:
        rep.warn("La historia tiene pocos días distintos", f"{len(days)} días")
    else:
        rep.fail("Todas las ventas de la historia caen en un solo día: la tendencia no se puede mostrar")

    bad = {d for d in days if d and (d < "2026-10-05" or d > "2026-10-21")}
    if bad:
        rep.warn("Hay pedidos de historia fuera del 05-20 de octubre", ", ".join(sorted(bad)))

    print_dates(confirmed)


def check_web(odoo, rep: Report) -> tuple[int, float]:
    print("\n--- Pedidos del sitio ---")
    fields = ["name", "state", "amount_untaxed", "amount_total", "date_order", "team_id", "website_id", "partner_id"]

    # 1. Compras directas: tienen website_id.
    direct = odoo(
        "sale.order", "search_read",
        [["website_id", "!=", False], ["date_order", ">=", WEB_START]],
        fields=fields,
    )
    direct_confirmed = [o for o in direct if o.get("state") in ("sale", "done")]
    direct_drafts = [o for o in direct if o.get("state") in ("draft", "sent")]

    # 2. WEB-09 y WEB-11: son cotizaciones creadas desde el CRM, no carritos del sitio,
    #    así que puede que no tengan website_id. Se buscan por cliente y fecha.
    partners = odoo("res.partner", "search_read", [["name", "in", ROLE4_PARTNERS]], fields=["name"])
    pids = [int(p["id"]) for p in partners]
    role4 = odoo(
        "sale.order", "search_read",
        [["partner_id", "in", pids], ["state", "in", ["sale", "done"]], ["date_order", ">=", ROLE4_START]],
        fields=fields,
    ) if pids else []

    by_id = {int(o["id"]): o for o in direct_confirmed}
    for o in role4:
        by_id.setdefault(int(o["id"]), o)
    confirmed = list(by_id.values())
    total = sum(money(o.get("amount_total")) for o in confirmed)
    net = sum(money(o.get("amount_untaxed")) for o in confirmed)

    if role4:
        web_team_ids = {
            t["id"] for t in odoo("crm.team", "search_read", [], fields=["name"])
            if any(x in (t.get("name") or "").lower() for x in ("website", "sitio", "web"))
        }
        wrong_team = [
            o["name"] for o in role4
            if many2one_id(o.get("team_id")) not in web_team_ids
        ]
        if wrong_team:
            rep.warn(
                "WEB-09/WEB-11 no están en el equipo del sitio",
                f"{', '.join(wrong_team)}. El reporte por canal los va a poner en otro canal; "
                "asignales el equipo «Website Sales» antes de capturar.",
            )

    if len(confirmed) == WEB_ORDERS:
        rep.ok(f"Pedidos del sitio: {len(confirmed)} confirmados")
    elif len(confirmed) == 0:
        rep.warn(
            "No hay pedidos del sitio",
            "El BI puede usar la historia, pero el flujo B (WEB-09/11) no está hecho. "
            "No captures el manual del CRM sin esos dos pedidos.",
        )
    else:
        rep.warn(
            f"Pedidos del sitio: hay {len(confirmed)} de {WEB_ORDERS}",
            "Si vas a capturar con corte, decláralo en el informe: «corte al 23-10, N pedidos». "
            "No inventes los que faltan.",
        )

    if abs(total - WEB_TOTAL) <= TOL:
        rep.ok(
            "Venta del sitio (IVA incluido)",
            f"Q {total:,.2f} (esperado Q {WEB_TOTAL:,.2f}); sin IVA Q {net:,.2f}",
        )
    else:
        rep.warn(
            "Venta del sitio distinta del plan",
            f"Odoo Q {total:,.2f} con IVA vs plan Q {WEB_TOTAL:,.2f}. Revisá tarifa B2B, "
            f"impuestos y WEB-07; sin IVA Odoo muestra Q {net:,.2f}.",
        )

    if direct_drafts:
        rep.info("Cotizaciones del sitio sin confirmar", f"{len(direct_drafts)} (WEB-07 debería ser una)")
    else:
        rep.warn("No hay ninguna cotización abandonada", "WEB-07 debería quedar como cotización")

    if len(confirmed) != WEB_ORDERS:
        print("  Detalle de pedidos del sitio:")
        for o in sorted(confirmed, key=lambda x: x.get("date_order") or ""):
            partner = o.get("partner_id")
            partner = partner[1] if isinstance(partner, (list, tuple)) and len(partner) > 1 else (partner or "—")
            print(
                f"    {o.get('name')} · {partner} · {(o.get('date_order') or '')[:10]} · "
                f"Q {money(o.get('amount_total')):,.2f}"
            )
    rep.info("Desglose", f"{len(direct_confirmed)} compras directas + {len(role4)} cotizaciones del CRM")
    return len(confirmed), total


def check_totals(rep: Report, hist_n: int, hist_total: float, web_n: int, web_total: float) -> None:
    print("\n--- Total del plan (historia + sitio) ---")
    n = hist_n + web_n
    total = hist_total + web_total
    if n == TOTAL_ORDERS:
        rep.ok(f"Total de pedidos: {n}")
    else:
        rep.warn(f"Total de pedidos: {n} (esperado {TOTAL_ORDERS})")
    if abs(total - TOTAL_SALES) <= TOL:
        rep.ok(
            "Total vendido (IVA incluido)",
            f"Q {total:,.2f} (esperado Q {TOTAL_SALES:,.2f})",
        )
    else:
        rep.warn(
            "Total vendido distinto del plan",
            f"Odoo Q {total:,.2f} con IVA vs plan Q {TOTAL_SALES:,.2f}",
        )


def check_other_orders(odoo, rep: Report) -> None:
    """Pedidos confirmados del período que no son historia ni sitio.

    La instancia ya trae pedidos de la Fase 2 (por ejemplo S00013, del 07-10).
    El informe de ventas los va a incluir; hay que decidir si se excluyen o se explican.
    """
    print("\n--- Otros pedidos confirmados en el período ---")
    fields = [
        "name", "client_order_ref", "state", "amount_total", "amount_untaxed",
        "date_order", "team_id", "website_id", "partner_id",
    ]
    orders = odoo(
        "sale.order", "search_read",
        [["state", "in", ["sale", "done"]], ["date_order", ">=", START]],
        fields=fields,
    )
    partners = odoo("res.partner", "search_read", [["name", "in", ROLE4_PARTNERS]], fields=["name"])
    pids = {int(p["id"]) for p in partners}

    others = []
    for o in orders:
        ref = o.get("client_order_ref") or ""
        if ref.startswith("HIST-"):
            continue
        if o.get("website_id"):
            continue
        if many2one_id(o.get("partner_id")) in pids and (o.get("date_order") or "") >= ROLE4_START:
            continue
        others.append(o)

    if not others:
        rep.ok("No hay otros pedidos confirmados en el período")
        return

    total = sum(money(o.get("amount_total")) for o in others)
    net = sum(money(o.get("amount_untaxed")) for o in others)
    print(f"  {len(others)} pedido(s) extra: Q {total:,.2f} con IVA / Q {net:,.2f} sin IVA")
    for o in others[:12]:
        print(
            f"    {o.get('name')} · ref {o.get('client_order_ref') or '—'} · "
            f"{(o.get('date_order') or '')[:10]} · Q {money(o.get('amount_total')):,.2f}"
        )
    rep.warn(
        "Hay pedidos que no son de la historia ni del sitio",
        f"{len(others)} pedidos, Q {total:,.2f} con IVA. El informe de ventas los va a incluir: "
        "decidí si los excluís por fecha/equipo o los explicás en el texto. No los borres de la base.",
    )


def check_top5(odoo, rep: Report) -> None:
    print("\n--- Top 5 por unidades ---")
    lines = odoo(
        "sale.order.line", "search_read",
        [["order_id.state", "in", ["sale", "done"]], ["order_id.date_order", ">=", START]],
        fields=["product_id", "product_uom_qty"],
    )
    qty: dict[int, float] = defaultdict(float)
    for line in lines:
        pid = many2one_id(line.get("product_id"))
        if pid:
            qty[pid] += float(line.get("product_uom_qty") or 0)

    # Excluir productos de servicio/flete: no son catálogo vendible.
    rows = odoo(
        "product.product", "read", sorted(qty),
        fields=["default_code", "name", "type"],
    )
    info = {
        int(r["id"]): (r.get("default_code") or f"id={r['id']}", (r.get("name") or ""), r.get("type"))
        for r in rows
    }
    total_by_code = {}
    excluded = []
    for pid, q in qty.items():
        code, name, ptype = info.get(pid, (str(pid), "", ""))
        low = f"{code} {name}".lower()
        if ptype == "service" or any(x in low for x in ("delivery", "envío", "envio", "flete", "shipping")):
            excluded.append((code, q))
            continue
        total_by_code[code] = q
    top = sorted(total_by_code.items(), key=lambda kv: (-kv[1], kv[0]))[:5]

    if excluded:
        print("  Excluidos (servicio/flete):", ", ".join(f"{c} ({q:g})" for c, q in excluded))
    print("  Obtenido:")
    for code, q in top:
        print(f"    {code}: {q:g}")
    print("  Esperado:")
    for code, q in TOP5.items():
        print(f"    {code}: {q}")

    if {c: int(round(q)) for c, q in top} == TOP5:
        rep.ok("Top 5 coincide con el plan")
    else:
        rep.warn(
            "Top 5 distinto del plan",
            "Si cambió por pedidos o entregas, decilo en el informe; no lo maquilles.",
        )


def check_low_stock(odoo, rep: Report) -> None:
    print("\n--- Productos bajo el mínimo ---")
    low: dict[str, tuple[float, float]] = {}
    try:
        ops = odoo(
            "stock.warehouse.orderpoint", "search_read", [],
            fields=["product_id", "product_min_qty", "qty_available", "qty_to_order"],
        )
        codes = read_codes(odoo, {many2one_id(o.get("product_id")) for o in ops if many2one_id(o.get("product_id"))})
        for op in ops:
            pid = many2one_id(op.get("product_id"))
            available = op.get("qty_available")
            minimum = op.get("product_min_qty")
            if pid and available is not None and minimum is not None and available < minimum:
                low[codes.get(pid, str(pid))] = (float(available), float(minimum))
    except xmlrpc.client.Fault:
        # Plan B: leer existencias y mínimos por separado.
        prods = odoo(
            "product.product", "search_read",
            [["default_code", "!=", False], ["sale_ok", "=", True]],
            fields=["default_code", "qty_available"],
        )
        ops = odoo("stock.warehouse.orderpoint", "search_read", [], fields=["product_id", "product_min_qty"])
        prod_qty = {p["id"]: p.get("qty_available") or 0 for p in prods}
        code_by_id = {p["id"]: p["default_code"] for p in prods}
        for op in ops:
            pid = many2one_id(op.get("product_id"))
            if pid in prod_qty and prod_qty[pid] < (op.get("product_min_qty") or 0):
                low[code_by_id.get(pid, str(pid))] = (
                    float(prod_qty[pid]), float(op.get("product_min_qty") or 0)
                )

    print("  Obtenido:", ", ".join(f"{k} ({v[0]:g}/{v[1]:g})" for k, v in sorted(low.items())) or "ninguno")
    print("  Esperado:", ", ".join(sorted(LOW_STOCK)))

    if set(low) == LOW_STOCK:
        rep.ok("Bajo el mínimo coincide con el plan", f"{len(low)} productos")
    else:
        rep.warn(
            "Bajo el mínimo distinto del plan",
            f"Faltan: {', '.join(sorted(LOW_STOCK - set(low))) or 'ninguno'}; "
            f"sobran: {', '.join(sorted(set(low) - LOW_STOCK)) or 'ninguno'}",
        )


def check_zero(odoo, rep: Report) -> None:
    print("\n--- Productos en cero ---")
    prods = odoo(
        "product.product", "search_read",
        [["default_code", "!=", False], ["sale_ok", "=", True]],
        fields=["default_code", "qty_available", "type", "is_storable"],
    )
    zero = []
    for p in prods:
        is_storable = p.get("is_storable")
        if is_storable is None:
            is_storable = p.get("type") == "consu"
        if is_storable and (p.get("qty_available") or 0) <= 0:
            zero.append(p["default_code"])
    if not zero:
        rep.ok("Productos en cero: 0 (sin quiebre)")
    else:
        rep.warn("Hay productos en cero", ", ".join(sorted(zero)))


def check_role4_orders(odoo, rep: Report) -> None:
    print("\n--- Pedidos WEB-09 y WEB-11 (rol 4) ---")
    partners = odoo(
        "res.partner", "search_read",
        [["name", "in", ROLE4_PARTNERS]],
        fields=["name"],
    )
    pids = {int(p["id"]): p["name"] for p in partners}
    if set(pids.values()) != ROLE4_EXPECTED:
        rep.fail("No se encontraron los dos clientes del flujo B", ", ".join(sorted(pids.values())) or "ninguno")
        return

    orders = odoo(
        "sale.order", "search_read",
        [["partner_id", "in", list(pids)], ["state", "in", ["sale", "done"]], ["date_order", ">=", ROLE4_START]],
        fields=["name", "partner_id", "date_order", "amount_untaxed", "amount_total", "invoice_ids", "picking_ids"],
    )
    if len(orders) != 2:
        rep.fail(f"Se esperaban 2 pedidos del sitio para el rol 4 y hay {len(orders)}")
    else:
        rep.ok("Dos pedidos del flujo B", ", ".join(sorted(o["name"] for o in orders)))

    for order in sorted(orders, key=lambda o: o["name"]):
        partner = pids.get(many2one_id(order.get("partner_id")), "?")
        print(f"\n  {order['name']} · {partner} · Q {money(order.get('amount_total')):,.2f} con IVA "
              f"(Q {money(order.get('amount_untaxed')):,.2f} sin IVA)")

        inv_ids = order.get("invoice_ids") or []
        if not inv_ids:
            rep.fail(f"{order['name']} no tiene factura")
        else:
            invs = odoo(
                "account.move", "read", inv_ids,
                fields=["name", "state", "payment_state", "amount_total", "invoice_date"],
            )
            for inv in invs:
                paid = inv.get("payment_state") in ("paid", "in_payment")
                (rep.ok if paid else rep.fail)(
                    f"Factura {inv.get('name')}",
                    f"estado {inv.get('payment_state')} · Q {money(inv.get('amount_total')):,.2f}",
                )

        pick_ids = order.get("picking_ids") or []
        if not pick_ids:
            rep.fail(f"{order['name']} no tiene entrega")
        else:
            picks = odoo("stock.picking", "read", pick_ids, fields=["name", "state", "date_done"])
            for pick in picks:
                done = pick.get("state") == "done"
                (rep.ok if done else rep.fail)(
                    f"Entrega {pick.get('name')}",
                    f"estado {pick.get('state')}",
                )


def check_margin(odoo, rep: Report) -> None:
    print("\n--- Margen por canal ---")
    try:
        fields = odoo("sale.report", "fields_get", [], attributes=["string", "type"])
    except xmlrpc.client.Fault as exc:
        rep.warn("No se pudo leer sale.report", str(exc))
        return
    if "margin" not in fields:
        rep.warn("La medida Margen no está en sale.report", "Activá Márgenes o instalá sale_margin.")
        return

    try:
        groups = odoo(
            "sale.report", "read_group",
            [["state", "in", ["sale", "done"]], ["date", ">=", START]],
            ["price_total:sum", "price_subtotal:sum", "margin:sum"],
            ["team_id"],
        )
    except xmlrpc.client.Fault as exc:
        rep.warn("No se pudo agrupar por equipo de ventas", str(exc))
        return

    for g in groups:
        team = g.get("team_id")
        name = team[1] if isinstance(team, (list, tuple)) and len(team) > 1 else (team or "Sin equipo")
        print(
            f"  {name}: venta Q {money(g.get('price_total')):,.2f} con IVA "
            f"(Q {money(g.get('price_subtotal')):,.2f} sin IVA) · "
            f"margen Q {money(g.get('margin')):,.2f}"
        )


# --- Main --------------------------------------------------------------------


def main() -> int:
    here = Path(__file__).resolve()
    default_json = here.parents[2] / "3_Archivos_Datos" / "historial_ventas_fase3.json"

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--url", default="http://localhost:8069")
    ap.add_argument("--db", default="rutamoto")
    ap.add_argument("--usuario", default="admin@rutamoto.gt")
    ap.add_argument("--clave", default=None, help="También se puede usar la variable ODOO_CLAVE")
    ap.add_argument("--json", default=str(default_json), help="historial_ventas_fase3.json")
    ap.add_argument("--dry-run", action="store_true", help="No se conecta; solo muestra el plan")
    args = ap.parse_args()

    print("Plan de la hoja 4_Cuadre")
    print(f"  Historia: {HIST_ORDERS} pedidos · Q {HIST_TOTAL:,.2f}")
    print(f"  Sitio:    {WEB_ORDERS} pedidos · Q {WEB_TOTAL:,.2f}")
    print(f"  Total:    {TOTAL_ORDERS} pedidos · Q {TOTAL_SALES:,.2f}")
    print(f"  JSON:     {args.json}")

    if args.json and os.path.exists(args.json):
        with open(args.json, encoding="utf-8") as fh:
            plan = json.load(fh)
        print(f"  JSON leído: {len(plan.get('pedidos', []))} pedidos · equipo {plan.get('equipo_ventas')}")
    else:
        print("  Aviso: no se encontró el JSON; se usan los valores del plan.")

    if args.dry_run:
        print("\nDry run: no se conecta a Odoo.")
        return 0

    clave = args.clave or os.environ.get("ODOO_CLAVE") or getpass.getpass(f"Clave de {args.usuario}: ")
    odoo = conectar(args.url.rstrip("/"), args.db, args.usuario, clave)

    rep = Report()
    try:
        teams = [t.get("name") or "" for t in odoo("crm.team", "search_read", [], fields=["name"])]
        rep.info("Equipos de venta", ", ".join(teams) or "ninguno")
    except xmlrpc.client.Fault as exc:
        rep.warn("No se pudieron leer los equipos de venta", str(exc))
        teams = []

    try:
        check_recent_leads(odoo, rep)
        check_history(odoo, rep)
        web_n, web_total = check_web(odoo, rep)
        hist = odoo(
            "sale.order", "search_read",
            [["client_order_ref", "like", "HIST-"], ["state", "in", ["sale", "done"]]],
            fields=["amount_total"],
        )
        hist_total = sum(money(o.get("amount_total")) for o in hist)
        check_totals(rep, len(hist), hist_total, web_n, web_total)
        check_other_orders(odoo, rep)
        check_top5(odoo, rep)
        check_low_stock(odoo, rep)
        check_zero(odoo, rep)
        check_role4_orders(odoo, rep)
        check_margin(odoo, rep)
    except xmlrpc.client.Fault as exc:
        rep.fail("Error de Odoo", f"{exc.faultCode}: {exc.faultString}")
    except Exception as exc:  # noqa: BLE001 - queremos ver el error y seguir
        rep.fail("Error inesperado", repr(exc))

    return rep.close()


if __name__ == "__main__":
    sys.exit(main())
