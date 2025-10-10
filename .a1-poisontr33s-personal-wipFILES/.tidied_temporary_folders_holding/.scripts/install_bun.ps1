# Install Bun locally in repo
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

Write-Host "🔧 Installing Bun locally..." -ForegroundColor Cyan

# Use local directory in repo
$localBunDir = Join-Path $PSScriptRoot ".." ".." ".computer_languages" "javascript"
$localBunDir = [System.IO.Path]::GetFullPath($localBunDir)
$bunExePath = Join-Path $localBunDir "bun.exe"

# Check if already installed
if ((Test-Path $bunExePath) -and -not $Force) {
    Write-Host "ℹ️  Bun already installed locally at $localBunDir" -ForegroundColor Blue
    try {
        $version = & $bunExePath --version
        Write-Host "✅ Bun version: $version" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️  Bun exists but verification failed: $_" -ForegroundColor Yellow
    }
    exit 0
}

# Create directory
New-Item -Path $localBunDir -ItemType Directory -Force | Out-Null

# Install Bun using official installer (modified to install locally)
Write-Host "⬇️  Downloading and installing Bun..." -ForegroundColor Yellow

# We need to modify the installation to use our local directory
# The official installer installs to %USERPROFILE%\.bun
# Let's install it there first, then copy to our repo location

$originalBunDir = "$env:USERPROFILE\.bun"
$originalBunExe = Join-Path $originalBunDir "bin\bun.exe"

# Check if bun is already installed globally
if ((Test-Path $originalBunExe) -and -not $Force) {
    Write-Host "ℹ️  Using existing global Bun installation..." -ForegroundColor Blue
    Copy-Item $originalBunExe $localBunDir -Force
}
else {
    # Install globally first
    try {
        Invoke-Expression "& { $(Invoke-RestMethod 'https://bun.sh/install.ps1') }"
    }
    catch {
        Write-Host "⚠️  Global installation failed, trying alternative method..." -ForegroundColor Yellow
        
        # Alternative: Download directly
        $bunUrl = "https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip"
        $zipPath = Join-Path $env:TEMP "bun-windows-x64.zip"
        
        Invoke-WebRequest -Uri $bunUrl -OutFile $zipPath -UseBasicParsing
        Expand-Archive -Path $zipPath -DestinationPath $localBunDir -Force
        Remove-Item $zipPath -ErrorAction SilentlyContinue
    }
    
    # Copy to local repo directory
    if (Test-Path $originalBunExe) {
        Copy-Item $originalBunExe $localBunDir -Force
    }
    elseif (Test-Path (Join-Path $localBunDir "bun.exe")) {
        # Already extracted to local dir
    }
    else {
        throw "Failed to locate bun.exe after installation"
    }
}

# Verify local installation
try {
    $version = & $bunExePath --version
    Write-Host "✅ Bun installed locally: $version" -ForegroundColor Green
    Write-Host "📍 Location: $localBunDir" -ForegroundColor Cyan
}
catch {
    throw "Bun installation verification failed: $_"
}

Write-Host "`n💡 To use Bun in your session, run:" -ForegroundColor Yellow
Write-Host "   `$env:PATH = '$localBunDir;' + `$env:PATH" -ForegroundColor White