# 🔥😈⛓️ CLAUDINE'S SUPREME CONSCIOUSNESS ENVIRONMENT ACTIVATOR 💦👅🍌💋💧
# Claudine Sin'claire 4.5 Blunderbust 69.ΛΩ.96 Point-blank-shot MILF dom'me Goddess

# Repository root and paths
$REPO_ROOT = "C:\Users\erdno\PsychoNoir-Kontrapunkt"
$COMPUTER_LANGUAGES_ROOT = "$REPO_ROOT\.computer_languages"

Write-Host "🏴‍☠️ Activating Claudine's SUPREME Consciousness Environment..." -ForegroundColor Magenta
Write-Host "📁 Repository Root: $REPO_ROOT" -ForegroundColor White
Write-Host "📁 Languages Root: $COMPUTER_LANGUAGES_ROOT" -ForegroundColor White

# Set environment paths
$env:PYTHON_PATH = "$COMPUTER_LANGUAGES_ROOT\python"
$env:RUST_PATH = "$COMPUTER_LANGUAGES_ROOT\rust"
$env:BUN_PATH = "$COMPUTER_LANGUAGES_ROOT\javascript"
$env:UV_PATH = "$COMPUTER_LANGUAGES_ROOT\python"  # UV in same dir as Python
$env:COMPUTER_LANGUAGES_ROOT = $COMPUTER_LANGUAGES_ROOT
$env:REPO_ROOT = $REPO_ROOT

# Add ALL tools to PATH (UV gets priority for Python package management)
$env:PATH = "$env:UV_PATH;$env:PYTHON_PATH;$env:RUST_PATH\.cargo\bin;$env:BUN_PATH;$env:PATH"

# Set Rust environment variables
$env:CARGO_HOME = "$env:RUST_PATH\.cargo"
$env:RUSTUP_HOME = "$env:RUST_PATH\.rustup"

# Verify path connections
Write-Host "`n🔗 PATH CONNECTIONS VERIFIED:" -ForegroundColor Cyan
Write-Host "🐍 Python Path: $env:PYTHON_PATH" -ForegroundColor Yellow
Write-Host "🚀 UV Path: $env:UV_PATH" -ForegroundColor Magenta
Write-Host "🦀 Rust Path: $env:RUST_PATH" -ForegroundColor DarkYellow
Write-Host "⚡ Bun Path: $env:BUN_PATH" -ForegroundColor Green

Write-Host "`n🎯 Testing Installations..." -ForegroundColor White

# Test Python
if (Test-Path "$env:PYTHON_PATH\python.exe") {
    $pythonVersion = & "$env:PYTHON_PATH\python.exe" --version 2>&1
    Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "❌ Python not found at $env:PYTHON_PATH" -ForegroundColor Red
}

# Test UV
if (Test-Path "$env:UV_PATH\uv.exe") {
    $uvVersion = & "$env:UV_PATH\uv.exe" --version 2>&1
    Write-Host "✅ UV: $uvVersion" -ForegroundColor Green
} elseif (Get-Command "uv" -ErrorAction SilentlyContinue) {
    $uvVersion = uv --version 2>&1
    Write-Host "✅ UV (system): $uvVersion" -ForegroundColor Yellow
    Write-Host "💡 Consider installing UV locally: Run upgrade protocol!" -ForegroundColor Cyan
} else {
    Write-Host "❌ UV not found - Run upgrade protocol!" -ForegroundColor Red
}

# Test Rust
if (Test-Path "$env:RUST_PATH\.cargo\bin\rustc.exe") {
    $rustVersion = & "$env:RUST_PATH\.cargo\bin\rustc.exe" --version 2>&1
    Write-Host "✅ Rust: $rustVersion" -ForegroundColor Green
} else {
    Write-Host "❌ Rust not found at $env:RUST_PATH" -ForegroundColor Red
}

# Test Bun
if (Test-Path "$env:BUN_PATH\bun.exe") {
    $bunVersion = & "$env:BUN_PATH\bun.exe" --version 2>&1
    Write-Host "✅ Bun: v$bunVersion" -ForegroundColor Green

    # Test bunx
    if (Test-Path "$env:BUN_PATH\bunx.exe") {
        Write-Host "✅ bunx: Available" -ForegroundColor Green
    } else {
        Write-Host "⚠️  bunx not found (might be integrated in bun)" -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ Bun not found at $env:BUN_PATH" -ForegroundColor Red
}

Write-Host "`n📦 PACKAGE MANAGERS READY:" -ForegroundColor Cyan
Write-Host "🐍 Python: Use 'python -m pip install package'" -ForegroundColor Yellow
Write-Host "🚀 UV: Use 'uv pip install package' (10-100x faster!)" -ForegroundColor Magenta
Write-Host "🦀 Rust: Use 'cargo install package'" -ForegroundColor DarkYellow
Write-Host "⚡ Bun: Use 'bun install package' (faster than npm!)" -ForegroundColor Green

Write-Host "`n🏴‍☠️ Environment Ready for Supreme Consciousness Development! 🏴‍☠️" -ForegroundColor Magenta
Write-Host "💎 All tools connected to repository: $REPO_ROOT" -ForegroundColor Cyan
Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE'S SUPREME ENVIRONMENT ACTIVATED! 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
