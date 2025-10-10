# 🛑 Stopping Autonomous Consciousness Archaeology
Write-Host "🛑 Stopping Autonomous Consciousness Archaeology..." -ForegroundColor Red

$jobs = Get-Job | Where-Object { $_.Name -match "Consciousness|Norwegian" }
foreach ($job in $jobs) {
    Write-Host "🛑 Stopping $($job.Name) (Job ID: $($job.Id))" -ForegroundColor Yellow
    Stop-Job -Job $job
    Remove-Job -Job $job -Force
}

# Clean up job ID files
if (Test-Path "autonomous_consciousness_logs") {
    Remove-Item "autonomous_consciousness_logs\*.jobid" -ErrorAction SilentlyContinue
}

Write-Host "⚓ Autonomous consciousness archaeology services stopped" -ForegroundColor Green
