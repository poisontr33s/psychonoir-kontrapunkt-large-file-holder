#!/usr/bin/env pwsh

# PATH Cleanup Script - Fjern gamle og dupliserte Ruby/MSYS2 stier
# Må kjøres som Administrator for system PATH

Write-Host "🧹 CLAUDINE PATH CLEANUP SYSTEM" -ForegroundColor Magenta
Write-Host "=" * 60 -ForegroundColor Gray

# Sjekk Administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ Dette skriptet må kjøres som Administrator!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Hent nåværende system PATH
$currentSystemPath = [System.Environment]::GetEnvironmentVariable("PATH", "Machine")
Write-Host "📋 Analyserer system PATH..." -ForegroundColor Cyan

# Definer stier som skal fjernes
$pathsToRemove = @(
    "C:\msys2\usr\bin",
    "C:\msys2\mingw64\bin", 
    "C:\msys2\ucrt64\bin",
    "C:\Users\eldno\PsychoNoir-Kontrapunkt\.scripting_coding_programming_languages\msys2\ucrt64\bin",
    "C:\Users\eldno\PsychoNoir-Kontrapunkt\.scripting_coding_programming_languages\msys2\usr\bin",
    "C:\Users\eldno\PsychoNoir-Kontrapunkt\.scripting_coding_programming_languages\ruby\bin"
)

# Definer korrekte stier som skal være der
$correctPaths = @(
    "C:\Users\eldno\.computer_languages\msys2\usr\bin",
    "C:\Users\eldno\.computer_languages\msys2\ucrt64\bin",
    "C:\Users\eldno\.computer_languages\ruby\bin"
)

Write-Host "`n🗑️  Removing obsolete/duplicate paths..." -ForegroundColor Yellow

# Splitt PATH og fjern problematiske stier
$pathArray = $currentSystemPath.Split(';') | Where-Object { $_ -and $_.Trim() -ne "" }
$cleanedPaths = @()
$removedPaths = @()

foreach ($path in $pathArray) {
    $shouldRemove = $false
    
    foreach ($removePattern in $pathsToRemove) {
        if ($path.Trim() -eq $removePattern) {
            $shouldRemove = $true
            $removedPaths += $path
            Write-Host "❌ Removing: $path" -ForegroundColor Red
            break
        }
    }
    
    if (-not $shouldRemove) {
        # Sjekk for dupliserte Ruby-stier
        if ($path -like "*\.computer_languages\ruby\bin" -and $cleanedPaths -contains $path) {
            $removedPaths += $path
            Write-Host "❌ Removing duplicate: $path" -ForegroundColor Red
        }
        else {
            $cleanedPaths += $path
        }
    }
}

Write-Host "`n✅ Adding correct paths..." -ForegroundColor Green

# Legg til korrekte stier først (hvis de ikke allerede finnes)
$finalPaths = @()
foreach ($correctPath in $correctPaths) {
    if ($cleanedPaths -notcontains $correctPath) {
        $finalPaths += $correctPath
        Write-Host "✅ Adding: $correctPath" -ForegroundColor Green
    }
}

# Legg til resten av de rene stiene
$finalPaths += $cleanedPaths

# Bygg ny PATH string
$newSystemPath = ($finalPaths -join ';')

Write-Host "`n📊 Summary:" -ForegroundColor White
Write-Host "  Removed paths: $($removedPaths.Count)" -ForegroundColor Red
Write-Host "  Final paths: $($finalPaths.Count)" -ForegroundColor Green

# Oppdater system PATH
try {
    [System.Environment]::SetEnvironmentVariable("PATH", $newSystemPath, "Machine")
    Write-Host "`n✅ System PATH oppdatert!" -ForegroundColor Green
    
    # Oppdater denne sesjonens PATH
    $env:PATH = $newSystemPath
    Write-Host "✅ Session PATH oppdatert!" -ForegroundColor Green
    
}
catch {
    Write-Host "`n❌ Feil ved oppdatering av PATH: $($_.Exception.Message)" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "`n🧪 Testing cleaned PATH..." -ForegroundColor Cyan

# Test Ruby
try {
    $rubyVersion = ruby --version 2>$null
    Write-Host "✅ Ruby: $rubyVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Ruby test failed" -ForegroundColor Red
}

# Test ridk
try {
    ridk version >$null 2>&1
    Write-Host "✅ ridk working" -ForegroundColor Green
}
catch {
    Write-Host "❌ ridk test failed" -ForegroundColor Red
}

# Test GCC
try {
    $gccVersion = gcc --version 2>$null | Select-Object -First 1
    Write-Host "✅ GCC: $($gccVersion.Split(' ')[0])" -ForegroundColor Green
}
catch {
    Write-Host "❌ GCC test failed" -ForegroundColor Red
}

Write-Host "`n🔥😈⛓️💦👅🍌💋💧 CLAUDINE PATH CLEANUP COMPLETE! 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
Write-Host "🎯 Gamle og dupliserte stier fjernet. System PATH er nå ren og optimal!" -ForegroundColor Yellow

Read-Host "`nPress Enter to exit"