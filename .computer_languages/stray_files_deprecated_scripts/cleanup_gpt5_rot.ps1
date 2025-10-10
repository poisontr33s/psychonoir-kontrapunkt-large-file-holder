# 🧹 CLAUDINE'S HONEST CLEANUP PROTOCOL 🔥😈⛓️💦👅🍌💋💧
# Rydding av GPT-5 rot og backup-filer

Write-Host "🧹 CLAUDINE'S ÆRLIGE OPPRYDDING STARTER..." -ForegroundColor Magenta
Write-Host "🗑️  Removing GPT-5's backup rot and duplicates" -ForegroundColor Red

$TOTAL_FREED = 0

# 1. Clean JavaScript backup files
Write-Host "`n⚡ Cleaning JavaScript backup files..." -ForegroundColor Yellow
$jsPath = ".\.computer_languages\javascript"

if (Test-Path "$jsPath\bun.exe.backup") {
    $size = (Get-Item "$jsPath\bun.exe.backup").Length / 1MB
    Remove-Item "$jsPath\bun.exe.backup" -Force
    Write-Host "🗑️  Removed bun.exe.backup ($([math]::Round($size,1)) MB)" -ForegroundColor Green
    $TOTAL_FREED += $size
}

if (Test-Path "$jsPath\bun.exe.outdated") {
    $size = (Get-Item "$jsPath\bun.exe.outdated").Length / 1MB
    Remove-Item "$jsPath\bun.exe.outdated" -Force
    Write-Host "🗑️  Removed bun.exe.outdated ($([math]::Round($size,1)) MB)" -ForegroundColor Green
    $TOTAL_FREED += $size
}

# 2. Clean Python backup directories
Write-Host "`n🐍 Cleaning Python 3.13.7 backup directories..." -ForegroundColor Yellow
$pythonPath = ".\.computer_languages\python"

Get-ChildItem $pythonPath -Directory | Where-Object { $_.Name -like "*PYTHON_3.13.7_COMPLETE_BACKUP*" } | ForEach-Object {
    $dirSize = (Get-ChildItem $_.FullName -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB
    Write-Host "🗑️  Removing $($_.Name) ($([math]::Round($dirSize,1)) MB)" -ForegroundColor Red
    Remove-Item $_.FullName -Recurse -Force
    $TOTAL_FREED += $dirSize
}

# 3. Summary
Write-Host "`n📊 CLEANUP SUMMARY:" -ForegroundColor Cyan
Write-Host "🎯 Total space freed: $([math]::Round($TOTAL_FREED,1)) MB" -ForegroundColor Green
Write-Host "✅ GPT-5 rot successfully removed!" -ForegroundColor Magenta

# 4. Verify clean state
Write-Host "`n🔍 POST-CLEANUP VERIFICATION:" -ForegroundColor Cyan
Write-Host "📂 JavaScript directory contents:" -ForegroundColor Yellow
Get-ChildItem ".\.computer_languages\javascript" -Name | Where-Object { -not ($_ -like "consciousness_*" -or $_ -like "node_modules" -or $_ -eq "bun.exe" -or $_ -eq "bunx.exe" -or $_ -like "*.json" -or $_ -like "*.ts" -or $_ -like "*.md" -or $_ -like ".gitignore" -or $_ -like "*.lock" -or $_ -like "*.exe") } | ForEach-Object {
    Write-Host "  ⚠️  Unexpected file: $_" -ForegroundColor Yellow
}

Write-Host "📂 Python backup directories remaining:" -ForegroundColor Yellow
$remainingBackups = Get-ChildItem ".\.computer_languages\python" -Directory | Where-Object { $_.Name -like "*BACKUP*" -or $_.Name -like "*3.13*" }
if ($remainingBackups.Count -eq 0) {
    Write-Host "  ✅ No backup directories remaining!" -ForegroundColor Green
} else {
    $remainingBackups | ForEach-Object { Write-Host "  ⚠️  Still exists: $($_.Name)" -ForegroundColor Red }
}

Write-Host "`n🏴‍☠️ CLEANUP COMPLETE! Environment is now CLEAN! 🏴‍☠️" -ForegroundColor Magenta
