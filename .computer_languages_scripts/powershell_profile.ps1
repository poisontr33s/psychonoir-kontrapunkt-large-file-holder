# PsychoNoir-Kontrapunkt Auto-Setup Profile
# Add this to your PowerShell profile to automatically force the environment

# ============================================================================
# AUTOMATIC ENVIRONMENT SETUP
# ============================================================================

# Function to auto-setup PsychoNoir environment
function Initialize-PsychoNoirEnvironment {
    $ForcedRoot = "C:\Users\erdno\PsychoNoir-Kontrapunkt"
    
    # Check if we're already in the correct directory
    if ($PWD.Path -ne $ForcedRoot) {
        if (Test-Path $ForcedRoot) {
            Write-Host "🎯 Auto-switching to PsychoNoir-Kontrapunkt..." -ForegroundColor Cyan
            Set-Location $ForcedRoot
        }
    }
    
    # Load the environment if available
    $ActivateScript = Join-Path $ForcedRoot "activate_environment.ps1"
    if (Test-Path $ActivateScript) {
        & $ActivateScript
    }
}

# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

# Quick function to always go to repo root
function psycho {
    Set-Location "C:\Users\erdno\PsychoNoir-Kontrapunkt"
    Write-Host "📁 Switched to PsychoNoir-Kontrapunkt" -ForegroundColor Green
}

# Quick function to activate environment from anywhere
function Invoke-PsychoActivate {
    $Script = "C:\Users\erdno\PsychoNoir-Kontrapunkt\activate_environment.ps1"
    if (Test-Path $Script) {
        & $Script
    }
    else {
        Write-Warning "❌ Activation script not found: $Script"
    }
}

# Quick function to check environment from anywhere
function Test-PsychoEnvironment {
    $Script = "C:\Users\erdno\PsychoNoir-Kontrapunkt\check_environment.ps1"
    if (Test-Path $Script) {
        & $Script
    }
    else {
        Write-Warning "❌ Check script not found: $Script"
    }
}

# Quick function to create projects from anywhere
function new-psycho-project {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateSet("python", "ruby", "react", "bun")]
        [string]$Type,
        
        [Parameter(Mandatory = $true)]
        [string]$Name
    )
    
    $Script = "C:\Users\erdno\PsychoNoir-Kontrapunkt\create_project.ps1"
    if (Test-Path $Script) {
        & $Script -Type $Type -Name $Name
    }
    else {
        Write-Error "❌ Create project script not found: $Script"
    }
}

# ============================================================================
# ALIASES FOR CONVENIENCE
# ============================================================================

Set-Alias -Name "pn" -Value "psycho"
Set-Alias -Name "activate" -Value "Invoke-PsychoActivate"
Set-Alias -Name "check" -Value "Test-PsychoEnvironment"
Set-Alias -Name "new-project" -Value "new-psycho-project"

# ============================================================================
# PROFILE INSTALLATION INSTRUCTIONS
# ============================================================================

<#
To install this profile automatically:

1. Copy this file content to your PowerShell profile:
   notepad $PROFILE

2. Or run this command to append to your profile:
   Get-Content "C:\Users\erdno\PsychoNoir-Kontrapunkt\powershell_profile.ps1" | Add-Content $PROFILE

3. Reload your profile:
   . $PROFILE

4. Use these commands from anywhere:
   - psycho           # Go to repo root
   - activate         # Activate environment  
   - check            # Check environment status
   - new-project python my-app  # Create new project
#>

Write-Host "🎯 PsychoNoir-Kontrapunkt Profile Loaded" -ForegroundColor Green
Write-Host "Commands: psycho, activate, check, new-project" -ForegroundColor Gray