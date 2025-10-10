# Install Rust toolchain
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

Write-Host "🔧 Installing Rust..." -ForegroundColor Cyan

# Download rustup-init
$rustupUrl = "https://win.rustup.rs"
$rustupPath = "$env:TEMP\rustup-init.exe"

Invoke-WebRequest -Uri $rustupUrl -OutFile $rustupPath -UseBasicParsing

# Install Rust (non-interactive)
& $rustupPath -y

# Clean up
Remove-Item $rustupPath -ErrorAction SilentlyContinue

# Refresh PATH for current session
$env:PATH = [System.Environment]::GetEnvironmentVariable("Path", "Machine")

# Verify installation
try {
    $version = & rustc --version
    Write-Host "✅ Rust installed: $version" -ForegroundColor Green
}
catch {
    throw "Rust installation verification failed: $_"
}

try {
    $cargoVersion = & cargo --version
    Write-Host "✅ Cargo installed: $cargoVersion" -ForegroundColor Green
}
catch {
    throw "Cargo verification failed: $_"
}