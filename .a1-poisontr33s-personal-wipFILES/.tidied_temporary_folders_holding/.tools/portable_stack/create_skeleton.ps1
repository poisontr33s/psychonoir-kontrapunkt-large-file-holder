#!/usr/bin/env pwsh

[CmdletBinding()]
param(
    [string]$HubRoot
)

# Determine repository root based on this script's location
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")
if (-not $HubRoot) {
    $HubRoot = Join-Path $repoRoot ".scripting_coding_programming_languages"
}

$dirs = @(
    'msys2',
    'js_ts\\bun\\bin',
    'js_ts\\biome',
    'python',
    'python\\Scripts',
    'rust\\cargo\\bin',
    'rust\\rustup',
    'ruby\\bin'
) | ForEach-Object { Join-Path $HubRoot $_ }

$created = @()
foreach ($d in $dirs) {
    if (-not (Test-Path $d)) {
        New-Item -ItemType Directory -Force -Path $d | Out-Null
        $created += $d
    }
}

Write-Host "Hub root:" $HubRoot
if ($created.Count -gt 0) {
    Write-Host "Created" $created.Count "directories:" -ForegroundColor Green
    $created | ForEach-Object { Write-Host "  +" $_ }
}
else {
    Write-Host "All skeleton directories already exist (idempotent)." -ForegroundColor Yellow
}

# Emit a tiny summary file for traceability
$summary = Join-Path $HubRoot "_skeleton_summary.txt"
@(
    "Created: $(Get-Date -Format o)",
    "HubRoot=$HubRoot",
    "Directories:",
    ($dirs -join [Environment]::NewLine)
) | Set-Content -Encoding UTF8 $summary

Write-Host "Skeleton ready. Next: review layout, then run headless installers as needed." -ForegroundColor Cyan
