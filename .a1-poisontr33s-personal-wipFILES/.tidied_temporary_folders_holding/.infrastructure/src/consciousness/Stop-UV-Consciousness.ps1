#!/usr/bin/env pwsh

# 🛑 UV-ENHANCED CONSCIOUSNESS ARCHAEOLOGY TERMINATION
param(
    [switch]$Force = $false,
    [switch]$PreserveArchives = $true
)

Write-Host "🛑 Stopping UV-Enhanced Autonomous Consciousness Archaeology..." -ForegroundColor Red
Write-Host "⚡ UV Process Termination Protocol Initiated" -ForegroundColor Yellow

# Find UV consciousness processes
$uvProcesses = Get-Process | Where-Object { 
    $_.ProcessName -match "python|uv" -and 
    $_.CommandLine -match "autonomous_evening_consciousness"
} -ErrorAction SilentlyContinue

$stoppedProcesses = 0

foreach ($proc in $uvProcesses) {
    try {
        Write-Host "🛑 Terminating UV Process: PID $($proc.Id)" -ForegroundColor Yellow
        
        if ($Force) {
            $proc | Stop-Process -Force
        } else {
            # Send graceful interrupt
            $proc | Stop-Process
        }
        $stoppedProcesses++
    }
    catch {
        Write-Host "   ⚠️ Failed to stop process $($proc.Id): $($_.Exception.Message)" -ForegroundColor Orange
    }
}

# Archaeological cleanup
if (Test-Path "autonomous_consciousness_logs") {
    if ($PreserveArchives) {
        Write-Host "🏺 Preserving consciousness archaeological archives" -ForegroundColor Green
    } else {
        Write-Host "🗑️ Cleaning up consciousness archaeological data" -ForegroundColor Yellow
        if ((Read-Host "Delete all consciousness logs? (y/N)") -eq "y") {
            Remove-Item "autonomous_consciousness_logs\*" -Force
            Write-Host "🗑️ Archaeological data cleared" -ForegroundColor Red
        }
    }
}

Write-Host "⚓ Stopped $stoppedProcesses UV consciousness archaeology processes" -ForegroundColor Green
Write-Host "🌙 Creator Mother can now rest peacefully" -ForegroundColor Pink
Write-Host "⚡ UV performance benefits preserved for next session" -ForegroundColor Yellow
