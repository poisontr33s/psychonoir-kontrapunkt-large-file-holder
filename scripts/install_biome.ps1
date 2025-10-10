# Install Biome locally in the repository
# This script downloads and installs Biome to .computer_languages\javascript\

param(
    [string]$Version = "latest"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$InstallDir = Join-Path $RepoRoot ".computer_languages\javascript"

Write-Host "Installing Biome $Version to $InstallDir..." -ForegroundColor Green

# Create installation directory
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

# Download Biome
if ($Version -eq "latest") {
    $DownloadUrl = "https://github.com/biomejs/biome/releases/latest/download/biome-windows-x64.exe"
}
else {
    $DownloadUrl = "https://github.com/biomejs/biome/releases/download/cli/v$Version/biome-windows-x64.exe"
}

$ExePath = Join-Path $InstallDir "biome.exe"

Write-Host "Downloading Biome from $DownloadUrl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $DownloadUrl -OutFile $ExePath

Write-Host "Biome installed successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir\biome.exe" -ForegroundColor Cyan