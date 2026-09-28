# Guion de los videos demostrativos — Fase 1

Documento 4 de los cinco entregables. El enunciado pide *"videos alojados en Google Drive que evidencien el proceso de instalación y validación de los sistemas (ERP/CRM)"*.

Son **dos videos**, uno por rol, para que ninguno dependa del otro para grabar.

| Video | Quién graba | Carné | Duración objetivo |
|---|---|---|---|
| Instalación y validación del ERP (Odoo 18.0 Community + PostgreSQL 16) | Alberto Josué Hernández Armas — Rol 3 | 201903553 | 6 a 9 minutos |
| Instalación y validación del CRM (Odoo CRM) | Brayan Emanuel García — Rol 4 | 202300848 | 4 a 6 minutos |

> **Importante:** la instalación documentada en el informe y en el manual se hizo **con contenedores (Docker), no con el instalador de escritorio**. El guion sigue ese mismo procedimiento. Si el video muestra algo distinto de lo que dicen el manual y el informe, la incoherencia se nota en la evaluación técnica.

---

## Reglas para los dos

- **Grabá la pantalla, no la cara.** OBS Studio o Xbox Game Bar (`Win + G`) bastan; los dos son gratis y ya vienen o se instalan en un minuto.
- **Narrá mientras hacés.** Un video mudo no evidencia dominio, y el dominio es lo que se califica.
- **Una sola toma es suficiente.** No hace falta editar. Si te equivocás, explicá el error y cómo lo resolvés: eso suma, no resta.
- **Resolución mínima 1080p** y que el texto de la pantalla se lea. Si tenés la pantalla en 4K, bajá la resolución antes de grabar o no se va a leer nada. Subí el tamaño de fuente de la terminal antes de empezar.
- **Aparecé identificándote** al inicio: nombre, carné y qué vas a mostrar.
- **Subilo a la carpeta del grupo en Drive** y verificá el enlace **desde una sesión distinta** o en ventana de incógnito. Un enlace con permisos mal puestos es lo mismo que no entregar.
- Nombre del archivo: `Fase1_Video_ERP_Grupo14.mp4` y `Fase1_Video_CRM_Grupo14.mp4`.

---

## Video 1 — Instalación del ERP · Rol 3 (Alberto Josué Hernández Armas, 201903553)

Sigue los once pasos del apartado 1.2 del manual de instalación. Si podés, tené el manual abierto en otra ventana.

### 0:00 — Presentación
> "Buenas, soy Alberto Josué Hernández Armas, carné 201903553, del Grupo 14. En este video muestro la instalación y validación de Odoo 18.0 Community con PostgreSQL 16, el ERP que seleccionamos para el proyecto de RutaMoto, nuestra tienda en línea de repuestos para motocicleta."

### 0:30 — Requerimientos y por qué contenedores
Mostrá en pantalla, antes de ejecutar nada (paso 1 del manual):

- Las propiedades del sistema (`Win + Pausa`): Windows 11 de 64 bits, Ryzen 7 5700U, 15.3 GB de RAM.
- El espacio libre en disco.
- `docker --version`, `docker compose version` y `docker info`.

Explicá la decisión en una frase:

> "No usamos el instalador de escritorio. Todo el ambiente — servidor de aplicaciones, base de datos, red, puertos y volúmenes — queda descrito en un solo archivo, así que reproducirlo en el servidor de producción es un comando y no una secuencia de pasos que alguien tenga que recordar."

### 1:30 — El archivo docker-compose.yml
Abrí el archivo y recorrelo señalando tres cosas (paso 2):

1. El servicio `db` con **PostgreSQL 16** — señalalo explícitamente, porque el enunciado pide indicar el gestor de base de datos.
2. El `healthcheck` con `pg_isready` y el `depends_on: condition: service_healthy`. Contá que sin eso Odoo arrancaba antes que la base y el contenedor entraba en ciclo de reinicio: es el primer problema documentado en el manual.
3. Los **volúmenes con nombre**, y por qué los datos no pueden vivir dentro del contenedor.

### 2:30 — Descarga y arranque
Grabá sin cortar (pasos 3 y 4):

1. `docker compose pull` — mostrá el avance de las 25 capas.
2. `docker compose up -d`.
3. `docker compose ps` — señalá que la base aparece `Healthy` **antes** de que Odoo aparezca `Started`.

### 4:00 — Verificación del servicio
Pasos 5 y 6:

1. `docker exec rutamoto-db psql -U odoo -d postgres -c "SELECT version();"` → PostgreSQL 16.15.
2. `docker compose logs --tail=10 odoo` → versión 18.0-20260908.
3. `Invoke-WebRequest http://localhost:8069/...` → HTTP 200, y `netstat` con el puerto 8069 en escucha.

### 5:00 — Base de datos y usuario administrador
Pasos 7 y 8:

1. Abrir `localhost:8069` y crear la base `rutamoto`.
2. Idioma **Español de Guatemala** y país **Guatemala** — explicá que eso deja la moneda en quetzales de una vez.
3. Dejar **sin marcar** los datos de demostración, y decir por qué: la base tiene que quedar limpia para la carga de la Fase 2.
4. Crear `admin@rutamoto.gt` e iniciar sesión.

### 6:30 — Instalación de módulos
Paso 9. Instalá **Inventario, Ventas, Compras y Facturación**. Mientras lo hacés, explicá en una frase para qué sirve cada uno en RutaMoto:

> "Inventario porque necesitamos alertas de stock bajo: si no hay la pieza, el cliente se va al local de enfrente. Compras porque el ciclo de requisición a recepción es la operación normal del negocio. Ventas porque los talleres piden cotización antes de comprar. Facturación porque de ahí salen el ticket promedio y las ventas del trimestre que medimos."

### 7:30 — Validación
Pasos 10 y 11. Mostrá funcionando:

- La interfaz web con sesión iniciada y la compañía RutaMoto activa.
- Los cuatro módulos en el menú.
- Crear el producto `LUB-001 Aceite mineral 20W-50`, con precio Q 45.00 y costo Q 28.00.
- Aplicar el ajuste de inventario de 24 unidades en la Bodega Central RutaMoto.
- Que la existencia aparece tanto en Inventario como en la ficha del producto.

### 8:30 — Cierre
> "Con esto queda validada la instalación del ERP. El módulo CRM lo muestra Brayan Emanuel García en el segundo video, sobre esta misma instalación y sobre la misma base de datos."

---

## Video 2 — Instalación y validación del CRM · Rol 4 (Brayan Emanuel García, 202300848)

Sigue los cinco pasos del apartado 2.2 del manual.

### 0:00 — Presentación
> "Buenas, soy Brayan Emanuel García, carné 202300848, del Grupo 14. En este video muestro la instalación y validación de Odoo CRM para el proyecto de RutaMoto."

### 0:20 — Por qué este CRM
Antes de tocar nada, mostrá el cuadro comparativo del informe (tabla 14) y explicá la decisión en treinta segundos:

> "Comparamos Odoo CRM contra Zoho CRM y HubSpot CRM. Elegimos Odoo CRM porque comparte base de datos con el ERP, así que el cliente que se registra en la tienda queda disponible en Ventas sin construir una integración por API. Con el plazo que teníamos, esa integración era el riesgo más grande del proyecto."

### 1:00 — Verificación de la instancia
Paso 1. Mostrá que la instalación del video anterior sigue en pie:

- `docker compose ps` con los dos contenedores activos.
- `localhost:8069` respondiendo.

Explicá que el CRM **no necesita infraestructura nueva**: corre sobre los mismos contenedores.

### 1:45 — Instalación del módulo
Pasos 2, 3 y 4:

1. Entrar con `admin@rutamoto.gt` y verificar la compañía RutaMoto.
2. Ir a Aplicaciones y buscar CRM.
3. Activar.
4. Ver que aparece en el menú principal.

> Si te pasa que el módulo no aparece en el buscador, actualizá la lista de aplicaciones desde el modo desarrollador. Está documentado como incidencia en el apartado 2.4 del manual: mostralo, suma.

### 3:00 — Validación
Paso 5. Mostrá funcionando:

- El tablero Kanban del pipeline con las etapas Nuevo, Calificado, Propuesta y Ganado.
- Crear una oportunidad de prueba con uno de nuestros segmentos, por ejemplo un taller mecánico.
- Moverla de etapa arrastrándola.
- **Lo más importante:** que el cliente creado en el CRM aparece también en Ventas del ERP, y que en el gestor de bases de datos sigue habiendo **una sola base**, `rutamoto`. Esa es la evidencia de que comparten base y de que la integración de la Fase 3 es viable.

### 4:30 — Qué queda para la Fase 2
Decilo explícitamente, para que no parezca un olvido:

> "La configuración del servidor de correo saliente, las etapas comerciales propias de RutaMoto y los permisos del usuario comercial son tareas de la Fase 2. En esta fase el módulo queda instalado y validado; el correo depende del dominio rutamoto.gt, que todavía no está publicado."

### 5:00 — Cierre
> "Con esto quedan validados el ERP y el CRM sobre la misma instalación. En la Fase 2 se cargan los datos maestros y se configura la cadena de suministros."

---

## Antes de subir: lista de comprobación

- [ ] Se lee el texto de la pantalla y de la terminal sin forzar la vista.
- [ ] Se escucha la narración, sin ruido de fondo que tape la voz.
- [ ] Aparece el nombre y el carné de quien graba.
- [ ] Se ve la instalación **y** la validación, no solo una de las dos.
- [ ] Lo que se muestra coincide con el manual: contenedores, no instalador de escritorio.
- [ ] El archivo está en la carpeta del grupo en Drive.
- [ ] El enlace abre desde una ventana de incógnito.
- [ ] El enlace está pegado en el **Anexo** del informe, filas C y D.

---

## Un aviso honesto

El enunciado dice *"videos"* en plural y menciona *"los sistemas (ERP/CRM)"*, pero **no especifica si debe ser uno o dos**. Acá está planteado como dos porque permite que los roles 3 y 4 graben en paralelo. Si prefieren uno solo, se junta el contenido en el mismo orden y también cumple.
