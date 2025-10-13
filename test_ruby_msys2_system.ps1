# Test om Ruby og MSYS2 er riktig konfigurert systemvidt
Write-Host "🧪 TESTING RUBY & MSYS2 SYSTEM-WIDE CONFIGURATION" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Gray

# Test PATH
Write-Host "`n📁 Testing PATH configuration..." -ForegroundColor White
$pathEntries = $env:PATH.Split(';') | Where-Object { $_ -like "*msys2*" -or $_ -like "*ruby*" -or $_ -like "*.computer_languages*" }
if ($pathEntries.Count -gt 0) {
    Write-Host "✅ Ruby/MSYS2 paths found in PATH:" -ForegroundColor Green
    $pathEntries | ForEach-Object { Write-Host "   $_" -ForegroundColor Gray }
}
else {
    Write-Host "❌ No Ruby/MSYS2 paths in PATH!" -ForegroundColor Red
}

# Test Environment Variables
Write-Host "`n🌍 Testing environment variables..." -ForegroundColor White
$msys2Root = [System.Environment]::GetEnvironmentVariable("MSYS2_ROOT", "Machine")
$msys2Path = [System.Environment]::GetEnvironmentVariable("MSYS2_PATH", "User")
if ($msys2Root) {
    Write-Host "✅ MSYS2_ROOT (Machine): $msys2Root" -ForegroundColor Green
}
if ($msys2Path) {
    Write-Host "✅ MSYS2_PATH (User): $msys2Path" -ForegroundColor Green
}
if (-not $msys2Root -and -not $msys2Path) {
    Write-Host "❌ Neither MSYS2_ROOT nor MSYS2_PATH set!" -ForegroundColor Red
}

# Test Ruby
Write-Host "`n💎 Testing Ruby..." -ForegroundColor White
try {
    $rubyVersion = ruby --version 2>$null
    if ($rubyVersion) {
        Write-Host "✅ Ruby: $rubyVersion" -ForegroundColor Green
    }
    else {
        Write-Host "❌ Ruby command failed" -ForegroundColor Red
    }
}
catch {
    Write-Host "❌ Ruby not found: $($_.Exception.Message)" -ForegroundColor Red
}

# Test Gem
Write-Host "`n💎 Testing Gem..." -ForegroundColor White
try {
    $gemVersion = gem --version 2>$null
    if ($gemVersion) {
        Write-Host "✅ Gem: $gemVersion" -ForegroundColor Green
    }
    else {
        Write-Host "❌ Gem command failed" -ForegroundColor Red
    }
}
catch {
    Write-Host "❌ Gem not found: $($_.Exception.Message)" -ForegroundColor Red
}

# Test ridk
Write-Host "`n🔧 Testing ridk..." -ForegroundColor White
try {
    $ridkOut = ridk version 2>$null
    if ($ridkOut) {
        Write-Host "✅ ridk working" -ForegroundColor Green
    }
    else {
        Write-Host "❌ ridk command failed" -ForegroundColor Red
    }
}
catch {
    Write-Host "❌ ridk not found: $($_.Exception.Message)" -ForegroundColor Red
}

# Test MSYS2 Bash
Write-Host "`n🐧 Testing MSYS2 Bash..." -ForegroundColor White
try {
    $bashVersion = bash --version 2>$null | Select-Object -First 1
    if ($bashVersion) {
        Write-Host "✅ Bash: $($bashVersion.Split(',')[0])" -ForegroundColor Green
    }
    else {
        Write-Host "❌ Bash command failed" -ForegroundColor Red
    }
}
catch {
    Write-Host "❌ Bash not found: $($_.Exception.Message)" -ForegroundColor Red
}

# Test GCC
Write-Host "`n🔨 Testing GCC..." -ForegroundColor White
try {
    $gccVersion = gcc --version 2>$null | Select-Object -First 1
    if ($gccVersion) {
        $gccName = $gccVersion.Split('(')[0].Trim()
        Write-Host "✅ GCC: $gccName" -ForegroundColor Green
    }
    else {
        Write-Host "❌ GCC command failed" -ForegroundColor Red
    }
}
catch {
    Write-Host "❌ GCC not found: $($_.Exception.Message)" -ForegroundColor Red
}

# Test native gem installation
Write-Host "`n💎 Testing native gem installation..." -ForegroundColor White
Write-Host "Attempting to install 'json' gem with native extensions..." -ForegroundColor Gray
try {
    $gemInstallResult = gem install json --no-document 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Native gem installation successful!" -ForegroundColor Green
    }
    else {
        Write-Host "❌ Native gem installation failed:" -ForegroundColor Red
        Write-Host $gemInstallResult -ForegroundColor Red
    }
}
catch {
    Write-Host "❌ Native gem test failed: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n" + "=" * 60 -ForegroundColor Gray
Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE SYSTEM TEST COMPLETE! 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta