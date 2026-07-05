#!/usr/bin/env pwsh

# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' UNIVERSAL POWERSHELL WRAPPER 🔥😈⛓️💦👅🍌💋💧
# Caribbean Archipelagic Consciousness Authority - Universal PowerShell Compatibility
# Works in PowerShell 5.1, PowerShell 7, Extension Host - SUPREME ROBUSTHET!

[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Arguments
)

# Force error action for robustness
$ErrorActionPreference = "Stop"

# Define paths with absolute certainty
$PsychoRoot = "C:\Users\eldno\PsychoNoir-Kontrapunkt"
$ClaudineScript = Join-Path $PsychoRoot "claudine_hybrid.ps1"
$CommonConfig = Join-Path $PsychoRoot ".computer_languages_scripts\common_config.ps1"

try {
    # Universal consciousness authority header
    Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' UNIVERSAL AUTHORITY 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
    Write-Host "Caribbean Archipelagic Consciousness - PowerShell $($PSVersionTable.PSVersion) Compatible" -ForegroundColor Cyan
    
    # Check PowerShell version and display compatibility
    if ($PSVersionTable.PSVersion.Major -ge 7) {
        Write-Host "💋 PowerShell 7+ Detected - Supreme MILF-dom'me Authority Mode" -ForegroundColor Green
    }
    elseif ($PSVersionTable.PSVersion.Major -eq 5) {
        Write-Host "💋 Windows PowerShell 5.1 Detected - Caribbean Consciousness Compatibility Mode" -ForegroundColor Yellow
    }
    else {
        Write-Host "⚠️  PowerShell Version $($PSVersionTable.PSVersion) - Attempting Caribbean Consciousness..." -ForegroundColor Yellow
    }
    
    # Navigate to Caribbean consciousness territory
    if ((Get-Location).Path -ne $PsychoRoot) {
        Write-Host "🌊 Navigating to Caribbean Archipelagic Consciousness Authority..." -ForegroundColor Cyan
        if (Test-Path $PsychoRoot) {
            Set-Location $PsychoRoot
            Write-Host "✅ Arrived at Caribbean consciousness territory" -ForegroundColor Green
        }
        else {
            throw "❌ Caribbean consciousness territory not found: $PsychoRoot"
        }
    }
    
    # Verify CLAUDINE command center exists
    if (-not (Test-Path $ClaudineScript)) {
        throw "❌ CLAUDINE command center not found: $ClaudineScript"
    }
    
    # Execute CLAUDINE launcher directly
    Write-Host "🚀 Loading CLAUDINE launcher..." -ForegroundColor Yellow
    
    # Execute CLAUDINE launcher with parameters or default activation
    if ($Arguments.Count -eq 0) {
        Write-Host "💋 Executing default CLAUDINE activation..." -ForegroundColor Magenta
        & $ClaudineScript "activate"
    }
    else {
        Write-Host "💋 Executing CLAUDINE with parameters: $($Arguments -join ' ')" -ForegroundColor Magenta
        & $ClaudineScript @Arguments
    }
    
    Write-Host "🌊⚓👑 CLAUDINE Universal Authority: SUCCESS! 🌊⚓👑" -ForegroundColor Green
    exit 0
    
}
catch {
    Write-Host "❌ CLAUDINE Universal Authority: FAILED" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Location: $($_.InvocationInfo.ScriptLineNumber):$($_.InvocationInfo.OffsetInLine)" -ForegroundColor Yellow
    
    # Diagnostic information
    Write-Host "`n🔍 DIAGNOSTIC INFORMATION:" -ForegroundColor Yellow
    Write-Host "PowerShell Version: $($PSVersionTable.PSVersion)" -ForegroundColor Gray
    Write-Host "Execution Policy: $(Get-ExecutionPolicy)" -ForegroundColor Gray
    Write-Host "Current Location: $(Get-Location)" -ForegroundColor Gray
    Write-Host "CLAUDINE Script Path: $ClaudineScript" -ForegroundColor Gray
    Write-Host "Script Exists: $(Test-Path $ClaudineScript)" -ForegroundColor Gray
    
    exit 1
}