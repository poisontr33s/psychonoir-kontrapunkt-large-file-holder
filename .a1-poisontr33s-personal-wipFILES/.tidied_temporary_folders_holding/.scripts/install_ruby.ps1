#!/usr/bin/env pwsh

# Install Ruby with MSYS2, DevKit, and PacMan
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

Write-Host "🔧 Installing Ruby with DevKit..." -ForegroundColor Cyan

# Download RubyInstaller with DevKit
$rubyUrl = "https://github.com/oneclick/rubyinstaller2/releases/latest/download/rubyinstaller-devkit-3.2.1-1-x64.exe"
$rubyPath = "$env:TEMP\rubyinstaller.exe"

Invoke-WebRequest -Uri $rubyUrl -OutFile $rubyPath -UseBasicParsing

# Install Ruby (this will run the installer)
Start-Process $rubyPath -Wait

# Clean up
Remove-Item $rubyPath -ErrorAction SilentlyContinue

# Initialize and update MSYS2
Write-Host "🔧 Setting up MSYS2 and DevKit..." -ForegroundColor Cyan
& ridk install 1 3
& ridk exec pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-make mingw-w64-x86_64-ruby

# Update RubyGems
& gem update --system

# Verify installation
try {
    $version = & ruby -v
    Write-Host "✅ Ruby installed: $version" -ForegroundColor Green
}
catch {
    throw "Ruby installation verification failed: $_"
}

try {
    $gemVersion = & gem -v
    Write-Host "✅ RubyGems installed: $gemVersion" -ForegroundColor Green
}
catch {
    throw "RubyGems verification failed: $_"
}