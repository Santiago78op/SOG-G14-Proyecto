---
tags: [odoo, docker, ambiente, infraestructura]
aliases: [Odoo, Instancia, Túnel, Servidor de correo]
---

# Ambiente Odoo

## Lo instalado en la Fase 1 (documentado en el MU-00)

| Pieza | Valor |
|---|---|
| Máquina | Laptop del rol 3: Windows 11, Ryzen 7 5700U, 15.3 GB de RAM, Docker Desktop 28.3.2 |
| Contenedores | `rutamoto-odoo` (imagen `odoo:18.0`, build 18.0-20260908) y `rutamoto-db` (`postgres:16`, 16.15) |
| Puertos | 8069 y 8072 |
| Base | `rutamoto`, en español de Guatemala, **sin datos de demostración** |
| Administrador | `admin@rutamoto.gt` |
| Módulos | Inventario, Ventas, Compras, Facturación y CRM |
| Almacén | «Bodega Central RutaMoto», código corto **RMT**: su ubicación interna es `RMT/Existencias`, no `WH/Existencias` |

## Cómo se trabaja en la Fase 2

- **Una sola instancia.** Los demás entran por un túnel de Cloudflare. Está envuelto en el script `odoo-docker/scripts/13_tunel.ps1`, que instala `cloudflared` si falta y abre el túnel. La URL `*.trycloudflare.com` es temporal y cambia en cada reinicio: se pasa por el grupo. `proxy_mode = True` ya está puesto en `config/odoo.conf` (hace falta `docker compose restart odoo` para que tome efecto).
- **Un usuario interno por integrante**, ya creados: `santiago@rutamoto.gt`, `jemima@rutamoto.gt` y `brayan@rutamoto.gt`, con permisos de Inventario, Ventas, Compras, Facturación, Contactos y CRM. **Están sin contraseña**: las define el administrador desde Ajustes › Usuarios y las pasa por el grupo. El historial de cada registro muestra quién hizo qué, y eso es la evidencia de autoría en la evaluación técnica.
- **Respaldos** desde `/web/database/manager`: antes de la carga, después de la carga y al cierre. Todos a Drive.
- **Plan B**, si el túnel falla: relevo de respaldos en el orden 3 → 2 → 4. Solo trabaja uno a la vez.
- **En la demo en vivo se usa `localhost`**, no el túnel, con un respaldo restaurado en una segunda laptop por si la primera falla.

## Servidor de correo (rol 4)

| Opción | Cómo | A favor | En contra |
|---|---|---|---|
| **A · Mailpit** (recomendada) | servicio `axllent/mailpit` en el compose; puertos 8025 (web) y 1025 (SMTP). En Odoo: host `mailpit`, puerto 1025, sin seguridad | captura todos los correos y los muestra renderizados, sin credenciales | no llega a buzones reales |
| B · Gmail del grupo | contraseña de aplicación | se ven en un buzón real | los `@example.com` rebotan: hay que agregar contactos de prueba con los correos del equipo |

## Punto único de falla

Todo vive en una laptop, igual que en la Fase 1. Si esa laptop no está encendida y con el túnel abierto, nadie trabaja. Es un riesgo **abierto**, no resuelto.

## Scripts del proyecto (carpeta `odoo-docker/scripts`)

| Script | Para qué |
|---|---|
| `09_reanudar.ps1` | Levanta los contenedores y abre Odoo |
| `08_detener.ps1` | Respalda y baja los contenedores sin borrar datos |
| `02_respaldo.ps1` | Respaldo en zip más volcado SQL |
| `11_capturas_fase2.ps1` | 26 capturas de la carga y las compras, para el manual |
| `11b_capturas_extra.ps1` | Dos capturas más (informe de existencias y regla de FRE-001) |
| `12_video_fase2.ps1` | Conduce la pantalla con los tiempos del guion del video |
| `13_tunel.ps1` | Abre el túnel público hacia la instancia |

Relacionado: [[Decisiones y límites]] · [[Reparto y calendario Fase 2]]
