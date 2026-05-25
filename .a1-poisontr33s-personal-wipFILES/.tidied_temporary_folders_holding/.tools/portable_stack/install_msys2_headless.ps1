#!/usr/bin/env pwsh

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$HubRoot,
    [string]$ArchivePath,  # e.g. msys2-base-x86_64-20250830.tar.xz (recommended) or extracted msys64 folder path
    [switch]$InitToolchain  # also install base-devel + mingw-w64-ucrt-x86_64-toolchain
)

# Resolve defaults
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")
if (-not $HubRoot) {
    $HubRoot = Join-Path $repoRoot ".scripting_coding_programming_languages"
}
$msysRoot = Join-Path $HubRoot "msys2"

New-Item -ItemType Directory -Force -Path $msysRoot | Out-Null

# Strategy:
# 1) Prefer a provided base archive (msys2-base-x86_64-YYYYMMDD.tar.xz)
# 2) Extract to a temp dir, then move the contained 'msys64' to $msysRoot
# 3) Initialize pacman & keyring headlessly (no GUI)
# 4) Optionally install UCRT64 toolchain headlessly

if (-not $ArchivePath) {
    Write-Host "No -ArchivePath provided. Please download an official MSYS2 base archive (msys2-base-x86_64-YYYYMMDD.tar.xz) and pass its path via -ArchivePath." -ForegroundColor Yellow
    Write-Host "Download page: https://www.msys2.org/ (click 'Installation->Manual installation')"
    exit 2
}

if (-not (Test-Path $ArchivePath)) {
    throw "Archive not found: $ArchivePath"
}

$tmp = Join-Path $env:TEMP ("msys2_extract_" + [guid]::NewGuid())
New-Item -ItemType Directory -Force -Path $tmp | Out-Null

Write-Host "Extracting archive to temp..." $ArchivePath
# Windows 11 bsdtar typically supports .xz
& tar -xf $ArchivePath -C $tmp
if ($LASTEXITCODE -ne 0) { throw "Extraction failed for $ArchivePath" }

# Expect 'msys64' directory inside temp
$extracted = Join-Path $tmp "msys64"
if (-not (Test-Path $extracted)) {
    throw "Expected 'msys64' directory inside the archive. Found: $(Get-ChildItem $tmp | Select-Object -ExpandProperty Name -ErrorAction SilentlyContinue | Out-String)"
}

Write-Host "Syncing extracted msys64 ->" $msysRoot
# Use robocopy for robust sync; fallback to Copy-Item if not available
$null = robocopy $extracted $msysRoot /MIR /NFL /NDL /NJH /NJS /NP
if ($LASTEXITCODE -ge 8) {
    Write-Warning "robocopy returned $LASTEXITCODE, attempting PowerShell copy"
    Copy-Item -Path (Join-Path $extracted '*') -Destination $msysRoot -Recurse -Force
}

# Verify bash
$bash = Join-Path $msysRoot 'usr\\bin\\bash.exe'
if (-not (Test-Path $bash)) {
    throw "MSYS2 bash not found at $bash after extraction"
}

Write-Host "Initializing pacman keyring & updating (headless)..." -ForegroundColor Cyan
& $bash -lc "set -e; pacman-key --init; pacman-key --populate msys2; pacman -Syu --noconfirm"
if ($LASTEXITCODE -ne 0) { throw "pacman init/update failed" }

if ($InitToolchain) {
    Write-Host "Installing UCRT64 toolchain headlessly..." -ForegroundColor Cyan
    & $bash -lc "set -e; pacman -S --needed --noconfirm base-devel mingw-w64-ucrt-x86_64-toolchain"
    if ($LASTEXITCODE -ne 0) { throw "toolchain install failed" }
}

Write-Host "MSYS2 headless setup complete at: $msysRoot" -ForegroundColor Green
Write-Host "Tip: Ensure VS Code terminal PATH includes: $($msysRoot)\\ucrt64\\bin; $($msysRoot)\\usr\\bin (already configured in settings.json)."
