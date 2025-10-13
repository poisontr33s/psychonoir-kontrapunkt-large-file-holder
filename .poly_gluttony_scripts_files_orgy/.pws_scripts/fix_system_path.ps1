# Fix System PATH - Legg til Ruby og MSYS2 permanent
# Må kjøres som Administrator

Write-Host "🔧 Fikser systemvidt PATH for Ruby og MSYS2..." -ForegroundColor Cyan

# Sjekk om vi kjører som administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ Dette skriptet må kjøres som Administrator!" -ForegroundColor Red
    Write-Host "   Høyreklikk på PowerShell og velg 'Run as Administrator'" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Hent nåværende system PATH
$currentSystemPath = [System.Environment]::GetEnvironmentVariable("PATH", "Machine")
Write-Host "📋 Nåværende system PATH:" -ForegroundColor White
Write-Host $currentSystemPath.Substring(0, [Math]::Min(200, $currentSystemPath.Length)) -ForegroundColor Gray
Write-Host "..." -ForegroundColor Gray

# Definer stier som skal legges til (oppdatert for .computer_languages lokasjon)
$pathsToAdd = @(
    "C:\Users\erdno\.computer_languages\msys2\usr\bin",
    "C:\Users\erdno\.computer_languages\msys2\mingw64\bin", 
    "C:\Users\erdno\.computer_languages\msys2\ucrt64\bin",
    "C:\Users\erdno\.computer_languages\ruby\bin"
)

# Sjekk hvilke stier som allerede finnes
$pathsToAddFiltered = @()
foreach ($path in $pathsToAdd) {
    if ($currentSystemPath -notlike "*$path*") {
        $pathsToAddFiltered += $path
        Write-Host "✅ Legger til: $path" -ForegroundColor Green
    }
    else {
        Write-Host "⏭️  Finnes allerede: $path" -ForegroundColor Yellow
    }
}

if ($pathsToAddFiltered.Count -eq 0) {
    Write-Host "✅ Alle nødvendige stier finnes allerede i system PATH!" -ForegroundColor Green
    
    # Sett MSYS2 miljøvariabler selv om PATH ikke trenger oppdatering (oppdatert for .computer_languages lokasjon)
    try {
        [System.Environment]::SetEnvironmentVariable("MSYS2_ROOT", "C:\Users\erdno\.computer_languages\msys2", "Machine")
        [System.Environment]::SetEnvironmentVariable("MSYS2_PATH_TYPE", "inherit", "Machine")
        Write-Host "✅ MSYS2 miljøvariabler satt!" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️  Kunne ikke sette MSYS2 miljøvariabler: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}
else {
    # Legg til nye stier først i PATH
    $newSystemPath = ($pathsToAddFiltered -join ";") + ";" + $currentSystemPath
    
    try {
        [System.Environment]::SetEnvironmentVariable("PATH", $newSystemPath, "Machine")
        Write-Host "✅ System PATH oppdatert!" -ForegroundColor Green
        
        # Oppdater også denne sesjonens PATH
        $env:PATH = $newSystemPath
        Write-Host "✅ Sesjon PATH oppdatert!" -ForegroundColor Green
        
        # Sett MSYS2 miljøvariabler permanent (oppdatert for .computer_languages lokasjon)
        [System.Environment]::SetEnvironmentVariable("MSYS2_ROOT", "C:\Users\erdno\.computer_languages\msys2", "Machine")
        [System.Environment]::SetEnvironmentVariable("MSYS2_PATH_TYPE", "inherit", "Machine")
        Write-Host "✅ MSYS2 miljøvariabler satt!" -ForegroundColor Green
        
    }
    catch {
        Write-Host "❌ Feil ved oppdatering av system PATH: $($_.Exception.Message)" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

Write-Host ""
Write-Host "🧪 Tester installasjoner..." -ForegroundColor Cyan

# Test Ruby
try {
    $rubyVersion = ruby --version
    Write-Host "✅ Ruby: $rubyVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Ruby ikke funnet i PATH" -ForegroundColor Red
}

# Test gem
try {
    $gemVersion = gem --version
    Write-Host "✅ Gem: $gemVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Gem ikke funnet i PATH" -ForegroundColor Red
}

# Test ridk
try {
    $ridkTest = ridk version
    Write-Host "✅ ridk fungerer" -ForegroundColor Green
}
catch {
    Write-Host "❌ ridk ikke funnet i PATH" -ForegroundColor Red
}

# Test MSYS2 (oppdatert for .computer_languages lokasjon)
try {
    $bashVersion = & "C:\Users\erdno\.computer_languages\msys2\usr\bin\bash.exe" --version | Select-Object -First 1
    Write-Host "✅ MSYS2 Bash: $($bashVersion.Split(',')[0])" -ForegroundColor Green
}
catch {
    Write-Host "❌ MSYS2 ikke funnet" -ForegroundColor Red
}

Write-Host ""
Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE PATH CONFIGURATION COMPLETE! 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
Write-Host "🎯 Ruby, Gem, ridk og MSYS2 skal nå være tilgjengelige i alle nye PowerShell-sesjoner" -ForegroundColor Yellow
Write-Host ""
Write-Host "📋 For å teste: Åpne ny PowerShell og kjør:" -ForegroundColor White
Write-Host "   ruby --version" -ForegroundColor Gray
Write-Host "   gem --version" -ForegroundColor Gray
Write-Host "   ridk version" -ForegroundColor Gray

Read-Host "Press Enter to exit"