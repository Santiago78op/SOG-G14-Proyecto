# Scripts de la instancia (Fase 2)

Son de PowerShell y corren en la máquina donde vive Odoo. No traen contraseñas.

| Script | Qué hace |
|---|---|
| `11_capturas_fase2.ps1` | Abre 26 vistas de Odoo en Chrome y fotografía la ventana. Deja las capturas en `capturas_fase2\` |
| `11b_capturas_extra.ps1` | Dos capturas más: informe de existencias y regla de reabastecimiento de FRE-001 |
| `12_video_fase2.ps1` | Conduce la pantalla con los tiempos del guion del video de carga y compras. Con `-Manual` avanza con ENTER |
| `13_tunel.ps1` | Instala `cloudflared` si falta y abre un túnel público hacia `localhost:8069`. La dirección es temporal |

Para que el acceso remoto funcione bien hay que tener `proxy_mode = True` en el `odoo.conf` de
la instancia y reiniciar el contenedor de Odoo una vez.

Los scripts asumen la estructura de carpetas del proyecto local de la instancia
(`odoo-docker\scripts`), no la del repositorio.
