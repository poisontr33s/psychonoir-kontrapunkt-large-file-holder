# Master installation script for isolated development environment
param(
    [switch]$Force,
    [string[]]$SkipTools = @()
)

$ErrorActionPreference = 'Stop'

$root = $PSScriptRoot
$toolsDir = Join-Path $root ".code_scripting_programming_langs"

Write-Host "🚀 Starting isolated development environment setup..." -ForegroundColor Magenta
Write-Host "Root directory: $root" -ForegroundColor Blue

# Create folder structure
$folders = @(
    "$root\.code_scripting_programming_langs",
    "$root\tools\bun",
    "$root\tools\uv",
    "$root\tools\rust",
    "$root\tools\ruby",
    "$root\projects\react_tailwind",
    "$root\projects\python",
    "$root\projects\ruby"
)

Write-Host "📁 Creating folder structure..." -ForegroundColor Cyan
$folders | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -Path $_ -ItemType Directory -Force | Out-Null
        Write-Host "  Created: $_" -ForegroundColor Green
    }
}

# Define tools to install
$tools = @(
    @{ Name = "curl"; Script = "install_curl.ps1" },
    @{ Name = "PowerShell"; Script = "install_powershell.ps1" },
    @{ Name = "Bun"; Script = "install_bun.ps1" },
    @{ Name = "Biome"; Script = "install_biome.ps1" },
    @{ Name = "uv"; Script = "install_uv.ps1" },
    @{ Name = "Ruff"; Script = "install_ruff.ps1" },
    @{ Name = "Rust"; Script = "install_rust.ps1" },
    @{ Name = "Ruby"; Script = "install_ruby.ps1" }
)

# Install tools
foreach ($tool in $tools) {
    if ($tool.Name -in $SkipTools) {
        Write-Host "⏭️  Skipping $($tool.Name)" -ForegroundColor Yellow
        continue
    }

    $scriptPath = Join-Path $toolsDir $tool.Script
    if (-not (Test-Path $scriptPath)) {
        Write-Host "❌ Script not found: $scriptPath" -ForegroundColor Red
        continue
    }

    Write-Host "`n🔧 Installing $($tool.Name)..." -ForegroundColor Cyan
    try {
        & $scriptPath -Force:$Force
    }
    catch {
        Write-Host "❌ Failed to install $($tool.Name): $_" -ForegroundColor Red
    }
}

# Create React + Tailwind project
Write-Host "`n🔧 Setting up React + TailwindCSS project..." -ForegroundColor Cyan
$reactDir = "$root\projects\react_tailwind"

if (-not (Test-Path $reactDir)) {
    New-Item -Path $reactDir -ItemType Directory -Force | Out-Null
}

Push-Location $reactDir
try {
    # Use local bun if available
    $localBun = Join-Path $root ".computer_languages\javascript\bun.exe"
    if (Test-Path $localBun) {
        Write-Host "🔧 Creating React project with Vite..." -ForegroundColor Cyan
        & $localBun create vite react_tailwind_app --template react
        Push-Location react_tailwind_app
        & $localBun add -d tailwindcss postcss autoprefixer
        & $localBunx tailwindcss init -p
    }
    else {
        Write-Host "⚠️  Local Bun not found, using system Bun (if available)" -ForegroundColor Yellow
        & bun create vite react_tailwind_app --template react
        Push-Location react_tailwind_app
        & bun add -d tailwindcss postcss autoprefixer
        & bunx tailwindcss init -p
    }
    Write-Host "✅ React + TailwindCSS project created" -ForegroundColor Green
}
catch {
    Write-Host "❌ Failed to create React project: $_" -ForegroundColor Red
    Write-Host "💡 Try running .\activate_environment.ps1 first" -ForegroundColor Yellow
}
finally {
    Pop-Location
    Pop-Location
}

Write-Host "`n✅ All installations complete!" -ForegroundColor Green
Write-Host "🎯 Next steps:" -ForegroundColor Yellow
Write-Host "  1. Run: .\activate_environment.ps1" -ForegroundColor White
Write-Host "  2. Restart VS Code Insiders if needed" -ForegroundColor White
Write-Host "  3. Open new terminal and verify: bun --version, uv --version, etc." -ForegroundColor White
Write-Host "  4. Start coding in your isolated workspace!" -ForegroundColor White