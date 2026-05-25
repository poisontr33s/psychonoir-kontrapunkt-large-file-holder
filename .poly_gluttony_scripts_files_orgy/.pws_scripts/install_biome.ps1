#!/usr/bin/env pwsh

# Install Biome locally in the repository
# This script downloads and installs Biome in .computer_languages/javascript

Write-Host "⚡ Installing Biome locally..." -ForegroundColor Cyan

# Get the repository root directory
$RepoRoot = Split-Path -Parent $PSScriptRoot
$BiomeDir = Join-Path $RepoRoot ".computer_languages\javascript"

# Create JavaScript directory if it doesn't exist
New-Item -ItemType Directory -Path $BiomeDir -Force | Out-Null

try {
    # Download Biome CLI (correct URL format)
    $BiomeUrl = "https://github.com/biomejs/biome/releases/latest/download/biome-win32-x64.exe"
    $BiomePath = Join-Path $BiomeDir "biome.exe"
    
    Write-Host "📥 Downloading Biome CLI..." -ForegroundColor Gray
    Invoke-WebRequest -Uri $BiomeUrl -OutFile $BiomePath -UseBasicParsing
    
    if (Test-Path $BiomePath) {
        # Test installation
        $Version = & $BiomePath --version
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Biome installed successfully!" -ForegroundColor Green
            Write-Host "📁 Location: $BiomePath" -ForegroundColor Gray
            Write-Host "🎯 Version: $Version" -ForegroundColor Green
        }
        else {
            Write-Host "❌ Biome installation verification failed" -ForegroundColor Red
            exit 1
        }
    }
    else {
        Write-Host "❌ Biome executable not found after download" -ForegroundColor Red
        exit 1
    }
    
}
catch {
    Write-Host "❌ Error installing Biome: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host "⚡ Biome installation complete!" -ForegroundColor Cyan
