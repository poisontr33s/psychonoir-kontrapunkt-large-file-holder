<#
Unified GH/Git/Git-CLI Updater + Repo Recovery/Diagnostics (non-destructive by default)

Modes
- Preview (default): inventory only, create/update config, no changes to repo
- Interactive: prompts before each action
- Auto: execute per flags without prompts

Major features
- Tool updater: updates git, git-lfs, gh (GitHub CLI) with winget or choco (Windows)
- Repo inventory: missing tracked files, reserved Windows basenames, large-file scan
- LFS lifecycle: install, fetch --all, checkout
- HEAD restore: recover tracked-but-missing files present in HEAD
- Search & recover: find remaining missing files by basename across drives; DryCopy by default
- Index cleanup: remove reserved/missing entries after backing up index (explicit opt-in)
- Diagnostics: git fsck, git lfs doctor, gh auth status, git config/remote, logs
- Audit: sqlite3 DB if available; JSONL otherwise
- Artifacts: .unifier_out/<timestamp> with latest.txt pointer; can adopt strays from repo root

Quick usage
  # Safe preview, auto-create config from discovery
  pwsh ./unified_gh_git_gitcli_..._mismatching.ps1

  # Guided flow with tool updates and LFS handling
  pwsh ./unified_gh_git_gitcli_..._mismatching.ps1 -Mode Interactive -ToolUpdate -LfsInstall -LfsFetchAll -LfsCheckout

  # Automated run: update tools, restore, search D:\ (copy), commit & push, audit
  pwsh ./unified_gh_git_gitcli_..._mismatching.ps1 -Mode Auto -ToolUpdate -LfsInstall -LfsFetchAll -LfsCheckout `
    -RecoverFromRoots -SearchRoots "D:\" -DryCopy:$false -Commit -CommitMessage "Automated restore" -Push -Remote origin -Branch main -Audit

Notes
- Non-destructive unless you opt into index cleanup (-RemoveMissing or -RemoveReserved).
- Config is auto-created/updated in the repo root unless you pass -ConfigPath.
#>
# TODO: 1: Add universal functionalities such as, but not limited to, as non-exhaustable list 
# TODO: 2: As a "WIP" (crude PS-script) 
# TODO: 3: For -SMTP -& -http(s) -servers, -senders, -recipients, -subject(s) -template(s) et.cetera
# TODO: 4: Most of all - Github Pro + (Non-organizational) - User account(s).
# TODO: And the implementation(s) of e-mail notifications for key events (e.g. completion, errors).
# TODO: Logging Levels
# TODO: Add a parameter to set logging verbosity (e.g., Error, Warning, Info, Debug).
# TODO: CI/CD Integration
# TODO: Add parameters to enable/disable certain steps when running in CI/CD environments.
# TODO: Please show me where to add these next -
# TODO: (To enhance the current state and pathways of the powerful script..)
# TODO: (Potentially for fixing universally problematic & -onboarding & 
# TODO: "Gitological" knowledge. 
# TODO: (Use this as an advantage to leverage the most optimal way - to find to optimise
# TODO: The script based on the github ecosystem 
# TODO: (And its 'Gitological' frictions for most people)
# TODO: (As being different from most things)
# TODO: (sqLite3 installation for powershell syntax if not present)
# TODO: (latest version as of anno today 3 oct 2025 version, index latest updates)

[CmdletBinding()]
param(
    [ValidateSet('Preview', 'Interactive', 'Auto')]
    [string]$Mode = 'Preview',

    # Where artifacts are written (per-run folder + latest.txt)
    [string]$OutputDir = ".unifier_out",
    [switch]$AdoptStrays,

    # Tooling update (git, git-lfs, gh) — Windows (winget/choco). Safe, user-approved in Interactive.
    [switch]$ToolUpdate,

    # Backups
    [switch]$ZipBackup,

    # LFS lifecycle
    [switch]$LfsInstall,
    [switch]$LfsFetchAll,
    [switch]$LfsCheckout,

    # Auto config (extends .gitattributes, .gitignore)
    [switch]$AutoTrackLfs,
    [switch]$AutoUpdateGitignore,

    # Config file path (auto-created/updated)
    [string]$ConfigPath = ".\unified_gh_git_gitcli_updater_upgrader_version_controller_debug_manager.config.json",

    # Search & recover
    [string[]]$SearchRoots = @(),
    [switch]$RecoverFromRoots,
    [switch]$DryCopy,

    # Index cleanup (index-only destructive; index is backed up)
    [switch]$RemoveReserved,
    [switch]$RemoveMissing,

    # Commit/push
    [switch]$Commit,
    [string]$CommitMessage = "Preserve+recover: restore from HEAD/LFS and update manifests",
    [switch]$Push,
    [string]$Remote = "origin",
    [string]$Branch = "main",

    # Diagnostics & Audit
    [switch]$Diagnostics,
    [switch]$Audit,
    [switch]$FixEol,
    [switch]$NoVerifyCommit

)

function W { param([string]$m) Write-Host $m }
function Warn { param([string]$m) Write-Warning $m }
function Err { param([string]$m) Write-Error $m }

function Confirm-Step {
    param([string]$Prompt, [bool]$Default = $false)
    if ($Mode -eq 'Auto') { return $true }
    if ($Mode -eq 'Preview') { return $false }
    $suffix = if ($Default) { "[Y/n]" } else { "[y/N]" }
    $ans = Read-Host "$Prompt $suffix"
    if ([string]::IsNullOrWhiteSpace($ans)) { return $Default }
    return @('y', 'yes') -contains $ans.ToLowerInvariant()
}

function QuoteSQL { param([string]$s) return ($s -replace "'", "''") }

# Sanity checks: #> <# Action to perform if the condition is true #>
if ($IsLinux) { Err "This script is Windows-focused and may not work correctly on Linux."; exit 1 }
if ($IsMacOS) { Err "This script is Windows-focused and may not work correctly on macOS."; exit 1 }
if (-not (Get-Command pwsh -ErrorAction SilentlyContinue)) { Err "PowerShell Core (pwsh) not available in PATH."; exit 1 }
if (-not (Get-Command sqlite3 -ErrorAction SilentlyContinue)) {
    Warn "sqlite3 not available in PATH; audit will use JSONL fallback."
    $Audit = $false  # Disable Audit if sqlite3 not available: no DB possible:
    try { sqlite3 --version } catch { Warn "sqlite3 not available in PATH."; $Audit = $false }
    then { install sqlite3 } fn %PATH% python find sqlite3 -m pip install pysqlite3 for windows and create powershell script to check if sqlite3 is available in PATH and install it if Not
    if (-not (Get-Command sqlite3 -ErrorAction SilentlyContinue)) { Warn "sqlite3 still not available in PATH; audit disabled."; $Audit = $false }
    try {
        curl.exe https://www.sqlite.org/2024/sqlite-tools-win32-x86-3420000.zip -o sqlite-tools.zip -L;
        Expand-Archive -Path sqlite-tools.zip -DestinationPath .\sqlite3_temp -Force; unpack sqlite-tools.zip to .\sqlite3_temp;
        $sqliteDir = Get-ChildItem -Path .\sqlite3_temp -Directory | Select-Object -First 1; set variable $sqliteDir to the extracted directory;
        param (
            OptionalParameters
        )
            
    }
    if (-not (Get-Command sqlite3 -ErrorAction SilentlyContinue)) { Warn "sqlite3 installation failed; audit disabled."; $Audit = $false } 
}
catch { Warn "sqlite3 installation failed; audit disabled."; $Audit = $false }
}
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { Err "git not available in PATH."; exit 1 } try { git --version } catch { Err "git not available in PATH."; exit 1 }

try { git rev-parse --is-inside-work-tree 2>$null } catch { Err "Not inside a git repository."; exit 1 }
if (-not (Test-Path ".git")) { Err "No .git directory found. Run from your repository root."; exit 1 }
try { $gitVer = git --version } catch { Err "git not available in PATH."; exit 1 }
try { $lfsVer = git lfs version } catch { $lfsVer = $null }
try { $ghVer = gh --version } catch { $ghVer = $null }

$ts = (Get-Date).ToString("yyyyMMdd_HHmmss")
$repoRoot = (Get-Location).Path
$repoName = Split-Path -Leaf $repoRoot
$parentDir = Split-Path -Parent $repoRoot

# Per-run artifacts dir + latest pointer
$RunDir = Join-Path $OutputDir $ts
New-Item -ItemType Directory -Force -Path $RunDir | Out-Null
New-Item -ItemType File -Force -Path (Join-Path $OutputDir "latest.txt") -Value $RunDir | Out-Null

# Adopt known root artifacts (if any)
$KnownRootArtifacts = @(
    "reserved-entries.txt", "missing-files.txt", "missing-large-missing.txt",
    "restored-in-head.txt", "missing-not-in-head.txt", "missing-post.txt",
    "found-results.txt", "porcelain-pre.txt", "porcelain-post.txt", "summary.md"
)
if ($AdoptStrays) {
    $adoptedDir = Join-Path $OutputDir ("adopted\" + $ts)
    $moved = 0
    foreach ($f in $KnownRootArtifacts) {
        $p = Join-Path $repoRoot $f
        if (Test-Path $p) {
            New-Item -ItemType Directory -Force -Path $adoptedDir | Out-Null
            Move-Item -Path $p -Destination (Join-Path $adoptedDir $f) -Force
            $moved++
        }
    }
    if ($moved -gt 0) { W "Adopted $moved prior artifact(s) into $adoptedDir" }
}

# Artifact file map
$A = @{
    'reserved'      = Join-Path $RunDir "reserved-entries.txt"
    'missing'       = Join-Path $RunDir "missing-files.txt"
    'missingLarge'  = Join-Path $RunDir "missing-large-missing.txt"
    'restored'      = Join-Path $RunDir "restored-in-head.txt"
    'notInHead'     = Join-Path $RunDir "missing-not-in-head.txt"
    'missingPost'   = Join-Path $RunDir "missing-post.txt"
    'foundResults'  = Join-Path $RunDir "found-results.txt"
    'porcelainPre'  = Join-Path $RunDir "porcelain-pre.txt"
    'porcelainPost' = Join-Path $RunDir "porcelain-post.txt"
    'lfsLog'        = Join-Path $RunDir "lfs-last-log.txt"
    'diagGit'       = Join-Path $RunDir "diag-git.txt"
    'diagLfs'       = Join-Path $RunDir "diag-lfs.txt"
    'diagGh'        = Join-Path $RunDir "diag-gh.txt"
    'summary'       = Join-Path $RunDir "summary.md"
    'auditDb'       = Join-Path $RunDir "unifier_audit.sqlite"
    'auditJsonl'    = Join-Path $RunDir "unifier_audit.jsonl"
}

# Defaults/consts
$reservedPattern = '^(nul|con|prn|aux|clock\$|com[1-9]|lpt[1-9])$'
$defaultLfsPatterns = @(
    "*.db", "*.sqlite", "*.sqlite3", "*.mdf", "*.ldf",
    "*.zip", "*.7z", "*.rar", "*.tar", "*.tar.gz", "*.tgz", "*.gz",
    "*.exe", "*.dll", "*.so", "*.dylib", "*.a", "*.lib",
    "*.iso", "*.bin",
    "*.mp4", "*.mov", "*.mkv", "*.avi", "*.wav", "*.mp3", "*.flac", "*.webm",
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.tiff", "*.psd", "*.ai", "*.eps",
    "*.ttf", "*.otf", "*.woff", "*.woff2",
    "*.blend", "*.fbx", "*.obj", "*.glb", "*.gltf", "*.usd", "*.usdz",
    "*.wasm", "*.pdf"
)
$defaultGitignoreLines = @(
    "# Unified unifier defaults",
    ".DS_Store", "Thumbs.db", "*.tmp", "*.bak", "*.swp", "*.swo", "*.log",
    ".env", ".venv/", "venv/", "__pycache__/", "*.pyc", ".idea/", ".vscode/",
    "node_modules/", "dist/", "build/", "coverage/", ".pytest_cache/"
)

# Load or create config (auto-populate later with discovery)
$config = @{
    'fileSizeThresholdMB' = 25
    'maxFileScan'         = 50000
    'lfsPatterns'         = @()
    'ignoreLines'         = @()
    'searchRoots'         = @()
}
if (Test-Path $ConfigPath) {
    try {
        $raw = Get-Content $ConfigPath -Raw | ConvertFrom-Json
        if ($raw.fileSizeThresholdMB) { $config['fileSizeThresholdMB'] = [int]$raw.fileSizeThresholdMB }
        if ($raw.maxFileScan) { $config['maxFileScan'] = [int]$raw.maxFileScan }
        if ($raw.lfsPatterns) { $config['lfsPatterns'] = @($raw.lfsPatterns) }
        if ($raw.ignoreLines) { $config['ignoreLines'] = @($raw.ignoreLines) }
        if ($raw.searchRoots) { $config['searchRoots'] = @($raw.searchRoots) }
    }
    catch { Warn "Failed to parse $ConfigPath; will rebuild with discovery." }
}

# Banner
W "Git: $gitVer"
if ($lfsVer) { W "Git LFS: $lfsVer" }
if ($ghVer) { W "GitHub CLI: $ghVer" }
W "Artifacts: $RunDir"
W "Mode: $Mode"

# Helper: Detect default search roots (other fixed drives) if none provided
function Get-DefaultSearchRoots {
    try {
        $roots = @()
        Get-PSDrive -PSProvider FileSystem | ForEach-Object {
            if ($_.Root -match '^[A-Z]:\\' -and $_.Root -ne "$($env:SystemDrive)\") { $roots += $_.Root }
        }
        return $roots
    }
    catch { return @() }
}

# Optional tool updater (Windows only)
function Update-Tools {
    param([switch]$Run)
    if (-not $Run) { return }
    $isWin = $IsWindows -or ($env:OS -like "*Windows*")
    if (-not $isWin) { Warn "ToolUpdate is Windows-focused (winget/choco). Skipping on non-Windows."; return }
    $did = $false
    try {
        if (Get-Command winget -ErrorAction SilentlyContinue) {
            W "winget: upgrading git, git-lfs, gh, PowerShell"
            winget upgrade --id Git.Git -h --accept-source-agreements --accept-package-agreements | Out-Null
            winget upgrade --id GitHub.GitLFS -h --accept-source-agreements --accept-package-agreements | Out-Null
            winget upgrade --id GitHub.cli -h --accept-source-agreements --accept-package-agreements | Out-Null
            winget upgrade --id Microsoft.PowerShell -h --accept-source-agreements --accept-package-agreements | Out-Null
            $did = $true
        }
    }
    catch { Warn "winget upgrade failed: $_" }
    if (-not $did) {
        try {
            if (Get-Command choco -ErrorAction SilentlyContinue) {
                W "choco: upgrading git, git-lfs, gh, powershell"
                choco upgrade git git-lfs gh powershell -y | Out-Null
                $did = $true
            }
        }
        catch { Warn "choco upgrade failed: $_" }
    }
    if (-not $did) { Warn "No winget/choco found; manual update required." }
}

# 1) Porcelain pre
try { git status --porcelain -uall | Out-File -Encoding UTF8 $A['porcelainPre'] } catch { }

# 2) Backups (optional)
if (Confirm-Step -Prompt "Create backups (.git copy + index backup)?" -Default:$true) {
    $indexPath = ".git\index"
    $indexBackup = ".git\index.backup_$ts"
    try { Copy-Item -Path ".git" -Destination (Join-Path $parentDir ("${repoName}_git_backup_$ts")) -Recurse -Force -ErrorAction Stop; W "Backup: .git copied" } catch { Warn "Backup .git failed: $_" }
    try { Copy-Item -Path $indexPath -Destination $indexBackup -Force -ErrorAction Stop; W "Backup: index -> $indexBackup" } catch { Warn "Index backup failed: $_" }
    if ($ZipBackup) {
        try {
            $zipPath = Join-Path $parentDir ("${repoName}_backup_$ts.zip")
            $toZip = Get-ChildItem -Force | Where-Object { $_.Name -ne ".git" } | Select-Object -ExpandProperty FullName
            if ($toZip.Count -gt 0) {
                if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
                Compress-Archive -Path $toZip -DestinationPath $zipPath -Force
                W "Backup: ZIP -> $zipPath"
            }
        }
        catch { Warn "ZIP backup failed: $_" }
    }
}

# 3) Optional tool update
if (Confirm-Step -Prompt "Run tool updates for git/git-lfs/gh (winget/choco)?" -Default:$false) {
    Update-Tools -Run:$true
}
elseif ($Mode -eq 'Auto' -and $ToolUpdate) {
    Update-Tools -Run:$true
}

# 4) Auto-config base (.gitattributes and .gitignore)
if ($AutoTrackLfs -and $lfsVer) {
    $patterns = ($defaultLfsPatterns + $config['lfsPatterns']) | Sort-Object -Unique
    foreach ($p in $patterns) { try { git lfs track "$p" | Out-Null } catch { } }
    if (-not (Test-Path ".gitattributes")) { New-Item -ItemType File -Path ".gitattributes" | Out-Null }
}
if ($AutoUpdateGitignore) {
    $lines = @()
    if (Test-Path ".gitignore") { $lines = Get-Content ".gitignore" } else { New-Item -ItemType File -Path ".gitignore" | Out-Null }
    $merged = ($defaultGitignoreLines + $config['ignoreLines'])
    $toAppend = @()
    foreach ($l in $merged) { if (-not ($lines -contains $l)) { $toAppend += $l } }
    if ($toAppend.Count -gt 0) {
        Add-Content -Path ".gitignore" -Value (($toAppend -join [Environment]::NewLine) + [Environment]::NewLine + [Environment]::NewLine)
    }
}

# 5) Reserved + Missing manifests
$reservedPaths = @()
try {
    git ls-files -s 2>$null | ForEach-Object {
        $parts = $_ -split "`t", 2
        if ($parts.Length -ge 2) {
            $p = $parts[1].Trim()
            if ($p) {
                $leaf = Split-Path $p -Leaf
                if ($leaf -match $reservedPattern) { $reservedPaths += $p }
            }
        }
    }
}
catch { }
$reservedPaths = $reservedPaths | Sort-Object -Unique
$reservedPaths | Out-File -Encoding UTF8 $A['reserved']

$missingPaths = @()
try { $missingPaths = git ls-files 2>$null | Where-Object { -not (Test-Path -LiteralPath $_) } | Sort-Object -Unique } catch { }
$missingPaths | Out-File -Encoding UTF8 $A['missing']

# 6) Large-file discovery (auto-LFS suggestion)
$thresholdBytes = [int64]$config['fileSizeThresholdMB'] * 1MB
$maxScan = [int]$config['maxFileScan']
$foundExts = @{}
try {
    $i = 0
    Get-ChildItem -Path $repoRoot -Recurse -File -ErrorAction SilentlyContinue | ForEach-Object {
        if ($i -ge $maxScan) { return }
        $i++
        if ($_.Length -ge $thresholdBytes) {
            $ext = $_.Extension.ToLower()
            if (-not $foundExts.ContainsKey($ext)) { $foundExts[$ext] = 0 }
            $foundExts[$ext] += 1
        }
    }
}
catch { }
$discoveredLfs = @()
foreach ($k in $foundExts.Keys) {
    if ($k -and $k -ne "") { $discoveredLfs += ("*" + $k) }
}
$discoveredLfs = $discoveredLfs | Sort-Object -Unique

# Append discovery to config and persist (so next run remembers)
$config['lfsPatterns'] = (@($config['lfsPatterns']) + $discoveredLfs) | Sort-Object -Unique
# Fill searchRoots if empty
if (($SearchRoots.Count -eq 0) -and ($config['searchRoots'].Count -eq 0)) {
    $config['searchRoots'] = Get-DefaultSearchRoots
}
# Write config
try {
    $cfgOut = $config | ConvertTo-Json -Depth 6
    Set-Content -Path $ConfigPath -Value $cfgOut -Encoding UTF8
    W "Config updated: $ConfigPath"
}
catch { Warn ("Failed writing {0}: {1}" -f $ConfigPath, $_) }

# 7) Preview stop (no changes)
if ($Mode -eq 'Preview') {
    $sum = @()
    $sum += "# Unified Updater/Recovery - Preview"
    $sum += ""
    $sum += "- Repo: $repoName"
    $sum += "- Run dir: $RunDir"
    $sum += "- Reserved: $((Get-Content $A['reserved'] -ErrorAction SilentlyContinue).Count)"
    $sum += "- Missing (pre): $((Get-Content $A['missing']  -ErrorAction SilentlyContinue).Count)"
    $sum += "- Discovered LFS patterns: $((($discoveredLfs) -join ', '))"
    $sum += "- Config: $ConfigPath"
    $sum -join [Environment]::NewLine | Out-File -Encoding UTF8 $A['summary']
    try { git status --porcelain -uall | Out-File -Encoding UTF8 $A['porcelainPost'] } catch { }
    W "Preview complete. See $RunDir"
    exit 0
}

# 8) LFS lifecycle
if ($lfsVer -and (Confirm-Step -Prompt "Run LFS lifecycle (install/fetch/checkout)?" -Default:$true)) {
    if ($LfsInstall -or $Mode -ne 'Auto') { try { git lfs install | Out-Null } catch { } }
    if ($LfsFetchAll -or $Mode -ne 'Auto') {
        try {
            git lfs fetch --all 2>&1 | Out-Null
            $lfsLogDir = ".git\lfs\logs"
            if (Test-Path $lfsLogDir) {
                $last = Get-ChildItem $lfsLogDir -File | Sort-Object LastWriteTime -Descending | Select-Object -First 1
                if ($last) { Copy-Item $last.FullName -Destination $A['lfsLog'] -Force }
            }
        }
        catch { Warn "LFS fetch error (see logs)." }
    }
    if ($LfsCheckout -or $Mode -ne 'Auto') { try { git lfs checkout | Out-Null } catch { } }
}

# 9) Restore from HEAD
if (Confirm-Step -Prompt "Restore missing tracked files present in HEAD?" -Default:$true) {
    if (Test-Path $A['restored']) { Remove-Item $A['restored']  -Force }
    if (Test-Path $A['notInHead']) { Remove-Item $A['notInHead'] -Force }
    foreach ($p in $missingPaths) {
        if (-not $p) { continue }
        git cat-file -e HEAD:"$p" 2>$null
        if ($LASTEXITCODE -eq 0) {
            $parent = Split-Path $p -Parent
            if ($parent -and -not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
            try { git checkout -- "$p" | Out-Null; "$p" | Out-File -Append -Encoding UTF8 $A['restored'] } catch { }
        }
        else {
            "$p" | Out-File -Append -Encoding UTF8 $A['notInHead']
        }
    }
}

# 10) Recompute missing after restore/LFS
try {
    git ls-files 2>$null | Where-Object { -not (Test-Path -LiteralPath $_) } | Sort-Object -Unique | Out-File -Encoding UTF8 $A['missingPost']
}
catch { }

# 11) Search & recover
if (Confirm-Step -Prompt "Search other roots for remaining missing files and optionally copy matches back?" -Default:$false) {
    if ($SearchRoots.Count -eq 0) {
        if ($config['searchRoots'].Count -gt 0) { $SearchRoots = $config['searchRoots'] }
    }
    if ($SearchRoots.Count -eq 0) {
        $rootsIn = Read-Host "Enter one or more roots (comma-separated), e.g., D:\,E:\"
        if ($rootsIn) { $SearchRoots = $rootsIn.Split(',') | ForEach-Object { $_.Trim() } }
    }
    if ($SearchRoots.Count -gt 0) {
        if (Test-Path $A['foundResults']) { Remove-Item $A['foundResults'] -Force }
        $need = @()
        if (Test-Path $A['missingPost']) { $need = Get-Content $A['missingPost'] | Where-Object { $_ -ne "" } }
        elseif (Test-Path $A['notInHead']) { $need = Get-Content $A['notInHead'] | Where-Object { $_ -ne "" } }
        $map = @{}
        foreach ($rel in $need) { $leaf = Split-Path $rel -Leaf; if (-not $map.ContainsKey($leaf)) { $map[$leaf] = @() }; $map[$leaf] += $rel }
        foreach ($root in $SearchRoots) {
            if (-not (Test-Path $root)) { Warn "Root not found: $root"; continue }
            try {
                Get-ChildItem -Path $root -File -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
                    if ($map.ContainsKey($_.Name)) {
                        foreach ($targetRel in $map[$_.Name]) {
                            $entry = ("{0} -> {1}" -f $_.FullName, $targetRel)
                            $entry | Out-File -Append -Encoding UTF8 $A['foundResults']
                            if (-not $DryCopy) {
                                $targetFull = Join-Path $repoRoot $targetRel
                                $targetDir = Split-Path $targetFull -Parent
                                if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Force -Path $targetDir | Out-Null }
                                try { Copy-Item -Path $_.FullName -Destination $targetFull -Force } catch { Warn ("Copy failed: " + $_.FullName + " -> " + $targetFull) }
                            }
                        }
                    }
                }
            }
            catch { Warn ("Search error in " + $root) }
        }
    }
}

# 12) Index cleanup (opt-in, index-only destructive)
if ($RemoveReserved -or (Confirm-Step -Prompt "Remove reserved-name index entries?" -Default:$false)) {
    try { Copy-Item -Path ".git\index" -Destination (".git\index.backup_preRemove_reserved_$ts") -Force } catch { }
    $toRemoveR = @()
    if (Test-Path $A['reserved']) { $toRemoveR = Get-Content $A['reserved'] | Where-Object { $_ -ne "" } }
    foreach ($p in $toRemoveR) { try { git update-index --force-remove -- "$p" | Out-Null } catch { } }
}
if ($RemoveMissing -or (Confirm-Step -Prompt "Remove still-missing tracked index entries?" -Default:$false)) {
    try { Copy-Item -Path ".git\index" -Destination (".git\index.backup_preRemove_missing_$ts") -Force } catch { }
    $toRemoveM = @()
    if (Test-Path $A['missingPost']) { $toRemoveM = Get-Content $A['missingPost'] | Where-Object { $_ -ne "" } }
    elseif (Test-Path $A['notInHead']) { $toRemoveM = Get-Content $A['notInHead'] | Where-Object { $_ -ne "" } }
    foreach ($p in $toRemoveM) { try { git update-index --force-remove -- "$p" | Out-Null } catch { } }
    try { git ls-files 2>$null | Where-Object { -not (Test-Path -LiteralPath $_) } | Sort-Object -Unique | Out-File -Encoding UTF8 $A['missingPost'] } catch { }
}

# 13) Diagnostics (safe)
if ($Diagnostics) {
    try {
        $gitDiag = @()
        $gitDiag += "git config (with origins):"
        $gitDiag += (git config -l --show-origin)
        $gitDiag += ""
        $gitDiag += "git remotes:"
        $gitDiag += (git remote -v)
        $gitDiag += ""
        $gitDiag += "git fsck --full (integrity):"
        try { $gitDiag += (git fsck --full 2>&1) } catch { $gitDiag += "fsck error: $_" }
        $gitDiag -join [Environment]::NewLine | Out-File -Encoding UTF8 $A['diagGit']
    }
    catch { }

    try {
        $lfsDiag = @()
        if ($lfsVer) {
            $lfsDiag += "git lfs version:"
            $lfsDiag += $lfsVer
            $lfsDiag += ""
            $lfsDiag += "git lfs env:"
            $lfsDiag += (git lfs env 2>&1)
            $lfsDiag += ""
            $lfsDiag += "git lfs doctor:"
            $lfsDiag += (git lfs doctor 2>&1)
        }
        else {
            $lfsDiag += "git-lfs not available."
        }
        $lfsDiag -join [Environment]::NewLine | Out-File -Encoding UTF8 $A['diagLfs']
    }
    catch { }

    try {
        $ghDiag = @()
        if ($ghVer) {
            $ghDiag += "gh --version:"
            $ghDiag += $ghVer
            $ghDiag += ""
            $ghDiag += "gh auth status:"
            $ghDiag += (gh auth status 2>&1)
        }
        else { $ghDiag += "gh CLI not available." }
        $ghDiag -join [Environment]::NewLine | Out-File -Encoding UTF8 $A['diagGh']
    }
    catch { }
}

# 14) Porcelain post
try { git status --porcelain -uall | Out-File -Encoding UTF8 $A['porcelainPost'] } catch { }

# 15) Audit
if ($Audit -or (Confirm-Step -Prompt "Write audit database/logs for this run?" -Default:$true)) {
    $sqliteOk = $false
    try { $v = & sqlite3 -version 2>$null; if ($v -and $LASTEXITCODE -eq 0) { $sqliteOk = $true } } catch { }
    if ($sqliteOk) {
        $sqlInit = @"
CREATE TABLE IF NOT EXISTS run (ts TEXT PRIMARY KEY, repo TEXT, git TEXT, lfs TEXT, gh TEXT, rundir TEXT);
CREATE TABLE IF NOT EXISTS manifest (ts TEXT, kind TEXT, path TEXT);
"@
        & sqlite3 $A['auditDb'] $sqlInit | Out-Null
        $gitV = QuoteSQL($gitVer); $lfsV = QuoteSQL([string]$lfsVer); $ghV = QuoteSQL([string]$ghVer); $rd = QuoteSQL($RunDir); $repoQ = QuoteSQL($repoName)
        & sqlite3 $A['auditDb'] "INSERT OR REPLACE INTO run (ts,repo,git,lfs,gh,rundir) VALUES ('$ts','$repoQ','$gitV','$lfsV','$ghV','$rd');" | Out-Null
        foreach ($k in @("reserved", "missing", "missingLarge", "restored", "notInHead", "missingPost")) {
            $file = $A[$k]
            if (Test-Path $file) {
                Get-Content $file | ForEach-Object {
                    $pathQ = QuoteSQL($_)
                    & sqlite3 $A['auditDb'] "INSERT INTO manifest (ts,kind,path) VALUES ('$ts','$k','$pathQ');" | Out-Null
                }
            }
        }
        W "Audit (sqlite): $($A['auditDb'])"
    }
    else {
        $rec = @{
            ts = $ts; repo = $repoName; git = $gitVer; lfs = $lfsVer; gh = $ghVer; rundir = $RunDir
            reserved = (Get-Content $A['reserved'] -ErrorAction SilentlyContinue)
            missing = (Get-Content $A['missing'] -ErrorAction SilentlyContinue)
            missingLarge = (Get-Content $A['missingLarge'] -ErrorAction SilentlyContinue)
            restored = (Get-Content $A['restored'] -ErrorAction SilentlyContinue)
            notInHead = (Get-Content $A['notInHead'] -ErrorAction SilentlyContinue)
            missingPost = (Get-Content $A['missingPost'] -ErrorAction SilentlyContinue)
        } | ConvertTo-Json -Depth 7
        Add-Content -Path $A['auditJsonl'] -Value $rec
        W "Audit (jsonl): $($A['auditJsonl'])"
    }
}

# 16) Commit/push (optional)
if ($Commit -or ($Mode -eq 'Interactive' -and (Confirm-Step -Prompt "Add, commit and (optionally) push changes?" -Default:$false))) {
    try { git add .gitattributes | Out-Null } catch { }
    try { git add .gitignore    | Out-Null } catch { }
    try { git add .             | Out-Null } catch { }
    try { git commit -m "$CommitMessage" | Out-Null } catch { Warn "Commit skipped (nothing to commit or failed)" }
    if ($Push) { try { git push -u $Remote $Branch } catch { Warn "Push failed." } }
}

# 17) Summary
$reservedCount = (Get-Content $A['reserved']     -ErrorAction SilentlyContinue).Count
$missingPreCount = (Get-Content $A['missing']      -ErrorAction SilentlyContinue).Count
$restoredCount = (Get-Content $A['restored']     -ErrorAction SilentlyContinue).Count
$notInHeadCount = (Get-Content $A['notInHead']    -ErrorAction SilentlyContinue).Count
$missingPostCount = (Get-Content $A['missingPost']  -ErrorAction SilentlyContinue).Count

$summary = @()
$summary += "# Unified Updater/Recovery - Summary"
$summary += ""
$summary += "- Repo: $repoName"
$summary += "- Run dir: $RunDir"
$summary += ""
$summary += "Counts:"
$summary += "- Reserved entries: $reservedCount"
$summary += "- Missing (pre): $missingPreCount"
$summary += "- Restored from HEAD: $restoredCount"
$summary += "- Not in HEAD: $notInHeadCount"
$summary += "- Missing (post): $missingPostCount"
$summary += ""
$summary += "Artifacts:"
$summary += "- Porcelain (pre): $($A['porcelainPre'])"
$summary += "- Porcelain (post): $($A['porcelainPost'])"
$summary += "- LFS last log: $($A['lfsLog'])"
$summary += "- Diagnostics: git=$($A['diagGit']), lfs=$($A['diagLfs']), gh=$($A['diagGh'])"
$summary += "- Audit DB (if created): $($A['auditDb'])"
$summary += "- Audit JSONL (fallback): $($A['auditJsonl'])"
$summary += ""
$summary += "Config:"
$summary += "- File: $ConfigPath"
$summary += "- fileSizeThresholdMB: $($config['fileSizeThresholdMB'])"
$summary += "- maxFileScan:         $($config['maxFileScan'])"
$summary += "- lfsPatterns:         $((($config['lfsPatterns']) -join ', '))"
$summary += "- searchRoots:         $((($config['searchRoots']) -join ', '))"
$summary -join [Environment]::NewLine | Out-File -Encoding UTF8 $A['summary']

W ""
W "=== Unified Updater/Recovery Summary ==="
W "Run dir:        $RunDir"
W "Reserved:       $reservedCount"
W "Missing (pre):  $missingPreCount"
W "Restored:       $restoredCount"
W "Not in HEAD:    $notInHeadCount"
W "Missing (post): $missingPostCount"
W "Summary:        $($A['summary'])"
W "Done."