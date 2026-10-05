<#
    RutaMoto - Fase 2 - Dos capturas adicionales para el manual MU-01.
    Mismo mecanismo que 11_capturas_fase2.ps1. Corre en menos de un minuto.

    Uso:  powershell -ExecutionPolicy Bypass -File .\11b_capturas_extra.ps1
#>

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Add-Type -AssemblyName System.Drawing

Add-Type @"
using System;
using System.Drawing;
using System.Runtime.InteropServices;
public class Ventana3 {
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
$CapDir = Join-Path $Raiz 'capturas_fase2'
New-Item -ItemType Directory -Force -Path $CapDir | Out-Null

$exe = @("$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
         "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
         "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe") |
       Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $exe) { Write-Host "No se encontro Chrome." -ForegroundColor Red; exit 1 }

function CapturarVentanas([string]$nombre) {
    $vs = @(Get-Process chrome -ErrorAction SilentlyContinue |
            Where-Object { $_.MainWindowHandle -ne 0 -and [Ventana3]::IsWindowVisible($_.MainWindowHandle) })
    if ($vs.Count -eq 0) { Write-Host "   sin ventanas de Chrome visibles" -ForegroundColor Red; return }
    $i = 0
    foreach ($v in $vs) {
        $i++
        [void][Ventana3]::ShowWindow($v.MainWindowHandle, 3)
        Start-Sleep -Milliseconds 800
        $bmp = [Ventana3]::Capturar($v.MainWindowHandle)
        if ($bmp -eq $null) { continue }
        $sufijo = if ($vs.Count -gt 1) { "_v$i" } else { "" }
        $bmp.Save((Join-Path $CapDir "$nombre$sufijo.png"), [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Dispose()
        Write-Host ("   guardada: {0}{1}.png" -f $nombre, $sufijo) -ForegroundColor Green
    }
}

function Vista([string]$nombre, [string]$ruta, [int]$espera = 11) {
    Write-Host ""
    Write-Host ("-> {0}" -f $nombre) -ForegroundColor Cyan
    Start-Process $exe -ArgumentList ('http://localhost:8069' + $ruta) | Out-Null
    Start-Sleep -Seconds $espera
    CapturarVentanas $nombre
}

Vista "13_informe_existencias" "/odoo/action-352" 12
Vista "32_regla_fre001"        "/odoo/action-399/37" 11

Write-Host ""
Write-Host ("  LISTO. Capturas en: {0}" -f $CapDir) -ForegroundColor Green
Write-Host ""
