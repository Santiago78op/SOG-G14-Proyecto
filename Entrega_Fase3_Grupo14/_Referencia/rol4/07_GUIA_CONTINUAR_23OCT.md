# Guía para continuar · viernes 23-10, 17:00

> La nube responde: Odoo, tienda y Mailpit dan 200. La historia está cargada y el sitio publicado.
> **No hay ningún pedido del sitio todavía** (ni WEB-01 ni WEB-09), no hay usuarios de portal y el
> medio de pago es transferencia. Quedan horas, no días: esto es un plan de cierre, no de
> perfección. Si la presentación es antes de las 10:00 del sábado, el corte real es **hoy a
> medianoche**; el ensayo se hace hoy a las 00:30, no el sábado.

## Lo que cambió y te obliga a ajustar

1. **Los precios son con IVA incluido.** La historia da **Q 14,679.50 con IVA** y **Q 13,106.67 sin
   IVA**. El informe de ventas de Odoo muestra **sin IVA** por omisión. En el BI hay que decir
   siempre cuál se usa; para comparar con el plan, usa **Total con IVA**.
2. **Ya hay 5 pedidos de la Fase 2** además de la historia. La base tiene **50 pedidos por
   Q 16,794.50**. El informe de ventas los va a incluir. **No los borres**: se explican en 10.5/10.7
   o se filtran por fecha, pero se dice.
3. **El medio de pago es transferencia bancaria**, no Demo. El cliente acepta en el portal y recibe
   instrucciones; el pago **no se confirma solo**. Hay que registrarlo a mano en la factura, o usar
   Demo si Alberto lo habilita. El manual y el video deben mostrar el paso real, no un “pago
   automático” que no existe.
4. **Al corte, Odoo reporta CAS-005 y ELE-002 bajo el mínimo**, no los cuatro del plan (CAS-005,
   ELE-002, FRE-004, LUB-001). Usa la tabla real y explica la diferencia; no fuerces el número.
5. **El top 5 de la historia sola** es LUB-001 (37), LUB-004 (13), ELE-007 (13), ELE-003 (10),
   FRE-001 (8). Con los pedidos del sitio cambia. El plan (45/21/13/12/11) es una proyección, no
   el resultado.
6. **El manual es obligatorio.** No es un extra: el enunciado exige manuales con capturas. Si el
   tiempo aprieta, se recorta el tablero o el margen, no el manual.

## Decisión de BI (tómala ahora)

**Recomendación:** analiza **todas las ventas confirmadas del período 05-10 al 23-10** y di la
composición: “45 de la historia + 5 de la Fase 2 + N del sitio”. Es lo honesto y lo que muestra la
operación. Compara con el plan como referencia, no como verdad.

- En el gráfico/pivote usa la medida **Total** (con IVA) para que cuadre con el plan. Si usas
  **Importe sin impuestos**, dilo y usa **Q 13,106.67** para la historia, no Q 14,679.50.
- Filtra el período **05-10-2026 a 23-10-2026**; así dejas fuera lo viejo, pero S00013 (07-10)
  entra. El script te lista los “otros pedidos”; decide con esa lista.
- No borres los 5 pedidos de la Fase 2. Si los excluyes, explica el filtro.

## Orden de ataque

### Ahora - 17:30 · Entrar y confirmar

- [ ] Entra a `http://54.167.23.144:8069` con **tu usuario** (`brayan@`), no `admin`.
- [ ] Abre la tienda: 38 productos, 6 categorías, registro libre.
- [ ] Mira el medio de pago: ¿transferencia o Demo? Si es transferencia, ten a mano el paso
  “Registrar pago” de la factura.
- [ ] Invita al portal a **Mónica** y a **Taller Hermanos Cutzal**:
  `Contactos › cliente › Acción › Conceder acceso al portal`. El correo llega a Mailpit; abre el
  enlace, define contraseña y prueba en incógnito.
- [ ] Corre el script (ver comandos abajo). Te va a decir: historia 45/Q 14,679.50 con IVA, 0
  pedidos del sitio, 5 “otros” de la Fase 2 y ELE-002 bajo el mínimo. Eso es lo esperado hoy.

### 17:30 - 19:00 · WEB-09 (Mónica)

- [ ] Formulario `Contáctanos` con CAS-005 ×1 y CAS-006 ×1.
- [ ] Lead en CRM, oportunidad, cotización por **Q 860 con IVA**.
- [ ] Correo en Mailpit, portal, aceptar, medio de pago.
- [ ] Pedido confirmado, entrega validada, factura pagada o pago registrado a mano.
- [ ] Captura cada paso con el checklist (figuras 1-6). Una toma por paso; no reconstruyas.

### 19:00 - 20:00 · WEB-11 (Taller Hermanos Cutzal)

- [ ] Mismo flujo, LUB-004 ×6 y LUB-007 ×3, **Q 364.50 con IVA** (tarifa B2B).
- [ ] Valida la entrega y revisa la factura.
- [ ] Si el portal o el correo fallan, anótalo como problema del capítulo 1; no lo escondas.

### 18:00 · Estado de Jemima

- [ ] Pregunta en el grupo: ¿WEB-01 a WEB-12 van a estar hoy? ¿A qué hora WEB-12? ¿Validas las
  entregas?
- [ ] Si a las 18:30 no hay respuesta, avisa a Santiago: “sin WEB-12 no hay BI final”.
- [ ] Si Jemima no llega, tu BI se captura con **corte** y se declara: “corte al 23-10, 21:00,
  N de 11 pedidos del sitio”. Si a las 19:00 no apareció, **no hagas los 9**: haz 2-3 pedidos
  representativos (un cliente nuevo, un taller, un producto con stock) y documenta el corte. El
  enunciado pide el flujo, no los 12 pedidos del plan.

### 20:00 - 21:00 · Mientras esperas WEB-12

- [ ] Pasa los textos del borrador al **MU-06** y inserta las capturas 1-6.
- [ ] Llena las tablas de validación con lo que ya tienes.
- [ ] Pasa 6.2 y 10 al borrador del informe; deja los números del BI en blanco hasta el corte.
- [ ] Avisa a Santiago que a las 22:00 le mandas las secciones; no lo dejes esperando.

### 21:00 · Corte del BI

- [ ] Corre el script otra vez. Mira: pedidos del sitio, “otros” pedidos, total con IVA, top 5,
  stock bajo.
- [ ] Si WEB-12 está: captura el BI final.
- [ ] Si no está: captura con lo que haya y declara el corte. No inventes los pedidos que faltan.

### 21:00 - 22:00 · Capturas del BI (primero lo obligatorio)

1. Barras por producto.
2. Pastel por categoría.
3. Tabla de stock bajo (la real: ELE-002, o lo que muestre).
4. Líneas por día, semana y mes (tres tomas).
5. Top 5 real.

Si sobra tiempo: margen por canal y tablero. Si no, se declaran como extra no incluido.

### 22:00 - 23:00 · Cerrar documentos

- [ ] Termina el **MU-06** con las 13 figuras (o 11 si recortaste extras).
- [ ] Termina **6.2 y 10** con los números reales y el filtro usado.
- [ ] Manda a Santiago: el `.docx` de secciones, el `.docx` del MU-06, la carpeta de capturas y
  una nota con: composición de pedidos, base de IVA, corte y qué faltó.
- [ ] Que Santiago confirme que lo recibió. Si no, mándalo igual y deja constancia.

### 23:00 - 00:00 · Video y diapositivas

- [ ] Graba el video de 8-10 min en una toma (o 5 min si el tiempo no da).
- [ ] Súbelo a Drive y pasa el enlace.
- [ ] Llena las diapositivas 6, 10 y 11 con las capturas y los números reales.

### Sábado 08:30 - 09:30

- [ ] Ensayo de los 4 minutos.
- [ ] Verifica que el paquete tenga MU-06, secciones 6.2/10 y video.
- [ ] Capturas de respaldo por si la nube falla en la presentación.

## Mínimo viable si no llegas

- **2 pedidos** (WEB-09 y WEB-11) con capturas. Si Jemima no llegó, agrega 2-3 pedidos del sitio
  para que el BI tenga más de un caso; no los 11.
- **5 reportes obligatorios** (barras, pastel, stock bajo, líneas día/semana/mes, top 5).
- **MU-06** con al menos 11 figuras.
- **6.2 y 10** con los números reales y el corte declarado.
- **Video** de una toma, aunque sea de 5 minutos.
- **Diapositivas** 6, 10 y 11.

Lo que **no** se recorta: el manual, la captura del lead/cotización/portal y el BI de inventario
y ventas.

## Comandos

```bash
export ODOO_CLAVE='...'          # no la escribas en el repo
python3 'Entrega_Fase3_Grupo14/_Referencia/rol4/05_VERIFICAR_BI.py' \
  --url 'http://54.167.23.144:8069' \
  --db rutamoto \
  --usuario 'brayan@rutamoto.gt'
```

El script es de solo lectura. Si dice **NO CAPTURAR**, revisa lo que marca; si dice **Listo para
capturar**, dale. El aviso de “otros pedidos” son los 5 de la Fase 2: no es un error, es una
decisión que tienes que explicar.

## Lo que no harías

- No vuelvas a `localhost`: la base buena es la nube.
- No uses `admin` para las capturas del portal.
- No borres los 5 pedidos de la Fase 2 ni los “otros” para que cuadre el plan.
- No fuerces el stock bajo a 4 ni el top 5 a los números del plan.
- No cambies a Shopify ni a otra plataforma a estas horas.
- No entregues el MU-06 sin capturas.

## Números de referencia rápida

| Dato | Valor real / leído de Odoo |
|---|---|
| Historia | 45 pedidos · Q 14,679.50 con IVA · Q 13,106.67 sin IVA · margen Q 3,781.67 |
| Base completa | 50 pedidos · Q 16,794.50 (45 historia + 5 Fase 2) |
| Pedidos del sitio | 0 al 23-10 17:00; se esperan 11 (sin WEB-07) |
| Bajo el mínimo | CAS-005 (1/2) y ELE-002 (12/30); el plan preveía 4 |
| Top 5 historia | LUB-001 37 · LUB-004 13 · ELE-007 13 · ELE-003 10 · FRE-001 8 |
| Productos | 38 de 38 publicados · 6 categorías · 0 en cero |
| Pago | transferencia bancaria; el pago se registra a mano |
| Portal | sin usuarios al 23-10; invitar a Mónica y Taller |
