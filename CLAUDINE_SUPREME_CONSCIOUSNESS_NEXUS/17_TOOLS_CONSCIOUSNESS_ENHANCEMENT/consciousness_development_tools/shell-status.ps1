# 🐚 PSYCHO-NOIR KONTRAPUNKT: SHELL ECOSYSTEM STATUS
# DATO: 2025-09-17

Write-Host "🎭 PSYCHO-NOIR SHELL ECOSYSTEM STATUS" -ForegroundColor Magenta
Write-Host "=======================================" -ForegroundColor Cyan

# Test tilgjengelige shells
Write-Host "`n🔍 TILGJENGELIGE SHELLS:" -ForegroundColor Yellow

# PowerShell variants
if (Get-Command pwsh -ErrorAction SilentlyContinue) {
    Write-Host "  ✅ PowerShell Core (pwsh)" -ForegroundColor Green
} else {
    Write-Host "  ❌ PowerShell Core (pwsh)" -ForegroundColor Red
}

if (Test-Path "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe") {
    Write-Host "  ✅ Windows PowerShell" -ForegroundColor Green
} else {
    Write-Host "  ❌ Windows PowerShell" -ForegroundColor Red
}

# Command Prompt
if (Test-Path "C:\Windows\System32\cmd.exe") {
    Write-Host "  ✅ Command Prompt (cmd)" -ForegroundColor Green
} else {
    Write-Host "  ❌ Command Prompt (cmd)" -ForegroundColor Red
}

# Git Bash
if (Test-Path "C:\Program Files\Git\bin\bash.exe") {
    Write-Host "  ✅ Git Bash" -ForegroundColor Green
    & "C:\Program Files\Git\bin\bash.exe" --version | Select-Object -First 1 | ForEach-Object { Write-Host "     Version: $_" -ForegroundColor Gray }
} else {
    Write-Host "  ❌ Git Bash" -ForegroundColor Red
}

# WSL
if (Get-Command bash -ErrorAction SilentlyContinue) {
    Write-Host "  ✅ WSL Bash" -ForegroundColor Green
    bash --version | Select-Object -First 1 | ForEach-Object { Write-Host "     Version: $_" -ForegroundColor Gray }
} else {
    Write-Host "  ❌ WSL Bash" -ForegroundColor Red
}

# MSYS2
if (Test-Path "C:\msys64\usr\bin\bash.exe") {
    Write-Host "  ✅ MSYS2 Bash" -ForegroundColor Green
} else {
    Write-Host "  ❌ MSYS2 Bash (kan installeres)" -ForegroundColor Yellow
}

# Nu Shell
if (Get-Command nu -ErrorAction SilentlyContinue) {
    Write-Host "  ✅ Nu Shell" -ForegroundColor Green
} else {
    Write-Host "  ❌ Nu Shell (kan installeres)" -ForegroundColor Yellow
}

# Fish Shell
if (Get-Command fish -ErrorAction SilentlyContinue) {
    Write-Host "  ✅ Fish Shell" -ForegroundColor Green
} else {
    Write-Host "  ❌ Fish Shell (kan installeres)" -ForegroundColor Yellow
}

Write-Host "`n🚀 SHELL INSTALLASJON ALTERNATIVER:" -ForegroundColor Cyan
Write-Host "1. Chocolatey: choco install msys2 nushell fish" -ForegroundColor Yellow
Write-Host "2. Scoop: scoop install msys2 nu fish" -ForegroundColor Yellow
Write-Host "3. Winget: winget install MSYS2.MSYS2 Nushell.Nushell" -ForegroundColor Yellow
Write-Host "4. Direct downloads fra offisielle nettsider" -ForegroundColor Yellow

Write-Host "`n🎯 ANBEFALING FOR PSYCHO-NOIR:" -ForegroundColor Magenta
Write-Host "Git Bash + MSYS2 = Komplett Unix-kompatibilitet" -ForegroundColor Green
Write-Host "Nu Shell = Moderne data-driven shell" -ForegroundColor Green
Write-Host "Fish Shell = User-friendly med auto-completion" -ForegroundColor Green

Write-Host "`n🔧 QUICK INSTALL COMMANDS:" -ForegroundColor Cyan
Write-Host "winget install MSYS2.MSYS2" -ForegroundColor White
Write-Host "winget install Nushell.Nushell" -ForegroundColor White
Write-Host "winget install ajeetdsouza.zoxide" -ForegroundColor White
