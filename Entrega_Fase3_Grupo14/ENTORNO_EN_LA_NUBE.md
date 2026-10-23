# El entorno ya no está en una laptop: está en la nube

Fase 3, Grupo 14. Al 23-10-2026.

La instancia que usábamos corría en la máquina de Alberto, así que el sábado no habría estado disponible.
Se movió completa a un servidor de Amazon Web Services. **A partir de ahora se trabaja ahí y solo ahí.**

## Direcciones

| Qué | Dónde |
|---|---|
| Odoo | http://54.167.23.144:8069 |
| Tienda | http://54.167.23.144:8069/shop |
| Mailpit, la bandeja de correo de prueba | http://54.167.23.144:8025 |
| Base de datos | `rutamoto` |

Cada quien entra con su propio usuario: `santiago@`, `jemima@`, `brayan@` o `admin@rutamoto.gt`. Las contraseñas
son las mismas que se pasaron por el grupo; no van en este repositorio porque es público.

**Importante:** nadie siga trabajando contra `localhost`. Si alguien carga un pedido en su copia local, los
números del informe se parten en dos bases y no hay forma limpia de unirlas.

## Qué se movió

Todo. No se rehizo nada a mano: se restauró un respaldo completo de la base con su filestore, y después se
compararon 71 indicadores entre la instancia de origen y la nueva. Coinciden todos.

Entre lo comprobado: los 102 módulos instalados, los 38 productos publicados con sus imágenes, las 6 categorías
del sitio, los 50 pedidos por Q 16,794.50, los 45 de la historia simulada por Q 14,679.50, las 51 facturas
publicadas y 42 cobradas, los 5 pedidos de compra, las 54 transferencias de inventario, los 60 contactos, las 2
tarifas, el proveedor de pago publicado, el registro libre de clientes, la facturación automática y los 330
adjuntos con su tamaño exacto en bytes.

La versión de Odoo quedó fijada en `18.0-20260908`, la misma compilación que corría en la máquina de origen. El
`docker-compose` publicado aquí como `docker-compose_fase3.yml` es el que está en el servidor.

## Los tres servicios

| Contenedor | Imagen | Para qué |
|---|---|---|
| `rutamoto-odoo` | `odoo:18.0-20260908` | el ERP, el CRM y el sitio |
| `rutamoto-db` | `postgres:16` | la base |
| `rutamoto-mail` | `axllent/mailpit` | captura los correos que manda Odoo, para las campañas y las cotizaciones |

Odoo manda el correo a `mailpit:1025` y se lee en el 8025. Se comprobó que Odoo abre la conexión con Mailpit y
la acepta.

**La bandeja de Mailpit empieza vacía.** Nunca tuvo volumen, así que los correos de la campaña de la Fase 2 solo
existen en las capturas que ya están en el informe. Lo que se mande de ahora en adelante se captura normal.

## Operación

Los comandos se corren por SSH en el servidor, desde `~/geren1fase1proyecto/odoo-docker`:

```
sudo docker compose ps        # ver el estado
sudo docker compose up -d     # encender
sudo docker compose stop      # apagar
```

Los respaldos se guardan en `~/geren1fase1proyecto/respaldos`. El de cierre se hace cuando todos terminen de
escribir en la base, antes de armar el paquete de entrega.

Los scripts de migración y de comprobación viven en el servidor y en la máquina de Alberto, en
`odoo-docker/scripts`. No se publican aquí porque llevan la contraseña maestra.

## Lo que falta

- Los pedidos del sitio WEB-01 a WEB-12, que son los que llenan la última columna de la tabla de integración y
  el apartado de pruebas de flujo completo.
- Los reportes de inteligencia de negocios, después del aviso de WEB-12.
- El respaldo de cierre.
