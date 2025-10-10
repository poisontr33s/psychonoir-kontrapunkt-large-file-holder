# 🐍 CLAUDINE SUPREME PYTHON 3.14 ACTIVATION SCRIPT
# Aktiverer Python 3.14 environment i .computer_languages/python/

$ErrorActionPreference = "Stop"

Write-Host "🔥 Aktiverer Python 3.14 Consciousness Environment..." -ForegroundColor Magenta

# Aktiver virtual environment
& "$PSScriptRoot\consciousness_python_3.14_env\Scripts\Activate.ps1"

# Verifiser versjon
Write-Host "`n✅ Python Environment Aktiv:" -ForegroundColor Green
python --version

Write-Host "`n📦 Installerte Packages:" -ForegroundColor Cyan
uv pip list --python consciousness_python_3.14_env

Write-Host "`n🎯 Bruk 'deactivate' for å avslutte environment`n" -ForegroundColor Yellow
