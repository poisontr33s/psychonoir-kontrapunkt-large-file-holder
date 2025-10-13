# Organize and consolidate language installations
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$root = $PSScriptRoot

Write-Host "🔧 Organizing language installations..." -ForegroundColor Cyan

# Define target structure
$targetStructure = @{
    "powershell" = ".code_scripting_programming_langs\powershell"
    "bun"        = ".computer_languages\javascript"
    "biome"      = ".computer_languages\javascript"
    "uv"         = ".computer_languages\python"
    "python"     = ".computer_languages\python"
    "ruff"       = ".computer_languages\python"
    "rust"       = ".computer_languages\rust"
    "ruby"       = ".computer_languages\ruby"
    "curl"       = ".code_scripting_programming_langs\curl"
}

# Source directories to check
$sourceDirs = @(
    ".i_am_idiot_gpt",
    ".code_scripting_programming_langs",
    ".computer_languages"
)

# Create target directories
foreach ($dir in $targetStructure.Values) {
    $fullPath = Join-Path $root $dir
    if (-not (Test-Path $fullPath)) {
        New-Item -Path $fullPath -ItemType Directory -Force | Out-Null
        Write-Host "📁 Created: $dir" -ForegroundColor Green
    }
}

# Move files from old locations to new organized structure
# This is a complex operation - for now, just report current status

Write-Host "`n📊 Current installation status:" -ForegroundColor Yellow

foreach ($source in $sourceDirs) {
    $sourcePath = Join-Path $root $source
    if (Test-Path $sourcePath) {
        Write-Host "📂 $source/ exists" -ForegroundColor Blue
        Get-ChildItem $sourcePath -Directory | ForEach-Object {
            Write-Host "  ├── $($_.Name)/" -ForegroundColor Gray
        }
    }
}

Write-Host "`n✅ Organization analysis complete" -ForegroundColor Green
Write-Host "💡 Recommendation: Use the modular install scripts in .code_scripting_programming_langs/" -ForegroundColor Cyan
Write-Host "   to maintain clean separation between installation scripts and installed tools." -ForegroundColor Cyan