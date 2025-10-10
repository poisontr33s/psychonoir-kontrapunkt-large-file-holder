# Step-by-Step Setup Guide for .computer_languages

This guide provides manual installation steps for setting up programming languages locally in the repository root, without relying on existing Python scripts.

## Prerequisites
- Windows 10/11
- PowerShell
- Internet connection for downloads

## 1. Create .computer_languages Directory Structure

If not already present, create the following structure in your repository root:

```
.computer_languages/
├── javascript/     # For Bun/Node.js ecosystem
├── python/         # For Python 3.14+
├── rust/           # For Rust toolchain
├── ruby/           # For Ruby (optional)
└── downloads/      # Temporary download folder
```

## 2. Install Bun (JavaScript Runtime)

Bun is a fast JavaScript runtime that replaces Node.js.

### Manual Steps:
1. Open PowerShell in repository root
2. Create downloads folder: `mkdir .computer_languages\downloads`
3. Download latest Bun:
   ```powershell
   Invoke-WebRequest -Uri "https://api.github.com/repos/oven-sh/bun/releases/latest" -OutFile ".computer_languages\downloads\bun_release.json"
   $release = Get-Content ".computer_languages\downloads\bun_release.json" | ConvertFrom-Json
   $asset = $release.assets | Where-Object { $_.name -match '^bun-windows-x64(?:-baseline)?\.zip$' } | Select-Object -First 1
   Invoke-WebRequest -Uri $asset.browser_download_url -OutFile ".computer_languages\downloads\bun.zip"
   ```
4. Extract Bun:
   ```powershell
   Expand-Archive -Path ".computer_languages\downloads\bun.zip" -DestinationPath ".computer_languages\javascript" -Force
   ```
5. Verify installation:
   ```powershell
   & ".computer_languages\javascript\bun.exe" --version
   ```

## 3. Install Python 3.14

### Manual Steps:
1. Download Python 3.14 embeddable:
   ```powershell
   $pythonUrl = "https://www.python.org/ftp/python/3.14.0/python-3.14.0-embed-amd64.zip"
   Invoke-WebRequest -Uri $pythonUrl -OutFile ".computer_languages\downloads\python314.zip"
   ```
2. Extract Python:
   ```powershell
   Expand-Archive -Path ".computer_languages\downloads\python314.zip" -DestinationPath ".computer_languages\python" -Force
   ```
3. Verify installation:
   ```powershell
   & ".computer_languages\python\python.exe" --version
   ```

## 4. Install Rust

### Manual Steps:
1. Download rustup-init:
   ```powershell
   Invoke-WebRequest -Uri "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe" -OutFile ".computer_languages\downloads\rustup-init.exe"
   ```
2. Install Rust locally:
   ```powershell
   $env:CARGO_HOME = "$PWD\.computer_languages\rust\.cargo"
   $env:RUSTUP_HOME = "$PWD\.computer_languages\rust\.rustup"
   & ".computer_languages\downloads\rustup-init.exe" -y --default-toolchain stable --profile minimal --no-modify-path
   ```
3. Verify installation:
   ```powershell
   & ".computer_languages\rust\.cargo\bin\rustc.exe" --version
   & ".computer_languages\rust\.cargo\bin\cargo.exe" --version
   ```

## 5. Environment Activation

Create activation scripts to use these tools:

### activate_computer_languages.ps1
```powershell
# Add to PATH
$env:PATH = "$PWD\.computer_languages\javascript;$PWD\.computer_languages\python;$PWD\.computer_languages\rust\.cargo\bin;$env:PATH"

# Set environment variables
$env:BUN_PATH = "$PWD\.computer_languages\javascript"
$env:PYTHON_PATH = "$PWD\.computer_languages\python"
$env:RUST_PATH = "$PWD\.computer_languages\rust"
$env:CARGO_HOME = "$PWD\.computer_languages\rust\.cargo"
$env:RUSTUP_HOME = "$PWD\.computer_languages\rust\.rustup"
```

## 6. Verification

After setup, run:
```powershell
# Activate environment
. .\.computer_languages\activate_computer_languages.ps1

# Test tools
bun --version
python --version
rustc --version
cargo --version
```

## Notes
- All installations are contained within the repository
- No system-wide changes required
- Tools can be updated by re-running the installation steps
- Add `.computer_languages/` to `.gitignore` to avoid committing binaries
