# Install PowerShell 7.5.3# Install PowerShell 7.5.3 and configure VS Code Insiders

param(param(

        [switch]$Force    [switch]$Force

    ))



$ErrorActionPreference = 'Stop'$ErrorActionPreference = 'Stop'



Write-Host "🔧 Installing PowerShell 7.5.3..." -ForegroundColor CyanWrite-Host "🔧 Installing PowerShell 7.5.3..." -ForegroundColor Cyan



# Install via winget# Install via winget

winget install --id Microsoft.PowerShell --version 7.5.3 --accept-package-agreements --accept-source-agreementswinget install --id Microsoft.PowerShell --version 7.5.3 --accept-package-agreements --accept-source-agreements



$pwshPath = "$env:ProgramFiles\PowerShell\7\pwsh.exe"$pwshPath = "$env:ProgramFiles\PowerShell\7\pwsh.exe"



if (-not (Test-Path $pwshPath)) {
    if (-not (Test-Path $pwshPath)) {

        throw "PowerShell 7.5.3 installation failed"    throw "PowerShell 7.5.3 installation failed"

    }
}



Write-Host "✅ PowerShell 7.5.3 installed at $pwshPath" -ForegroundColor GreenWrite-Host "✅ PowerShell 7.5.3 installed at $pwshPath" -ForegroundColor Green

# Configure VS Code Insiders
$settingsPath = "$env:APPDATA\Code - Insiders\User\settings.json"

if (Test-Path $settingsPath) {
    Write-Host "🔧 Configuring VS Code Insiders to use PowerShell 7.5.3..." -ForegroundColor Cyan

    $settings = Get-Content $settingsPath -Raw | ConvertFrom-Json
    $settings."terminal.integrated.defaultProfile.windows" = "PowerShell"
    $settings."terminal.integrated.profiles.windows"."PowerShell" = @{ "path" = $pwshPath }
    $settings | ConvertTo-Json -Depth 10 | Set-Content $settingsPath

    Write-Host "✅ VS Code Insiders configured" -ForegroundColor Green
}
else {
    Write-Host "⚠️  VS Code Insiders settings.json not found. Please ensure VS Code Insiders is installed." -ForegroundColor Yellow
}