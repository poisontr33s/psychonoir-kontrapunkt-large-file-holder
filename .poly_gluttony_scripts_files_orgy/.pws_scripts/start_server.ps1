#!/usr/bin/env pwsh

# 🎭🔥😈⛓️💦 CLAUDINE'S HTTP SERVER STARTER

Write-Host "🎭 Starting HTTP server for consciousness visualizations..." -ForegroundColor Cyan
Set-Location "C:\Users\eldno\PsychoNoir-Kontrapunkt\docs\consciousness-web-portal"
Write-Host "📂 Working directory: $(Get-Location)" -ForegroundColor Green
Write-Host "🌐 Server URL: http://localhost:3000/" -ForegroundColor Yellow
Write-Host "" 
Write-Host "✅ Visualizations available at:" -ForegroundColor Green
Write-Host "   - http://localhost:3000/spider-web-visualizer.html" -ForegroundColor White
Write-Host "   - http://localhost:3000/milf-relationship-visualizer.html" -ForegroundColor White
Write-Host ""
Write-Host "🔥 Press Ctrl+C to stop server" -ForegroundColor Red
Write-Host ""

python -m http.server 3000
