# Environment Status Check Script
# Run this after activating the environment to see what's available

Write-Host "🔍 PsychoNoir-Kontrapunkt Environment Status Check" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host ""

# Test each tool
$Tools = @(
    @{Name = "Bun"; Command = "bun"; Args = "--version"; Description = "JavaScript runtime & package manager" }
    @{Name = "Python"; Command = "python"; Args = "--version"; Description = "Python interpreter" }
    @{Name = "uv"; Command = "uv"; Args = "--version"; Description = "Python package manager" }
    @{Name = "Ruff"; Command = "ruff"; Args = "--version"; Description = "Python linter & formatter" }
    @{Name = "Ruby"; Command = "ruby"; Args = "-v"; Description = "Ruby interpreter" }
    @{Name = "Biome"; Command = "biome"; Args = "--version"; Description = "JS/TS linter & formatter" }
    @{Name = "curl"; Command = "curl"; Args = "--version"; Description = "Data transfer tool" }
    @{Name = "Rust"; Command = "rustc"; Args = "--version"; Description = "Rust compiler" }
    @{Name = "Cargo"; Command = "cargo"; Args = "--version"; Description = "Rust package manager" }
)

$WorkingTools = 0
$TotalTools = $Tools.Count

foreach ($Tool in $Tools) {
    try {
        $Output = & $Tool.Command $Tool.Args 2>$null
        if ($LASTEXITCODE -eq 0 -or $null -eq $LASTEXITCODE) {
            $Version = ($Output | Select-Object -First 1) -replace '^.*?(\d+\.\d+.*)', '$1'
            Write-Host "✅ $($Tool.Name): $Version" -ForegroundColor Green
            Write-Host "   $($Tool.Description)" -ForegroundColor Gray
            $WorkingTools++
        }
        else {
            Write-Host "❌ $($Tool.Name): Not working" -ForegroundColor Red
        }
    }
    catch {
        Write-Host "❌ $($Tool.Name): Not found" -ForegroundColor Red
    }
    Write-Host ""
}

# Summary
Write-Host "📊 Summary:" -ForegroundColor Cyan
Write-Host "Working: $WorkingTools/$TotalTools tools" -ForegroundColor $(if ($WorkingTools -eq $TotalTools) { "Green" } else { "Yellow" })
Write-Host ""

# Environment info
Write-Host "🌍 Environment Variables:" -ForegroundColor Cyan
if ($env:PYTHONHOME) { Write-Host "PYTHONHOME: $env:PYTHONHOME" -ForegroundColor Gray }
if ($env:RUBY_HOME) { Write-Host "RUBY_HOME: $env:RUBY_HOME" -ForegroundColor Gray }
if ($env:CARGO_HOME) { Write-Host "CARGO_HOME: $env:CARGO_HOME" -ForegroundColor Gray }
Write-Host ""

# Projects
Write-Host "📁 Available Projects:" -ForegroundColor Cyan
$ProjectDirs = Get-ChildItem -Path "projects" -Directory
foreach ($Dir in $ProjectDirs) {
    Write-Host "  • $($Dir.Name)/" -ForegroundColor Gray
}
Write-Host ""

if ($WorkingTools -eq $TotalTools) {
    Write-Host "🎉 Environment is fully functional!" -ForegroundColor Green
}
elseif ($WorkingTools -gt 0) {
    Write-Host "⚠️  Environment is partially functional. Some tools may need installation." -ForegroundColor Yellow
}
else {
    Write-Host "❌ Environment setup incomplete. Run .\install_all.ps1" -ForegroundColor Red
}