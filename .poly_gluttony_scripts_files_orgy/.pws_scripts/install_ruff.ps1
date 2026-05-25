#!/usr/bin/env pwsh

# Install Ruff locally in the repository
# This script downloads and installs Ruff to .computer_languages\python\

param(
    [string]$Version = "latest"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$InstallDir = Join-Path $RepoRoot ".computer_languages\python"

Write-Host "Installing Ruff $Version to $InstallDir..." -ForegroundColor Green

# Create installation directory
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

# Download Ruff
if ($Version -eq "latest") {
    $DownloadUrl = "https://github.com/astral-sh/ruff/releases/latest/download/ruff-x86_64-pc-windows-msvc.zip"
}
else {
    $DownloadUrl = "https://github.com/astral-sh/ruff/releases/download/v$Version/ruff-x86_64-pc-windows-msvc.zip"
}

$ZipPath = Join-Path $InstallDir "ruff.zip"

Write-Host "Downloading Ruff from $DownloadUrl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath

# Extract Ruff
Write-Host "Extracting Ruff..." -ForegroundColor Yellow
Expand-Archive -Path $ZipPath -DestinationPath $InstallDir -Force

# Clean up zip file
Remove-Item $ZipPath

Write-Host "Ruff installed successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir\ruff.exe" -ForegroundColor Cyan