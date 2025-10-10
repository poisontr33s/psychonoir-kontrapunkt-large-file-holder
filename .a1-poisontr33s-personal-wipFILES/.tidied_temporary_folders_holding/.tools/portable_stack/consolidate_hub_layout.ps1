[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$HubRoot,
    [switch]$Apply,
    [switch]$Backup
)

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")
if (-not $HubRoot) {
    $HubRoot = Join-Path $repoRoot ".scripting_coding_programming_languages"
}

if (-not (Test-Path $HubRoot)) { throw "Hub root not found: $HubRoot" }

$report = @()

function Add-Report($Type, $Path, $Note = '') {
    $report += [pscustomobject]@{ Type = $Type; Path = $Path; Note = $Note }
}

# Detect potential redundancy patterns
# 1) Duplicate top-level MSYS2 artifacts (msys2 and peers at root)
$msysRoot = Join-Path $HubRoot 'msys2'
$rootDupes = @('msys2_shell.cmd', 'msys2.exe', 'ucrt64.exe', 'mingw64.exe', 'mingw32.exe', 'clang64.exe', 'clangarm64.exe', 'uninstall.exe', 'uninstall.dat', 'uninstall.ini', 'components.xml', 'installer.dat', 'InstallationLog.txt', 'network.xml', 'autorebase.bat')
foreach ($f in $rootDupes) {
    $p = Join-Path $HubRoot $f
    if (Test-Path $p) {
        Add-Report 'RedundantFileAtHubRoot' $p 'Likely copied installer artifacts; msys2/* already contains these'
        if ($Apply) { Remove-Item -Force $p }
    }
}

# 2) Top-level toolchain dirs duplicated beside msys2 (ucrt64/, mingw64/, clang64/, etc.)
$dupeDirs = @('ucrt64', 'mingw64', 'mingw32', 'clang64', 'clangarm64', 'usr', 'var', 'opt', 'etc', 'home', 'dev')
foreach ($d in $dupeDirs) {
    $p = Join-Path $HubRoot $d
    if (Test-Path $p) {
        Add-Report 'RedundantDirAtHubRoot' $p 'These should live inside msys2/, not at hub root'
        if ($Apply) { Remove-Item -Recurse -Force $p }
    }
}

# 3) Minimal expected layout; flag unexpected top-level vendors
$expectedTop = @('msys2', 'python', 'rust', 'ruby', 'js_ts', 'linters', 'tmp')
Get-ChildItem -Path $HubRoot -Directory | ForEach-Object {
    if ($expectedTop -notcontains $_.Name) {
        Add-Report 'UnexpectedTopLevelDir' $_.FullName 'Review whether this belongs under a known vendor folder'
    }
}

# 4) js_ts layout sanity
$js = Join-Path $HubRoot 'js_ts'
if (Test-Path $js) {
    $expectedJs = @('bun', 'biome', 'projects')
    Get-ChildItem -Path $js -Directory | ForEach-Object {
        if ($expectedJs -notcontains $_.Name) {
            Add-Report 'UnexpectedJsSubdir' $_.FullName 'Consider moving under js_ts/projects'
        }
    }
}

# 5) Optional backup of report context
if ($Backup) {
    $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $bakDir = Join-Path $HubRoot ("layout_backup_" + $stamp)
    New-Item -ItemType Directory -Force -Path $bakDir | Out-Null
    $report | ConvertTo-Json -Depth 5 | Set-Content -Encoding UTF8 (Join-Path $bakDir 'consolidation_report.json')
}

# Output report
if ($report.Count -eq 0) {
    Write-Host "No redundancies detected. Layout looks clean." -ForegroundColor Green
}
else {
    Write-Host ("Detected {0} potential redundancies:" -f $report.Count) -ForegroundColor Yellow
    $report | ForEach-Object { Write-Host ("- [{0}] {1} {2}" -f $_.Type, $_.Path, $_.Note) }
    if (-not $Apply) { Write-Host "Run with -Apply to remove listed redundancies (a backup is recommended with -Backup)." -ForegroundColor Cyan }
}
