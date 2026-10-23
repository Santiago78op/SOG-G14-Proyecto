<#
    RutaMoto - Fase 3 - Capturas de la trazabilidad de un pedido y de la historia cargada.

    Completa las que faltan para la seccion 6.3 del informe y para el MU-04:
      f16_pedido_s00013   el pedido de venta
      f17_entrega_s00013  la entrega que nacio de ese pedido
      f18_factura_s00013  la factura que nacio de ese pedido
      f19_pedidos_historia  la lista de pedidos con la historia cargada

    Antes de correrlo:
      1. Contenedores arriba y sesion iniciada en Odoo con admin@rutamoto.gt.
      2. Cerra las demas ventanas de Chrome.

    Uso:  powershell -ExecutionPolicy Bypass -File .\16_capturas_trazabilidad.ps1
#>

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Add-Type -AssemblyName System.Drawing

Add-Type @"
using System;
using System.Drawing;
using System.Runtime.InteropServices;
public class Ventana5 {
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
            Where-Object { $_.MainWindowHandle -ne 0 -and [Ventana5]::IsWindowVisible($_.MainWindowHandle) })
    if ($vs.Count -eq 0) { Write-Host "   sin ventanas de Chrome visibles" -ForegroundColor Red; return }
    $i = 0
    foreach ($v in $vs) {
        $i++
        [void][Ventana5]::ShowWindow($v.MainWindowHandle, 3)
        Start-Sleep -Milliseconds 900
        $bmp = [Ventana5]::Capturar($v.MainWindowHandle)
        if ($bmp -eq $null) { continue }
        $sufijo = if ($vs.Count -gt 1) { "_v$i" } else { "" }
        $bmp.Save((Join-Path $CapDir "$nombre$sufijo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Dispose()
        Write-Host ("   guardada: {0}{1}.png" -f $nombre, $sufijo) -ForegroundColor Green
    }
}

$Odoo = 'http://localhost:8069'
function Vista([string]$nombre, [string]$ruta, [int]$espera = 12) {
    Write-Host ""
    Write-Host ("-> {0}" -f $nombre) -ForegroundColor Cyan
    Start-Process $exe -ArgumentList ($Odoo + $ruta) | Out-Null
    Start-Sleep -Seconds $espera
    CapturarVentanas $nombre
}

Write-Host ""
Write-Host "  RUTAMOTO - FASE 3 - TRAZABILIDAD DE S00013 Y LISTA DE PEDIDOS" -ForegroundColor Cyan
Write-Host "  Son 4 vistas. Tarda alrededor de un minuto." -ForegroundColor Yellow
Write-Host ""

Vista "f16_pedido_s00013"     "/odoo/sales/13"              13
Vista "f17_entrega_s00013"    "/odoo/deliveries/17"         13
Vista "f18_factura_s00013"    "/odoo/customer-invoices/22"  13
Vista "f19_pedidos_historia"  "/odoo/orders"                14

Write-Host ""
Write-Host ("=" * 70) -ForegroundColor Green
Write-Host ("  LISTO. Capturas en: {0}" -f $CapDir) -ForegroundColor Green
Write-Host ("=" * 70) -ForegroundColor Green
Write-Host ""
