<#
    RutaMoto - Fase 2 - Video: cadena de suministros, carga y compras
    Alberto Josue Hernandez Armas, carne 201903553

    Conduce la pantalla sola, con los tiempos del guion
    (entregables_fase2\guion_video_carga_y_compras.md). Vos solo hablas.

        (sin parametros)  corrida con los tiempos del guion
        -Manual           espera ENTER entre bloque y bloque
        -SinExcel         no abre el archivo de datos maestros

    Uso:  powershell -ExecutionPolicy Bypass -File .\12_video_fase2.ps1
#>

param([switch]$Manual, [switch]$SinExcel)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class VentV2 {
    [DllImport("kernel32.dll")] public static extern IntPtr GetConsoleWindow();
    [DllImport("user32.dll")]   public static extern bool SetForegroundWindow(IntPtr h);
    [DllImport("user32.dll")]   public static extern bool ShowWindow(IntPtr h, int n);
    [DllImport("user32.dll")]   public static extern bool BringWindowToTop(IntPtr h);
}
"@

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class ModoV2 {
    [DllImport("kernel32.dll")] public static extern IntPtr GetStdHandle(int n);
    [DllImport("kernel32.dll")] public static extern bool GetConsoleMode(IntPtr h, out uint m);
    [DllImport("kernel32.dll")] public static extern bool SetConsoleMode(IntPtr h, uint m);
    public static void SinQuickEdit() {
        IntPtr h = GetStdHandle(-10);
        uint m; if (!GetConsoleMode(h, out m)) return;
        m &= ~((uint)0x0040); m |= ((uint)0x0080);
        SetConsoleMode(h, m);
    }
}
"@
try { [ModoV2]::SinQuickEdit() } catch { }

$ErrorActionPreference = 'Continue'
$Base = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Raiz = Split-Path -Parent $Base
$CapDir = Join-Path $Raiz 'capturas_fase2'
$Excel = Join-Path $Raiz 'repositorio_grupo\SOG-G14-Proyecto\Entrega_Fase2_Grupo14\3_Archivos_Datos\RutaMoto_datos_maestros_Fase2.xlsx'

$exeChrome = @("$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
               "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
               "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe") |
             Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $exeChrome) { Write-Host "No se encontro Chrome." -ForegroundColor Red; exit 1 }

try { Invoke-WebRequest -Uri 'http://localhost:8069/web/login' -UseBasicParsing -TimeoutSec 8 | Out-Null }
catch { Write-Host "Odoo no responde. Corre primero 09_reanudar.ps1" -ForegroundColor Red; exit 1 }

$reloj = [System.Diagnostics.Stopwatch]::StartNew()
$primeraVentana = $true
$Odoo = 'http://localhost:8069'

function ConsolaAlFrente {
    $h = [VentV2]::GetConsoleWindow()
    if ($h -ne [IntPtr]::Zero) {
        [void][VentV2]::ShowWindow($h, 3)
        [void][VentV2]::BringWindowToTop($h)
        [void][VentV2]::SetForegroundWindow($h)
    }
}

function Reloj { '{0:mm\:ss}' -f [TimeSpan]::FromSeconds($reloj.Elapsed.TotalSeconds) }

function EsperarHasta([int]$segundos) {
    if ($Manual) {
        Write-Host ""
        Write-Host "   [ ENTER para el siguiente bloque ]" -ForegroundColor DarkGray
        [void](Read-Host)
        return
    }
    while ($reloj.Elapsed.TotalSeconds -lt $segundos) { Start-Sleep -Milliseconds 250 }
}

function Bloque([string]$titulo) {
    Write-Host ""
    Write-Host ("  [{0}]  {1}" -f (Reloj), $titulo) -ForegroundColor Cyan
}

function Vista([string]$ruta, [string]$queSeVe) {
    Write-Host ("          {0}" -f $queSeVe) -ForegroundColor Gray
    $url = $Odoo + $ruta
    if ($primeraVentana) {
        Start-Process $exeChrome -ArgumentList '--new-window', $url | Out-Null
        $script:primeraVentana = $false
        Start-Sleep -Seconds 3
    } else {
        Start-Process $exeChrome -ArgumentList $url | Out-Null
        Start-Sleep -Seconds 2
    }
    $v = Get-Process chrome -ErrorAction SilentlyContinue |
         Where-Object { $_.MainWindowHandle -ne 0 } | Select-Object -First 1
    if ($v) {
        [void][VentV2]::ShowWindow($v.MainWindowHandle, 3)
        [void][VentV2]::SetForegroundWindow($v.MainWindowHandle)
    }
}

function Imagen([string]$archivo, [string]$queSeVe) {
    Write-Host ("          {0}" -f $queSeVe) -ForegroundColor Gray
    $ruta = Join-Path $CapDir $archivo
    if (-not (Test-Path $ruta)) {
        Write-Host ("          NO SE ENCONTRO {0}" -f $ruta) -ForegroundColor Red
        return
    }
    $url = 'file:///' + ($ruta -replace '\\','/')
    if ($primeraVentana) {
        Start-Process $exeChrome -ArgumentList '--new-window', $url | Out-Null
        $script:primeraVentana = $false
        Start-Sleep -Seconds 3
    } else {
        Start-Process $exeChrome -ArgumentList $url | Out-Null
        Start-Sleep -Seconds 2
    }
    $v = Get-Process chrome -ErrorAction SilentlyContinue |
         Where-Object { $_.MainWindowHandle -ne 0 } | Select-Object -First 1
    if ($v) {
        [void][VentV2]::ShowWindow($v.MainWindowHandle, 3)
        [void][VentV2]::SetForegroundWindow($v.MainWindowHandle)
    }
}

Clear-Host
ConsolaAlFrente

# --- 0:00  Presentacion ------------------------------------------------------
Write-Host ""
Write-Host ""
Write-Host "        CADENA DE SUMINISTROS: CARGA DE DATOS Y CICLO DE COMPRAS" -ForegroundColor Green
Write-Host ""
Write-Host "        Odoo Community 18 sobre PostgreSQL 16" -ForegroundColor Gray
Write-Host ""
Write-Host "        RutaMoto  |  Fase 2  |  Grupo 14" -ForegroundColor Gray
Write-Host "        Alberto Josue Hernandez Armas  |  Carne 201903553" -ForegroundColor Gray
Write-Host "        Sistemas Organizacionales y Gerenciales 1, Seccion A" -ForegroundColor Gray
Write-Host ""
EsperarHasta 30

# --- 0:30  El archivo de datos maestros --------------------------------------
Bloque "El archivo de datos maestros"
if (-not $SinExcel -and (Test-Path $Excel)) {
    Write-Host "          abriendo el Excel: hojas, columnas azules y hoja Cuadre" -ForegroundColor Gray
    Start-Process $Excel | Out-Null
} else {
    Write-Host "          mostra el Excel (hojas, columnas azules y hoja Cuadre)" -ForegroundColor Yellow
}
EsperarHasta 90

# --- 1:30  Lo que se prepara antes de importar -------------------------------
Bloque "Preparacion previa"
Vista "/odoo/action-181" "categorias de producto, sin categoria padre"
EsperarHasta 110
Vista "/odoo/action-59"  "etiquetas de contacto: los cuatro segmentos"
EsperarHasta 128
Vista "/odoo/action-287" "terminos de pago, con el de 50 y 50"
EsperarHasta 150

# --- 2:30  La importacion y la validacion previa -----------------------------
Bloque "El asistente de importacion y la validacion previa"
Imagen "07_import_subir_archivo.png" "el importador con el archivo, la hoja y el mapeo de columnas"
EsperarHasta 180
Imagen "08_import_error_ubicacion.png" "la prueba detiene la importacion: WH/Existencias no existe aqui"
EsperarHasta 210

# --- 3:30  El resultado de la carga ------------------------------------------
Bloque "Resultado de la carga"
Vista "/odoo/action-391"   "catalogo agrupado por categoria, con imagenes"
EsperarHasta 240
Vista "/odoo/action-391/1" "ficha de LUB-001: referencia, precio, costo, inventario"
EsperarHasta 258
Vista "/odoo/action-351"   "existencias por ubicacion y total al costo: Q 38,096"
EsperarHasta 270

# --- 4:30  Proveedores y clientes --------------------------------------------
Bloque "Proveedores y clientes"
Vista "/odoo/action-56"     "los cinco proveedores con su plazo de pago"
EsperarHasta 288
Vista "/odoo/action-56/54"  "ficha del proveedor con su contacto hijo"
EsperarHasta 300
Vista "/odoo/action-391/33" "pestana Compra de LUB-004: proveedor, costo y plazo"
EsperarHasta 312
Vista "/odoo/action-477"    "35 clientes agrupados por segmento: 12, 11, 7 y 5"
EsperarHasta 315

# --- 5:15  La requisicion: la alerta de reabastecimiento ---------------------
Bloque "La requisicion: la alerta de reabastecimiento"
Vista "/odoo/action-399" "las reglas de minimo y maximo importadas"
EsperarHasta 345
Vista "/odoo/action-398" "pantalla de reabastecimiento: de aqui sale Ordenar una vez"
EsperarHasta 375

# --- 6:15  De la solicitud a la orden ----------------------------------------
Bloque "De la solicitud de cotizacion a la orden de compra"
Vista "/odoo/action-424/1" "P00001: 44 unidades a Q 55, Q 2,420 en total"
EsperarHasta 400
Vista "/odoo/action-418/1" "la misma orden confirmada, con el boton de Recepcion"
EsperarHasta 420

# --- 7:00  La recepcion y el efecto en el inventario -------------------------
Bloque "La recepcion y el efecto en el inventario"
Vista "/odoo/action-361/4" "recepcion RMT/IN/00001 validada, estado Hecho"
EsperarHasta 440
Vista "/odoo/action-391/36" "FRE-001 ahora en 50 unidades"
EsperarHasta 455
Vista "/odoo/action-358" "historial: entrada de proveedores a RMT/Existencias"
EsperarHasta 465

# --- 7:45  Productos adicionales y las cinco compras -------------------------
Bloque "Productos adicionales y las cinco compras"
Vista "/odoo/action-391/60" "LUB-007, creado desde el sistema"
EsperarHasta 485
Vista "/odoo/action-391/61" "ELE-007, creado desde el sistema"
EsperarHasta 500
Vista "/odoo/action-418" "las cinco compras: 3 recibidas, 1 por recibir, 1 enviada"
EsperarHasta 525

# --- 8:45  Cierre ------------------------------------------------------------
ConsolaAlFrente
Bloque "Cierre"
Write-Host ""
Write-Host "        32 productos  |  5 proveedores  |  35 clientes segmentados" -ForegroundColor Green
Write-Host "        Inventario al costo: Q 38,096 tras la carga, Q 43,456 tras las compras" -ForegroundColor Green
Write-Host "        Ciclo de compras demostrado: alerta, solicitud, orden y recepcion" -ForegroundColor Green
Write-Host ""
EsperarHasta 555
Write-Host ""
Write-Host "   Fin del recorrido. Deja de grabar." -ForegroundColor Cyan
Write-Host ""
