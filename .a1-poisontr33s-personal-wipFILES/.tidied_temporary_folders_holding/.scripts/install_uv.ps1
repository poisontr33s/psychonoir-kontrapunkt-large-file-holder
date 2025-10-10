# Install uv (Python package manager)
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

Write-Host "🔧 Installing uv..." -ForegroundColor Cyan

# Install uv using official installer
Invoke-Expression "& { $(Invoke-RestMethod 'https://github.com/astral-sh/uv/releases/latest/download/uv-installer.ps1') }"

# Verify installation
try {
    $version = & uv --version
    Write-Host "✅ uv installed: $version" -ForegroundColor Green
}
catch {
    throw "uv installation verification failed: $_"
}

# Install Python 3.14
Write-Host "🔧 Installing Python 3.14 via uv..." -ForegroundColor Cyan
& uv python install 3.14 --default

# Upgrade pip
& uv pip install --upgrade pip

Write-Host "✅ Python 3.14 installed and configured" -ForegroundColor Green