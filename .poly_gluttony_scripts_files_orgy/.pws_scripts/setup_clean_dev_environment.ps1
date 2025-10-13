# 🔥 CLEAN DEV ENVIRONMENT SETUP - NO MORE FUCKING AROUND
# Install everything ONCE in proper structure

param(
    [switch]$Setup,
    [switch]$InstallAll,
    [switch]$UpdateAll,
    [switch]$Verify,
    [string]$Category
)

$ErrorActionPreference = "Stop"

# Clean directory structure
$DEV_ROOT = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.dev_tools"

$STRUCTURE = @{
    "javascript" = @{
        tools       = @("bun", "bunx")
        install_cmd = "powershell -c `"irm bun.sh/install.ps1 | iex`""
        update_cmd  = "bun upgrade"
    }
    "python"     = @{
        tools       = @("uv", "python", "pip", "ruff")
        install_cmd = "powershell -c `"irm https://astral.sh/uv/install.ps1 | iex`""
        update_cmd  = "uv self update"
    }
    "ruby"       = @{
        tools       = @("ruby", "gem", "bundle")
        install_cmd = "winget install RubyInstallerTeam.Ruby"
        update_cmd  = "gem update --system"
    }
    "rust"       = @{
        tools       = @("rustc", "cargo", "clippy")
        install_cmd = "powershell -c `"irm https://sh.rustup.rs/install.ps1 | iex`""
        update_cmd  = "rustup update"
    }
    "system"     = @{
        tools       = @("curl", "make", "gcc")
        install_cmd = "# System tools - separate installs"
        update_cmd  = "# System tools - separate updates"
    }
}

function Setup-CleanStructure {
    Write-Host "🏗️  Creating clean directory structure..." -ForegroundColor Cyan
    
    # Remove old mess
    if (Test-Path "$DEV_ROOT") {
        Remove-Item -Path "$DEV_ROOT" -Recurse -Force
    }
    
    # Create clean structure
    foreach ($category in $STRUCTURE.Keys) {
        $path = Join-Path $DEV_ROOT $category
        New-Item -ItemType Directory -Path $path -Force | Out-Null
        Write-Host "  ✅ Created: $category/" -ForegroundColor Green
    }
}

function Install-Category {
    param([string]$Category)
    
    Write-Host "📦 Installing $Category tools..." -ForegroundColor Yellow
    $config = $STRUCTURE[$Category]
    $installPath = Join-Path $DEV_ROOT $Category
    
    switch ($Category) {
        "javascript" {
            # Install Bun
            Invoke-Expression $config.install_cmd
            
            # Copy to our structure
            $userBun = "$env:USERPROFILE\.bun\bin"
            if (Test-Path $userBun) {
                Copy-Item -Path "$userBun\*" -Destination $installPath -Force
                Write-Host "  ✅ Bun + bunx installed" -ForegroundColor Green
            }
            
            # Update Bun
            & "$installPath\bun.exe" upgrade
            Write-Host "  ✅ Bun updated" -ForegroundColor Green
        }
        
        "python" {
            # Install UV
            Invoke-Expression $config.install_cmd
            
            # Copy UV to our structure
            $userUV = "$env:USERPROFILE\.local\bin"
            if (Test-Path $userUV) {
                Copy-Item -Path "$userUV\*" -Destination $installPath -Force
                Write-Host "  ✅ UV installed" -ForegroundColor Green
            }
            
            # Install Python with UV
            & "$installPath\uv.exe" python install 3.14
            
            # Install/update Ruff with UV
            & "$installPath\uv.exe" tool install ruff --force
            Copy-Item -Path "$env:USERPROFILE\.local\bin\ruff.exe" -Destination $installPath -Force
            
            Write-Host "  ✅ Python + Ruff installed" -ForegroundColor Green
        }
        
        "ruby" {
            # Install Ruby with winget
            winget install RubyInstallerTeam.Ruby.3.3 --silent
            
            # Find Ruby installation
            $rubyPath = Get-ChildItem "C:\Ruby*" | Sort-Object Name -Descending | Select-Object -First 1
            if ($rubyPath) {
                Copy-Item -Path "$($rubyPath.FullName)\bin\*" -Destination $installPath -Force
                Write-Host "  ✅ Ruby + gems installed" -ForegroundColor Green
            }
        }
        
        "rust" {
            # Install Rust
            Invoke-Expression $config.install_cmd
            
            # Copy Rust tools to our structure
            $cargoPath = "$env:USERPROFILE\.cargo\bin"
            if (Test-Path $cargoPath) {
                Copy-Item -Path "$cargoPath\*" -Destination $installPath -Force
                Write-Host "  ✅ Rust + Cargo + Clippy installed" -ForegroundColor Green
            }
        }
        
        "system" {
            Write-Host "  ℹ️  System tools handled separately" -ForegroundColor Gray
        }
    }
}

function Update-Category {
    param([string]$Category)
    
    Write-Host "🔄 Updating $Category tools..." -ForegroundColor Cyan
    $installPath = Join-Path $DEV_ROOT $Category
    
    switch ($Category) {
        "javascript" {
            & "$installPath\bun.exe" upgrade
            Write-Host "  ✅ Bun updated" -ForegroundColor Green
        }
        "python" {
            & "$installPath\uv.exe" self update
            & "$installPath\uv.exe" tool upgrade ruff
            Write-Host "  ✅ UV + Ruff updated" -ForegroundColor Green
        }
        "ruby" {
            & "$installPath\gem.exe" update --system
            Write-Host "  ✅ Ruby gems updated" -ForegroundColor Green
        }
        "rust" {
            & "$installPath\rustup.exe" update
            Write-Host "  ✅ Rust updated" -ForegroundColor Green
        }
    }
}

function Verify-Installation {
    Write-Host "🔍 Verifying installations..." -ForegroundColor Cyan
    
    foreach ($category in $STRUCTURE.Keys) {
        if ($category -eq "system") { continue }
        
        $installPath = Join-Path $DEV_ROOT $category
        $tools = $STRUCTURE[$category].tools
        
        Write-Host "  📂 ${category}:" -ForegroundColor Yellow
        foreach ($tool in $tools) {
            $toolPath = Join-Path $installPath "$tool.exe"
            if (Test-Path $toolPath) {
                try {
                    $version = & $toolPath --version 2>$null | Select-Object -First 1
                    Write-Host "    ✅ $tool : $version" -ForegroundColor Green
                }
                catch {
                    Write-Host "    ⚠️  $tool : Installed but version check failed" -ForegroundColor Yellow
                }
            }
            else {
                Write-Host "    ❌ $tool : Not found" -ForegroundColor Red
            }
        }
    }
}

# MAIN EXECUTION

if ($Setup -or (-not $InstallAll -and -not $UpdateAll -and -not $Verify -and -not $Category)) {
    Setup-CleanStructure
}

if ($InstallAll) {
    Setup-CleanStructure
    foreach ($cat in @("javascript", "python", "ruby", "rust")) {
        Install-Category -Category $cat
    }
    Verify-Installation
}

if ($UpdateAll) {
    foreach ($cat in @("javascript", "python", "ruby", "rust")) {
        Update-Category -Category $cat
    }
    Verify-Installation
}

if ($Category) {
    Install-Category -Category $Category
}

if ($Verify) {
    Verify-Installation
}

Write-Host "🎯 DEV ENVIRONMENT READY!" -ForegroundColor Green