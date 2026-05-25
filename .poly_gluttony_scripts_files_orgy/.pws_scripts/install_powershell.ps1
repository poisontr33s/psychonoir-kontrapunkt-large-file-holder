#!/usr/bin/env pwsh

# Install PowerShell 7.5.3 locally in the repository
# This script downloads and installs PowerShell to .computer_languages\powershell\

param(
    [string]$Version = "7.5.3"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$InstallDir = Join-Path $RepoRoot ".computer_languages\powershell"

Write-Host "Installing PowerShell $Version to $InstallDir..." -ForegroundColor Green

# Create installation directory
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

# Download PowerShell
$DownloadUrl = "https://github.com/PowerShell/PowerShell/releases/download/v$Version/PowerShell-$Version-win-x64.zip"
$ZipPath = Join-Path $InstallDir "powershell.zip"

Write-Host "Downloading PowerShell from $DownloadUrl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath

# Extract PowerShell
Write-Host "Extracting PowerShell..." -ForegroundColor Yellow
Expand-Archive -Path $ZipPath -DestinationPath $InstallDir -Force

# Clean up zip file
Remove-Item $ZipPath

Write-Host "PowerShell $Version installed successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir\pwsh.exe" -ForegroundColor Cyan

# Test installation
$PwshPath = Join-Path $InstallDir "pwsh.exe"
if (Test-Path $PwshPath) {
    $VersionOutput = & $PwshPath --version
    Write-Host "PowerShell version: $VersionOutput" -ForegroundColor Cyan
}