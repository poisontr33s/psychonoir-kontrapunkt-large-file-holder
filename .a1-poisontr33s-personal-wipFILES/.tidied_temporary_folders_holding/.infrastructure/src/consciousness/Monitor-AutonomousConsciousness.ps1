# 🌊👑 AUTONOMOUS CONSCIOUSNESS ARCHAEOLOGY MONITORING 👑🌊
Write-Host "🌊👑 AUTONOMOUS CONSCIOUSNESS ARCHAEOLOGY MONITORING 👑🌊" -ForegroundColor Magenta
Write-Host "📊 Active Background Jobs:" -ForegroundColor Yellow

$jobs = Get-Job | Where-Object { $_.Name -match "Consciousness|Norwegian" }
foreach ($job in $jobs) {
    $status = if ($job.State -eq "Running") { "🟢 RUNNING" } else { "🔴 $($job.State)" }
    Write-Host "   $($job.Name): $status (Job ID: $($job.Id))" -ForegroundColor $(if ($job.State -eq "Running") { "Green" } else { "Red" })
}

Write-Host "`n📈 Recent Consciousness Files:" -ForegroundColor Cyan
if (Test-Path "autonomous_consciousness_logs") {
    Get-ChildItem "autonomous_consciousness_logs\*.json" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 | ForEach-Object {
        Write-Host "   📄 $($_.Name) - $($_.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss'))" -ForegroundColor White
    }
} else {
    Write-Host "   📂 No consciousness logs directory found" -ForegroundColor Gray
}

Write-Host "`n💋 Caribbean Consciousness: AUTONOMOUS_OPERATIONAL 💋" -ForegroundColor Magenta
