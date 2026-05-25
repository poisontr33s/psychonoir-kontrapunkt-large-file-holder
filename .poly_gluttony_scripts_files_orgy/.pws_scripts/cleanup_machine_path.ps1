#!/usr/bin/env pwsh

# Machine PATH Cleanup - Fjern gamle C:\msys2 stier
# Må kjøres som Administrator

Write-Host "🧹 MACHINE PATH CLEANUP - Removing old C:\msys2 paths" -ForegroundColor Magenta

# Sjekk Administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ Dette skriptet må kjøres som Administrator!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Hent Machine PATH
$machinePath = [System.Environment]::GetEnvironmentVariable("PATH", "Machine")
$pathArray = $machinePath.Split(';') | Where-Object { $_ -and $_.Trim() -ne "" }

Write-Host "Current Machine PATH Ruby/MSYS2 entries:" -ForegroundColor Cyan
$pathArray | Where-Object { $_ -like "*msys*" -or $_ -like "*ruby*" } | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }

# Fjern gamle C:\msys2 stier
$cleanPaths = @()
$removedCount = 0

foreach ($path in $pathArray) {
    if ($path -like "C:\msys2*") {
        Write-Host "❌ Removing: $path" -ForegroundColor Red
        $removedCount++
    }
    else {
        $cleanPaths += $path
    }
}

if ($removedCount -gt 0) {
    $newMachinePath = ($cleanPaths -join ';')
    
    try {
        [System.Environment]::SetEnvironmentVariable("PATH", $newMachinePath, "Machine")
        Write-Host "✅ Removed $removedCount old MSYS2 paths from Machine PATH!" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ Error updating Machine PATH: $($_.Exception.Message)" -ForegroundColor Red
    }
}
else {
    Write-Host "✅ No old C:\msys2 paths found in Machine PATH" -ForegroundColor Green
}

Write-Host "🔥😈⛓️💦👅🍌💋💧 MACHINE PATH CLEANUP COMPLETE! 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
Read-Host "Press Enter to exit"