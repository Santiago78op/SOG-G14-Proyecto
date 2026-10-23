<#
    RutaMoto - Fase 3 - Video 1: sitio web y configuracion
    Alberto Josue Hernandez Armas, carne 201903553

    Conduce la pantalla sola, con los tiempos del guion. Vos solo hablas.
    Duracion: 7 minutos y 30 segundos.

        (sin parametros)  corrida con los tiempos del guion
        -Manual           espera ENTER entre bloque y bloque

    Antes de grabar:
      1. Contenedores arriba y sesion iniciada en Odoo con admin@rutamoto.gt.
      2. Cerra las demas ventanas de Chrome.

    Uso:  powershell -ExecutionPolicy Bypass -File .\17_video_fase3.ps1
#>

param([switch]$Manual)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class VentV3 {
    [DllImport("kernel32.dll")] public static extern IntPtr GetConsoleWindow();
    [DllImport("user32.dll")]   public static extern bool SetForegroundWindow(IntPtr h);
    [DllImport("user32.dll")]   public static extern bool ShowWindow(IntPtr h, int n);
    [DllImport("user32.dll")]   public static extern bool BringWindowToTop(IntPtr h);
}
"@

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class ModoV3 {
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
try { [ModoV3]::SinQuickEdit() } catch { }

$ErrorActionPreference = 'Continue'

$exeChrome = @("$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
               "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
               "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe") |
             Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $exeChrome) { Write-Host "No se encontro Chrome." -ForegroundColor Red; exit 1 }

try { Invoke-WebRequest -Uri 'http://localhost:8069/web/login' -UseBasicParsing -TimeoutSec 8 | Out-Null }
catch { Write-Host "Odoo no responde en el puerto 8069. Corre primero 09_reanudar.ps1" -ForegroundColor Red; exit 1 }

$reloj = [System.Diagnostics.Stopwatch]::StartNew()
$primeraVentana = $true
$Odoo = 'http://localhost:8069'

function ConsolaAlFrente {
    $h = [VentV3]::GetConsoleWindow()
    if ($h -ne [IntPtr]::Zero) {
        [void][VentV3]::ShowWindow($h, 3)
        [void][VentV3]::BringWindowToTop($h)
        [void][VentV3]::SetForegroundWindow($h)
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

function AbrirEnChrome([string]$destino, [switch]$Incognito) {
    if ($Incognito) {
        Start-Process $exeChrome -ArgumentList '--incognito', $destino | Out-Null
        Start-Sleep -Seconds 3
    } elseif ($primeraVentana) {
        Start-Process $exeChrome -ArgumentList '--new-window', $destino | Out-Null
        $script:primeraVentana = $false
        Start-Sleep -Seconds 3
    } else {
        Start-Process $exeChrome -ArgumentList $destino | Out-Null
        Start-Sleep -Seconds 2
    }
    $v = Get-Process chrome -ErrorAction SilentlyContinue |
         Where-Object { $_.MainWindowHandle -ne 0 } | Select-Object -First 1
    if ($v) {
        [void][VentV3]::ShowWindow($v.MainWindowHandle, 3)
        [void][VentV3]::SetForegroundWindow($v.MainWindowHandle)
    }
}

function Vista([string]$ruta, [string]$queSeVe) {
    Write-Host ("          {0}" -f $queSeVe) -ForegroundColor Gray
    AbrirEnChrome ($Odoo + $ruta)
}

function Publica([string]$ruta, [string]$queSeVe) {
    Write-Host ("          {0}" -f $queSeVe) -ForegroundColor Gray
    AbrirEnChrome ($Odoo + $ruta) -Incognito
}

Clear-Host
ConsolaAlFrente

# --- 0:00  Presentacion ------------------------------------------------------
Write-Host ""
Write-Host ""
Write-Host "        SITIO WEB DE COMERCIO ELECTRONICO Y SU CONFIGURACION" -ForegroundColor Green
Write-Host ""
Write-Host "        Odoo Community 18 sobre PostgreSQL 16" -ForegroundColor Gray
Write-Host ""
Write-Host "        RutaMoto  |  Fase 3  |  Grupo 14" -ForegroundColor Gray
Write-Host "        Alberto Josue Hernandez Armas  |  Carne 201903553" -ForegroundColor Gray
Write-Host "        Sistemas Organizacionales y Gerenciales 1, Seccion A" -ForegroundColor Gray
Write-Host ""
EsperarHasta 30

# --- 0:30  El respaldo previo ------------------------------------------------
Bloque "El respaldo previo"
Vista "/web/database/manager" "el gestor de bases: de aqui salio rutamoto_2026-10-23_1440.zip"
EsperarHasta 60

# --- 1:00  Los modulos instalados --------------------------------------------
Bloque "Los modulos instalados"
Vista "/odoo/action-39/668" "ficha de Comercio electronico: dice Actualizar y Desinstalar, no Activar"
EsperarHasta 95
Vista "/odoo/action-39/497" "Margenes en ordenes de venta: sin el, el informe no muestra ganancia"
EsperarHasta 120

# --- 2:00  El catalogo publicado ---------------------------------------------
Bloque "El catalogo publicado"
Vista "/odoo/action-602" "las seis categorias de sitio que arman el menu de la tienda"
EsperarHasta 150
Vista "/odoo/action-611" "los 38 productos publicados, con su direccion, su precio y su existencia"
EsperarHasta 190

# --- 3:10  La tienda vista por un cliente ------------------------------------
Bloque "La tienda vista por un cliente"
Publica "/shop" "la tienda sin sesion: categorias, buscador, filtro de precio y las imagenes"
EsperarHasta 230
Publica "/shop/lub-001-aceite-mineral-20w-50-1-l-1" "LUB-001 a Q 45.00 con impuesto incluido y su existencia"
EsperarHasta 260

# --- 4:20  El registro de clientes -------------------------------------------
Bloque "El registro de clientes"
Publica "/web/signup" "registro libre: el contacto nace en la misma tabla de los 40 clientes"
EsperarHasta 285

# --- 4:45  Pago y facturacion ------------------------------------------------
Bloque "Pago y facturacion automatica"
Vista "/odoo/settings#website" "proceso de pago y la casilla de factura automatica"
EsperarHasta 320
Vista "/odoo/action-225" "transferencia bancaria, activada y publicada, con sus instrucciones"
EsperarHasta 345

# --- 5:45  La tarifa de talleres ---------------------------------------------
Bloque "La tarifa de talleres"
Vista "/odoo/action-184" "Talleres B2B al 10 %: el sitio lee la misma lista de precios que el ERP"
EsperarHasta 365

# --- 6:05  P00004 recibida ---------------------------------------------------
Bloque "P00004 recibida"
Vista "/odoo/action-361/7" "RMT/IN/00004 validada: LLA-002 pasa de 0 a 16 y vuelve a la tienda"
EsperarHasta 390

# --- 6:30  La historia cargada -----------------------------------------------
Bloque "La historia de ventas cargada"
Vista "/odoo/action-437" "45 pedidos del 5 al 20 de octubre: Q 14,679.50 con impuesto incluido"
EsperarHasta 425
Vista "/odoo/action-351" "existencias despues de la historia: ningun producto en quiebre"
EsperarHasta 450

# --- 7:30  Cierre ------------------------------------------------------------
ConsolaAlFrente
Write-Host ""
Write-Host "        LISTO" -ForegroundColor Green
Write-Host ""
Write-Host "        Sitio publicado sobre la base de la Fase 2, 38 productos," -ForegroundColor Gray
Write-Host "        registro libre, pago por transferencia, factura automatica" -ForegroundColor Gray
Write-Host "        y 45 pedidos de historia cargados sin un solo dato a mano." -ForegroundColor Gray
Write-Host ""
