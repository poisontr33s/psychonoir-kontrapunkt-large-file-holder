# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE PERSISTENT INSTALLATION SCRIPT
# This script installs Claudine command permanently in your PowerShell profile

param(
    [switch]$Force = $false,
    [switch]$Uninstall = $false
)

Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' INSTALLATION" -ForegroundColor Magenta
Write-Host "Installing Supreme MILF-dom'me Goddess Command Permanently..." -ForegroundColor Cyan
Write-Host ""

# Get PowerShell profile path
$ProfilePath = $PROFILE
$ProfileDir = Split-Path $ProfilePath -Parent

# Create profile directory if it doesn't exist
if (!(Test-Path $ProfileDir)) {
    New-Item -ItemType Directory -Path $ProfileDir -Force | Out-Null
    Write-Host "📁 Created PowerShell profile directory: $ProfileDir" -ForegroundColor Green
}

# Claudine installation code block
$ClaudineInstallBlock = @'

# ============================================================================
# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' AUTO-LOADER 🔥😈⛓️💦👅🍌💋💧
# Caribbean MILF-dom'me Goddess Command Center - Auto-loaded on PowerShell start
# ============================================================================

$ClaudineCommandPath = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages_scripts\claudine_command_center.ps1"
if (Test-Path $ClaudineCommandPath) {
    . $ClaudineCommandPath
    Write-Host "💋 Claudine Sin'claire 4.5' ready! Type 'claudine' to activate!" -ForegroundColor Magenta
} else {
    Write-Host "⚠️  Claudine command center not found at: $ClaudineCommandPath" -ForegroundColor Yellow
}

# ============================================================================
'@

if ($Uninstall) {
    # Remove Claudine from profile
    if (Test-Path $ProfilePath) {
        $ProfileContent = Get-Content $ProfilePath -Raw
        $CleanedContent = $ProfileContent -replace [regex]::Escape($ClaudineInstallBlock), ""
        $CleanedContent | Set-Content $ProfilePath -Encoding UTF8
        Write-Host "❌ Claudine removed from PowerShell profile" -ForegroundColor Yellow
        Write-Host "🔄 Please restart PowerShell for changes to take effect" -ForegroundColor Cyan
    }
}
else {
    # Install Claudine to profile
    $InstallClaudine = $true
    
    if (Test-Path $ProfilePath) {
        $ProfileContent = Get-Content $ProfilePath -Raw
        if ($ProfileContent -like "*CLAUDINE SIN'CLAIRE*") {
            if ($Force) {
                Write-Host "🔄 Claudine already installed, updating..." -ForegroundColor Yellow
                # Remove old version first
                $ProfileContent = $ProfileContent -replace [regex]::Escape($ClaudineInstallBlock), ""
            }
            else {
                Write-Host "✅ Claudine already installed in PowerShell profile!" -ForegroundColor Green
                Write-Host "💡 Use -Force to reinstall/update" -ForegroundColor Cyan
                $InstallClaudine = $false
            }
        }
    }
    else {
        # Create new profile
        New-Item -ItemType File -Path $ProfilePath -Force | Out-Null
        Write-Host "📄 Created new PowerShell profile: $ProfilePath" -ForegroundColor Green
    }
    
    if ($InstallClaudine) {
        # Add Claudine to profile
        Add-Content -Path $ProfilePath -Value $ClaudineInstallBlock -Encoding UTF8
        Write-Host "✅ Claudine installed to PowerShell profile!" -ForegroundColor Green
        Write-Host "📁 Profile location: $ProfilePath" -ForegroundColor Gray
        Write-Host ""
        Write-Host "🎯 INSTALLATION COMPLETE!" -ForegroundColor Magenta
        Write-Host ""
        Write-Host "💋 What happens now:" -ForegroundColor Cyan
        Write-Host "  • Every new PowerShell session will have 'claudine' command" -ForegroundColor White
        Write-Host "  • Type 'claudine' to activate development environment" -ForegroundColor White
        Write-Host "  • All tools (python, ruby, bun, rust) will be available" -ForegroundColor White
        Write-Host ""
        Write-Host "🔄 To activate in current session, run:" -ForegroundColor Cyan
        Write-Host "  . `$PROFILE" -ForegroundColor Yellow
        Write-Host "  claudine" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "🌊⚓👑 Claudine Sin'claire 4.5' - Your Caribbean Command Gateway! 🌊⚓👑" -ForegroundColor Magenta