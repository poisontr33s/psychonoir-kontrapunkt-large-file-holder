#!/usr/bin/env pwsh

# PsychoNoir-Kontrapunkt Development Environment Activation Script
# This script sets up the PATH to use all locally installed tools

Write-Host "🚀 Activating PsychoNoir-Kontrapunkt Development Environment..." -ForegroundColor Cyan

# Load forced configuration (always uses hardcoded root path)
$ConfigPath = "C:\Users\eldno\PsychoNoir-Kontrapunkt\common_config.ps1"
if (Test-Path $ConfigPath) {
    . $ConfigPath
    $RepoRoot = $global:PSYCHO_NOIR_ROOT
    Write-Host "✅ Loaded forced configuration: $RepoRoot" -ForegroundColor Green
}
else {
    # Fallback to hardcoded path if config file missing
    $RepoRoot = "C:\Users\eldno\PsychoNoir-Kontrapunkt"
    Write-Host "⚠️  Using fallback hardcoded root: $RepoRoot" -ForegroundColor Yellow
}

# Get tool paths using forced root
$ToolPaths = Get-ToolPaths

# Add paths to current session PATH
$CurrentPath = $env:PATH
foreach ($Path in $ToolPaths) {
    if (Test-Path $Path) {
        if ($CurrentPath -notlike "*$Path*") {
            $env:PATH = "$Path;$env:PATH"
            Write-Host "✅ Added to PATH: $Path" -ForegroundColor Green
        }
        else {
            Write-Host "ℹ️  Already in PATH: $Path" -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "⚠️  Path not found: $Path" -ForegroundColor Red
    }
}

# Set environment variables using forced configuration
Set-EnvironmentVariables
Write-Host "🌍 Environment variables configured for forced root" -ForegroundColor Green

Write-Host ""
Write-Host "🎯 Environment Activation Complete!" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 Available Tools:" -ForegroundColor White
Write-Host "  • bun, bunx       (JavaScript runtime & package manager)" -ForegroundColor Gray
Write-Host "  • biome           (JavaScript/TypeScript linter & formatter)" -ForegroundColor Gray
Write-Host "  • uv, uvx         (Python package manager)" -ForegroundColor Gray
Write-Host "  • python          (Python 3.14)" -ForegroundColor Gray
Write-Host "  • ruff            (Python linter & formatter)" -ForegroundColor Gray
Write-Host "  • rustc, cargo    (Rust compiler & package manager)" -ForegroundColor Gray
Write-Host "  • ruby, gem       (Ruby interpreter & package manager)" -ForegroundColor Gray
Write-Host "  • curl            (Data transfer tool)" -ForegroundColor Gray
Write-Host ""
Write-Host "🧪 Test your setup:" -ForegroundColor White
Write-Host "  Get-Command bun, uv, python, rustc, ruby, curl" -ForegroundColor Gray
Write-Host ""
Write-Host "📁 Sample projects available in ./projects/" -ForegroundColor White
Write-Host "  • react_tailwind/ - React + Vite + TailwindCSS" -ForegroundColor Gray
Write-Host "  • python/         - Python projects" -ForegroundColor Gray
Write-Host "  • ruby/           - Ruby projects" -ForegroundColor Gray
Write-Host ""
