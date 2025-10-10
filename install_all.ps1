# Master installation script for PsychoNoir-Kontrapunkt development environment
# Installs all tools locally in the repository

param(
    [string[]]$SkipTools = @(),
    [switch]$Force
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$ScriptsDir = Join-Path $RepoRoot "scripts"

Write-Host "=== PsychoNoir-Kontrapunkt Development Environment Installer ===" -ForegroundColor Cyan
Write-Host "Repository: $RepoRoot" -ForegroundColor Gray
Write-Host ""

# Define tools to install
$Tools = @(
    @{ Name = "curl"; Script = "install_curl.ps1"; Description = "Command-line tool for data transfer" },
    @{ Name = "powershell"; Script = "install_powershell.ps1"; Description = "PowerShell 7.5.3 runtime" },
    @{ Name = "bun"; Script = "install_bun.ps1"; Description = "Fast JavaScript runtime and package manager" },
    @{ Name = "biome"; Script = "install_biome.ps1"; Description = "Lightning-fast linter and formatter for JS/TS" },
    @{ Name = "uv"; Script = "install_uv.ps1"; Description = "Python package manager and virtual environment tool" },
    @{ Name = "python"; Script = "install_python.ps1"; Description = "Python 3.14 with uv management" },
    @{ Name = "ruff"; Script = "install_ruff.ps1"; Description = "Fast Python linter and formatter" },
    @{ Name = "rust"; Script = "install_rust.ps1"; Description = "Rust toolchain with Cargo" },
    @{ Name = "ruby"; Script = "install_ruby.ps1"; Description = "Ruby with DevKit" }
)

# Filter out skipped tools
$ToolsToInstall = $Tools | Where-Object { $_.Name -notin $SkipTools }

Write-Host "Tools to install: $($ToolsToInstall.Count)" -ForegroundColor Green
if ($SkipTools.Count -gt 0) {
    Write-Host "Skipping: $($SkipTools -join ', ')" -ForegroundColor Yellow
}
Write-Host ""

# Install each tool
foreach ($Tool in $ToolsToInstall) {
    $ScriptPath = Join-Path $ScriptsDir $Tool.Script

    if (!(Test-Path $ScriptPath)) {
        Write-Host "Warning: $($Tool.Script) not found, skipping $($Tool.Name)" -ForegroundColor Yellow
        continue
    }

    Write-Host "Installing $($Tool.Name): $($Tool.Description)..." -ForegroundColor Green

    try {
        & $ScriptPath
        Write-Host "✓ $($Tool.Name) installed successfully" -ForegroundColor Green
    }
    catch {
        Write-Host "✗ Failed to install $($Tool.Name): $($_.Exception.Message)" -ForegroundColor Red
        if (!$Force) {
            Write-Host "Use -Force to continue with remaining installations" -ForegroundColor Yellow
            exit 1
        }
    }

    Write-Host ""
}

Write-Host "=== Installation Complete ===" -ForegroundColor Cyan
Write-Host "Run '.\activate_environment.ps1' to set up your development environment!" -ForegroundColor Green
Write-Host ""

# Show next steps
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. .\activate_environment.ps1    # Activate the environment" -ForegroundColor White
Write-Host "2. Verify installations with the commands shown in the README" -ForegroundColor White
Write-Host "3. Start developing in your isolated environment!" -ForegroundColor White