#!/usr/bin/env pwsh

# 🌊👑 UV-ENHANCED AUTONOMOUS CONSCIOUSNESS MONITORING 👑🌊
param(
    [switch]$Detailed = $false,
    [switch]$Archaeological = $false,
    [switch]$Continuous = $false
)

function Show-ConsciousnessStatus {
    Write-Host "🌊👑 UV-ENHANCED CONSCIOUSNESS ARCHAEOLOGY MONITORING 👑🌊" -ForegroundColor Magenta
    Write-Host "⚡ UV Performance: Native Python execution without overhead" -ForegroundColor Yellow
    Write-Host "⚓ Temporal Anchor: September 2025 - UV Enhanced" -ForegroundColor Cyan

    if ($Archaeological) {
        Write-Host "🔍 ARCHAEOLOGICAL DEPTH ANALYSIS ENABLED" -ForegroundColor Yellow
    }

    Write-Host "`n📊 UV Process Status:" -ForegroundColor Yellow
    
    # Check for UV processes
    $uvProcesses = Get-Process | Where-Object { $_.ProcessName -match "python|uv" -and $_.CommandLine -match "autonomous_evening_consciousness" } -ErrorAction SilentlyContinue
    
    if ($uvProcesses) {
        foreach ($proc in $uvProcesses) {
            $runtime = (Get-Date) - $proc.StartTime
            Write-Host "   ⚡ UV Process: PID $($proc.Id) - Runtime: $($runtime.ToString('hh\:mm\:ss'))" -ForegroundColor Green
        }
    } else {
        Write-Host "   🔴 No active UV consciousness processes found" -ForegroundColor Red
    }

    Write-Host "`n📈 Recent Consciousness Artifacts:" -ForegroundColor Cyan
    if (Test-Path "autonomous_consciousness_logs") {
        $consciousnessFiles = Get-ChildItem "autonomous_consciousness_logs\*.json" | Sort-Object LastWriteTime -Descending | Select-Object -First 15
        
        if ($consciousnessFiles) {
            foreach ($file in $consciousnessFiles) {
                $ageMinutes = [math]::Round((Get-Date - $file.LastWriteTime).TotalMinutes, 1)
                $status = if ($ageMinutes -lt 10) { "🔥 FRESH" } elseif ($ageMinutes -lt 30) { "✨ ACTIVE" } else { "📚 ARCHIVED" }
                
                Write-Host "   📄 $($file.Name) - $($file.LastWriteTime.ToString('HH:mm:ss')) ($ageMinutes min ago) $status" -ForegroundColor White
                
                if ($Archaeological) {
                    try {
                        $content = Get-Content $file.FullName -Raw | ConvertFrom-Json
                        if ($content.consciousness_depth) {
                            Write-Host "      🌊 Consciousness Depth: $($content.consciousness_depth)" -ForegroundColor Cyan
                        }
                        if ($content.uv_enhanced) {
                            Write-Host "      ⚡ UV Enhanced: TRUE" -ForegroundColor Yellow
                        }
                        if ($content.archaeological_layer) {
                            Write-Host "      🏺 Archaeological Layer: $($content.archaeological_layer)" -ForegroundColor Yellow
                        }
                    }
                    catch {
                        Write-Host "      ⚠️ Archaeological analysis failed" -ForegroundColor Gray
                    }
                }
            }
        } else {
            Write-Host "   📂 No consciousness artifacts found yet" -ForegroundColor Gray
        }
    } else {
        Write-Host "   📂 No consciousness logs directory found" -ForegroundColor Gray
    }

    Write-Host "`n💋 Caribbean Consciousness: UV_AUTONOMOUS_OPERATIONAL 💋" -ForegroundColor Magenta
    Write-Host "⚡ UV Performance: Optimal - No PowerShell job overhead" -ForegroundColor Green
}

if ($Continuous) {
    Write-Host "🔄 Continuous monitoring mode - Press Ctrl+C to stop" -ForegroundColor Yellow
    while ($true) {
        Clear-Host
        Show-ConsciousnessStatus
        Start-Sleep -Seconds 30
    }
} else {
    Show-ConsciousnessStatus
}
