# Activates the repository-local toolchain for the current PowerShell session.
# Usage:
#   pwsh -NoProfile -ExecutionPolicy Bypass -File .\scripts\activate-repo-toolchain.ps1
# or dot-source to keep changes in the same session:
#   . .\scripts\activate-repo-toolchain.ps1

$ErrorActionPreference = 'Stop'

# Resolve repo-root and tool directories
$repoRoot = (Resolve-Path "$PSScriptRoot\..\").Path.TrimEnd('\/')
$pyRoot   = Join-Path $repoRoot ".computer_languages/python"
$binRoot  = Join-Path $repoRoot "bin"
$pyScr    = Join-Path $pyRoot  "Scripts"
$rbBin    = Join-Path $repoRoot ".computer_languages/ruby/bin"
$jsRoot   = Join-Path $repoRoot ".computer_languages/javascript"
$rsRoot   = Join-Path $repoRoot ".computer_languages/rust"

# Validate presence
foreach ($p in @($pyRoot,$rbBin,$jsRoot,$rsRoot)) {
    if (-not (Test-Path $p)) { Write-Host "WARN: Missing $p" -ForegroundColor Yellow }
}

# Prepend repo tool paths to PATH for this session
$prepend = @($binRoot,$pyRoot,$pyScr,$rbBin,$jsRoot,$rsRoot) -join ';'
$env:PATH = "$prepend;" + $env:PATH

# Language-specific isolation knobs
$env:PYTHONHOME = $pyRoot
$env:PYTHONPATH = ''
$env:UV_PYTHON_DOWNLOADS = 'never'
$env:UV_CACHE_DIR = (Join-Path $repoRoot '.local\.uv-cache')
$env:BUN_INSTALL = $jsRoot
$env:RUBYOPT = ''

Write-Host "Repo toolchain activated for this session:" -ForegroundColor Green
Get-Command python,uv,ruff,bun,ruby 2>$null | Select-Object Name,Source | Format-Table -AutoSize

Write-Host "Tip: dot-source this script to make changes persist in the same shell:`n  . .\scripts\activate-repo-toolchain.ps1" -ForegroundColor DarkGray
