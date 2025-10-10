# Activate local development environment
# Sets up PATH for all locally installed tools

param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$repoRoot = $PSScriptRoot

Write-Host "🔥 Activating PsychoNoir-Kontrapunkt Development Environment 🔥" -ForegroundColor Magenta
Write-Host "Repository: $repoRoot" -ForegroundColor Blue

# Define tool paths
$toolPaths = @(
    # JavaScript/Bun
    (Join-Path $repoRoot ".computer_languages\javascript"),
    # Python/uv
    (Join-Path $repoRoot ".computer_languages\python"),
    # Rust
    (Join-Path $repoRoot ".computer_languages\rust\.cargo\bin"),
    # Ruby
    (Join-Path $repoRoot ".computer_languages\ruby\bin"),
    # Curl
    (Join-Path $repoRoot ".computer_languages\curl"),
    # PowerShell (if installed locally)
    (Join-Path $repoRoot ".computer_languages\powershell")
)

# Add paths to current session PATH
$addedPaths = @()
foreach ($path in $toolPaths) {
    if (Test-Path $path) {
        if ($env:PATH -notlike "*$path*") {
            $env:PATH = "$path;$env:PATH"
            $addedPaths += $path
            Write-Host "✅ Added to PATH: $path" -ForegroundColor Green
        }
        else {
            Write-Host "ℹ️  Already in PATH: $path" -ForegroundColor Blue
        }
    }
    else {
        Write-Host "⚠️  Path not found: $path" -ForegroundColor Yellow
    }
}

Write-Host "`n🔧 Environment activated!" -ForegroundColor Green

# Test tools
$tools = @(
    @{Name = "bun"; Command = "bun --version" },
    @{Name = "uv"; Command = "uv --version" },
    @{Name = "python"; Command = "python --version" },
    @{Name = "rustc"; Command = "rustc --version" },
    @{Name = "ruby"; Command = "ruby -v" },
    @{Name = "curl"; Command = "curl --version" }
)

Write-Host "`n🧪 Testing tools:" -ForegroundColor Cyan
foreach ($tool in $tools) {
    try {
        $output = Invoke-Expression $tool.Command 2>$null
        if ($output) {
            $firstLine = $output | Select-Object -First 1
            Write-Host "✅ $($tool.Name): $firstLine" -ForegroundColor Green
        }
        else {
            Write-Host "✅ $($tool.Name): Available" -ForegroundColor Green
        }
    }
    catch {
        Write-Host "❌ $($tool.Name): Not found or failed" -ForegroundColor Red
    }
}

if ($addedPaths.Count -gt 0) {
    Write-Host "`n💡 Tools added to PATH for this session:" -ForegroundColor Yellow
    $addedPaths | ForEach-Object { Write-Host "   $_" -ForegroundColor White }
}
else {
    Write-Host "`nℹ️  No new paths added to PATH" -ForegroundColor Blue
}

Write-Host "`n🚀 Ready to code! Happy developing! 👑" -ForegroundColor Magenta