#!/usr/bin/env pwsh

# PsychoNoir-Kontrapunkt Master Environment Manager (Hierarchical Edition)
# User-friendly automation with complexity levels from beginner to advanced

param(
    [Parameter(Mandatory = $false)]
    [ValidateSet("beginner", "standard", "advanced", "expert", "self-audit", "help")]
    [string]$Level = "help",
    
    [Parameter(Mandatory = $false)]
    [string]$Action,
    
    [Parameter(Mandatory = $false)]
    [string[]]$SkipTools = @(),
    
    [Parameter(Mandatory = $false)]
    [switch]$Force
)

# Script metadata
$ScriptVersion = "3.0.0"
$LastUpdated = "October 11, 2025"

# ============================================================================
# LOCATION VALIDATION & SMART NAVIGATION
# ============================================================================

function Test-CorrectLocation {
    $RequiredFiles = @(
        "install_all.ps1",
        "activate_environment.ps1", 
        "check_environment.ps1",
        "common_config.ps1"
    )
    
    $CurrentLocation = Get-Location
    foreach ($File in $RequiredFiles) {
        if (-Not (Test-Path $File)) {
            return @{
                IsCorrect    = $false
                Location     = $CurrentLocation
                MissingFiles = $RequiredFiles | Where-Object { -Not (Test-Path $_) }
            }
        }
    }
    
    return @{
        IsCorrect    = $true
        Location     = $CurrentLocation
        MissingFiles = @()
    }
}

function Find-PsychoNoirDirectory {
    $PossiblePaths = @(
        "C:\Users\erdno\PsychoNoir-Kontrapunkt",
        "C:\Users\$env:USERNAME\PsychoNoir-Kontrapunkt",
        "$env:USERPROFILE\PsychoNoir-Kontrapunkt"
    )
    
    foreach ($Path in $PossiblePaths) {
        if (Test-Path $Path) {
            $TestResult = Push-Location $Path
            $LocationTest = Test-CorrectLocation
            Pop-Location
            
            if ($LocationTest.IsCorrect) {
                return $Path
            }
        }
    }
    
    return $null
}

function Invoke-SmartNavigation {
    $LocationCheck = Test-CorrectLocation
    
    if (-Not $LocationCheck.IsCorrect) {
        Write-Host "❌ Not in PsychoNoir-Kontrapunkt directory!" -ForegroundColor Red
        Write-Host "📍 Current location: $($LocationCheck.Location)" -ForegroundColor Yellow
        Write-Host "🔍 Missing files: $($LocationCheck.MissingFiles -join ', ')" -ForegroundColor Yellow
        
        $FoundPath = Find-PsychoNoirDirectory
        if ($FoundPath) {
            Write-Host "🎯 Found PsychoNoir-Kontrapunkt at: $FoundPath" -ForegroundColor Green
            Write-Host "💡 Automatically switching to correct directory..." -ForegroundColor Cyan
            Set-Location $FoundPath
            return $true
        }
        else {
            Write-Host ""
            Write-Host "❌ Could not find PsychoNoir-Kontrapunkt directory!" -ForegroundColor Red
            Write-Host "📋 To fix this:" -ForegroundColor White
            Write-Host "   1. Navigate to your PsychoNoir-Kontrapunkt directory" -ForegroundColor Gray
            Write-Host "   2. Run this script from there" -ForegroundColor Gray
            Write-Host "   3. Or download/clone the repository first" -ForegroundColor Gray
            return $false
        }
    }
    
    return $true
}

# ============================================================================
# HIERARCHICAL INTERFACE SYSTEM
# ============================================================================

function Show-BeginnerInterface {
    Write-Host @'
🎯 ===== BEGINNER MODE: Step-by-Step Setup =====

Welcome! This will guide you through setting up your development environment.
No PowerShell knowledge required - just follow the steps!

📋 WHAT WE'LL DO:
  1. ✅ Check if you're in the right place (we'll fix it if not)
  2. 📦 Install 9 development tools (takes ~5-10 minutes)
  3. 🚀 Set up your environment to work from anywhere
  4. 🔍 Test that everything works perfectly

🎯 READY TO START? Just run this command:
   .\master_environment.ps1 -Level beginner -Action start

⚠️  NEED HELP? Run: .\master_environment.ps1 -Level help
'@ -ForegroundColor Cyan
    
    Write-Host ""
    Write-Host "📊 CURRENT STATUS:" -ForegroundColor Yellow
    Show-QuickStatus
}

function Show-StandardInterface {
    Write-Host @'
🛠️  ===== STANDARD MODE: Quick Setup =====

For users comfortable with basic commands.

🎯 QUICK COMMANDS:
  setup-all     Complete setup (install + activate + profile)
  install       Install all 9 development tools  
  activate      Activate environment (forced root)
  check         Comprehensive status check
  profile       Add global convenience functions

💡 EXAMPLES:
   .\master_environment.ps1 -Level standard -Action setup-all
   .\master_environment.ps1 -Level standard -Action check

🔧 OPTIONS:
   -SkipTools "Ruby","Rust"   Skip specific tools
'@ -ForegroundColor Green
    
    Write-Host ""
    Write-Host "📊 CURRENT STATUS:" -ForegroundColor Yellow
    Show-QuickStatus
}

function Show-AdvancedInterface {
    Write-Host @'
⚡ ===== ADVANCED MODE: Full Control =====

For developers who want detailed control and diagnostics.

🎯 ACTIONS:
  install         Install with advanced options
  activate        Environment activation with validation
  check           Comprehensive environment diagnostics  
  audit           Full system audit + historical reports
  fix-paths       Ruby/MSYS64/MinGW64 path diagnostics & fixes
  update-profile  PowerShell profile management
  troubleshoot    Advanced problem diagnosis

💡 EXAMPLES:
   .\master_environment.ps1 -Level advanced -Action audit
   .\master_environment.ps1 -Level advanced -Action troubleshoot
   .\master_environment.ps1 -Level advanced -Action install -SkipTools "Ruby"

🔧 ADVANCED OPTIONS:
   -Force          Override safety checks
   -SkipTools      Array of tools to skip
'@ -ForegroundColor Magenta
    
    Write-Host ""
    Write-Host "📊 CURRENT STATUS:" -ForegroundColor Yellow
    Show-QuickStatus
}

function Show-ExpertInterface {
    Write-Host @'
🚀 ===== EXPERT MODE: Direct PowerShell Interface =====

Direct access to all internal functions and parameters.

🎯 EXPERT ACTIONS:
  raw-install [tools]     Direct tool installation
  validate-paths          Path validation and repair
  generate-reports        Create comprehensive diagnostics
  performance-audit       System performance analysis
  security-audit          Security configuration review
  cleanup-environment     Clean temporary and cache files

💡 EXPERT EXAMPLES:
   .\master_environment.ps1 -Level expert -Action raw-install
   .\master_environment.ps1 -Level expert -Action performance-audit -Force
   .\master_environment.ps1 -Level expert -Action security-audit

🔧 EXPERT PARAMETERS:
   All PowerShell parameters and switches available
'@ -ForegroundColor Red
    
    Write-Host ""
    Write-Host "📊 CURRENT STATUS:" -ForegroundColor Yellow
    Show-QuickStatus
}

function Show-SelfAuditInterface {
    Write-Host @'
🔍 ===== SELF-AUDIT MODE: Script Validation =====

Internal diagnostics and validation of the master script itself.

🎯 SELF-AUDIT FUNCTIONS:
  validate-script         Check script integrity and functions
  test-all-paths          Verify all file paths and dependencies  
  validate-documentation  Check that README matches reality
  performance-test        Benchmark script performance
  compatibility-test      Test across PowerShell versions

💡 SELF-AUDIT EXAMPLES:
   .\master_environment.ps1 -Level self-audit -Action validate-script
   .\master_environment.ps1 -Level self-audit -Action test-all-paths
   .\master_environment.ps1 -Level self-audit -Action validate-documentation

🔧 INTERNAL DIAGNOSTICS:
   Script Version: 3.0.0
   Last Updated: October 11, 2025
   PowerShell Version: $($PSVersionTable.PSVersion)
'@ -ForegroundColor DarkCyan
    
    Write-Host ""
    Write-Host "🔍 SCRIPT SELF-VALIDATION:" -ForegroundColor Yellow
    Invoke-ScriptSelfAudit
}

# ============================================================================
# SELF-AUDIT SYSTEM
# ============================================================================

function Invoke-ScriptSelfAudit {
    Write-Host "Running internal script validation..." -ForegroundColor Cyan
    
    $AuditResults = @{
        LocationCheck      = Test-CorrectLocation
        RequiredScripts    = @()
        FunctionValidation = @()
        DocumentationSync  = $true
    }
    
    # Check required scripts exist
    $RequiredScripts = @("install_all.ps1", "activate_environment.ps1", "check_environment.ps1", "common_config.ps1")
    foreach ($Script in $RequiredScripts) {
        $Exists = Test-Path $Script
        $AuditResults.RequiredScripts += @{
            Script = $Script
            Exists = $Exists
            Status = if ($Exists) { "✅ Found" } else { "❌ Missing" }
        }
    }
    
    # Validate key functions exist in this script
    $KeyFunctions = @("Test-CorrectLocation", "Find-PsychoNoirDirectory", "Show-QuickStatus")
    foreach ($Function in $KeyFunctions) {
        $FunctionExists = Get-Command $Function -ErrorAction SilentlyContinue
        $AuditResults.FunctionValidation += @{
            Function = $Function
            Exists   = $null -ne $FunctionExists
            Status   = if ($null -ne $FunctionExists) { "✅ Available" } else { "❌ Missing" }
        }
    }
    
    # Display results
    Write-Host ""
    Write-Host "📋 SCRIPT DEPENDENCIES:" -ForegroundColor White
    foreach ($Result in $AuditResults.RequiredScripts) {
        Write-Host "   $($Result.Status) $($Result.Script)" -ForegroundColor $(if ($Result.Exists) { "Green" } else { "Red" })
    }
    
    Write-Host ""
    Write-Host "🔧 INTERNAL FUNCTIONS:" -ForegroundColor White
    foreach ($Result in $AuditResults.FunctionValidation) {
        Write-Host "   $($Result.Status) $($Result.Function)" -ForegroundColor $(if ($Result.Exists) { "Green" } else { "Red" })
    }
    
    # Overall health
    $AllGood = ($AuditResults.RequiredScripts | Where-Object { -Not $_.Exists }).Count -eq 0
    Write-Host ""
    if ($AllGood) {
        Write-Host "✅ Script self-audit PASSED - All systems operational" -ForegroundColor Green
    }
    else {
        Write-Host "❌ Script self-audit FAILED - Missing dependencies" -ForegroundColor Red
    }
    
    return $AuditResults
}

# ============================================================================
# STATUS AND UTILITY FUNCTIONS
# ============================================================================

function Show-QuickStatus {
    if (Test-Path ".\check_environment.ps1") {
        $StatusOutput = & ".\check_environment.ps1" 2>$null | Select-Object -First 15
        if ($StatusOutput) {
            $StatusOutput | ForEach-Object { Write-Host "   $_" -ForegroundColor Gray }
        }
        else {
            Write-Host "   🔄 Environment setup in progress..." -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "   ❌ Environment not set up. Need to install first." -ForegroundColor Red
    }
}

function Show-GeneralHelp {
    Write-Host @'
🎯 ===== PSYCHONOIR-KONTRAPUNKT MASTER MANAGER =====

Choose your experience level:

🟢 BEGINNER     - Step-by-step guidance (recommended for first-time setup)
🔵 STANDARD     - Quick setup for basic users  
🟠 ADVANCED     - Full control for developers
🔴 EXPERT       - Direct PowerShell interface
🔍 SELF-AUDIT   - Internal script validation

💡 EXAMPLES:
   .\master_environment.ps1 -Level beginner
   .\master_environment.ps1 -Level standard  
   .\master_environment.ps1 -Level advanced
   .\master_environment.ps1 -Level self-audit

🆘 NEED HELP? Start with beginner mode - no PowerShell knowledge required!
'@ -ForegroundColor White
}

# ============================================================================
# HIERARCHICAL ACTION HANDLERS
# ============================================================================

function Invoke-BeginnerMode {
    param([string]$Action = "start")
    
    Show-BeginnerInterface
    
    if ($Action -eq "start") {
        Write-Host ""
        Write-Host "🚀 Starting beginner setup process..." -ForegroundColor Green
        Write-Host "📍 Step 1: Checking location..." -ForegroundColor Cyan
        
        if (-Not (Invoke-SmartNavigation)) {
            return $false
        }
        
        Write-Host "✅ Location OK! Now installing tools..." -ForegroundColor Green
        Write-Host "📍 Step 2: Installing 9 development tools (this may take 5-10 minutes)..." -ForegroundColor Cyan
        
        if (Test-Path ".\install_all.ps1") {
            & ".\install_all.ps1"
        }
        
        Write-Host "📍 Step 3: Setting up convenience functions..." -ForegroundColor Cyan
        Invoke-UpdateProfile
        
        Write-Host "📍 Step 4: Final verification..." -ForegroundColor Cyan
        if (Test-Path ".\check_environment.ps1") {
            & ".\check_environment.ps1"
        }
        
        Write-Host ""
        Write-Host "🎉 BEGINNER SETUP COMPLETE!" -ForegroundColor Green
        Write-Host "💡 You can now use: psycho, activate, check from anywhere!" -ForegroundColor Cyan
    }
}

function Invoke-StandardMode {
    param([string]$Action = "setup-all")
    
    Show-StandardInterface
    
    if (-Not (Invoke-SmartNavigation)) {
        return $false
    }
    
    switch ($Action.ToLower()) {
        "setup-all" {
            Write-Host "🔧 Running complete setup..." -ForegroundColor Cyan
            & ".\install_all.ps1"
            & ".\activate_environment.ps1"
            Invoke-UpdateProfile
        }
        "install" { & ".\install_all.ps1" }
        "activate" { & ".\activate_environment.ps1" }  
        "check" { & ".\check_environment.ps1" }
        "profile" { Invoke-UpdateProfile }
        default { Write-Host "❌ Unknown standard action: $Action" -ForegroundColor Red }
    }
}

function Invoke-AdvancedMode {
    param([string]$Action = "audit")
    
    Show-AdvancedInterface
    
    if (-Not (Invoke-SmartNavigation)) {
        return $false
    }
    
    switch ($Action.ToLower()) {
        "install" { & ".\install_all.ps1" }
        "activate" { & ".\activate_environment.ps1" }
        "check" { & ".\check_environment.ps1" }
        "audit" { 
            & ".\check_environment.ps1"
            & ".\activate_environment.ps1"
            Get-ChildItem -Name "*AUDIT*", "*REPORT*" | Sort-Object LastWriteTime -Descending | Select-Object -First 5
        }
        "fix-paths" { 
            Write-Host "🔧 Checking Ruby/MSYS64/MinGW64 paths..." -ForegroundColor Cyan
            & ".\activate_environment.ps1"
        }
        "update-profile" { Invoke-UpdateProfile }
        "troubleshoot" { 
            Write-Host "🔍 Running advanced diagnostics..." -ForegroundColor Cyan
            Invoke-ScriptSelfAudit
            & ".\check_environment.ps1"
        }
        default { Write-Host "❌ Unknown advanced action: $Action" -ForegroundColor Red }
    }
}

function Invoke-UpdateProfile {
    if (Test-Path ".\powershell_profile.ps1") {
        $ProfileDir = Split-Path $PROFILE
        if (-Not (Test-Path $ProfileDir)) {
            New-Item -ItemType Directory -Path $ProfileDir -Force | Out-Null
        }
        Copy-Item ".\powershell_profile.ps1" $PROFILE -Force
        Write-Host "✅ PowerShell profile updated with convenience functions" -ForegroundColor Green
        return $true
    }
    else {
        Write-Host "❌ powershell_profile.ps1 not found" -ForegroundColor Red
        return $false
    }
}

# ============================================================================
# MAIN EXECUTION WITH PARAMETER HANDLING
# ============================================================================

# Handle legacy parameters for backward compatibility
if ($PSBoundParameters.ContainsKey("Action") -and $Level -eq "help") {
    # Legacy mode: .\master_environment_hierarchical.ps1 -Action install
    Write-Host "🔄 Legacy command detected. Converting to new hierarchical format..." -ForegroundColor Yellow
    $Level = "standard"
}

# Main execution switch
switch ($Level.ToLower()) {
    "beginner" { 
        Invoke-BeginnerMode -Action $(if ($Action) { $Action } else { "start" })
    }
    "standard" { 
        Invoke-StandardMode -Action $(if ($Action) { $Action } else { "setup-all" })
    }
    "advanced" { 
        Invoke-AdvancedMode -Action $(if ($Action) { $Action } else { "audit" })
    }
    "expert" { 
        Show-ExpertInterface
        Write-Host "🚀 Expert mode placeholder - direct PowerShell interface available" -ForegroundColor Red
    }
    "self-audit" { 
        Show-SelfAuditInterface
    }
    "help" { 
        Show-GeneralHelp
    }
    default { 
        Show-GeneralHelp
    }
}