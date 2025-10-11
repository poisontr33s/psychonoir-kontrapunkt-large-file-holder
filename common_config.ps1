# PsychoNoir-Kontrapunkt Common Configuration
# Forces environment root to C:\Users\erdno\PsychoNoir-Kontrapunkt regardless of current directory

# ============================================================================
# FORCED ROOT DIRECTORY CONFIGURATION
# ============================================================================

# Define the absolute root directory (NEVER CHANGES)
$FORCED_REPO_ROOT = "C:\Users\erdno\PsychoNoir-Kontrapunkt"

# Function to force set the repository root
function Set-ForcedRepoRoot {
    # Always return the hardcoded path, ignore $PSScriptRoot or current directory
    return $FORCED_REPO_ROOT
}

# Function to validate and ensure we're working with the correct root
function Test-RepoRoot {
    param([string]$Path = $FORCED_REPO_ROOT)
    
    $RequiredMarkers = @(
        "README.md",
        "activate_environment.ps1", 
        ".computer_languages",
        "projects",
        "scripts"
    )
    
    foreach ($Marker in $RequiredMarkers) {
        $MarkerPath = Join-Path $Path $Marker
        if (-not (Test-Path $MarkerPath)) {
            Write-Warning "⚠️  Missing required marker: $MarkerPath"
            return $false
        }
    }
    
    return $true
}

# Function to force change directory to repo root
function Set-RepoLocation {
    try {
        Set-Location $FORCED_REPO_ROOT -ErrorAction Stop
        Write-Host "📁 Forced location to: $FORCED_REPO_ROOT" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Error "❌ Cannot access forced root directory: $FORCED_REPO_ROOT"
        Write-Error "   Error: $($_.Exception.Message)"
        return $false
    }
}

# ============================================================================
# ENVIRONMENT PATH CONFIGURATION
# ============================================================================

# Function to get all tool paths based on forced root
function Get-ToolPaths {
    $Root = $FORCED_REPO_ROOT
    return @(
        "$Root\.computer_languages\javascript"                 # Bun, Bunx & Biome
        "$Root\.computer_languages\javascript\node_modules\.bin" # NPM tools (if any)
        "$Root\.computer_languages\python"                     # Python, uv, uvx, ruff
        "$Root\.computer_languages\python\Scripts"             # Python Scripts
        "$Root\.computer_languages\rust\bin"                   # Rust & Cargo
        "$Root\.computer_languages\ruby\bin"                   # Ruby
        "$Root\.computer_languages\ruby\msys64\mingw64\bin"    # Ruby DevKit
        "$Root\.computer_languages\curl"                       # curl
    )
}

# Function to set environment variables based on forced root
function Set-EnvironmentVariables {
    $Root = $FORCED_REPO_ROOT
    
    # Python environment
    if (Test-Path "$Root\.computer_languages\python") {
        $env:PYTHONHOME = "$Root\.computer_languages\python"
        $env:PYTHONPATH = "$Root\.computer_languages\python\Lib;$Root\.computer_languages\python\Lib\site-packages"
    }
    
    # Ruby environment
    if (Test-Path "$Root\.computer_languages\ruby") {
        $env:RUBY_HOME = "$Root\.computer_languages\ruby"
    }
    
    # Rust environment
    if (Test-Path "$Root\.computer_languages\rust") {
        $env:CARGO_HOME = "$Root\.computer_languages\rust"
        $env:RUSTUP_HOME = "$Root\.computer_languages\rust\rustup"
    }
    
    # Force working directory environment variable
    $env:PSYCHO_NOIR_ROOT = $FORCED_REPO_ROOT
    $env:REPO_ROOT = $FORCED_REPO_ROOT
}

# ============================================================================
# AUTOMATIC INITIALIZATION
# ============================================================================

# Function to initialize the forced environment
function Initialize-ForcedEnvironment {
    param([switch]$Quiet = $false)
    
    if (-not $Quiet) {
        Write-Host "🎯 Initializing PsychoNoir-Kontrapunkt Forced Environment..." -ForegroundColor Cyan
        Write-Host "📍 Root Directory: $FORCED_REPO_ROOT" -ForegroundColor White
    }
    
    # Test if the forced root exists and is valid
    if (-not (Test-Path $FORCED_REPO_ROOT)) {
        Write-Error "❌ FORCED ROOT DIRECTORY DOES NOT EXIST: $FORCED_REPO_ROOT"
        return $false
    }
    
    if (-not (Test-RepoRoot $FORCED_REPO_ROOT)) {
        Write-Error "❌ FORCED ROOT DIRECTORY IS NOT A VALID PSYCHO-NOIR REPOSITORY"
        return $false
    }
    
    # Force change to the correct directory
    if (-not (Set-RepoLocation)) {
        return $false
    }
    
    # Set environment variables
    Set-EnvironmentVariables
    
    if (-not $Quiet) {
        Write-Host "✅ Forced environment initialized successfully!" -ForegroundColor Green
    }
    
    return $true
}

# ============================================================================
# EXPORT FUNCTIONS AND VARIABLES
# ============================================================================

# Make key variables and functions available globally
$global:PSYCHO_NOIR_ROOT = $FORCED_REPO_ROOT
$global:REPO_ROOT = $FORCED_REPO_ROOT

# Functions and variables are available globally when dot-sourced

# ============================================================================
# AUTO-INITIALIZATION (runs when this file is loaded)
# ============================================================================

# Automatically initialize when this config is loaded
if ($MyInvocation.InvocationName -ne '.') {
    Initialize-ForcedEnvironment -Quiet:$false
}
