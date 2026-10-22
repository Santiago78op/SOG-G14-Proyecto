# Mensajes listos para mandar

> Mandalos **hoy**, no el viernes. El de Alberto primero: sin la URL no hay nada que hacer.
> Cambiá lo que haga falta, pero no quites las horas límite.

## 1) Para Alberto (rol 3)

> Alberto, para arrancar mi parte hoy necesito confirmar 6 cosas. Si algo no está, decime qué
> falta y a qué hora lo vas a tener; no sigo hasta que esté.
>
> 1. **URL del túnel** y usuario/clave con el que entro (mi usuario, no `admin`).
> 2. ¿El **sitio** ya está publicado con los 38 productos, las 6 categorías y el registro gratuito?
> 3. ¿El **pago de prueba** y la **factura automática** ya funcionan? ¿Qué proveedor quedó?
> 4. ¿**P00004** ya está recibida? LLA-002 debería estar en 16.
> 5. ¿La **historia** ya se cargó? ¿La corriste con `--probar`? ¿Los 45 pedidos quedaron con
>    fechas del 05 al 20 y la venta en **Q 14,679.50**?
> 6. ¿**Mailpit** está arriba y el equipo del sitio quedó como «Website Sales»? ¿Los **márgenes**
>    están activos?
>
> Hoy a las **18:00** necesito la URL y la confirmación de 2, 3 y 5. Si no, mi BI no se puede
> capturar y el informe de Santiago se retrasa.

**Por qué:** la URL y el sitio son la llave; la historia y las fechas son la base del BI.
No es una lista de deseos: son las seis cosas que bloquean las capturas.

## 2) Para Jemima (rol 2)

> Jemima, para el BI final necesito dos cosas:
>
> 1. Cuando termines **WEB-12**, avisame por acá. Con ese aviso hago las capturas finales.
> 2. Antes de avisar, **validá las entregas** de todos tus pedidos (WEB-01 a 08, 10 y 12).
>    Si no se validan, el stock no baja y el BI no cuadra con la hoja `4_Cuadre`.
>
> Si podés, pasame la lista de números de pedido que te dio Odoo para cada WEB; me sirve para
> cruzar el reporte. Fecha límite: **viernes 23 a las 12:00**. Si no llegás, decime a qué hora;
> el informe se cierra el viernes a las 20:00.

**Por qué:** el BI final es lo último; si WEB-12 se corre al viernes en la noche, no queda
tiempo para el informe de Santiago. Y si las entregas no están validadas, la tabla de stock
bajo muestra 2 productos en vez de 4.

## 3) Para Santiago (rol 1)

> Santiago, estoy armando mis secciones **6.2 y 10** en un archivo aparte para no pisar el
> generador. Te las paso el **viernes a las 18:00** con las capturas; el **MU-06** va en su
> propio `.docx`.
>
> No corras `generar_documentos.py` sobre el MU-06 después de que lo empiece a llenar, o se
> borra. Si preferís que el texto vaya al generador, decime y lo hacemos en una rama para que
> hagas el merge. ¿Cuál te sirve más?

**Por qué:** el repo genera los Word con `generar_documentos.py`; si los dos editan el mismo
archivo, uno pisa al otro. Mejor acordarlo antes.

## 4) Mensaje corto para el grupo (opcional)

> Grupo: mi parte (6.2, 10 y MU-06) depende de tres cosas: URL + sitio + historia de Alberto
> hoy 18:00; WEB-12 y entregas validadas de Jemima viernes 12:00; y el informe de Santiago
> viernes 20:00. Si alguna se corre, aviso ese mismo día para que no se caiga el cierre.

## Si no contestan

- A las **18:30** de hoy, si Alberto no mandó la URL, escribile a Santiago: «no tengo acceso a
  la instancia; mi parte queda bloqueada». No esperes al sábado.
- Si Jemima no avisa a las **12:00** del viernes, preguntá en el grupo y avisá a Santiago.
- Guardá los mensajes: si algo falta, que quede claro que la dependencia era externa.
