# PsychoNoir-Kontrapunkt Master Installation Script
# Installs all development tools locally in the repository

param(
    [string[]]$SkipTools = @(),
    [switch]$Force = $false
)

Write-Host "🎯 PsychoNoir-Kontrapunkt: Isolated Development Environment Setup" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host ""

# Get the repository root directory
$RepoRoot = $PSScriptRoot
$ScriptsPath = Join-Path $RepoRoot "scripts"

# Define all available tools and their installation scripts
$Tools = @{
    "PowerShell" = "install_powershell.ps1"
    "Curl"       = "install_curl.ps1"
    "Bun"        = "install_bun.ps1"
    "Biome"      = "install_biome.ps1"
    "UV"         = "install_uv.ps1"
    "Python"     = "install_python.ps1"
    "Ruff"       = "install_ruff.ps1"
    "Rust"       = "install_rust.ps1"
    "Ruby"       = "install_ruby.ps1"
}

# Installation counters
$SuccessCount = 0
$FailCount = 0
$SkipCount = 0

Write-Host "📋 Installation Plan:" -ForegroundColor White
foreach ($Tool in $Tools.Keys) {
    if ($SkipTools -contains $Tool) {
        Write-Host "  ⏭️  $Tool (SKIPPED)" -ForegroundColor Yellow
        $SkipCount++
    }
    else {
        Write-Host "  ✅ $Tool" -ForegroundColor Green
    }
}
Write-Host ""

# Confirmation prompt
if (-not $Force) {
    $Confirm = Read-Host "Continue with installation? (y/N)"
    if ($Confirm -notmatch '^[Yy]') {
        Write-Host "❌ Installation cancelled." -ForegroundColor Red
        exit 1
    }
}

Write-Host "🚀 Starting installation..." -ForegroundColor Cyan
Write-Host ""

# Install each tool
foreach ($Tool in $Tools.Keys) {
    if ($SkipTools -contains $Tool) {
        Write-Host "⏭️  Skipping $Tool" -ForegroundColor Yellow
        continue
    }
    
    $ScriptPath = Join-Path $ScriptsPath $Tools[$Tool]
    
    Write-Host "🔧 Installing $Tool..." -ForegroundColor Cyan
    
    if (-not (Test-Path $ScriptPath)) {
        Write-Host "   ❌ Script not found: $ScriptPath" -ForegroundColor Red
        $FailCount++
        continue
    }
    
    try {
        & $ScriptPath
        if ($LASTEXITCODE -eq 0 -or $null -eq $LASTEXITCODE) {
            Write-Host "   ✅ $Tool installed successfully" -ForegroundColor Green
            $SuccessCount++
        }
        else {
            Write-Host "   ❌ $Tool installation failed (Exit code: $LASTEXITCODE)" -ForegroundColor Red
            $FailCount++
        }
    }
    catch {
        Write-Host "   ❌ $Tool installation failed: $($_.Exception.Message)" -ForegroundColor Red
        $FailCount++
    }
    
    Write-Host ""
}

# Installation summary
Write-Host "📊 Installation Summary:" -ForegroundColor Cyan
Write-Host "========================" -ForegroundColor Cyan
Write-Host "✅ Successful: $SuccessCount" -ForegroundColor Green
Write-Host "❌ Failed:     $FailCount" -ForegroundColor Red
Write-Host "⏭️  Skipped:    $SkipCount" -ForegroundColor Yellow
Write-Host "📦 Total:      $($Tools.Count)" -ForegroundColor White
Write-Host ""

if ($FailCount -eq 0) {
    Write-Host "🎉 All installations completed successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🏁 Next Steps:" -ForegroundColor White
    Write-Host "  1. Run: .\activate_environment.ps1" -ForegroundColor Gray
    Write-Host "  2. Test: Get-Command bun, uv, python, rustc, ruby, curl" -ForegroundColor Gray
    Write-Host "  3. Explore sample projects in ./projects/" -ForegroundColor Gray
}
else {
    Write-Host "⚠️  Some installations failed. Check the logs above." -ForegroundColor Yellow
    Write-Host "   You can re-run individual scripts from the ./scripts/ directory." -ForegroundColor Gray
}

Write-Host ""
Write-Host "🛠️  Development environment ready in: $RepoRoot" -ForegroundColor Cyan
