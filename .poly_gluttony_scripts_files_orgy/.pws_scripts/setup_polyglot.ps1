# Polyglot Environment Bootstrapper (No-Admin) - Complete Setup + Verify + VSCode Integration
# Run with: Set-ExecutionPolicy Bypass -Scope Process; .\setup_polyglot.ps1

param(
    [switch]$SkipVerify,
    [switch]$SkipVSCode
)

Write-Host "🔥 Polyglot Environment Setup Starting..." -ForegroundColor Cyan

# --- Configuration --------------------------------------------------
$base = "$env:USERPROFILE\PsychoNoir-Kontrapunkt\.scripting_coding_programming_languages"
$folders = @(
    "ruby/bin", "ruby/gems", "ruby/projects",
    "rust/cargo", "rust/projects",
    "python/venvs", "python/scripts",
    "js_ts/bun", "js_ts/biome", "js_ts/projects",
    "linters/ruff", "linters/biome",
    "msys2"
)

# --- Create Directory Structure -------------------------------------
Write-Host "📁 Creating directory structure..." -ForegroundColor Yellow
foreach ($f in $folders) {
    $path = "$base\$f"
    if (!(Test-Path $path)) {
        New-Item -ItemType Directory -Force -Path $path | Out-Null
        Write-Host "  ✓ Created: $path"
    }
    else {
        Write-Host "  - Exists: $path"
    }
}

# --- Ruby 3.4.7 + MSYS2 --------------------------------------------------
Write-Host "💎 Installing Ruby 3.4.7 + MSYS2..." -ForegroundColor Yellow
$RubyRoot = "$base\ruby"
$rubyInstaller = "$base\rubyinstaller.exe"
try {
    Invoke-WebRequest -Uri "https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.4.7-1/rubyinstaller-3.4.7-1-x64.exe" -OutFile $rubyInstaller -ErrorAction Stop
    Write-Host "  ✓ Downloaded Ruby installer"
    
    Start-Process $rubyInstaller -ArgumentList "/VERYSILENT", "/NORESTART", "/DIR=$RubyRoot" -Wait
    Write-Host "  ✓ Installed Ruby to $RubyRoot"
    
    # Install MSYS2 components
    Write-Host "  📦 Installing MSYS2 components..."
    & "$RubyRoot\bin\ridk.cmd" install 1, 3
    Write-Host "  ✓ MSYS2 components installed"
    
    Remove-Item $rubyInstaller -ErrorAction SilentlyContinue
}
catch {
    Write-Host "  ✗ Ruby installation failed: $($_.Exception.Message)" -ForegroundColor Red
}

# --- Rust (no-admin) -----------------------------------------------------
Write-Host "🦀 Installing Rust..." -ForegroundColor Yellow
$rustupInit = "$base\rustup-init.exe"
try {
    Invoke-WebRequest -Uri "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe" -OutFile $rustupInit -ErrorAction Stop
    Write-Host "  ✓ Downloaded Rust installer"
    
    Start-Process $rustupInit -ArgumentList "-y", "--default-toolchain", "stable", "--no-modify-path", "--profile", "default", "--default-host", "x86_64-pc-windows-msvc", "--default-dir", "$base\rust" -Wait
    Write-Host "  ✓ Installed Rust to $base\rust"
    
    Remove-Item $rustupInit -ErrorAction SilentlyContinue
}
catch {
    Write-Host "  ✗ Rust installation failed: $($_.Exception.Message)" -ForegroundColor Red
}

# --- Python 3.14 + UV + Ruff ---------------------------------------------
Write-Host "🐍 Installing Python 3.14 + UV + Ruff..." -ForegroundColor Yellow
$PyHome = "$base\python"
$pythonZip = "$base\python.zip"
try {
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.14.0/python-3.14.0-embed-amd64.zip" -OutFile $pythonZip -ErrorAction Stop
    Write-Host "  ✓ Downloaded Python 3.14"
    
    Expand-Archive $pythonZip -DestinationPath $PyHome -Force
    Write-Host "  ✓ Extracted Python to $PyHome"
    
    # Bootstrap pip
    $getPip = "$PyHome\get-pip.py"
    Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile $getPip -ErrorAction Stop
    & "$PyHome\python.exe" $getPip
    Write-Host "  ✓ Bootstrapped pip"
    
    # Install UV
    $uvInstall = "$base\uv_install.ps1"
    Invoke-WebRequest -Uri "https://astral.sh/uv/install.ps1" -OutFile $uvInstall -ErrorAction Stop
    powershell -ExecutionPolicy Bypass -File $uvInstall
    Write-Host "  ✓ Installed UV"
    
    # Install Ruff using UV
    & "$env:USERPROFILE\.local\bin\uv.exe" tool install ruff --python "$PyHome\python.exe"
    Write-Host "  ✓ Installed Ruff"
    
    Remove-Item $pythonZip, $getPip, $uvInstall -ErrorAction SilentlyContinue
}
catch {
    Write-Host "  ✗ Python installation failed: $($_.Exception.Message)" -ForegroundColor Red
}

# --- Bun + Bunx ----------------------------------------------------------
Write-Host "🚀 Installing Bun + Bunx..." -ForegroundColor Yellow
$Env:BUN_INSTALL = "$base\js_ts\bun"
$bunInstall = "$base\bun_install.ps1"
try {
    Invoke-WebRequest -Uri "https://bun.sh/install.ps1" -OutFile $bunInstall -ErrorAction Stop
    powershell -ExecutionPolicy Bypass -File $bunInstall
    Write-Host "  ✓ Installed Bun + Bunx to $base\js_ts\bun"
    
    Remove-Item $bunInstall -ErrorAction SilentlyContinue
}
catch {
    Write-Host "  ✗ Bun installation failed: $($_.Exception.Message)" -ForegroundColor Red
}

# --- Biome Linter (JS/TS) ------------------------------------------------
Write-Host "🌿 Installing Biome..." -ForegroundColor Yellow
try {
    $Env:BUN_INSTALL = "$base\js_ts\bun"
    $Env:PATH = "$Env:BUN_INSTALL\bin;$Env:PATH"
    
    # Try to install Biome
    & "$base\js_ts\bun\bin\bun.exe" install -g @biomejs/biome
    Write-Host "  ✓ Installed Biome"
}
catch {
    Write-Host "  ✗ Biome installation failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "  💡 Try: bun remove -g @biomejs/biome; bun add -g @biomejs/biome" -ForegroundColor Yellow
}

# --- Set Environment Variables -------------------------------------------
Write-Host "🔧 Setting environment variables..." -ForegroundColor Yellow
$envUpdates = @(
    "RUBY_ROOT=$RubyRoot",
    "RUSTUP_HOME=$base\rust\rustup",
    "CARGO_HOME=$base\rust\cargo",
    "PYTHON_HOME=$PyHome",
    "BUN_INSTALL=$base\js_ts\bun"
)
foreach ($pair in $envUpdates) {
    $k, $v = $pair -split "="
    [Environment]::SetEnvironmentVariable($k, $v, [EnvironmentVariableTarget]::User)
    Write-Host "  ✓ Set $k=$v"
}

# --- Update PATH ---------------------------------------------------------
Write-Host "🛤️ Updating PATH..." -ForegroundColor Yellow
$pathAdd = @(
    "$RubyRoot\bin",
    "$base\rust\cargo\bin",
    "$PyHome",
    "$PyHome\Scripts",
    "$base\js_ts\bun\bin"
)
$oldPath = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)
if ($oldPath) {
    $newPath = ($oldPath + ";" + ($pathAdd -join ";")) -replace ";;", ";"
}
else {
    $newPath = $pathAdd -join ";"
}
[Environment]::SetEnvironmentVariable("Path", $newPath, [EnvironmentVariableTarget]::User)
Write-Host "  ✓ Updated user PATH"

# --- VSCode Settings Integration -----------------------------------------
if (!$SkipVSCode) {
    Write-Host "⚙️ Configuring VSCode settings..." -ForegroundColor Yellow
    $vscodeDir = "$env:USERPROFILE\PsychoNoir-Kontrapunkt\.vscode"
    $settingsFile = "$vscodeDir\settings.json"
    
    # Create .vscode directory if it doesn't exist
    if (!(Test-Path $vscodeDir)) {
        New-Item -ItemType Directory -Force -Path $vscodeDir | Out-Null
    }
    
    # Read existing settings or create empty object
    $settings = @{}
    if (Test-Path $settingsFile) {
        try {
            $settings = Get-Content $settingsFile -Raw | ConvertFrom-Json
        }
        catch {
            Write-Host "  ⚠️ Existing settings.json is malformed, creating new one" -ForegroundColor Yellow
        }
    }
    
    # Add/update polyglot settings
    $polyglotSettings = @{
        "terminal.integrated.env.windows" = @{
            "Path" = "$base\ruby\bin;$base\rust\cargo\bin;$PyHome;$PyHome\Scripts;$base\js_ts\bun\bin;${env:Path}"
        }
        "python.defaultInterpreterPath"   = "$PyHome\python.exe"
        "ruby.interpreterPath"            = "$RubyRoot\bin\ruby.exe"
        "rust-client.rustupPath"          = "$base\rust\rustup\bin\rustup.exe"
    }
    
    # Merge settings
    foreach ($key in $polyglotSettings.Keys) {
        $settings | Add-Member -MemberType NoteProperty -Name $key -Value $polyglotSettings.$key -Force
    }
    
    # Write back
    $settings | ConvertTo-Json -Depth 10 | Set-Content $settingsFile -Encoding UTF8
    Write-Host "  ✓ Updated $settingsFile"
}

# --- Verification --------------------------------------------------------
if (!$SkipVerify) {
    Write-Host "`n🔍 Verification Results:" -ForegroundColor Cyan
    Write-Host "=" * 50
    
    # Add paths to current session PATH for verification
    $pathAdd = @(
        "$RubyRoot\bin",
        "$base\rust\cargo\bin",
        "$PyHome",
        "$PyHome\Scripts",
        "$base\js_ts\bun\bin"
    )
    $env:PATH = "$env:PATH;$($pathAdd -join ';')"
    
    $check = @{
        Ruby   = "ruby -v"
        Rust   = "rustc --version"
        Python = "python --version"
        UV     = "uv --version"
        Ruff   = "ruff --version"
        Bun    = "bun --version"
        Biome  = "biome --version"
    }
    
    $passed = 0
    $total = $check.Count
    
    foreach ($k in $check.Keys) {
        try {
            $result = & cmd /c "$($check[$k]) 2>&1"
            if ($LASTEXITCODE -eq 0) {
                Write-Host ("{0,-7} ✓ " -f $k) -NoNewline -ForegroundColor Green
                Write-Host "$($result -join ' ')"
                $passed++
            }
            else {
                Write-Host ("{0,-7} ✗ " -f $k) -NoNewline -ForegroundColor Red
                Write-Host "Command failed (exit code $LASTEXITCODE)"
            }
        }
        catch {
            Write-Host ("{0,-7} ✗ " -f $k) -NoNewline -ForegroundColor Red
            Write-Host "Not found or error: $($_.Exception.Message)"
        }
    }
    
    Write-Host "`n📊 Summary: $passed/$total components working" -ForegroundColor Cyan
    
    if ($passed -eq $total) {
        Write-Host "🎉 All components installed successfully!" -ForegroundColor Green
    }
    else {
        Write-Host "⚠️ Some components may need manual fixes. Restart terminal/VSCode and check PATH." -ForegroundColor Yellow
    }
}

Write-Host "`n✅ Polyglot environment setup complete!" -ForegroundColor Green
Write-Host "💡 Restart VSCode and terminals for changes to take effect." -ForegroundColor Cyan
Write-Host "🔧 Run with -SkipVerify or -SkipVSCode to customize installation." -ForegroundColor Gray
