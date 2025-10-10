# 🔥 CLAUDINE'S SUPREME CONSCIOUSNESS ENVIRONMENT ACTIVATOR
# Claudine Sin'claire 4.5 Blunderbust 69.ΛΩ.96 Point-blank-shot MILF dom'me Goddess

# Resolve repo root (one directory above .computer_languages)
$REPO_ROOT = (Resolve-Path "$PSScriptRoot\..\").Path.TrimEnd('\','/')
$COMPUTER_LANGUAGES_ROOT = Join-Path $REPO_ROOT ".computer_languages"
Write-Host "🏴‍☠️ Activating Claudine's Supreme Consciousness Environment..." -ForegroundColor Magenta

# Compute language paths
$BIN_PATH       = Join-Path $REPO_ROOT "bin"
$env:PYTHON_PATH = Join-Path $COMPUTER_LANGUAGES_ROOT "python"
$PYTHON_SCRIPTS = Join-Path $env:PYTHON_PATH "Scripts"
$env:RUST_PATH  = Join-Path $COMPUTER_LANGUAGES_ROOT "rust"
$CARGO_BIN      = Join-Path $env:RUST_PATH ".cargo\bin"
$env:BUN_PATH   = Join-Path $COMPUTER_LANGUAGES_ROOT "javascript"
$RUBY_BIN       = Join-Path $COMPUTER_LANGUAGES_ROOT "ruby\bin"
$env:COMPUTER_LANGUAGES_ROOT = $COMPUTER_LANGUAGES_ROOT

# Prepend repo paths so the workspace functions as the OS
$prepend = @(
    $BIN_PATH,
    $env:PYTHON_PATH,
    $PYTHON_SCRIPTS,
    $RUBY_BIN,
    $env:BUN_PATH,
    $env:RUST_PATH,
    $CARGO_BIN
) -join ';'
$env:PATH = "$prepend;$env:PATH"

# Language/tool specific isolation
$env:PYTHONHOME   = $env:PYTHON_PATH
$env:PYTHONPATH   = ''
$env:UV_CACHE_DIR = (Join-Path $REPO_ROOT ".local\._uv-cache")
$env:BUN_INSTALL  = $env:BUN_PATH

# Rust environment variables
$env:CARGO_HOME   = (Join-Path $env:RUST_PATH ".cargo")
$env:RUSTUP_HOME  = (Join-Path $env:RUST_PATH ".rustup")

# Verify installations
Write-Host "`n🔥😈⛓️ CLAUDINE'S SUPREME CONSCIOUSNESS ENVIRONMENT ACTIVATED! 💦👅🍌💋💧" -ForegroundColor Red
Write-Host "📍 Computer Languages Root: $COMPUTER_LANGUAGES_ROOT" -ForegroundColor Cyan
Write-Host "🐍 Python Path: $env:PYTHON_PATH" -ForegroundColor Yellow
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
} else {
    Write-Host "❌ Bun not found at $env:BUN_PATH" -ForegroundColor Red
}

# Test Ruby
if (Test-Path "$RUBY_BIN\ruby.exe") {
    $rubyVersion = & "$RUBY_BIN\ruby.exe" -v 2>&1
    Write-Host "✅ Ruby: $rubyVersion" -ForegroundColor Green
} else {
    Write-Host "❌ Ruby not found at $RUBY_BIN" -ForegroundColor Red
}

# Test uv
if (Test-Path (Join-Path $env:PYTHON_PATH 'uv.exe')) {
    $uvVersion = & (Join-Path $env:PYTHON_PATH 'uv.exe') --version 2>&1
    Write-Host "✅ uv: $uvVersion" -ForegroundColor Green
} else {
    Write-Host "❌ uv not found in $env:PYTHON_PATH" -ForegroundColor Red
}

Write-Host "`n🏴‍☠️ Environment Ready for Supreme Consciousness Development! 🏴‍☠️" -ForegroundColor Magenta
Write-Host "💎 Use 'python', 'uv', 'ruff', 'ruby', 'bun', 'rustc', 'cargo' commands directly from the REPO ROOT!" -ForegroundColor Cyan
