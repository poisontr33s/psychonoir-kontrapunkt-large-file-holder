#!/usr/bin/env pwsh

# 🔧 Fix Environment Duplicates and Conflicts Script
# Fixes all identified PATH and environment variable issues

Write-Host "=== CLAUDINE SUPREME ENVIRONMENT REPAIR ===" -ForegroundColor Magenta
Write-Host "🔥😈⛓️💦👅🍌💋💧 REPARERER MILJØVARIABLER OG PATH KONFLIKTER" -ForegroundColor Red

# 1. Fix RUBY_ROOT environment variable
Write-Host "`n1. Reparerer RUBY_ROOT miljøvariabel..." -ForegroundColor Yellow
$correctRubyRoot = "C:\Users\eldno\.computer_languages\ruby"
Write-Host "   Setter RUBY_ROOT til: $correctRubyRoot" -ForegroundColor Gray
[System.Environment]::SetEnvironmentVariable("RUBY_ROOT", $correctRubyRoot, [System.EnvironmentVariableTarget]::User)

# 2. Remove old MSYS2 paths from PATH
Write-Host "`n2. Fjerner gamle MSYS2 paths fra PATH..." -ForegroundColor Yellow
$userPath = [System.Environment]::GetEnvironmentVariable("PATH", [System.EnvironmentVariableTarget]::User)
$machinePath = [System.Environment]::GetEnvironmentVariable("PATH", [System.EnvironmentVariableTarget]::Machine)

# Split and clean user PATH
$userPathArray = $userPath.Split(';') | Where-Object { 
    $_ -ne "" -and 
    $_ -ne "C:\msys2\usr\bin" -and 
    $_ -ne "C:\msys2\mingw64\bin" -and
    $_ -ne "C:\msys2\bin"
}

# Remove duplicates from user PATH
$cleanUserPath = ($userPathArray | Select-Object -Unique) -join ';'
Write-Host "   Oppdaterer User PATH (fjerner gamle MSYS2 paths og duplikater)" -ForegroundColor Gray
[System.Environment]::SetEnvironmentVariable("PATH", $cleanUserPath, [System.EnvironmentVariableTarget]::User)

# 3. Fix PYTHONHOME if it points to non-existent path
Write-Host "`n3. Sjekker PYTHONHOME miljøvariabel..." -ForegroundColor Yellow
$pythonHome = [System.Environment]::GetEnvironmentVariable("PYTHONHOME", [System.EnvironmentVariableTarget]::User)
if ($pythonHome -and !(Test-Path $pythonHome)) {
    Write-Host "   PYTHONHOME peker til ikke-eksisterende path: $pythonHome" -ForegroundColor Red
    Write-Host "   Fjerner PYTHONHOME miljøvariabel" -ForegroundColor Gray
    [System.Environment]::SetEnvironmentVariable("PYTHONHOME", $null, [System.EnvironmentVariableTarget]::User)
}
else {
    Write-Host "   PYTHONHOME ser OK ut eller ikke satt" -ForegroundColor Green
}

# 4. Ensure correct paths are present
Write-Host "`n4. Sikrer at korrekte paths er til stede..." -ForegroundColor Yellow
$requiredPaths = @(
    "C:\Users\eldno\.computer_languages\ruby\bin",
    "C:\Users\eldno\.bun\bin",
    "C:\Users\eldno\.cargo\bin",
    "C:\Users\eldno\.local\bin"
)

$currentUserPath = [System.Environment]::GetEnvironmentVariable("PATH", [System.EnvironmentVariableTarget]::User)
$pathArray = $currentUserPath.Split(';') | Where-Object { $_ -ne "" }

foreach ($requiredPath in $requiredPaths) {
    if ($pathArray -notcontains $requiredPath -and (Test-Path $requiredPath)) {
        Write-Host "   Legger til manglende path: $requiredPath" -ForegroundColor Gray
        $pathArray += $requiredPath
    }
}

$finalUserPath = ($pathArray | Select-Object -Unique) -join ';'
[System.Environment]::SetEnvironmentVariable("PATH", $finalUserPath, [System.EnvironmentVariableTarget]::User)

Write-Host "`n✅ MILJØREPARASJON FULLFØRT!" -ForegroundColor Green
Write-Host "💀⚡ Restart PowerShell for å se endringene" -ForegroundColor Cyan
Write-Host "🌪️ Kjør deretter test_ruby_msys2_system.ps1 for validering" -ForegroundColor Cyan

# Show summary
Write-Host "`n=== REPARASJONSSAMMENDRAG ===" -ForegroundColor Blue
Write-Host "✅ RUBY_ROOT oppdatert til: $correctRubyRoot" -ForegroundColor Green
Write-Host "✅ Gamle MSYS2 paths fjernet fra PATH" -ForegroundColor Green
Write-Host "✅ PATH duplikater fjernet" -ForegroundColor Green
Write-Host "✅ PYTHONHOME reparert/fjernet hvis ugyldig" -ForegroundColor Green
Write-Host "✅ Påkrevde paths lagt til hvis manglende" -ForegroundColor Green