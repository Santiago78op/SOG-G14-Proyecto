<#
    RutaMoto - Fase 2 - Tunel publico hacia la instancia de Odoo
    Alberto Josue Hernandez Armas, carne 201903553

    Publica http://localhost:8069 en una direccion temporal de Cloudflare para que
    el resto del equipo trabaje sobre LA MISMA base. La direccion cambia cada vez
    que se vuelve a abrir el tunel: hay que pasarla por el grupo.

        -Instalar   instala cloudflared con winget y sale

    Uso:  powershell -ExecutionPolicy Bypass -File .\13_tunel.ps1

    Mientras esta corriendo, NO cierres esta ventana: el tunel vive aqui.
    Para cerrarlo: Ctrl+C.
#>

param([switch]$Instalar)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = 'Continue'

function HayCloudflared {
    $c = Get-Command cloudflared -ErrorAction SilentlyContinue
    if ($c) { return $c.Source }
    $local = "$env:LOCALAPPDATA\Microsoft\WinGet\Links\cloudflared.exe"
    if (Test-Path $local) { return $local }
    return $null
}

$cf = HayCloudflared
if ($Instalar -or -not $cf) {
    Write-Host ""
    Write-Host "  Instalando cloudflared con winget..." -ForegroundColor Cyan
    winget install --id Cloudflare.cloudflared --accept-package-agreements --accept-source-agreements
    Write-Host ""
    Write-Host "  Cerra y volve a abrir PowerShell para que tome el PATH." -ForegroundColor Yellow
    $cf = HayCloudflared
    if ($Instalar) { exit 0 }
}
if (-not $cf) { Write-Host "No se encontro cloudflared. Corre el script con -Instalar." -ForegroundColor Red; exit 1 }

try { Invoke-WebRequest -Uri 'http://localhost:8069/web/login' -UseBasicParsing -TimeoutSec 8 | Out-Null }
catch { Write-Host "Odoo no responde en 8069. Corre primero 09_reanudar.ps1" -ForegroundColor Red; exit 1 }

Write-Host ""
Write-Host "  ============================================================" -ForegroundColor Green
Write-Host "   TUNEL HACIA LA INSTANCIA DE RUTAMOTO" -ForegroundColor Green
Write-Host "  ============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "   La direccion publica aparece abajo, en una linea que termina" -ForegroundColor Gray
Write-Host "   en trycloudflare.com. Copiala y pasala por el grupo." -ForegroundColor Gray
Write-Host ""
Write-Host "   Cada integrante entra con SU usuario, no con admin." -ForegroundColor Yellow
Write-Host "   No cierres esta ventana mientras el equipo este trabajando." -ForegroundColor Yellow
Write-Host ""

& $cf tunnel --url http://localhost:8069
