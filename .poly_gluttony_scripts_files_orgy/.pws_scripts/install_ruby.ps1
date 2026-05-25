#!/usr/bin/env pwsh

# Install Ruby locally in the repository
# This script downloads and installs Ruby+DevKit to .computer_languages\ruby\

param(
    [string]$Version = "3.4.7-1"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$InstallDir = Join-Path $RepoRoot ".computer_languages\ruby"

Write-Host "Installing Ruby $Version to $InstallDir..." -ForegroundColor Green

# Create installation directory
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

# Download Ruby+DevKit
$DownloadUrl = "https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-$Version/rubyinstaller-$Version-x64.exe"
$InstallerPath = Join-Path $InstallDir "rubyinstaller.exe"

Write-Host "Downloading Ruby installer from $DownloadUrl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $DownloadUrl -OutFile $InstallerPath

# Install Ruby silently with custom directory
Write-Host "Installing Ruby..." -ForegroundColor Yellow
$InstallArgs = "/SP-", "/SILENT", "/NORESTART", "/DIR=$InstallDir", "/SUPPRESSMSGBOXES", "/LOG=$InstallDir\install.log"
Start-Process -FilePath $InstallerPath -ArgumentList $InstallArgs -Wait -NoNewWindow

# Clean up installer
Remove-Item $InstallerPath

# Add Ruby to PATH for this session
$RubyBinPath = Join-Path $InstallDir "bin"
if (Test-Path $RubyBinPath) {
    $env:PATH = "$RubyBinPath;$env:PATH"
}

Write-Host "Ruby $Version installed successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir\bin\" -ForegroundColor Cyan

# Test installation
if (Get-Command ruby -ErrorAction SilentlyContinue) {
    Write-Host "Ruby version: $(ruby -v)" -ForegroundColor Cyan
    Write-Host "Gem version: $(gem -v)" -ForegroundColor Cyan
}
else {
    Write-Host "Warning: Ruby commands not found in PATH. Run activate_environment.ps1 to add to PATH." -ForegroundColor Yellow
}