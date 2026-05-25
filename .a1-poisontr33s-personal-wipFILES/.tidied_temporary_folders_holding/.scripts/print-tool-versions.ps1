#!/usr/bin/env pwsh

# Prints where each tool is resolved from and its version in the current shell
param(
    [switch]$VerboseOutput
)

function Show-Tool($name, $versionCmd) {
    $cmd = Get-Command $name -ErrorAction SilentlyContinue
    if (-not $cmd) { Write-Host ("{0}: NOT FOUND" -f $name) -ForegroundColor Red; return }
    $path = $cmd.Source
    $version = & $versionCmd 2>$null
    if (-not $version) { $version = "(no version output)" }
    Write-Host ("{0}: {1}" -f $name, $path) -ForegroundColor Cyan
    Write-Host ("    version: {0}" -f $version.Trim())
}

if ($VerboseOutput) {
    Write-Host "PATH (first 12 entries):" -ForegroundColor Yellow
    ($env:PATH -split ';') | Select-Object -First 12 | ForEach-Object { "  $_" }
}

Show-Tool python { python -V }
Show-Tool uv { uv --version }
Show-Tool bun { bun -version }
Show-Tool ruff { ruff --version }
Show-Tool ruby { ruby -v }

Write-Host "Tip: Use 'Get-Command <name>' or 'where.exe <name>' on Windows to locate binaries." -ForegroundColor DarkGray
