# Mensajes listos para mandar (actualizado 23-10, 17:00)

> Alberto ya entregó el entorno en la nube. **No mandes el mensaje viejo de las 6 preguntas.**
> Ahora hay tres frentes: confirmar dos dudas de la instancia, apurar a Jemima y cerrar con
> Santiago. Mandalos ya, no a las 11 de la noche.

## 1) Para Alberto (rol 3): dos dudas de la instancia

> Alberto, ya estoy en la nube. Tres cosas puntuales:
>
> 1. El medio de pago quedó como **transferencia bancaria**. ¿El pago se confirma solo o lo tengo
>    que registrar a mano en la factura? Si hay un proveedor **Demo** en modo de prueba, ¿lo
>    activo para WEB-09/11 o dejo la transferencia y documento el paso manual?
> 2. Mailpit arranca vacío. ¿Los correos nuevos de la cotización y del portal sí llegan, o hay
>    que reiniciar algo?
> 3. Vi **5 pedidos de la Fase 2** además de la historia (la base tiene 50 por Q 16,794.50,
>    con IVA). ¿Los dejo fuera del BI o los explico en el informe? No los voy a borrar.
>
> Si la transferencia es manual, decime el paso exacto para marcar la factura pagada. Es lo que
> me falta para cerrar el flujo B.

**Por qué:** el `ESTADO_SITIO_Y_HISTORIA.md` dice transferencia bancaria, no Demo. Eso cambia el
paso “el cliente paga en el portal” y el estado de la factura. Mejor saberlo antes de capturar.

## 2) Para Jemima (rol 2): la ruta crítica de hoy

> Jemima, para que el BI quede completo necesito que **WEB-12 esté hecha hoy antes de las 21:00**
> y que **valides las entregas** de todos tus pedidos (WEB-01 a 08, 10 y 12). Si no se validan,
> el stock no baja y la tabla de stock bajo no cuadra.
>
> Pasame la lista de números de pedido que te dio Odoo para cada WEB, o al menos decime cuáles
> terminaste. Si no llegás a las 21:00, avisame a qué hora: capturo el BI con el corte que haya
> y lo declaro en el informe, pero el informe de Santiago se aprieta.
>
> Si ya hiciste alguno, decime cuáles para no duplicar.

**Por qué:** el BI final es lo último y el sábado es la entrega. No queda tiempo para esperar
hasta la noche.

## 3) Para Santiago (rol 1): horario de entrega

> Santiago, hoy te paso:
> - **21:00:** secciones **6.2 y 10** con las capturas y los números reales.
> - **23:00:** **MU-06** en su `.docx`, con las 13 figuras.
> - **Mañana 09:00:** ensayo de los 4 minutos.
>
> No corras `generar_documentos.py` sobre el MU-06 ni sobre el informe después de que empiece a
> llenarlos, o se borra. Si querés el texto en el generador, decime y lo hacemos en una rama.
>
> Ojo: el BI puede dar más de 56 pedidos porque hay 5 de la Fase 2. Lo voy a explicar en 10.5 y
> 10.7. No cierres las conclusiones hasta que te pase los números.

**Por qué:** el informe, el PDF y el ZIP necesitan tiempo. Si le pasas las secciones a las 23:00,
no puede armar el paquete a las 23:30.

## 4) Mensaje corto para el grupo

> Grupo: el entorno ya está en la nube. Mi parte queda así: WEB-09/11 hoy, BI después de WEB-12,
> secciones 6.2/10 a las 21:00 y MU-06 a las 23:00. Necesito que Jemima avise WEB-12 antes de las
> 21:00 y que valide sus entregas. Si algo se corre, aviso para que el cierre no se caiga.

## Si no contestan

- **18:30:** si Alberto no aclaró lo del pago, prueba con la transferencia y documenta el paso
  manual. No esperes.
- **19:00:** si Jemima no dio señales, preguntá en el grupo y avisá a Santiago. Si a las 21:00 no
  hay WEB-12, captura el BI con corte y declara “corte al 23-10, 21:00”.
- **21:00:** si Santiago no confirma que recibió las secciones, mandate igual el archivo y dejá
  constancia por el grupo.
- Guardá los mensajes: si algo falta, que quede claro que la dependencia era externa.
