#!/usr/bin/env pwsh
<#
.SYNOPSIS
    PsychoNoir Polyglot Stack Setup Script v2 - Complete Automation
    Automated installation and configuration of Ruby, Rust, Python, JS/TS tools

.DESCRIPTION
    This script automatically:
    - Creates directory structure
    - Downloads and installs all tools
    - Sets environment variables
    - Configures VSCode settings
    - Runs verification

    Everything installs to: C:\Users\$env:USERNAME\PsychoNoir-Kontrapunkt\.scripting_coding_programming_languages

.PARAMETER Uninstall
    Remove all installed components and clean up

.PARAMETER SkipVSCode
    Skip VSCode settings update

.PARAMETER Verbose
    Enable verbose output

.EXAMPLE
    .\setup_polyglot_v2.ps1

.EXAMPLE
    .\setup_polyglot_v2.ps1 -Uninstall

.EXAMPLE
    .\setup_polyglot_v2.ps1 -SkipVSCode -Verbose
#>

param(
    [switch]$Uninstall,
    [switch]$SkipVSCode,
    [switch]$Verbose
)

#Requires -Version 5.1

# ============================================================================
# Configuration
# ============================================================================

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$userProfile = $env:USERPROFILE
$installDir = Join-Path $userProfile "PsychoNoir-Kontrapunkt\.scripting_coding_programming_languages"
$projectRoot = Join-Path $userProfile "PsychoNoir-Kontrapunkt"

# Tool versions
$rubyVersion = "3.4.7-1"  # Latest Ruby+Devkit
$pythonVersion = "3.14.0"  # Latest Python via UV
$biomeVersion = "cli/v2.2.5"

function Write-Status {
    param([string]$Message, [string]$Color = "Cyan")
    Write-Host "[$((Get-Date).ToString('HH:mm:ss'))] $Message" -ForegroundColor $Color
}

function Write-Success {
    param([string]$Message)
    Write-Status "✅ $Message" "Green"
}

function Write-Error {
    param([string]$Message)
    Write-Status "❌ $Message" "Red"
}

function Write-Warning {
    param([string]$Message)
    Write-Status "⚠️ $Message" "Yellow"
}

function Invoke-WebRequestWithRetry {
    param([string]$Uri, [string]$OutFile, [int]$MaxRetries = 3)

    for ($i = 1; $i -le $MaxRetries; $i++) {
        try {
            # Ensure modern TLS
            try {
                [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12 -bor [Net.SecurityProtocolType]::Tls13
            }
            catch {
                [System.Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
            }
            Invoke-WebRequest -Uri $Uri -OutFile $OutFile -UserAgent "Mozilla/5.0"
            return $true
        }
        catch {
            if ($i -eq $MaxRetries) {
                Write-Error "Failed to download $Uri after $MaxRetries attempts"
                return $false
            }
            Write-Warning "Download attempt $i failed, retrying..."
            Start-Sleep -Seconds 2
        }
    }
}

# ============================================================================
# Directory Structure Setup
# ============================================================================

function New-DirectoryStructure {
    Write-Status "Creating directory structure..."

    $dirs = @(
        "$installDir",
        "$installDir\ruby",
        "$installDir\rust",
        "$installDir\rust\rustup",
        "$installDir\rust\cargo",
        "$installDir\python",
        "$installDir\python\Scripts",
        "$installDir\js_ts",
        "$installDir\js_ts\bun",
        "$installDir\js_ts\biome",
        "$installDir\linters",
        "$installDir\msys2"
    )

    foreach ($dir in $dirs) {
        if (!(Test-Path $dir)) {
            [System.IO.Directory]::CreateDirectory($dir) | Out-Null
            Write-Status "  Created: $dir"
        }
    }

    Write-Success "Directory structure created"
}

# ============================================================================
# Tool Installation Functions
# ============================================================================

function Install-Ruby {
    Write-Status "Installing Ruby $rubyVersion..."
    
    $installerPath = "$env:TEMP\rubyinstaller.exe"
    $rubyCandidates = @(
        $rubyVersion,
        "3.4.6-1",
        "3.3.5-1",
        "3.2.6-1"
    ) | Select-Object -Unique

    $chosenVersion = $null
    foreach ($ver in $rubyCandidates) {
        $url = "https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-$ver/rubyinstaller-$ver-x64.exe"
        Write-Status "  Trying RubyInstaller $ver..."
        if (Invoke-WebRequestWithRetry -Uri $url -OutFile $installerPath) { $chosenVersion = $ver; break }
    }

    if ($null -ne $chosenVersion) {
        # Install Ruby with custom directory (Inno Setup flags)
        $rubyDir = "$installDir\ruby"
        $installArgs = "/VERYSILENT /NORESTART /DIR=`"$rubyDir`" /LOG=`"$env:TEMP\\rubyinstall.log`" /TASKS=modpath,assocfiles,noridkinstall"
        Start-Process -FilePath $installerPath -ArgumentList $installArgs -Wait -NoNewWindow

        # Best-effort MSYS2 provisioning with ridk
        $ridk = Join-Path "$installDir\ruby\bin" "ridk.cmd"
        if (Test-Path $ridk) {
            try {
                & $ridk enable | Out-Null
                & $ridk exec pacman -Syu --noconfirm
                & $ridk exec pacman -S --noconfirm --needed base-devel mingw-w64-ucrt-x86_64-toolchain
                Write-Success "MSYS2 toolchain installed via ridk"
            }
            catch {
                Write-Warning "ridk provisioning failed; attempting direct pacman fallback"
                $pacman = Join-Path "$installDir\ruby\msys64\usr\bin" "pacman.exe"
                if (Test-Path $pacman) {
                    $oldMSYSTEM = $env:MSYSTEM
                    $oldCHERE = $env:CHERE_INVOKING
                    try {
                        $env:MSYSTEM = 'UCRT64'
                        $env:CHERE_INVOKING = '1'
                        & $pacman -Syu --noconfirm 2>$null | Out-Null
                        & $pacman -S --noconfirm --needed base-devel mingw-w64-ucrt-x86_64-toolchain 2>$null | Out-Null
                        Write-Success "MSYS2 toolchain installed via direct pacman"
                    }
                    finally {
                        $env:MSYSTEM = $oldMSYSTEM
                        $env:CHERE_INVOKING = $oldCHERE
                    }
                }
                else {
                    Write-Warning "MSYS2 pacman not found under Ruby\msys64; you can run: ridk install 1 3 later"
                }
            }
        }

        # Persist RUBY_ROOT; PATH consolidated later
        [Environment]::SetEnvironmentVariable("RUBY_ROOT", "$installDir\ruby", "User")

        Write-Success "Ruby installed (version $chosenVersion)"
    }
    else {
        Write-Error "Ruby download failed for all candidate versions: $($rubyCandidates -join ', ')"
    }
}

function Install-Rust {
    Write-Status "Installing Rust toolchain..."

    # Set custom Rust directories
    $env:RUSTUP_HOME = "$installDir\rust\rustup"
    $env:CARGO_HOME = "$installDir\rust\cargo"

    # Download and install rustup
    $rustupUrl = "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe"
    $rustupPath = "$env:TEMP\rustup-init.exe"

    if (Invoke-WebRequestWithRetry -Uri $rustupUrl -OutFile $rustupPath) {
        # Install with custom directory
        $installArgs = "-y --no-modify-path --default-toolchain stable"
        Start-Process -FilePath $rustupPath -ArgumentList $installArgs -Wait -NoNewWindow

        # Set environment variables permanently
        [Environment]::SetEnvironmentVariable("RUSTUP_HOME", "$installDir\rust\rustup", "User")
        [Environment]::SetEnvironmentVariable("CARGO_HOME", "$installDir\rust\cargo", "User")

        Write-Success "Rust installed"
    }
}

function Install-Python {
    Write-Status "Installing Python $pythonVersion (embeddable) + pip + uv + ruff..."

    $pyZipUrl = "https://www.python.org/ftp/python/$pythonVersion/python-$pythonVersion-embed-amd64.zip"
    $pyZipPath = "$env:TEMP\python-$pythonVersion-embed-amd64.zip"
    if (Invoke-WebRequestWithRetry -Uri $pyZipUrl -OutFile $pyZipPath) {
        Expand-Archive -Path $pyZipPath -DestinationPath "$installDir\python" -Force

        # Enable import site in the embeddable distribution
        $pthFile = Get-ChildItem -Path "$installDir\python" -Filter "python*.pth" -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($null -ne $pthFile) {
            $content = Get-Content -Path $pthFile.FullName -Encoding ASCII
            $content = $content -replace '^(#\s*)?import site$', 'import site'
            Set-Content -Path $pthFile.FullName -Value $content -Encoding ASCII
        }

        if (!(Test-Path "$installDir\python\Scripts")) { New-Item -ItemType Directory -Force -Path "$installDir\python\Scripts" | Out-Null }

        # Bootstrap pip
        $getPip = "$installDir\python\get-pip.py"
        Invoke-WebRequestWithRetry -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile $getPip | Out-Null
        & "$installDir\python\python.exe" $getPip

        # Install uv standalone to Scripts
        $uvUrl = "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip"
        $uvZipPath = "$env:TEMP\uv.zip"
        $uvExtractPath = "$env:TEMP\uv"
        if (Invoke-WebRequestWithRetry -Uri $uvUrl -OutFile $uvZipPath) {
            Expand-Archive -Path $uvZipPath -DestinationPath $uvExtractPath -Force
            Copy-Item "$uvExtractPath\uv.exe" "$installDir\python\Scripts\uv.exe" -Force
        }

        # Install ruff via pip
        & "$installDir\python\python.exe" -m pip install --upgrade pip
        & "$installDir\python\python.exe" -m pip install ruff

        [Environment]::SetEnvironmentVariable("PYTHON_HOME", "$installDir\python", "User")
        Write-Success "Python installed"
    }
}

function Install-JSTools {
    Write-Status "Installing JavaScript/TypeScript tools..."

    # Install Bun into hub (set BUN_INSTALL)
    $env:BUN_INSTALL = "$installDir\js_ts\bun"
    $bunInstallScript = "irm https://bun.sh/install.ps1 | iex"
    powershell -NoProfile -ExecutionPolicy Bypass -Command $bunInstallScript | Out-Null

    # Install Biome
    Write-Status "Installing Biome..."
    $biomeUrl = "https://github.com/biomejs/biome/releases/download/$biomeVersion/biome-windows-x64.exe"
    $biomePath = "$installDir\js_ts\biome\biome.exe"
    if (Invoke-WebRequestWithRetry -Uri $biomeUrl -OutFile $biomePath) {
        Write-Success "Biome installed"
    }
    else {
        Write-Warning "Biome download failed, trying bun global fallback"
        try {
            & "$env:BUN_INSTALL\bin\bun.exe" add -g @biomejs/biome | Out-Null
            Write-Success "Biome installed via bun"
        }
        catch {
            Write-Warning "Biome installation via bun failed"
        }
    }

    Write-Success "JavaScript/TypeScript tools installed"
}

function Install-Ruff {
    Write-Status "Ensuring Ruff linter is installed..."
    $pyExe = "$installDir\python\python.exe"
    if (!(Test-Path $pyExe)) {
        Write-Warning "Python not found at $pyExe; skipping Ruff install"
        return
    }
    try {
        & $pyExe -m ruff --version | Out-Null
        if ($LASTEXITCODE -eq 0) { Write-Success "Ruff already installed"; return }
    }
    catch { }
    try {
        & $pyExe -m pip install --upgrade pip | Out-Null
        & $pyExe -m pip install ruff | Out-Null
        Write-Success "Ruff installed via pip"
    }
    catch {
        Write-Warning "Failed to install Ruff via pip: $($_.Exception.Message)"
    }
}

function New-MSYS2Link {
    Write-Status "Linking MSYS2 to hub path (if available)..."
    $rubyMsys = Join-Path "$installDir\ruby" "msys64"
    $hubMsys = Join-Path $installDir "msys2"
    if (Test-Path $rubyMsys) {
        try {
            if (Test-Path $hubMsys) {
                $attr = (Get-Item $hubMsys -ErrorAction SilentlyContinue).Attributes
                if (-not ($attr -band [IO.FileAttributes]::ReparsePoint)) {
                    # If it's a regular directory, try to remove (only if empty) before creating junction
                    try { Remove-Item $hubMsys -Recurse -Force -ErrorAction Stop } catch { }
                }
            }
            if (Test-Path $hubMsys) { Remove-Item $hubMsys -Force -Recurse -ErrorAction SilentlyContinue }
            New-Item -ItemType Junction -Path $hubMsys -Target $rubyMsys | Out-Null
            Write-Success "MSYS2 junction created: $hubMsys -> $rubyMsys"
        }
        catch {
            Write-Warning "Could not create MSYS2 junction; using Ruby msys64 path directly"
        }
    }
}

function Install-MSYS2 {
    Write-Status "Installing MSYS2 into hub (non-admin)..."
    $msysRoot = Join-Path $installDir "msys2"
    $pacman = Join-Path $msysRoot "usr\bin\pacman.exe"
    if (Test-Path $pacman) {
        Write-Status "MSYS2 already present at $msysRoot"
        return
    }

    $installer = Join-Path $env:TEMP "msys2-setup.exe"
    $urls = @(
        "https://github.com/msys2/msys2-installer/releases/latest/download/msys2-x86_64-latest.exe",
        "https://repo.msys2.org/distrib/x86_64/msys2-x86_64-latest.exe"
    )
    $downloaded = $false
    foreach ($u in $urls) {
        Write-Status "  Trying $u"
        if (Invoke-WebRequestWithRetry -Uri $u -OutFile $installer) { $downloaded = $true; break }
    }

    if (-not $downloaded) {
        Write-Warning "Could not download MSYS2 installer. You can install it later manually."
        return
    }

    $msysArgs = "/VERYSILENT /NORESTART /DIR=`"$msysRoot`" /NOICONS"
    Start-Process -FilePath $installer -ArgumentList $msysArgs -Wait -NoNewWindow

    if (Test-Path $pacman) {
        Write-Success "MSYS2 installed at $msysRoot"
    }
    else {
        Write-Warning "MSYS2 install did not produce pacman.exe; continuing without it."
    }
}

function Install-MSYS2Toolchain {
    Write-Status "Provisioning MSYS2 toolchain (ucrt64)..."
    $ridk = Join-Path "$installDir\ruby\bin" "ridk.cmd"
    $pacman = Join-Path "$installDir\msys2\usr\bin" "pacman.exe"

    if (!(Test-Path $pacman) -and (Test-Path $ridk)) {
        try {
            # Attempt non-interactive base + toolchain install
            Write-Status "Running 'ridk install 1 3'..."
            & $ridk install 1 3 | Out-Null
        }
        catch {
            Write-Warning "ridk install failed or was interactive; will retry with direct pacman if available."
        }
    }

    if (Test-Path $pacman) {
        $oldMSYSTEM = $env:MSYSTEM
        $oldCHERE = $env:CHERE_INVOKING
        try {
            $env:MSYSTEM = 'UCRT64'
            $env:CHERE_INVOKING = '1'
            & $pacman -Syu --noconfirm 2>$null | Out-Null
            & $pacman -S --noconfirm --needed base-devel mingw-w64-ucrt-x86_64-toolchain 2>$null | Out-Null
            Write-Success "MSYS2 ucrt64 base + toolchain installed"
        }
        finally {
            $env:MSYSTEM = $oldMSYSTEM
            $env:CHERE_INVOKING = $oldCHERE
        }
    }
    else {
        Write-Warning "MSYS2 pacman not found at $pacman. Ensure MSYS2 installed or run: ridk install 1 3 manually."
    }
}

function Update-VSCodeSettings {
    Write-Status "Updating VSCode settings..."

    $vscodeSettingsPath = "$projectRoot\.vscode\settings.json"
    $vscodeDir = "$projectRoot\.vscode"

    if (!(Test-Path $vscodeDir)) {
        New-Item -ItemType Directory -Force -Path $vscodeDir | Out-Null
    }

    $pathParts = @(
        "$installDir\ruby\bin",
        "$installDir\rust\cargo\bin",
        "$installDir\python",
        "$installDir\python\Scripts",
        "$installDir\js_ts\bun\bin",
        "$installDir\js_ts\biome",
        $env:PATH
    )

    $settings = @{
        "terminal.integrated.env.windows" = @{
            "PATH"        = ($pathParts -join ';')
            "RUBY_ROOT"   = "$installDir\ruby"
            "PYTHON_HOME" = "$installDir\python"
        }
        "python.defaultInterpreterPath"   = "$installDir\python\python.exe"
        "ruby.useLanguageServer"          = $true
        "ruby.lsp.useBundler"             = $false
        "rust-client.rustupPath"          = "$installDir\rust\cargo\bin\rustup.exe"
    }

    $settings | ConvertTo-Json -Depth 10 | Set-Content -Path $vscodeSettingsPath -Encoding UTF8

    Write-Success "VSCode settings updated"
}

# ============================================================================
# Environment Variables
# ============================================================================

function Set-EnvironmentVariables {
    Write-Status "Setting environment variables..."

    # Determine MSYS2 root preference (junction if exists, else Ruby's msys64)
    $msys2Preferred = "$installDir\msys2"
    if (!(Test-Path $msys2Preferred)) {
        $altMsys = "$installDir\ruby\msys64"
        if (Test-Path $altMsys) { $msys2Preferred = $altMsys }
    }

    $envVars = @{
        "RUBY_ROOT"   = "$installDir\ruby"
        "RUSTUP_HOME" = "$installDir\rust\rustup"
        "CARGO_HOME"  = "$installDir\rust\cargo"
        "PYTHON_HOME" = "$installDir\python"
        "BUN_INSTALL" = "$installDir\js_ts\bun"
        "MSYS2_ROOT"  = $msys2Preferred
    }

    foreach ($var in $envVars.GetEnumerator()) {
        [Environment]::SetEnvironmentVariable($var.Key, $var.Value, "User")
        Write-Status "  Set $($var.Key) = $($var.Value)"
    }

    # Consolidate PATH once (user profile) and update current session
    $pathsToAdd = @(
        "$installDir\ruby\bin",
        "$installDir\rust\cargo\bin",
        "$installDir\python",
        "$installDir\python\Scripts",
        "$installDir\js_ts\bun\bin",
        "$installDir\js_ts\biome"
    )
    $userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    if ([string]::IsNullOrEmpty($userPath)) { $userPath = "" }
    # Avoid duplicates
    $userPathParts = $userPath.Split(';') | Where-Object { $_ -ne '' }
    foreach ($p in $pathsToAdd) { if ($userPathParts -notcontains $p) { $userPathParts += $p } }
    $newUserPath = ($userPathParts -join ';')
    [Environment]::SetEnvironmentVariable("PATH", $newUserPath, "User")

    # Also update current session PATH so verification works immediately
    foreach ($p in $pathsToAdd) { if (-not $env:PATH.Split(';') -contains $p) { $env:PATH += ";$p" } }

    Write-Success "Environment variables set"
}

# ============================================================================
# Verification
# ============================================================================

function Test-Installation {
    Write-Status "Running verification..."

    $tests = @(
        @{ Command = "ruby"; Args = @("-v"); Name = "Ruby" }
        @{ Command = "rustc"; Args = @("--version"); Name = "Rust" }
        @{ Command = "python"; Args = @("--version"); Name = "Python" }
        @{ Command = "ruff"; Args = @("--version"); Name = "Ruff" }
        @{ Command = "uv"; Args = @("--version"); Name = "UV" }
        @{ Command = "bun"; Args = @("--version"); Name = "Bun" }
        @{ Command = "biome"; Args = @("--version"); Name = "Biome" }
    )

    $passed = 0
    foreach ($test in $tests) {
        try {
            $null = & $test.Command @($test.Args) 2>&1
            if ($LASTEXITCODE -eq 0) {
                Write-Success "$($test.Name) working"
                $passed++
            }
            else {
                Write-Error "$($test.Name) failed"
            }
        }
        catch {
            Write-Error "$($test.Name) not found"
        }
    }

    # Verify MSYS2/UCRT64 toolchain presence (gcc existence)
    $msysRootPref = "$installDir\msys2"
    if (!(Test-Path $msysRootPref)) { $msysRootPref = "$installDir\ruby\msys64" }
    $msysGcc = Join-Path $msysRootPref "ucrt64\bin\gcc.exe"
    if (Test-Path $msysGcc) {
        Write-Success "MSYS2 toolchain (gcc) present"
    }
    else {
        Write-Warning "MSYS2 toolchain not detected; run ridk install 1 3 or re-run script"
    }

    Write-Status "Results: $passed/$($tests.Count) components working" "Magenta"

    if ($passed -eq $tests.Count) {
        Write-Success "🎉 PsychoNoir Polyglot Stack is fully operational!"
    }
    else {
        Write-Warning "Some components need attention. Run .\verify_polyglot.ps1 for details."
    }
}

# ============================================================================
# Main Installation
# ============================================================================

Write-Status "PsychoNoir Polyglot Stack Setup v2" "Magenta"
Write-Status "===================================" "Magenta"
Write-Host ""

if ($Uninstall) {
    Write-Status "Uninstall mode not implemented yet" "Yellow"
    exit 0
}

# Create directory structure
New-DirectoryStructure
Write-Host ""

# Install tools
Install-Ruby
Write-Host ""

Install-MSYS2
Write-Host ""

Provision-MSYS2
Write-Host ""

Ensure-MSYS2Link
Write-Host ""

Install-Rust
Write-Host ""

Install-Python
Write-Host ""

Install-JSTools
Write-Host ""

Install-Ruff
Write-Host ""

# Configure environment
Set-EnvironmentVariables
Write-Host ""

Update-VSCodeSettings
Write-Host ""

# Verify installation
Test-Installation

Write-Host ""
Write-Success "Setup complete! Restart your terminal and VSCode for changes to take effect."
Write-Status "Run .\verify_polyglot.ps1 -Detailed for comprehensive verification" "Cyan"