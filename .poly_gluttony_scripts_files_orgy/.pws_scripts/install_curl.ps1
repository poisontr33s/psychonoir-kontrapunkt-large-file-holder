#!/usr/bin/env pwsh

# Install curl locally in the repository
# This script downloads and installs curl to .computer_languages\curl\

param(
    [string]$Version = "8.16.0"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$InstallDir = Join-Path $RepoRoot ".computer_languages\curl"

Write-Host "Installing curl $Version to $InstallDir..." -ForegroundColor Green

# Create installation directory
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

# Download curl
$DownloadUrl = "https://curl.se/windows/dl-$Version/curl-$Version-win64-mingw.zip"
$ZipPath = Join-Path $InstallDir "curl.zip"

Write-Host "Downloading curl from $DownloadUrl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath

# Extract curl
Write-Host "Extracting curl..." -ForegroundColor Yellow
Expand-Archive -Path $ZipPath -DestinationPath $InstallDir -Force

# Clean up zip file
Remove-Item $ZipPath

# Find the extracted directory
$ExtractedDir = Get-ChildItem $InstallDir -Directory | Where-Object { $_.Name -like "curl-*" } | Select-Object -First 1

if ($ExtractedDir) {
    # Move contents up one level
    Get-ChildItem $ExtractedDir.FullName | Move-Item -Destination $InstallDir
    Remove-Item $ExtractedDir.FullName -Recurse
}

Write-Host "curl $Version installed successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir\curl.exe" -ForegroundColor Cyan