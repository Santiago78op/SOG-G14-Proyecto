<#
    RutaMoto - Fase 2 - Carga masiva y ciclo de compras
    Capturas de la interfaz web de Odoo para el manual MU-01 y el informe.

    Abre cada vista de Odoo en Chrome y fotografia la ventana con PrintWindow,
    que funciona aunque la ventana este detras de otras. Podes seguir usando la
    computadora mientras corre.

    Antes de correrlo:
      1. Los contenedores arriba (09_reanudar.ps1).
      2. Sesion iniciada en Odoo en Chrome con admin@rutamoto.gt.
      3. Cerra las demas ventanas de Chrome: si hay varias, guarda una copia
         por ventana y despues hay que escoger.

    Uso:  powershell -ExecutionPolicy Bypass -File .\11_capturas_fase2.ps1
#>

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Add-Type -AssemblyName System.Drawing

Add-Type @"
using System;
using System.Drawing;
using System.Runtime.InteropServices;
public class Ventana2 {
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
            PrintWindow(h, hdc, 2);   // 2 = PW_RENDERFULLCONTENT
            g.ReleaseHdc(hdc);
        }
        return bmp;
    }
}
"@ -ReferencedAssemblies System.Drawing

$Base   = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Raiz   = Split-Path -Parent $Base
$CapDir = Join-Path $Raiz 'capturas_fase2'
New-Item -ItemType Directory -Force -Path $CapDir | Out-Null

$rutasChrome = @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)
$exe = $rutasChrome | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $exe) { Write-Host "No se encontro Chrome." -ForegroundColor Red; exit 1 }

try { $r = Invoke-WebRequest -Uri 'http://localhost:8069/web/login' -UseBasicParsing -TimeoutSec 8 }
catch { Write-Host "Odoo no responde en el puerto 8069. Corre primero 09_reanudar.ps1" -ForegroundColor Red; exit 1 }

function VentanasChrome {
    Get-Process chrome -ErrorAction SilentlyContinue |
        Where-Object { $_.MainWindowHandle -ne 0 -and [Ventana2]::IsWindowVisible($_.MainWindowHandle) }
}

function CapturarVentanas([string]$nombre) {
    $vs = @(VentanasChrome)
    if ($vs.Count -eq 0) { Write-Host "   sin ventanas de Chrome visibles" -ForegroundColor Red; return }
    $i = 0
    foreach ($v in $vs) {
        $i++
        [void][Ventana2]::ShowWindow($v.MainWindowHandle, 3)   # maximizar, sin robar el foco
        Start-Sleep -Milliseconds 800
        $bmp = [Ventana2]::Capturar($v.MainWindowHandle)
        if ($bmp -eq $null) { continue }
        $sufijo = if ($vs.Count -gt 1) { "_v$i" } else { "" }
        $ruta = Join-Path $CapDir "$nombre$sufijo.png"
        $bmp.Save($ruta, [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Dispose()
        Write-Host ("   guardada: {0}{1}.png" -f $nombre, $sufijo) -ForegroundColor Green
    }
}

$Odoo = 'http://localhost:8069'
function Vista([string]$nombre, [string]$ruta, [int]$espera = 9) {
    Write-Host ""
    Write-Host ("-> {0}" -f $nombre) -ForegroundColor Cyan
    Start-Process $exe -ArgumentList ($Odoo + $ruta) | Out-Null
    Start-Sleep -Seconds $espera
    CapturarVentanas $nombre
}

Write-Host ""
Write-Host "  RUTAMOTO - FASE 2 - CAPTURAS DE LA CARGA Y LAS COMPRAS" -ForegroundColor Cyan
Write-Host "  Son 26 vistas. Tarda unos 5 minutos. No cierres Chrome." -ForegroundColor Yellow
Write-Host ""

# --- Capitulo 1: preparacion -------------------------------------------------
Vista "01_gestor_bases"              "/web/database/manager" 8
Vista "02_usuarios"                  "/odoo/action-70"
Vista "03_categorias_producto"       "/odoo/action-181"
Vista "04_etiquetas_contacto"        "/odoo/action-59"
Vista "05_terminos_pago"             "/odoo/action-287"
Vista "06_ubicaciones"               "/odoo/action-395"

# --- Capitulo 2: productos ---------------------------------------------------
Vista "10_productos_por_categoria"   "/odoo/action-391" 12
Vista "11_ficha_lub001"              "/odoo/action-391/1" 11

# --- Capitulo 3: existencias -------------------------------------------------
Vista "12_existencias_por_ubicacion" "/odoo/action-351" 12

# --- Capitulo 4: reglas de reabastecimiento ----------------------------------
Vista "14_reglas_reabastecimiento"   "/odoo/action-399" 11
Vista "15_panel_reabastecimiento"    "/odoo/action-398" 11

# --- Capitulo 5: proveedores -------------------------------------------------
Vista "16_proveedores"               "/odoo/action-56" 11
Vista "17_ficha_proveedor_icr"       "/odoo/action-56/54" 11
Vista "18_listas_precio_proveedor"   "/odoo/action-186" 11
Vista "19_pestana_compra_lub004"     "/odoo/action-391/33" 11

# --- Capitulo 6: clientes ----------------------------------------------------
Vista "20_clientes_por_segmento"     "/odoo/action-477" 12

# --- Capitulo 7: productos adicionales ---------------------------------------
Vista "21_ficha_lub007"              "/odoo/action-391/60" 11
Vista "22_ficha_ele007"              "/odoo/action-391/61" 11

# --- Capitulo 8: requisicion y solicitud de cotizacion -----------------------
Vista "23_solicitud_p00001"          "/odoo/action-424/1" 11
Vista "24_solicitud_p00005_abierta"  "/odoo/action-424/5" 11

# --- Capitulo 9: orden de compra y recepcion ---------------------------------
Vista "25_orden_p00001_confirmada"   "/odoo/action-418/1" 11
Vista "26_recepcion_in00001"         "/odoo/action-361/4" 11
Vista "27_recepciones"               "/odoo/action-361" 11
Vista "28_historial_movimientos"     "/odoo/action-358" 12
Vista "29_lista_compras_5_estados"   "/odoo/action-418" 12
Vista "30_ficha_fre001_50_unidades"  "/odoo/action-391/36" 11

Write-Host ""
Write-Host ("=" * 70) -ForegroundColor Green
Write-Host ("  LISTO. Capturas en: {0}" -f $CapDir) -ForegroundColor Green
Write-Host "  Faltan 4 capturas que hay que tomar a mano: ver" -ForegroundColor Yellow
Write-Host "  entregables_fase2\GUIA_capturas_a_mano.md" -ForegroundColor Yellow
Write-Host ("=" * 70) -ForegroundColor Green
Write-Host ""
