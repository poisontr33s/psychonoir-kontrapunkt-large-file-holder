# Computer Languages Environment Activator
# Adds local tools to PATH for development

$RepoRoot = $PSScriptRoot

# Add tools to PATH (prepend to ensure priority)
$env:PATH = "$RepoRoot\msys64\ucrt64\bin;$RepoRoot\javascript;$RepoRoot\python;$RepoRoot\rust\.cargo\bin;$env:PATH"

# Set environment variables for tools
$env:BUN_PATH = "$RepoRoot\javascript"
$env:PYTHON_PATH = "$RepoRoot\python"
$env:RUST_PATH = "$RepoRoot\rust"
$env:CARGO_HOME = "$RepoRoot\rust\.cargo"
$env:RUSTUP_HOME = "$RepoRoot\rust\.rustup"
$env:MSYS2_PATH = "$RepoRoot\msys64"
$env:MSYSTEM = "UCRT64"
$env:MSYSTEM_PREFIX = "$RepoRoot\msys64\ucrt64"
$env:CC = "$RepoRoot\msys64\ucrt64\bin\gcc.exe"
$env:CXX = "$RepoRoot\msys64\ucrt64\bin\g++.exe"
$env:RUBY_PATH = "$RepoRoot\ruby"

# MSYS2 environment variables for Ruby native extensions
$env:MSYS2_ARG_CONV_EXCL = "*/mingw32-make.exe;*/make.exe;*"
$env:MSYS = "winsymlinks:nativestrict"

# Ensure MAKE environment variable is not set so RbConfig controls it
Remove-Item Env:MAKE -ErrorAction SilentlyContinue

# Optional: Set Python-specific variables
$env:PYTHONHOME = "$RepoRoot\python"
$env:PYTHONPATH = "$RepoRoot\python\Lib"

# Load RbConfig patch for MSYS2 path conversion
if (Test-Path "$env:RUBY_PATH\bin\ruby.exe") {
    $env:RUBYOPT = "-r$RepoRoot/ruby/lib/ruby/site_ruby/3.4.0/msys2_rbconfig_patch.rb"
}

Write-Host "🔥 Computer Languages Environment Activated 🔥"
Write-Host "Available tools:"
Write-Host "  bun: $($env:BUN_PATH)\bun.exe"
Write-Host "  python: $($env:PYTHON_PATH)\python.exe"
Write-Host "  rustc/cargo: $($env:RUST_PATH)\.cargo\bin\"
Write-Host "  gcc/make: $($env:MSYS2_PATH)\ucrt64\bin\"

# Test tools if they exist
if (Test-Path "$env:BUN_PATH\bun.exe") {
    Write-Host "  Bun version: $(& "$env:BUN_PATH\bun.exe" --version)"
}
if (Test-Path "$env:PYTHON_PATH\python.exe") {
    Write-Host "  Python version: $(& "$env:PYTHON_PATH\python.exe" --version)"
}
if (Test-Path "$env:RUST_PATH\.cargo\bin\rustc.exe") {
    Write-Host "  Rust version: $(& "$env:RUST_PATH\.cargo\bin\rustc.exe" --version)"
}
if (Test-Path "$env:MSYS2_PATH\ucrt64\bin\gcc.exe") {
    Write-Host "  GCC version: $(& "$env:MSYS2_PATH\ucrt64\bin\gcc.exe" --version | Select-Object -First 1)"
}