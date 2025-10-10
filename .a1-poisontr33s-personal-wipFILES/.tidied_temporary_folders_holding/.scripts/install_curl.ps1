# Install latest stable curl for Windows (local to repo)
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

Write-Host "🔧 Installing latest stable curl..." -ForegroundColor Cyan

# Use local directory in repo instead of system PATH
$repoRoot = Split-Path $PSScriptRoot -Parent
$localCurlDir = Join-Path $repoRoot ".computer_languages" "curl"
$localCurlDir = [System.IO.Path]::GetFullPath($localCurlDir)

# Check if already installed
$curlExePath = Join-Path $localCurlDir "curl.exe"
if ((Test-Path $curlExePath) -and -not $Force) {
    Write-Host "ℹ️  curl already installed locally at $localCurlDir" -ForegroundColor Blue
    try {
        $version = & $curlExePath --version | Select-Object -First 1
        Write-Host "✅ curl version: $version" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️  curl exists but verification failed: $_" -ForegroundColor Yellow
    }
    exit 0
}

# Create directory
New-Item -Path $localCurlDir -ItemType Directory -Force | Out-Null

# Download latest curl from official site
$curlUrl = "https://curl.se/windows/latest.cgi?p=win64-mingw.zip"
$zipPath = Join-Path $env:TEMP "curl-latest.zip"
$extractPath = Join-Path $env:TEMP "curl-extracted"

Write-Host "⬇️  Downloading curl..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $curlUrl -OutFile $zipPath -UseBasicParsing

Write-Host "📦 Extracting curl..." -ForegroundColor Yellow
if (Test-Path $extractPath) {
    Remove-Item $extractPath -Recurse -Force
}
Expand-Archive -Path $zipPath -DestinationPath $extractPath -Force

# Find curl.exe
$curlExe = Get-ChildItem -Path $extractPath -Filter "curl.exe" -Recurse | Select-Object -First 1

if (-not $curlExe) {
    throw "curl.exe not found in extracted archive"
}

# Copy to local directory
Copy-Item $curlExe.FullName $localCurlDir

# Clean up
Remove-Item $zipPath -ErrorAction SilentlyContinue
Remove-Item $extractPath -Recurse -ErrorAction SilentlyContinue

# Verify local installation
try {
    $version = & $curlExePath --version | Select-Object -First 1
    Write-Host "✅ curl installed locally: $version" -ForegroundColor Green
    Write-Host "📍 Location: $localCurlDir" -ForegroundColor Cyan
}
catch {
    throw "curl installation verification failed: $_"
}

Write-Host "`n💡 To use curl in your session, run:" -ForegroundColor Yellow
Write-Host "   `$env:PATH = '$localCurlDir;' + `$env:PATH" -ForegroundColor White