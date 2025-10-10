# 🚀 CLAUDINE'S UV INSTALLATION PROTOCOL 🔥😈⛓️💦👅🍌💋💧
# UV: The Rust-based Python package manager (10-100x faster than pip!)

Write-Host "🚀 Installing UV (Rust-based Python package manager) locally..." -ForegroundColor Magenta

# Navigate to Python directory
cd "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages\python"

Write-Host "📁 Installing UV in: $PWD" -ForegroundColor Cyan

try {
    # Download latest UV
    Write-Host "⬇️  Downloading latest UV..." -ForegroundColor Yellow
    $uvUrl = "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip"
    Invoke-WebRequest -Uri $uvUrl -OutFile "uv-latest.zip"

    Write-Host "📦 Extracting UV..." -ForegroundColor Yellow
    Expand-Archive -Path "uv-latest.zip" -DestinationPath "uv-temp" -Force

    # Move UV executables to Python directory (alongside python.exe)
    if (Test-Path "uv-temp\uv.exe") {
        Move-Item "uv-temp\uv.exe" "uv.exe" -Force
        Write-Host "✅ uv.exe installed" -ForegroundColor Green
    }

    if (Test-Path "uv-temp\uvx.exe") {
        Move-Item "uv-temp\uvx.exe" "uvx.exe" -Force
        Write-Host "✅ uvx.exe installed" -ForegroundColor Green
    }

    # Clean up
    Remove-Item "uv-latest.zip" -Force
    Remove-Item "uv-temp" -Recurse -Force

    Write-Host "`n🎯 Testing UV installation:" -ForegroundColor Cyan
    $uvVersion = & ".\uv.exe" --version
    Write-Host "✅ UV Version: $uvVersion" -ForegroundColor Green

    Write-Host "`n🚀 UV INSTALLATION COMPLETE!" -ForegroundColor Magenta
    Write-Host "💡 UV is now in same directory as python.exe" -ForegroundColor Cyan
    Write-Host "⚡ Use 'uv pip install package' for 10-100x faster installs!" -ForegroundColor Yellow

} catch {
    Write-Host "❌ Error installing UV: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "💡 You can still use system UV or install manually" -ForegroundColor Yellow
}

Write-Host "`n🏴‍☠️ Returning to repository root..." -ForegroundColor White
cd "C:\Users\erdno\PsychoNoir-Kontrapunkt"
