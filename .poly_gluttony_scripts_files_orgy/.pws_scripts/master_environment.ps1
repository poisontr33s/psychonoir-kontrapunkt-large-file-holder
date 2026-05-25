#!/usr/bin/env pwsh

# PsychoNoir-Kontrapunkt Master Environment Manager
# Comprehensive script for setup, activation, checking, and maintenance

param(
    [Parameter(Mandatory = $false)]
    [ValidateSet("install", "activate", "check", "audit", "fix-paths", "update-profile", "help")]
    [string]$Action = "help",
    
    [Parameter(Mandatory = $false)]
    [string[]]$SkipTools = @(),
    
    [Parameter(Mandatory = $false)]
    [switch]$Force
)

# Script metadata
$ScriptVersion = "2.0.0"
$LastUpdated = "October 11, 2025"

# ============================================================================
# BANNER AND HELP
# ============================================================================

function Show-Banner {
    Write-Host @'
🚀 ========================================================== 🚀
    PsychoNoir-Kontrapunkt Master Environment Manager
    Complete Isolated Development Environment
    Version: 2.0.0 | Last Updated: October 11, 2025
🚀 ========================================================== 🚀
'@ -ForegroundColor Cyan
}

function Show-Help {
    Show-Banner
    Write-Host @'

📋 USAGE:
    .\master_environment.ps1 -Action <action> [options]

🎯 ACTIONS:
    install         Install all development tools (9 tools total)
    activate        Activate environment (forced root configuration)
    check           Comprehensive environment status check
    audit           Full system audit and validation
    fix-paths       Fix Ruby/MSYS64/MinGW64 toolchain paths
    update-profile  Install/update PowerShell profile with convenience functions
    help            Show this help message

🔧 OPTIONS:
    -SkipTools      Skip specific tools during installation
                    Example: -SkipTools "Ruby","Rust"
    -Force          Force operations (overwrite existing files)

💡 EXAMPLES:
    .\master_environment.ps1 -Action install
    .\master_environment.ps1 -Action activate
    .\master_environment.ps1 -Action check
    .\master_environment.ps1 -Action audit
    .\master_environment.ps1 -Action install -SkipTools "Ruby"

🎯 CONVENIENCE FUNCTIONS (after profile installation):
    psycho          Jump to PsychoNoir-Kontrapunkt from anywhere
    activate        Activate environment from anywhere
    check           Check environment status from anywhere
    new-project     Create new project templates

📊 ENVIRONMENT STATUS:
'@ -ForegroundColor White
    
    # Show current environment status if scripts exist
    if (Test-Path ".\check_environment.ps1") {
        Write-Host "Running quick status check..." -ForegroundColor Yellow
        & ".\check_environment.ps1" | Select-Object -First 15
    }
    else {
        Write-Host "⚠️  Environment not yet set up. Run: .\master_environment.ps1 -Action install" -ForegroundColor Yellow
    }
}

# ============================================================================
# CORE FUNCTIONS
# ============================================================================

function Invoke-InstallAll {
    param([string[]]$SkipTools = @())
    
    Write-Host "🔧 Installing PsychoNoir-Kontrapunkt Development Environment..." -ForegroundColor Cyan
    
    if (Test-Path ".\install_all.ps1") {
        if ($SkipTools.Count -gt 0) {
            Write-Host "⏭️  Skipping tools: $($SkipTools -join ', ')" -ForegroundColor Yellow
            & ".\install_all.ps1" -SkipTools $SkipTools
        }
        else {
            & ".\install_all.ps1"
        }
    }
    else {
        Write-Error "❌ install_all.ps1 not found. Ensure you're in the PsychoNoir-Kontrapunkt directory."
        return $false
    }
    
    Write-Host "✅ Installation complete! Run 'master_environment.ps1 -Action activate' to activate." -ForegroundColor Green
    return $true
}

function Invoke-ActivateEnvironment {
    Write-Host "🚀 Activating PsychoNoir-Kontrapunkt Environment..." -ForegroundColor Cyan
    
    if (Test-Path ".\activate_environment.ps1") {
        & ".\activate_environment.ps1"
        Write-Host "✅ Environment activated! All tools are now available." -ForegroundColor Green
        return $true
    }
    else {
        Write-Error "❌ activate_environment.ps1 not found. Run installation first."
        return $false
    }
}

function Invoke-CheckEnvironment {
    Write-Host "🔍 Checking PsychoNoir-Kontrapunkt Environment Status..." -ForegroundColor Cyan
    
    if (Test-Path ".\check_environment.ps1") {
        & ".\check_environment.ps1"
        return $true
    }
    else {
        Write-Error "❌ check_environment.ps1 not found. Run installation first."
        return $false
    }
}

function Invoke-AuditEnvironment {
    Write-Host "📊 Running Comprehensive Environment Audit..." -ForegroundColor Cyan
    
    # Run all available diagnostic scripts
    $AuditScripts = @(
        ".\check_environment.ps1",
        ".\activate_environment.ps1"
    )
    
    foreach ($Script in $AuditScripts) {
        if (Test-Path $Script) {
            Write-Host "🔄 Running $Script..." -ForegroundColor Yellow
            & $Script
            Write-Host ""
        }
    }
    
    # Check for recent audit reports
    $AuditReports = Get-ChildItem -Name "*AUDIT*", "*REPORT*" | Sort-Object LastWriteTime -Descending | Select-Object -First 3
    if ($AuditReports) {
        Write-Host "📋 Recent Audit Reports Found:" -ForegroundColor Green
        foreach ($Report in $AuditReports) {
            $FileInfo = Get-Item $Report
            Write-Host "  📄 $($Report) ($(($FileInfo.LastWriteTime).ToString('yyyy-MM-dd HH:mm')))" -ForegroundColor Gray
        }
    }
    
    Write-Host "✅ Comprehensive audit complete!" -ForegroundColor Green
    return $true
}

function Invoke-FixPaths {
    Write-Host "🔧 Applying Ruby/MSYS64/MinGW64 Toolchain Path Fixes..." -ForegroundColor Cyan
    
    # Check if common_config.ps1 exists and contains the fixes
    if (Test-Path ".\common_config.ps1") {
        $ConfigContent = Get-Content ".\common_config.ps1" -Raw
        
        if ($ConfigContent -like "*mingw64\bin*" -and $ConfigContent -like "*msys64\usr\bin*" -and $ConfigContent -like "*msys64\ucrt64\bin*") {
            Write-Host "✅ Path fixes already applied!" -ForegroundColor Green
            Write-Host "   📁 MinGW64 GCC Toolchain: .computer_languages\mingw64\bin" -ForegroundColor Gray
            Write-Host "   📁 MSYS2 Unix Tools: .computer_languages\msys64\usr\bin" -ForegroundColor Gray
            Write-Host "   📁 MSYS2 UCRT64: .computer_languages\msys64\ucrt64\bin" -ForegroundColor Gray
        }
        else {
            Write-Host "⚠️  Path configuration needs updating. Please apply manual fixes or reinstall." -ForegroundColor Yellow
        }
    }
    else {
        Write-Error "❌ common_config.ps1 not found. Run installation first."
        return $false
    }
    
    # Test the paths
    Write-Host "🧪 Testing toolchain accessibility..." -ForegroundColor Yellow
    & ".\activate_environment.ps1"
    
    return $true
}

function Invoke-UpdateProfile {
    Write-Host "⚡ Installing/Updating PowerShell Profile..." -ForegroundColor Cyan
    
    if (Test-Path ".\powershell_profile.ps1") {
        # Install profile
        $ProfileDir = Split-Path $PROFILE
        if (-Not (Test-Path $ProfileDir)) {
            New-Item -ItemType Directory -Path $ProfileDir -Force | Out-Null
        }
        
        Copy-Item ".\powershell_profile.ps1" $PROFILE -Force
        Write-Host "✅ PowerShell profile installed at: $PROFILE" -ForegroundColor Green
        
        # Load profile for current session
        . $PROFILE
        
        Write-Host "🎯 Convenience functions now available:" -ForegroundColor Green
        Write-Host "   psycho          - Jump to repository from anywhere" -ForegroundColor Gray
        Write-Host "   activate        - Activate environment from anywhere" -ForegroundColor Gray
        Write-Host "   check           - Check environment status from anywhere" -ForegroundColor Gray
        Write-Host "   new-project     - Create new project templates" -ForegroundColor Gray
        
        return $true
    }
    else {
        Write-Error "❌ powershell_profile.ps1 not found. Run installation first."
        return $false
    }
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

switch ($Action.ToLower()) {
    "install" {
        Show-Banner
        $Success = Invoke-InstallAll -SkipTools $SkipTools
        if ($Success) {
            Write-Host ""
            Write-Host "🎯 Next Steps:" -ForegroundColor Cyan
            Write-Host "1. Run: .\master_environment.ps1 -Action activate" -ForegroundColor White
            Write-Host "2. Run: .\master_environment.ps1 -Action update-profile" -ForegroundColor White
            Write-Host "3. Run: .\master_environment.ps1 -Action check" -ForegroundColor White
        }
    }
    
    "activate" {
        Show-Banner
        Invoke-ActivateEnvironment
    }
    
    "check" {
        Show-Banner
        Invoke-CheckEnvironment
    }
    
    "audit" {
        Show-Banner
        Invoke-AuditEnvironment
    }
    
    "fix-paths" {
        Show-Banner
        Invoke-FixPaths
    }
    
    "update-profile" {
        Show-Banner
        Invoke-UpdateProfile
    }
    
    "help" {
        Show-Help
    }
    
    default {
        Write-Error "❌ Unknown action: $Action"
        Show-Help
    }
}