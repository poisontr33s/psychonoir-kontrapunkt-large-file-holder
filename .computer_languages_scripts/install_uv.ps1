# Install uv locally in the repository
# This script downloads and installs uv to .computer_languages\python\

param(
    [string]$Version = "latest"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$InstallDir = Join-Path $RepoRoot ".computer_languages\python"

Write-Host "Installing uv $Version to $InstallDir..." -ForegroundColor Green

# Create installation directory
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

# Download uv
if ($Version -eq "latest") {
    $DownloadUrl = "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip"
}
else {
    $DownloadUrl = "https://github.com/astral-sh/uv/releases/download/$Version/uv-x86_64-pc-windows-msvc.zip"
}

$ZipPath = Join-Path $InstallDir "uv.zip"

Write-Host "Downloading uv from $DownloadUrl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath

# Extract uv
Write-Host "Extracting uv..." -ForegroundColor Yellow
Expand-Archive -Path $ZipPath -DestinationPath $InstallDir -Force

# Clean up zip file
Remove-Item $ZipPath

Write-Host "uv installed successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir\uv.exe" -ForegroundColor Cyan
Write-Host "You can also use: $InstallDir\uvx.exe" -ForegroundColor Cyan