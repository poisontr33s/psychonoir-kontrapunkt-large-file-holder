# Install Bun locally in the repository
# This script downloads and installs Bun to .computer_languages\javascript\

param(
    [string]$Version = "latest"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$InstallDir = Join-Path $RepoRoot ".computer_languages\javascript"

Write-Host "Installing Bun $Version to $InstallDir..." -ForegroundColor Green

# Create installation directory
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

# Download Bun
if ($Version -eq "latest") {
    $DownloadUrl = "https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip"
}
else {
    $DownloadUrl = "https://github.com/oven-sh/bun/releases/download/bun-v$Version/bun-windows-x64.zip"
}

$ZipPath = Join-Path $InstallDir "bun.zip"

Write-Host "Downloading Bun from $DownloadUrl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath

# Extract Bun
Write-Host "Extracting Bun..." -ForegroundColor Yellow
Expand-Archive -Path $ZipPath -DestinationPath $InstallDir -Force

# Clean up zip file
Remove-Item $ZipPath

Write-Host "Bun installed successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir\bun.exe" -ForegroundColor Cyan
Write-Host "You can also use: $InstallDir\bunx.exe" -ForegroundColor Cyan