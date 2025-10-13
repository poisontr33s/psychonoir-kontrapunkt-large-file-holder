# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE UNIVERSAL PATH INSTALLER 🔥😈⛓️💦👅🍌💋💧
# Caribbean Archipelagic Consciousness Authority - Windows PATH Integration
# Makes claudine available in CMD, PowerShell 5.1, PowerShell 7, Extension Host

Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' UNIVERSAL PATH INSTALLER 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
Write-Host "Caribbean Archipelagic Consciousness Authority - Windows PATH Integration" -ForegroundColor Cyan

$PsychoRoot = "C:\Users\erdno\PsychoNoir-Kontrapunkt"
$CurrentUserPath = [Environment]::GetEnvironmentVariable("PATH", "User")

# Check if PsychoNoir-Kontrapunkt is already in PATH
if ($CurrentUserPath -like "*$PsychoRoot*") {
    Write-Host "✅ PsychoNoir-Kontrapunkt already in Windows PATH" -ForegroundColor Green
}
else {
    Write-Host "🚀 Adding PsychoNoir-Kontrapunkt to Windows PATH..." -ForegroundColor Yellow
    
    # Add to user PATH (no admin rights needed)
    $NewPath = "$CurrentUserPath;$PsychoRoot"
    [Environment]::SetEnvironmentVariable("PATH", $NewPath, "User")
    
    Write-Host "✅ Added to Windows PATH: $PsychoRoot" -ForegroundColor Green
    Write-Host "💋 Restart terminals to use claudine from anywhere!" -ForegroundColor Magenta
}

# Verify claudine files exist
$ClaudineBat = Join-Path $PsychoRoot "claudine.bat"
$ClaudinePs1 = Join-Path $PsychoRoot "claudine.ps1"

if (Test-Path $ClaudineBat) {
    Write-Host "✅ claudine.bat found - CMD compatibility ready" -ForegroundColor Green
}
else {
    Write-Host "❌ claudine.bat missing - CMD compatibility unavailable" -ForegroundColor Red
}

if (Test-Path $ClaudinePs1) {
    Write-Host "✅ claudine.ps1 found - PowerShell compatibility ready" -ForegroundColor Green
}
else {
    Write-Host "❌ claudine.ps1 missing - PowerShell compatibility unavailable" -ForegroundColor Red
}

Write-Host "`n🎯 CLAUDINE UNIVERSAL ACCESSIBILITY STATUS:" -ForegroundColor Yellow
Write-Host "🔹 CMD: claudine.bat (Windows batch file)" -ForegroundColor Cyan
Write-Host "🔹 PowerShell 5.1: claudine.ps1 (Universal PowerShell script)" -ForegroundColor Cyan  
Write-Host "🔹 PowerShell 7: claudine.ps1 (Universal PowerShell script)" -ForegroundColor Cyan
Write-Host "🔹 VS Code Extension Host: claudine.ps1 (Universal PowerShell script)" -ForegroundColor Cyan

Write-Host "`n💋 USAGE FROM ANYWHERE:" -ForegroundColor Magenta
Write-Host "CMD:          claudine" -ForegroundColor Gray
Write-Host "PowerShell:   claudine" -ForegroundColor Gray
Write-Host "              .\claudine.ps1" -ForegroundColor Gray

Write-Host "`n🌊⚓👑 Caribbean Archipelagic Consciousness - Universal Authority Installed! 🌊⚓👑" -ForegroundColor Green

# Test accessibility
Write-Host "`n🧪 TESTING UNIVERSAL ACCESS..." -ForegroundColor Yellow

try {
    # Test current session
    if (Get-Command "claudine" -ErrorAction SilentlyContinue) {
        Write-Host "✅ claudine command available in current session" -ForegroundColor Green
    }
    else {
        Write-Host "⚠️  claudine command not yet available (restart terminal)" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "⚠️  Command test inconclusive - try restarting terminal" -ForegroundColor Yellow
}