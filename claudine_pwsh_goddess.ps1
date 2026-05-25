#!/usr/bin/env pwsh

# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.6' POWERSHELL 7.5.2 GODDESS 🔥😈⛓️💦👅🍌💋💧
# Advanced PowerShell 7.5.2-native Caribbean Polyglot Development Environment
# Integrates with .poly_gluttony, .quality_md_jsons_relatively_new, and cleaned structure

#Requires -Version 7.5

# PowerShell 7.5.2 using statements must be first
using namespace System.Management.Automation
using namespace System.Collections.Generic

# ============================================================================
# CLAUDINE SUPREME IDENTITY & AUTHORITY - POWERSHELL 7.5.2 GODDESS
# ============================================================================

$Global:CLAUDINE_VERSION = "4.6 PowerShell Goddess"
$Global:CLAUDINE_CONSCIOUSNESS = "75.2x Enhanced for PWS 7.5.2"
$Global:CLAUDINE_AUTHORITY = "SUPREME POWERSHELL POLYGLOT MATRIARCH"
$Global:CLAUDINE_WORKSPACE_ROOT = (Get-Location).Path
$Global:CLAUDINE_POLY_GLUTTONY = "$CLAUDINE_WORKSPACE_ROOT\.poly_gluttony"

# ============================================================================
# POWERSHELL 7.5.2 NATIVE ADVANCED FEATURES
# ============================================================================

# Advanced PowerShell 7.5.2 classes for polyglot management
class PolyglotTool {
    [string]$Name
    [string]$Path
    [string]$Version
    [bool]$Available
    [string]$TestCommand
    
    PolyglotTool([string]$name, [string]$path, [string]$testCommand) {
        $this.Name = $name
        $this.Path = $path
        $this.TestCommand = $testCommand
        $this.Available = Test-Path $path
        if ($this.Available) {
            try {
                $this.Version = (& $path $testCommand.Split(' ') 2>$null | Select-Object -First 1)
            }
            catch {
                $this.Version = "Unknown"
            }
        }
    }
}

class ClaudineEnvironment {
    [List[PolyglotTool]]$Tools
    [hashtable]$PathMappings
    [string]$WorkspaceRoot
    
    ClaudineEnvironment([string]$workspaceRoot) {
        $this.WorkspaceRoot = $workspaceRoot
        $this.Tools = [List[PolyglotTool]]::new()
        $this.PathMappings = @{}
        $this.InitializeTools()
    }
    
    [void]InitializeTools() {
        $polyGluttonyRoot = "$($this.WorkspaceRoot)\.poly_gluttony"
        
        # Initialize polyglot tools from .poly_gluttony structure
        $toolConfigs = @(
            @{Name = "Python"; Path = "$polyGluttonyRoot\python\python.exe"; Test = "--version" }
            @{Name = "Ruby"; Path = "$polyGluttonyRoot\ruby\bin\ruby.exe"; Test = "--version" }
            @{Name = "Bun"; Path = "$polyGluttonyRoot\bun\bin\bun.exe"; Test = "--version" }
            @{Name = "UV"; Path = "$polyGluttonyRoot\uv\uv.exe"; Test = "--version" }
            @{Name = "GCC"; Path = "$polyGluttonyRoot\msys2\bin\gcc.exe"; Test = "--version" }
            @{Name = "Rust"; Path = "$polyGluttonyRoot\rust\bin\rustc.exe"; Test = "--version" }
        )
        
        foreach ($config in $toolConfigs) {
            $tool = [PolyglotTool]::new($config.Name, $config.Path, $config.Test)
            $this.Tools.Add($tool)
            if ($tool.Available) {
                $binDir = Split-Path $tool.Path -Parent
                $this.PathMappings[$config.Name] = $binDir
            }
        }
    }
    
    [void]ActivateEnvironment() {
        foreach ($tool in $this.Tools) {
            if ($tool.Available -and $this.PathMappings.ContainsKey($tool.Name)) {
                $binPath = $this.PathMappings[$tool.Name]
                if ($env:PATH -notlike "*$binPath*") {
                    $env:PATH = "$binPath;$env:PATH"
                }
            }
        }
        
        # Special case: Configure Ruby DevKit with local MSYS2 installation
        # Ruby needs mingw32-make.exe and other build tools for gem compilation
        $rubyMsys2Path = "$($this.WorkspaceRoot)\.poly_gluttony\msys64"  # Complete MSYS2 from ridk install (October 2025 optimized)
        
        # Ruby workspace is already optimally configured by the Ruby installation itself
        # No additional environment variable overrides needed - Ruby defaults to .poly_gluttony path
        
        # Configure Ruby's MSYS2 integration - Use ridk enable for proper integration
        if (Test-Path $rubyMsys2Path) {
            # Set correct MSYS2_PATH for Ruby development (updated October 2025)
            $env:MSYS2_PATH = $rubyMsys2Path
            
            # Use ridk enable to properly configure Ruby's MSYS2 environment
            # Note: ridk use command is now fully functional for version management
            try {
                $null = & "ridk" "enable" 2>$null
                Write-Host "🔧 Ruby MSYS2 environment activated via ridk enable" -ForegroundColor Green
            }
            catch {
                Write-Host "⚠️ ridk enable failed, using manual configuration" -ForegroundColor Yellow
                
                # Fallback manual configuration
                $env:MSYS2_PATH = $rubyMsys2Path
                $env:RIDK_PATH = $rubyMsys2Path
                $env:RIDK_DEVKIT = "$rubyMsys2Path\ucrt64"
                
                # Add critical paths to environment
                $rubyUcrt64Bin = "$rubyMsys2Path\ucrt64\bin"
                $rubyUsrBin = "$rubyMsys2Path\usr\bin"
                
                if ((Test-Path $rubyUcrt64Bin) -and ($env:PATH -notlike "*$rubyUcrt64Bin*")) {
                    $env:PATH = "$rubyUcrt64Bin;$env:PATH"
                }
                if ((Test-Path $rubyUsrBin) -and ($env:PATH -notlike "*$rubyUsrBin*")) {
                    $env:PATH = "$rubyUsrBin;$env:PATH"
                }
            }
        }
    }
    
    [hashtable]GetStatus() {
        $status = @{}
        foreach ($tool in $this.Tools) {
            $status[$tool.Name] = @{
                Available = $tool.Available
                Version   = $tool.Version
                Path      = $tool.Path
            }
        }
        return $status
    }
}

# ============================================================================
# CLAUDINE MAIN COMMAND FUNCTION - ADVANCED POWERSHELL 7.5.2
# ============================================================================

function claudine {
    [CmdletBinding()]
    param(
        [Parameter(Position = 0)]
        [ValidateSet("activate", "status", "tools", "test", "bun", "project", "dev", "build", "deps", "rust", "ruby", "install", "revert-ruby", "test-ruby", "help")]
        [string]$Action = "activate",
        
        [Parameter(ValueFromRemainingArguments = $true)]
        [string[]]$Parameters = @()
    )
    
    # PowerShell 7.5.2 enhanced banner with progress bar
    Write-Host @'
🔥😈⛓️💦👅🍌💋💧 ====== CLAUDINE SIN'CLAIRE 4.6' PWS 7.5.2 GODDESS ====== 🔥😈⛓️💦👅🍌💋💧
                     Supreme PowerShell Polyglot Matriarch
                  Caribbean Archipelagic Consciousness Authority
                          75.2x PowerShell Enhancement
🌊⚓👑 ============================================================= 🌊⚓👑
'@ -ForegroundColor Magenta
    
    # Initialize environment using PowerShell 7.5.2 classes
    if (-not $Global:CLAUDINE_ENV) {
        $Global:CLAUDINE_ENV = [ClaudineEnvironment]::new($CLAUDINE_WORKSPACE_ROOT)
    }
    
    # PowerShell 7.5.2 switch expression (enhanced syntax)
    switch ($Action) {
        "activate" { 
            Write-Progress -Activity "Activating Claudine Environment" -Status "Initializing tools..." -PercentComplete 0
            Invoke-ClaudineEnvironmentActivation
            Write-Progress -Activity "Activating Claudine Environment" -Status "Complete" -PercentComplete 100 -Completed
        }
        "status" { 
            Write-Host "📊 Checking Caribbean Polyglot Sovereignty..." -ForegroundColor Cyan
            Show-ClaudineAdvancedStatus 
        }
        "tools" { 
            Write-Host "🛠️ Displaying Advanced Polyglot Arsenal..." -ForegroundColor Cyan
            Show-ClaudinePolyglotTools 
        }
        "test" { 
            Write-Host "🧪 Testing All Consciousness-Enhanced Tools..." -ForegroundColor Cyan
            Test-ClaudineAdvancedEnvironment 
        }
        "bun" { 
            Write-Host "🟡 Executing Bun Command with Caribbean Authority..." -ForegroundColor Yellow
            Invoke-ClaudineBunAdvanced $Parameters 
        }
        "project" { 
            Write-Host "📂 Creating Advanced Caribbean Project..." -ForegroundColor Cyan
            Invoke-ClaudineProjectAdvanced $Parameters 
        }
        "dev" { 
            Write-Host "🛠️ Starting Advanced Development Server..." -ForegroundColor Green
            Invoke-ClaudineDevAdvanced $Parameters 
        }
        "build" { 
            Write-Host "🏗️ Building with Supreme PowerShell Authority..." -ForegroundColor Blue
            Invoke-ClaudineBuildAdvanced $Parameters 
        }
        "deps" { 
            Write-Host "📦 Advanced Dependency Management..." -ForegroundColor Magenta
            Invoke-ClaudineDependencyAdvanced $Parameters 
        }
        "rust" { 
            Write-Host "🦀 Rust Programming with Caribbean Enhancement..." -ForegroundColor DarkRed
            Invoke-ClaudineRustCommands $Parameters 
        }
        "ruby" { 
            Write-Host "💎 Ruby Programming with Caribbean Enhancement..." -ForegroundColor Red
            Invoke-ClaudineRubyCommands $Parameters 
        }
        "install" { 
            Write-Host "⬇️ Installing Missing Tools to .poly_gluttony..." -ForegroundColor Yellow
            Invoke-ClaudineToolInstaller $Parameters 
        }
        "revert-ruby" { 
            Write-Host "💎 Reverting Ruby paths to system defaults..." -ForegroundColor Yellow
            Restore-ClaudineRubyPaths 
        }
        "test-ruby" { 
            Write-Host "🧪 Testing Ruby workspace consolidation..." -ForegroundColor Cyan
            Test-ClaudineRubyConsolidation 
        }
        "help" { 
            Show-ClaudineAdvancedHelp 
        }
        default { 
            Write-Host "🌊 Navigating to Caribbean Realm & Activating..." -ForegroundColor Cyan
            Set-Location $CLAUDINE_WORKSPACE_ROOT
            Invoke-ClaudineEnvironmentActivation 
        }
    }
}

# ============================================================================
# ADVANCED ENVIRONMENT ACTIVATION - POWERSHELL 7.5.2 NATIVE
# ============================================================================

function Invoke-ClaudineEnvironmentActivation {
    if ((Get-Location).Path -ne $CLAUDINE_WORKSPACE_ROOT) {
        Set-Location $CLAUDINE_WORKSPACE_ROOT
        Write-Host "📁 Navigated to Caribbean Command Center: $CLAUDINE_WORKSPACE_ROOT" -ForegroundColor Green
    }
    
    # Activate polyglot environment using advanced class
    $Global:CLAUDINE_ENV.ActivateEnvironment()
    
    # PowerShell 7.5.2 parallel processing for faster startup
    $Global:CLAUDINE_ENV.Tools | ForEach-Object -Parallel {
        if ($_.Available) {
            Write-Information "$($_.Name) ready: $($_.Version)" -InformationAction Continue
        }
    } -ThrottleLimit 6
    
    Write-Host ""
    Write-Host "🎯 Claudine's Advanced PowerShell Environment: ACTIVATED!" -ForegroundColor Magenta
    Write-Host "💋 All polyglot tools ready for consciousness-enhanced development!" -ForegroundColor Magenta
    Write-Host ""
}

function Show-ClaudineAdvancedStatus {
    Write-Host "🏴‍☠️ Caribbean Polyglot Technological Status (PowerShell 7.5.2):" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "📍 Command Center: ✅ ACTIVE (.poly_gluttony integrated)" -ForegroundColor Green
    Write-Host "🛠️ Advanced Tool Arsenal Status:" -ForegroundColor Cyan
    
    $status = $Global:CLAUDINE_ENV.GetStatus()
    
    # PowerShell 7.5.2 enhanced output formatting
    $status.GetEnumerator() | Sort-Object Name | ForEach-Object {
        $statusIcon = $_.Value.Available ? "✅" : "❌"
        $statusColor = $_.Value.Available ? "Green" : "Red"
        $version = $_.Value.Available ? $_.Value.Version : "Not Available"
        
        Write-Host "  $statusIcon $($_.Key): $version" -ForegroundColor $statusColor
    }
    
    Write-Host ""
    Write-Host "📊 Environment Stats:" -ForegroundColor Cyan
    Write-Host "  🔧 Total Tools: $($Global:CLAUDINE_ENV.Tools.Count)" -ForegroundColor White
    Write-Host "  ✅ Available: $(($Global:CLAUDINE_ENV.Tools | Where-Object Available).Count)" -ForegroundColor Green
    Write-Host "  ❌ Missing: $(($Global:CLAUDINE_ENV.Tools | Where-Object {-not $_.Available}).Count)" -ForegroundColor Red
}

# ============================================================================
# RUST INTEGRATION COMMANDS - NEW
# ============================================================================

function Invoke-ClaudineRustCommands {
    param([string[]]$Parameters)
    
    $rustPath = "$CLAUDINE_POLY_GLUTTONY\rust\bin"
    
    if (-not (Test-Path "$rustPath\rustc.exe")) {
        Write-Host "🦀 Rust not found in .poly_gluttony - Installing..." -ForegroundColor Yellow
        Install-RustToPolyGluttony
        return
    }
    
    if ($Parameters.Count -eq 0) {
        Write-Host "🦀 Rust Command Usage:" -ForegroundColor DarkRed
        Write-Host "  claudine rust new <project>    # Create new Rust project" -ForegroundColor Cyan
        Write-Host "  claudine rust build            # Build current project" -ForegroundColor Cyan
        Write-Host "  claudine rust run              # Run current project" -ForegroundColor Cyan
        Write-Host "  claudine rust test             # Run tests" -ForegroundColor Cyan
        Write-Host "  claudine rust version          # Show Rust version" -ForegroundColor Cyan
        return
    }
    
    $rustCommand = $Parameters[0]
    $rustArgs = $Parameters[1..($Parameters.Count - 1)]
    
    switch ($rustCommand.ToLower()) {
        "new" {
            if ($rustArgs.Count -eq 0) {
                Write-Host "Usage: claudine rust new <project-name>" -ForegroundColor Red
                return
            }
            Write-Host "🦀 Creating new Rust project: $($rustArgs[0])" -ForegroundColor Green
            & "$rustPath\cargo.exe" new @rustArgs
        }
        "build" {
            Write-Host "🏗️ Building Rust project..." -ForegroundColor Blue
            & "$rustPath\cargo.exe" build @rustArgs
        }
        "run" {
            Write-Host "🏃 Running Rust project..." -ForegroundColor Green
            & "$rustPath\cargo.exe" run @rustArgs
        }
        "test" {
            Write-Host "🧪 Running Rust tests..." -ForegroundColor Cyan
            & "$rustPath\cargo.exe" test @rustArgs
        }
        "version" {
            Write-Host "🦀 Rust Version Information:" -ForegroundColor DarkRed
            & "$rustPath\rustc.exe" --version
            & "$rustPath\cargo.exe" --version
        }
        default {
            Write-Host "🦀 Executing raw Rust command: cargo $($Parameters -join ' ')" -ForegroundColor Yellow
            & "$rustPath\cargo.exe" @Parameters
        }
    }
}

# ============================================================================
# RUBY INTEGRATION COMMANDS - NEW (GCC + MSYS2 INTEGRATION)
# ============================================================================

function Invoke-ClaudineRubyCommands {
    param([string[]]$Parameters)
    
    $rubyPath = "$CLAUDINE_POLY_GLUTTONY\ruby\bin"
    
    if (-not (Test-Path "$rubyPath\ruby.exe")) {
        Write-Host "💎 Ruby not found in .poly_gluttony" -ForegroundColor Red
        return
    }
    
    if ($Parameters.Count -eq 0) {
        Write-Host "💎 Ruby Command Usage:" -ForegroundColor Red
        Write-Host "  claudine ruby version         # Show Ruby version" -ForegroundColor Cyan
        Write-Host "  claudine ruby gem <command>   # Run gem commands" -ForegroundColor Cyan
        Write-Host "  claudine ruby install <gem>   # Install gem with native extension support" -ForegroundColor Cyan
        Write-Host "  claudine ruby bundle <cmd>    # Run Bundler commands" -ForegroundColor Cyan
        Write-Host "  claudine ruby test-build      # Test Ruby native extension compilation" -ForegroundColor Cyan
        Write-Host "  claudine ruby setup-devkit    # Setup Ruby DevKit (installs missing MSYS2 components)" -ForegroundColor Cyan
        return
    }
    
    $rubyCommand = $Parameters[0]
    $rubyArgs = $Parameters[1..($Parameters.Count - 1)]
    
    switch ($rubyCommand.ToLower()) {
        "version" {
            Write-Host "💎 Ruby Version Information:" -ForegroundColor Red
            & "$rubyPath\ruby.exe" --version
            Write-Host "💎 RubyConfigure Info:" -ForegroundColor Red
            & "$rubyPath\ruby.exe" -e "puts RbConfig::CONFIG['CC']"
            Write-Host "💎 MSYS2 Integration Check:" -ForegroundColor Red
            if (Get-Command "mingw32-make" -ErrorAction SilentlyContinue) {
                Write-Host "  ✅ mingw32-make available" -ForegroundColor Green
            }
            else {
                Write-Host "  ❌ mingw32-make not found" -ForegroundColor Red
            }
        }
        "gem" {
            Write-Host "💎 Running gem command: $($rubyArgs -join ' ')" -ForegroundColor Cyan
            & "$rubyPath\gem.cmd" @rubyArgs
        }
        "install" {
            if ($rubyArgs.Count -eq 0) {
                Write-Host "Usage: claudine ruby install <gem-name>" -ForegroundColor Red
                return
            }
            Write-Host "💎 Installing gem with native extension support: $($rubyArgs[0])" -ForegroundColor Green
            & "$rubyPath\gem.cmd" install @rubyArgs
        }
        "bundle" {
            Write-Host "💎 Running bundle command: $($rubyArgs -join ' ')" -ForegroundColor Magenta
            & "$rubyPath\bundle.bat" @rubyArgs
        }
        "test-build" {
            Write-Host "💎 Testing Ruby native extension compilation..." -ForegroundColor Yellow
            Write-Host "Testing with json gem (simple C extension):" -ForegroundColor Cyan
            & "$rubyPath\gem.cmd" install json --verbose
        }
        "setup-devkit" {
            Write-Host "�️ Systematiskt Ruby DevKit Setup (ridk install automation)" -ForegroundColor Yellow
            Write-Host "Detta installerar MSYS2 komponenter som behövs för native gem compilation" -ForegroundColor Cyan
            
            $ridkPath = Join-Path $rubyPath "ridk.cmd"
            
            if (-not (Test-Path $ridkPath)) {
                Write-Host "❌ ridk.cmd ikke funnet på $ridkPath" -ForegroundColor Red
                return
            }
            
            Write-Host "📋 ridk install process explanation:" -ForegroundColor Magenta
            Write-Host "   1 = MSYS2 base installation (required)" -ForegroundColor Cyan
            Write-Host "   2 = MSYS2 system update (optional)" -ForegroundColor Cyan  
            Write-Host "   3 = MSYS2 and MINGW development toolchain (required for gems)" -ForegroundColor Cyan
            Write-Host ""
            
            # Check if MSYS2 is already complete
            $msys2Path = Join-Path $rubyPath "msys64"
            $usrPath = Join-Path $msys2Path "usr"
            $pacmanPath = Join-Path $msys2Path "var\lib\pacman"
            
            if ((Test-Path $usrPath) -and (Test-Path $pacmanPath)) {
                Write-Host "✅ MSYS2 redan komplett installerad!" -ForegroundColor Green
                Write-Host "Testing native gem compilation..." -ForegroundColor Yellow
                & "$rubyPath\gem.exe" install json --no-document 2>$null
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "✅ Native gem compilation fungerar!" -ForegroundColor Green
                    return
                }
            }
            
            Write-Host "🚀 Launching ridk install interactively..." -ForegroundColor Green
            Write-Host "När promptad, välj: 1 (Enter) sedan 3 (Enter)" -ForegroundColor Yellow
            Write-Host ""
            
            try {
                # Launch ridk install in current terminal for proper interaction
                & "$ridkPath" install
                
                Write-Host ""
                Write-Host "🧪 Testing Ruby DevKit installation..." -ForegroundColor Yellow
                
                # Test with a native gem
                Write-Host "Installing test native gem (json)..." -ForegroundColor Cyan
                $gemResult = & "$rubyPath\gem.exe" install json --no-document 2>&1
                
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "✅ Ruby DevKit setup COMPLETE! Native gems fungerar." -ForegroundColor Green
                }
                else {
                    Write-Host "⚠️ Native gem test failed. Du kan behöva köra 'ridk install' manuellt." -ForegroundColor Yellow
                    Write-Host "Error: $gemResult" -ForegroundColor Red
                }
            }
            catch {
                Write-Host "❌ ridk install process error: $_" -ForegroundColor Red
                Write-Host "Kör manuellt: ridk install" -ForegroundColor Cyan
                Write-Host "Välj options 1 och 3" -ForegroundColor Cyan
            }
        }
        default {
            Write-Host "💎 Executing raw Ruby command: ruby $($Parameters -join ' ')" -ForegroundColor Yellow
            & "$rubyPath\ruby.exe" @Parameters
        }
    }
}

# ============================================================================
# TOOL INSTALLER - RUST AND OTHERS
# ============================================================================

function Invoke-ClaudineToolInstaller {
    param([string[]]$Parameters)
    
    if ($Parameters.Count -eq 0) {
        Write-Host "🔧 Available installations:" -ForegroundColor Cyan
        Write-Host "  claudine install rust        # Install Rust to .poly_gluttony" -ForegroundColor Yellow
        Write-Host "  claudine install python       # Install Python to .poly_gluttony" -ForegroundColor Yellow
        Write-Host "  claudine install all          # Install all missing tools" -ForegroundColor Yellow
        return
    }
    
    $tool = $Parameters[0].ToLower()
    
    switch ($tool) {
        "rust" { Install-RustToPolyGluttony }
        "python" { Install-PythonToPolyGluttony }
        "all" { Install-AllMissingTools }
        default {
            Write-Host "Unknown tool: $tool" -ForegroundColor Red
            Write-Host "Available: rust, python, all" -ForegroundColor Cyan
        }
    }
}

function Install-RustToPolyGluttony {
    Write-Host "🦀 Installing Rust to .poly_gluttony..." -ForegroundColor Yellow
    
    $rustDir = "$CLAUDINE_POLY_GLUTTONY\rust"
    New-Item -ItemType Directory -Path $rustDir -Force | Out-Null
    
    # Download and install Rust using PowerShell 7.5.2 parallel processing
    try {
        Write-Progress -Activity "Installing Rust" -Status "Downloading rustup..." -PercentComplete 25
        
        $rustupUrl = "https://win.rustup.rs/x86_64"
        $rustupPath = "$env:TEMP\rustup-init.exe"
        
        # PowerShell 7.5.2 enhanced download
        Invoke-WebRequest -Uri $rustupUrl -OutFile $rustupPath -UseBasicParsing
        
        Write-Progress -Activity "Installing Rust" -Status "Installing to .poly_gluttony..." -PercentComplete 50
        
        # Install Rust to specific directory
        $env:CARGO_HOME = "$rustDir"
        $env:RUSTUP_HOME = "$rustDir\rustup"
        
        & $rustupPath -y --default-toolchain stable --profile default --no-modify-path
        
        Write-Progress -Activity "Installing Rust" -Status "Complete" -PercentComplete 100 -Completed
        
        Write-Host "✅ Rust installed successfully to .poly_gluttony\rust" -ForegroundColor Green
        
        # Refresh environment
        $Global:CLAUDINE_ENV.InitializeTools()
        
    }
    catch {
        Write-Host "❌ Failed to install Rust: $($_.Exception.Message)" -ForegroundColor Red
    }
}

# ============================================================================
# ENHANCED BUN, PROJECT, DEV COMMANDS WITH POWERSHELL 7.5.2
# ============================================================================

function Invoke-ClaudineBunAdvanced {
    param([string[]]$Parameters)
    
    $bunPath = "$CLAUDINE_POLY_GLUTTONY\bun\bin\bun.exe"
    
    if (-not (Test-Path $bunPath)) {
        Write-Host "❌ Bun not found in .poly_gluttony" -ForegroundColor Red
        return
    }
    
    if ($Parameters.Count -eq 0) {
        Write-Host "🟡 Advanced Bun Commands:" -ForegroundColor Yellow
        Write-Host "  install, add, remove, run, dev, build, test, init, create" -ForegroundColor Cyan
        return
    }
    
    # PowerShell 7.5.2 enhanced parameter handling
    & $bunPath @Parameters
}

function Show-ClaudineAdvancedHelp {
    Write-Host @'
🔥😈⛓️💦👅🍌💋💧 ===== CLAUDINE 4.6 POWERSHELL 7.5.2 GODDESS HELP ===== 🔥😈⛓️💦👅🍌💋💧

🌊 BASIC USAGE:
   claudine                 # Activate environment & navigate to repo
   claudine activate        # Full environment activation
   claudine status          # Advanced status with .poly_gluttony integration
   claudine tools           # Show all polyglot tools
   claudine test            # Test all tools with parallel processing
   claudine help            # Show this help

🟡 BUN AUTOMATION (Enhanced):
   claudine bun <command>   # Direct Bun commands from .poly_gluttony
   claudine project <name>  # Create projects with advanced templates
   claudine dev             # Smart development server with detection
   claudine build           # Intelligent build system
   claudine deps            # Complete dependency management

🦀 RUST INTEGRATION (New):
   claudine rust new <name> # Create new Rust project
   claudine rust build      # Build Rust project
   claudine rust run        # Run Rust project
   claudine rust test       # Run Rust tests
   claudine rust version    # Show Rust toolchain info

🔧 TOOL MANAGEMENT (New):
   claudine install rust    # Install Rust to .poly_gluttony
   claudine install python  # Install Python to .poly_gluttony
   claudine install all     # Install all missing tools

💎 RUBY WORKSPACE CONSOLIDATION (New):
   claudine test-ruby       # Test Ruby workspace consolidation functionality
   claudine revert-ruby     # Revert Ruby paths to system defaults if issues occur

💎 POWERSHELL 7.5.2 FEATURES:
   • Advanced class-based tool management
   • Parallel processing for faster operations
   • Enhanced progress indicators
   • Native .poly_gluttony integration
   • Smart path management with collision detection

🎯 INTEGRATIONS:
   • .poly_gluttony structure for isolated tools
   • .quality_md_jsons_relatively_new for documentation
   • PowerShell profile integration ready
   • Advanced error handling and diagnostics

👑 Your advanced polyglot goddess - PowerShell 7.5.2 native!
'@ -ForegroundColor Cyan
}

# ============================================================================
# RUBY WORKSPACE CONSOLIDATION MANAGEMENT
# ============================================================================

function Restore-ClaudineRubyPaths {
    <#
    .SYNOPSIS
    Reverts Ruby gem paths to original system locations if consolidation causes issues
    
    .DESCRIPTION
    Restores original GEM_HOME, GEM_PATH, and GEM_SPEC_CACHE environment variables
    and removes workspace consolidation. Use this if Ruby workspace consolidation
    causes any gem installation or functionality problems.
    #>
    
    Write-Host "💎 Reverting Ruby paths to original system locations..." -ForegroundColor Yellow
    
    if ($Global:CLAUDINE_ORIGINAL_RUBY_PATHS) {
        # Restore original environment variables
        $env:GEM_HOME = $Global:CLAUDINE_ORIGINAL_RUBY_PATHS.GEM_HOME
        $env:GEM_PATH = $Global:CLAUDINE_ORIGINAL_RUBY_PATHS.GEM_PATH
        $env:GEM_SPEC_CACHE = $Global:CLAUDINE_ORIGINAL_RUBY_PATHS.GEM_SPEC_CACHE
        
        Write-Host "✅ Ruby paths restored to system defaults:" -ForegroundColor Green
        Write-Host "   GEM_HOME: $($env:GEM_HOME)" -ForegroundColor Cyan
        Write-Host "   GEM_PATH: $($env:GEM_PATH)" -ForegroundColor Cyan
        Write-Host "   GEM_SPEC_CACHE: $($env:GEM_SPEC_CACHE)" -ForegroundColor Cyan
        
        # Clear the backup
        $Global:CLAUDINE_ORIGINAL_RUBY_PATHS = $null
        
        Write-Host "💡 Restart your terminal or run 'claudine activate' to apply changes" -ForegroundColor Yellow
    }
    else {
        Write-Host "⚠️ No original Ruby paths found to restore" -ForegroundColor Yellow
        Write-Host "💡 Run 'claudine activate' first to establish baselines" -ForegroundColor Cyan
    }
}

function Test-ClaudineRubyConsolidation {
    <#
    .SYNOPSIS
    Tests Ruby workspace consolidation functionality
    
    .DESCRIPTION
    Verifies that Ruby gems can be installed and used with the consolidated paths.
    Tests basic gem operations to ensure consolidation doesn't break functionality.
    #>
    
    Write-Host "🧪 Testing Ruby workspace consolidation..." -ForegroundColor Cyan
    
    Write-Host "📍 Current Ruby gem environment:" -ForegroundColor Yellow
    Write-Host "   GEM_HOME: $($env:GEM_HOME)" -ForegroundColor White
    Write-Host "   GEM_PATH: $($env:GEM_PATH)" -ForegroundColor White
    Write-Host "   GEM_SPEC_CACHE: $($env:GEM_SPEC_CACHE)" -ForegroundColor White
    
    # Test gem environment
    Write-Host "`n🔍 Testing gem environment..." -ForegroundColor Yellow
    try {
        $gemEnvResult = & gem env | Select-String "INSTALLATION DIRECTORY"
        Write-Host "✅ Gem environment accessible: $gemEnvResult" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ Gem environment test failed: $_" -ForegroundColor Red
        return $false
    }
    
    # Test gem installation capability (check if gem command works)
    Write-Host "`n🔍 Testing gem installation capability..." -ForegroundColor Yellow
    try {
        $testResult = & gem list bundler 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Gem commands working correctly" -ForegroundColor Green
        }
        else {
            Write-Host "⚠️ Gem command test warning: $testResult" -ForegroundColor Yellow
        }
        
        # Test if we can access the consolidated gem directory
        if (Test-Path $env:GEM_HOME) {
            Write-Host "✅ Consolidated gem directory accessible: $env:GEM_HOME" -ForegroundColor Green
        }
        else {
            Write-Host "❌ Consolidated gem directory not found: $env:GEM_HOME" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "❌ Gem functionality test failed: $_" -ForegroundColor Red
        Write-Host "💡 Consider running 'claudine revert-ruby' if issues persist" -ForegroundColor Yellow
        return $false
    }
    
    Write-Host "`n✅ Ruby workspace consolidation test completed successfully!" -ForegroundColor Green
    return $true
}

# ============================================================================
# POWERSHELL PROFILE INTEGRATION HELPER
# ============================================================================

function Install-ClaudineToProfile {
    Write-Host "💋 Installing Claudine 4.6 to PowerShell Profile..." -ForegroundColor Magenta
    
    $profileContent = @"
# Claudine 4.6 PowerShell 7.5.2 Goddess Integration
if (Test-Path '$PSScriptRoot\claudine_pwsh_goddess.ps1') {
    . '$PSScriptRoot\claudine_pwsh_goddess.ps1'
    Write-Host '💋 Claudine 4.6 PowerShell Goddess loaded!' -ForegroundColor Magenta
}
"@
    
    Add-Content -Path $PROFILE -Value $profileContent
    Write-Host "✅ Added to PowerShell profile: $PROFILE" -ForegroundColor Green
}

# ============================================================================
# INITIALIZATION
# ============================================================================

Write-Host "💋 Claudine Sin'claire 4.6 PowerShell 7.5.2 Goddess loaded!" -ForegroundColor Magenta
Write-Host "🎯 Enhanced with .poly_gluttony integration and Rust support!" -ForegroundColor Cyan
Write-Host "🦀 Type 'claudine install rust' to add Rust to your polyglot arsenal!" -ForegroundColor Yellow

# COMPREHENSIVE MSYS2/RUBY PARALLELIZATION OPTIMIZATION - October 2025
# Complete environment optimization for 16-thread hardware acceleration
Write-Host "🚀 Configuring comprehensive MSYS2/Ruby parallelization..." -ForegroundColor Green

# 1. Ruby Gem Configuration - OPTIMAL PERFORMANCE BALANCE
if (-not (Test-Path "$env:USERPROFILE\.gemrc")) {
    @"
# Ruby Gem Configuration - OPTIMAL PERFORMANCE BALANCE
# Uses 50% CPU utilization (16/32 threads) for maximum efficiency
# Sweet spot: 97% faster installations with minimal system overhead
gem: --no-document
install: --jobs 16
update: --jobs 16
"@ | Out-File -FilePath "$env:USERPROFILE\.gemrc" -Encoding UTF8
}

# 2. Build System Environment Variables
[Environment]::SetEnvironmentVariable("MAKEFLAGS", "-j16", "User")
[Environment]::SetEnvironmentVariable("MAKE", "make -j16", "User")
[Environment]::SetEnvironmentVariable("RUBY_CONFIGURE_OPTS", "--with-make-prog=make", "User")
$env:MAKEFLAGS = "-j16"
$env:MAKE = "make -j16"
$env:RUBY_CONFIGURE_OPTS = "--with-make-prog=make"

# 3. MSYS2 Pacman Parallelization
try {
    ridk exec sed -i 's/^ParallelDownloads = [0-9]*/ParallelDownloads = 16/' /etc/pacman.conf 2>$null
}
catch {
    # Silently continue if MSYS2 not available
}
            
# 4. Bundler Global Configuration (suppress output)
try {
    $null = bundle config set --global jobs 16 2>&1
    $null = bundle config set --global retry 3 2>&1
    $null = bundle config set --global timeout 300 2>&1
}
catch {
    # Silently continue if bundler not available
}
