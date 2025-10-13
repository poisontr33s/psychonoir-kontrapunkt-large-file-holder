# Install Python 3.14 locally using uv
# This script installs Python 3.14 to uv's managed location

param(
    [string]$Version = "3.14"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$UvPath = Join-Path $RepoRoot ".computer_languages\python\uv.exe"

if (!(Test-Path $UvPath)) {
    Write-Host "uv not found at $UvPath. Please run install_uv.ps1 first." -ForegroundColor Red
    exit 1
}

Write-Host "Installing Python $Version using uv..." -ForegroundColor Green

# Install Python using uv
& $UvPath python install $Version

Write-Host "Python $Version installed successfully!" -ForegroundColor Green

# Show installed versions
& $UvPath python list | Where-Object { $_ -match "cpython-$Version" -and $_ -notmatch "<download available>" }