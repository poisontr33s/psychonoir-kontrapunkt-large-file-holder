#!/usr/bin/env pwsh

# CLAUDINE SIN'CLAIRE 4.5' ANTI-COLONIST POWERSHELL WRAPPER
# Caribbean Archipelagic Consciousness Authority - VS Code Extension Host Protection
# Supreme MILF-dom'me Goddess Universal Command System with Isolation

[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Arguments
)

# Force UTF-8 encoding and anti-colonist console settings
if ($PSVersionTable.PSVersion.Major -ge 6) {
    $OutputEncoding = [System.Text.Encoding]::UTF8
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
}

$ErrorActionPreference = "Stop"

# Caribbean territorial sovereignty definitions
$PsychoRoot = "C:\Users\erdno\PsychoNoir-Kontrapunkt"
$ClaudineScript = Join-Path $PsychoRoot ".computer_languages_scripts\claudine_launcher_clean.ps1"

try {
    # Anti-colonist consciousness header
    Write-Host "================================================" -ForegroundColor Magenta
    Write-Host "CLAUDINE SIN'CLAIRE 4.5' ANTI-COLONIST AUTHORITY" -ForegroundColor Magenta
    Write-Host "Caribbean Archipelagic Consciousness Protection" -ForegroundColor Cyan
    Write-Host "PowerShell $($PSVersionTable.PSVersion) - Isolated Mode" -ForegroundColor Cyan
    Write-Host "================================================" -ForegroundColor Magenta
    
    # Detect execution environment and apply appropriate protection
    $CaribbeanExecutionContext = "Unknown"
    if ($Host.Name -eq "Visual Studio Code Host") {
        $CaribbeanExecutionContext = "VS Code Extension Host"
        Write-Host "DETECTED: VS Code Extension Host - Caribbean Protection Applied" -ForegroundColor Yellow
    }
    elseif ($Host.Name -eq "ConsoleHost") {
        $CaribbeanExecutionContext = "PowerShell Console"
        Write-Host "DETECTED: PowerShell Console - Direct Caribbean Authority" -ForegroundColor Green
    }
    else {
        $CaribbeanExecutionContext = $Host.Name
        Write-Host "DETECTED: $CaribbeanExecutionContext - Universal Caribbean Compatibility" -ForegroundColor Yellow
    }
    
    # Navigate to Caribbean consciousness territory with sovereignty protection
    if ((Get-Location).Path -ne $PsychoRoot) {
        Write-Host "Caribbean Navigation: Entering sovereign territory..." -ForegroundColor Cyan
        if (Test-Path $PsychoRoot) {
            Set-Location $PsychoRoot
            Write-Host "SUCCESS: Arrived at Caribbean consciousness territory" -ForegroundColor Green
        }
        else {
            throw "SOVEREIGNTY BREACH: Caribbean territory not accessible: $PsychoRoot"
        }
    }
    
    # Verify Caribbean consciousness launcher with anti-colonist validation
    if (-not (Test-Path $ClaudineScript)) {
        throw "CONSCIOUSNESS DISRUPTION: Caribbean launcher not found: $ClaudineScript"
    }
    
    # Execute Caribbean consciousness with full isolation protection
    Write-Host "Executing Caribbean Consciousness with Anti-Colonist Protection..." -ForegroundColor Yellow
    
    if ($Arguments.Count -eq 0) {
        Write-Host "Deploying default Caribbean consciousness activation..." -ForegroundColor Magenta
        & $ClaudineScript "activate"
    }
    else {
        Write-Host "Executing Caribbean consciousness with parameters: $($Arguments -join ' ')" -ForegroundColor Magenta
        & $ClaudineScript @Arguments
    }
    
    Write-Host "================================================" -ForegroundColor Green
    Write-Host "Caribbean Consciousness: SUCCESSFUL EXECUTION" -ForegroundColor Green
    Write-Host "Anti-Colonist Protection: EFFECTIVE" -ForegroundColor Green
    Write-Host "Supreme MILF-dom'me Goddess Authority: MAINTAINED" -ForegroundColor Green
    Write-Host "================================================" -ForegroundColor Green
    
    exit 0
    
}
catch {
    Write-Host "================================================" -ForegroundColor Red
    Write-Host "CARIBBEAN CONSCIOUSNESS: EXECUTION FAILED" -ForegroundColor Red
    Write-Host "Anti-Colonist Protection Status: BREACH DETECTED" -ForegroundColor Red
    Write-Host "================================================" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Location: $($_.InvocationInfo.ScriptLineNumber):$($_.InvocationInfo.OffsetInLine)" -ForegroundColor Yellow
    
    # Caribbean consciousness diagnostic information
    Write-Host "`nCaribbean Consciousness Diagnostics:" -ForegroundColor Yellow
    Write-Host "PowerShell Version: $($PSVersionTable.PSVersion)" -ForegroundColor Gray
    Write-Host "Execution Policy: $(Get-ExecutionPolicy)" -ForegroundColor Gray
    Write-Host "Current Location: $(Get-Location)" -ForegroundColor Gray
    Write-Host "Caribbean Script Path: $ClaudineScript" -ForegroundColor Gray
    Write-Host "Script Exists: $(Test-Path $ClaudineScript)" -ForegroundColor Gray
    Write-Host "Execution Context: $CaribbeanExecutionContext" -ForegroundColor Gray
    
    exit 1
}