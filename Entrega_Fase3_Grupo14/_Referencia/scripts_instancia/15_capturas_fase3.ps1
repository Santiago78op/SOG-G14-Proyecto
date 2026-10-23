<#
    RutaMoto - Fase 3 - Capturas del sitio y de su configuracion, para el manual MU-04.

    Mismo mecanismo que el de la Fase 2: abre cada vista en Chrome y fotografia la ventana
    con PrintWindow. Las paginas publicas se capturan en una ventana de incognito, para que
    se vean como las ve un cliente y no con la barra de edicion del administrador.

    Antes de correrlo:
      1. Contenedores arriba y sesion iniciada en Odoo con admin@rutamoto.gt.
      2. Cerra las demas ventanas de Chrome.

    Uso:  powershell -ExecutionPolicy Bypass -File .\15_capturas_fase3.ps1
#>

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Add-Type -AssemblyName System.Drawing

Add-Type @"
using System;
using System.Drawing;
using System.Runtime.InteropServices;
public class Ventana4 {
    [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr hWnd, IntPtr hdcBlt, uint nFlags);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hWnd, out RECT lpRect);
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
    [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr hWnd);
    [StructLayout(LayoutKind.Sequential)] public struct RECT { public int Left, Top, Right, Bottom; }
    public static Bitmap Capturar(IntPtr h) {
        RECT r; GetWindowRect(h, out r);
        int w = r.Right - r.Left, alto = r.Bottom - r.Top;
        if (w <= 0 || alto <= 0) return null;
        Bitmap bmp = new Bitmap(w, alto, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
        using (Graphics g = Graphics.FromImage(bmp)) {
            IntPtr hdc = g.GetHdc();
            PrintWindow(h, hdc, 2);
            g.ReleaseHdc(hdc);
        }
        return bmp;
    }
}
"@ -ReferencedAssemblies System.Drawing

$Base   = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Raiz   = Split-Path -Parent $Base
$CapDir = Join-Path $Raiz 'capturas_fase3'
New-Item -ItemType Directory -Force -Path $CapDir | Out-Null

$exe = @("$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
         "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
         "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe") |
       Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $exe) { Write-Host "No se encontro Chrome." -ForegroundColor Red; exit 1 }

try { Invoke-WebRequest -Uri 'http://localhost:8069/web/login' -UseBasicParsing -TimeoutSec 8 | Out-Null }
catch { Write-Host "Odoo no responde en el puerto 8069." -ForegroundColor Red; exit 1 }

function CapturarVentanas([string]$nombre) {
    $vs = @(Get-Process chrome -ErrorAction SilentlyContinue |
            Where-Object { $_.MainWindowHandle -ne 0 -and [Ventana4]::IsWindowVisible($_.MainWindowHandle) })
    if ($vs.Count -eq 0) { Write-Host "   sin ventanas de Chrome visibles" -ForegroundColor Red; return }
    $i = 0
    foreach ($v in $vs) {
        $i++
        [void][Ventana4]::ShowWindow($v.MainWindowHandle, 3)
        Start-Sleep -Milliseconds 900
        $bmp = [Ventana4]::Capturar($v.MainWindowHandle)
        if ($bmp -eq $null) { continue }
        $sufijo = if ($vs.Count -gt 1) { "_v$i" } else { "" }
        $bmp.Save((Join-Path $CapDir "$nombre$sufijo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Dispose()
        Write-Host ("   guardada: {0}{1}.png" -f $nombre, $sufijo) -ForegroundColor Green
    }
}

$Odoo = 'http://localhost:8069'
function Vista([string]$nombre, [string]$ruta, [int]$espera = 11) {
    Write-Host ""
    Write-Host ("-> {0}" -f $nombre) -ForegroundColor Cyan
    Start-Process $exe -ArgumentList ($Odoo + $ruta) | Out-Null
    Start-Sleep -Seconds $espera
    CapturarVentanas $nombre
}

Write-Host ""
Write-Host "  RUTAMOTO - FASE 3 - CAPTURAS DEL SITIO Y SU CONFIGURACION" -ForegroundColor Cyan
Write-Host "  Son 15 vistas. Tarda unos 4 minutos. No cierres Chrome." -ForegroundColor Yellow
Write-Host ""

# --- Capitulo 1: instalacion -------------------------------------------------
Vista "f01_gestor_bases"            "/web/database/manager" 8
Vista "f02_apps_ecommerce"          "/odoo/apps" 13
Vista "f03_ajustes_ventas_margenes" "/odoo/settings#sales" 13

# --- Capitulo 2: catalogo ----------------------------------------------------
Vista "f04_categorias_ecommerce"    "/odoo/action-602"
Vista "f05_productos_publicados"    "/odoo/action-611" 13
Vista "f06_ficha_lla002"            "/odoo/action-391/43" 12

# --- Capitulo 3: clientes, pago y facturacion --------------------------------
Vista "f09_proveedores_pago"        "/odoo/action-225" 12
Vista "f10_ajustes_sitio"           "/odoo/settings#website" 13
Vista "f11_tarifas"                 "/odoo/action-184" 11

# --- Capitulo 4: recepcion e historia ----------------------------------------
Vista "f12_recepcion_p00004"        "/odoo/action-361/7" 12
Vista "f13_informe_ventas"          "/odoo/action-437" 14
Vista "f14_existencias"             "/odoo/action-351" 13

# --- Paginas publicas, en incognito ------------------------------------------
Write-Host ""
Write-Host "-> paginas publicas (ventana de incognito)" -ForegroundColor Cyan
Start-Process $exe -ArgumentList '--incognito', ($Odoo + '/shop') | Out-Null
Start-Sleep -Seconds 14
CapturarVentanas "f07_tienda"

Start-Process $exe -ArgumentList '--incognito', ($Odoo + '/shop/lub-001-aceite-mineral-20w-50-1-l-1') | Out-Null
Start-Sleep -Seconds 12
CapturarVentanas "f08_producto_en_la_tienda"

Start-Process $exe -ArgumentList '--incognito', ($Odoo + '/web/signup') | Out-Null
Start-Sleep -Seconds 11
CapturarVentanas "f15_registro_cliente"

Write-Host ""
Write-Host ("=" * 70) -ForegroundColor Green
Write-Host ("  LISTO. Capturas en: {0}" -f $CapDir) -ForegroundColor Green
Write-Host "  Podes cerrar la ventana de incognito." -ForegroundColor Green
Write-Host ("=" * 70) -ForegroundColor Green
Write-Host ""
