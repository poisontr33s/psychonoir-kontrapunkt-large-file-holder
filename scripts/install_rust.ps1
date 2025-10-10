# Install Rust locally in the repository
# This script downloads and installs Rust to .computer_languages\rust\

param(
    [string]$Version = "stable"
)

$ErrorActionPreference = "Stop"

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$InstallDir = Join-Path $RepoRoot ".computer_languages\rust"

Write-Host "Installing Rust $Version to $InstallDir..." -ForegroundColor Green

# Create installation directory
New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

# Download and run rustup-init
$InstallerUrl = "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-gnu/rustup-init.exe"
$InstallerPath = Join-Path $InstallDir "rustup-init.exe"

Write-Host "Downloading Rust installer..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $InstallerUrl -OutFile $InstallerPath

# Install Rust with custom directory
Write-Host "Installing Rust..." -ForegroundColor Yellow
$InstallArgs = "-y", "--default-toolchain", $Version, "--no-modify-path", "--default-host", "x86_64-pc-windows-gnu"
Start-Process -FilePath $InstallerPath -ArgumentList $InstallArgs -Wait -NoNewWindow

# Clean up installer
Remove-Item $InstallerPath

# Add Rust to PATH for this session
$RustBinPath = Join-Path $InstallDir ".cargo\bin"
if (Test-Path $RustBinPath) {
    $env:PATH = "$RustBinPath;$env:PATH"
}

Write-Host "Rust $Version installed successfully!" -ForegroundColor Green
Write-Host "Location: $InstallDir\.cargo\bin\" -ForegroundColor Cyan

# Test installation
if (Get-Command rustc -ErrorAction SilentlyContinue) {
    Write-Host "Rust version: $(rustc --version)" -ForegroundColor Cyan
    Write-Host "Cargo version: $(cargo --version)" -ForegroundColor Cyan
}
else {
    Write-Host "Warning: Rust commands not found in PATH. Run activate_environment.ps1 to add to PATH." -ForegroundColor Yellow
}