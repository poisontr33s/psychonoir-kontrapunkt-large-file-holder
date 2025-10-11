# Install Rust locally in the repository
# This script downloads and installs Rust toolchain in .computer_languages/rust

Write-Host "🦀 Installing Rust locally..." -ForegroundColor Cyan

# Get the repository root directory
$RepoRoot = Split-Path -Parent $PSScriptRoot
$RustDir = Join-Path $RepoRoot ".computer_languages\rust"

# Create Rust directory
New-Item -ItemType Directory -Path $RustDir -Force | Out-Null

# Set environment variables for local installation
$env:CARGO_HOME = $RustDir
$env:RUSTUP_HOME = Join-Path $RustDir "rustup"

try {
    # Download rustup-init
    $RustupUrl = "https://win.rustup.rs/x86_64"
    $RustupPath = Join-Path $RustDir "rustup-init.exe"
    
    Write-Host "📥 Downloading rustup-init..." -ForegroundColor Gray
    Invoke-WebRequest -Uri $RustupUrl -OutFile $RustupPath -UseBasicParsing
    
    # Install Rust with default settings
    Write-Host "⚙️ Installing Rust toolchain..." -ForegroundColor Gray
    & $RustupPath -y --default-toolchain stable --no-modify-path
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Rust installed successfully!" -ForegroundColor Green
        Write-Host "📁 Location: $RustDir" -ForegroundColor Gray
        
        # Test installation
        $CargoPath = Join-Path $RustDir "bin\cargo.exe"
        if (Test-Path $CargoPath) {
            $Version = & $CargoPath --version
            Write-Host "🎯 Version: $Version" -ForegroundColor Green
        }
    }
    else {
        Write-Host "❌ Rust installation failed" -ForegroundColor Red
        exit 1
    }
    
    # Clean up installer
    Remove-Item $RustupPath -ErrorAction SilentlyContinue
    
}
catch {
    Write-Host "❌ Error installing Rust: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host "🦀 Rust installation complete!" -ForegroundColor Cyan
