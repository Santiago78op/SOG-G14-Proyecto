"""Carga la historia simulada de ventas (05-10 al 20-10-2026) en la instancia de Odoo 18.

Lee historial_ventas_fase3.json (lo genera _Referencia/generadores/generar_ventas.py) y, por cada
pedido: crea la orden de venta, la confirma, valida la entrega, crea y publica la factura, registra
el pago si corresponde y por último pone las fechas del plan (pedido, entrega y factura).

Solo usa la biblioteca estándar de Python, así que corre dentro del contenedor de Odoo:

  docker cp cargar_historial_ventas.py rutamoto-odoo:/tmp/
  docker cp ../../3_Archivos_Datos/historial_ventas_fase3.json rutamoto-odoo:/tmp/
  docker exec -it rutamoto-odoo python3 /tmp/cargar_historial_ventas.py --json /tmp/historial_ventas_fase3.json --probar
  docker exec -it rutamoto-odoo python3 /tmp/cargar_historial_ventas.py --json /tmp/historial_ventas_fase3.json

--probar solo lee: comprueba clientes, productos y existencias, y no escribe nada.
La contraseña se pide por teclado (o en la variable ODOO_CLAVE). Nunca va en el repo.

Es reanudable: un pedido cuyo «Referencia del cliente» ya es HIST-nnn se salta si está completo.
Se detiene en el primer error y dice en qué pedido y en qué paso quedó.

ANTES DE CORRERLO SIN --probar: respaldo de la base desde /web/database/manager.
"""
import argparse
import getpass
import json
import os
import sys
import xmlrpc.client


def conectar(url, db, usuario, clave):
    comun = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", allow_none=True)
    uid = comun.authenticate(db, usuario, clave, {})
    if not uid:
        sys.exit("No se pudo iniciar sesión: revisá base, usuario y contraseña.")
    modelos = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", allow_none=True)

    def odoo(modelo, metodo, *args, contexto=None, **kw):
        if contexto:
            kw["context"] = contexto
        return modelos.execute_kw(db, uid, clave, modelo, metodo, list(args), kw)

    return odoo


def resolver(odoo, plan):
    """Busca clientes y productos. Devuelve los mapas y la lista de problemas."""
    problemas = []
    clientes = {}
    for nombre in sorted({p["cliente"] for p in plan["pedidos"]}):
        ids = odoo("res.partner", "search", [("name", "=", nombre)])
        if len(ids) != 1:
            problemas.append(f"Cliente «{nombre}»: {len(ids)} coincidencias (se espera 1)")
        else:
            clientes[nombre] = ids[0]
    refs = sorted({l["producto"] for p in plan["pedidos"] for l in p["lineas"]})
    productos = {}
    for r in odoo("product.product", "search_read", [("default_code", "in", refs)],
                  fields=["default_code", "qty_available"]):
        productos[r["default_code"]] = r
    for ref in refs:
        if ref not in productos:
            problemas.append(f"Producto {ref}: no existe")
    return clientes, productos, problemas


def existentes(odoo):
    """Pedidos HIST-nnn que ya están en la base, con su estado."""
    filas = odoo("sale.order", "search_read", [("client_order_ref", "like", "HIST-")],
                 fields=["client_order_ref", "state", "invoice_status"])
    return {f["client_order_ref"]: f for f in filas}


def validar_entregas(odoo, so_id, fecha_entrega):
    ctx = {"skip_sms": True, "skip_backorder": True}
    picking_ids = odoo("sale.order", "read", [so_id], fields=["picking_ids"])[0]["picking_ids"]
    for pk in odoo("stock.picking", "read", picking_ids, fields=["state", "move_ids", "name"]):
        if pk["state"] in ("done", "cancel"):
            continue
        odoo("stock.picking", "action_assign", [pk["id"]])
        for mv in odoo("stock.move", "read", pk["move_ids"], fields=["product_uom_qty"]):
            odoo("stock.move", "write", [mv["id"]], {"quantity": mv["product_uom_qty"], "picked": True})
        res = odoo("stock.picking", "button_validate", [pk["id"]], contexto=ctx)
        if isinstance(res, dict) and res.get("res_model"):
            raise RuntimeError(f"La entrega {pk['name']} abrió el asistente {res['res_model']}: "
                               "falta existencia o hay una configuración que pide confirmación")
        odoo("stock.picking", "write", [pk["id"]], {"date_done": fecha_entrega, "scheduled_date": fecha_entrega})
        odoo("stock.move", "write", pk["move_ids"], {"date": fecha_entrega})
        lineas = odoo("stock.move.line", "search", [("move_id", "in", pk["move_ids"])])
        if lineas:
            odoo("stock.move.line", "write", lineas, {"date": fecha_entrega})


def facturar(odoo, so_id, fecha, pagada):
    ctx = {"active_model": "sale.order", "active_ids": [so_id], "active_id": so_id}
    asistente = odoo("sale.advance.payment.inv", "create", {"advance_payment_method": "delivered"}, contexto=ctx)
    odoo("sale.advance.payment.inv", "create_invoices", [asistente], contexto=ctx)
    facturas = odoo("sale.order", "read", [so_id], fields=["invoice_ids"])[0]["invoice_ids"]
    if not facturas:
        raise RuntimeError("No se creó la factura (¿la política de facturación es «cantidades entregadas»?)")
    fid = facturas[-1]
    odoo("account.move", "write", [fid], {"invoice_date": fecha, "date": fecha})
    odoo("account.move", "action_post", [fid])
    if pagada:
        ctx = {"active_model": "account.move", "active_ids": [fid], "active_id": fid}
        pago = odoo("account.payment.register", "create", {"payment_date": fecha}, contexto=ctx)
        odoo("account.payment.register", "action_create_payments", [pago], contexto=ctx)
    return fid


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", required=True)
    ap.add_argument("--url", default="http://localhost:8069")
    ap.add_argument("--db", default="rutamoto")
    ap.add_argument("--usuario", default="admin@rutamoto.gt")
    ap.add_argument("--probar", action="store_true", help="solo lee y valida; no escribe nada")
    a = ap.parse_args()

    plan = json.load(open(a.json, encoding="utf-8"))
    clave = os.environ.get("ODOO_CLAVE") or getpass.getpass(f"Contraseña de {a.usuario}: ")
    odoo = conectar(a.url, a.db, a.usuario, clave)

    clientes, productos, problemas = resolver(odoo, plan)
    hechos = existentes(odoo)
    pendientes = [p for p in plan["pedidos"] if p["ref"] not in hechos]
    # existencias: solo cuenta lo que falta cargar
    requeridas = {}
    for p in pendientes:
        for l in p["lineas"]:
            requeridas[l["producto"]] = requeridas.get(l["producto"], 0) + l["cantidad"]
    for ref, q in sorted(requeridas.items()):
        disp = productos.get(ref, {}).get("qty_available", 0)
        if disp < q + 1:
            problemas.append(f"Producto {ref}: hay {disp:g}, la historia saca {q} y tiene que quedar al menos 1")
    incompletos = [r for r, f in hechos.items() if f["state"] != "sale" or f["invoice_status"] != "invoiced"]
    for r in incompletos:
        problemas.append(f"{r} ya existe pero quedó a medias (estado {hechos[r]['state']}, "
                         f"facturación {hechos[r]['invoice_status']}): terminarlo o cancelarlo a mano")

    print(f"Plan: {len(plan['pedidos'])} pedidos · ya cargados: {len(hechos)} · por cargar: {len(pendientes)}")
    if problemas:
        print("\nPROBLEMAS (no se escribió nada):")
        for x in problemas:
            print("  -", x)
        sys.exit(1)
    print("Validación limpia: clientes, productos y existencias alcanzan.")
    if a.probar:
        return

    equipo = odoo("crm.team", "search", [("name", "=", plan["equipo_ventas"])])
    equipo = equipo[0] if equipo else odoo("crm.team", "create", {"name": plan["equipo_ventas"]})

    for i, p in enumerate(pendientes, 1):
        paso = "crear"
        try:
            so_id = odoo("sale.order", "create", {
                "partner_id": clientes[p["cliente"]],
                "team_id": equipo,
                "client_order_ref": p["ref"],
                "order_line": [(0, 0, {"product_id": productos[l["producto"]]["id"],
                                       "product_uom_qty": l["cantidad"]}) for l in p["lineas"]],
            })
            paso = "confirmar"
            odoo("sale.order", "action_confirm", [so_id])
            paso = "entregar"
            validar_entregas(odoo, so_id, p["entrega_utc"])
            paso = "facturar"
            facturar(odoo, so_id, p["entrega_utc"][:10], p["pagada"])
            paso = "fechar"
            # al confirmar, Odoo pone la fecha de hoy: se reescribe con la del plan
            odoo("sale.order", "write", [so_id], {"date_order": p["fecha_utc"]})
        except Exception as e:  # noqa: BLE001 - se informa y se detiene
            sys.exit(f"\nERROR en {p['ref']} ({p['cliente']}), paso «{paso}»: {e}\n"
                     "Lo anterior quedó cargado. Corregí la causa y volvé a correr: los completos se saltan.")
        nombre = odoo("sale.order", "read", [so_id], fields=["name"])[0]["name"]
        print(f"[{i:2}/{len(pendientes)}] {p['ref']} -> {nombre} · {p['cliente']} · {p['fecha_utc'][:10]}"
              f"{'' if p['pagada'] else ' · factura pendiente'}")
    print("\nListo. Revisá Ventas › Informes › Ventas agrupado por fecha (día) y Inventario › Existencias.")


if __name__ == "__main__":
    main()
