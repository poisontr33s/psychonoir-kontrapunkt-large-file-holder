# Install Ruff linter using uv
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

Write-Host "🔧 Installing Ruff..." -ForegroundColor Cyan

# Ensure uv is available
try {
    & uv --version | Out-Null
}
catch {
    throw "uv is not installed. Please run install_uv.ps1 first."
}

# Install Ruff
& uv pip install ruff

# Verify installation
try {
    $version = & ruff --version
    Write-Host "✅ Ruff installed: $version" -ForegroundColor Green
}
catch {
    throw "Ruff installation verification failed: $_"
}