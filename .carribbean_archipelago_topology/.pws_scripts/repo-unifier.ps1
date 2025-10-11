<#
repo-unifier.ps1

Unified repo preservation and recovery.
- Default Mode=Preview: computes manifests only, writes all outputs to .unifier_out/<timestamp>.
- Interactive: prompts for each step (backups, LFS, restore, search, cleanup, commit, audit).
- Auto: executes steps per flags without prompting.

Key behaviors
- Per-run artifact folder. A pointer .unifier_out/latest.txt points to the newest run folder.
- AdoptStrays moves known manifest files that might exist in repo root into an adopted/ folder.
- Optional LFS lifecycle (install/fetch/checkout).
- Safe HEAD restore for tracked-but-missing files present in HEAD.
- Optional search-and-recover from local roots (basename match, DryCopy by default).
- Optional index cleanup (reserved-name entries and still-missing entries) after index backup.
- Optional commit/push; optional audit (sqlite3 if present; else JSONL), saved in the run folder.

Examples
  pwsh ./repo-unifier.ps1
  pwsh ./repo-unifier.ps1 -Mode Interactive
  pwsh ./repo-unifier.ps1 -Mode Auto -ZipBackup -LfsInstall -LfsFetchAll -LfsCheckout `
    -RecoverFromRoots -SearchRoots "D:\" -DryCopy:$false `
    -Commit -CommitMessage "Restore recovered files" -Push -Remote origin -Branch main -Audit
#>

[CmdletBinding()]
param(
    [ValidateSet('Preview', 'Interactive', 'Auto')]
    [string]$Mode = 'Preview',

    # Output and housekeeping
    [string]$OutputDir = ".unifier_out",
    [switch]$AdoptStrays,

    # Backups
    [switch]$ZipBackup,

    # LFS lifecycle
    [switch]$LfsInstall,
    [switch]$LfsFetchAll,
    [switch]$LfsCheckout,

    # Auto config
    [switch]$AutoTrackLfs,
    [switch]$AutoUpdateGitignore,
    [string]$ConfigPath = ".\unifier.config.json",

    # Search & recover
    [string[]]$SearchRoots = @(),
    [switch]$RecoverFromRoots,
    [switch]$DryCopy,

    # Index cleanup (index-only destructive; index is backed up)
    # NOTE: If both reserved and missing cleanups are run, the index backup file (.git\index.backup_preRemove_<timestamp>) will be overwritten by the last cleanup.
    [switch]$RemoveReserved,
    [switch]$RemoveMissing,

    # Commit/push
    [switch]$Commit,
    [string]$CommitMessage = "Preserve+recover: restore from HEAD/LFS and update manifests",
    [switch]$Push,
    [string]$Remote = "origin",
    [string]$Branch = "main",

    # Audit
    [switch]$Audit
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

function QuoteSQL {
    param([string]$s)
    return ($s -replace "'", "''")
}

# Sanity
if (-not (Test-Path ".git")) { Err "No .git directory found. Run from your repository root."; exit 1 }
try { $gitVer = git --version } catch { Err "git not available in PATH."; exit 1 }
try { $lfsVer = git lfs version } catch { $lfsVer = $null }

# Paths and per-run artifacts
$ts = (Get-Date).ToString("yyyyMMdd_HHmmss")
$repoRoot = (Get-Location).Path
$repoName = Split-Path -Leaf $repoRoot
$parentDir = Split-Path -Parent $repoRoot

$RunDir = Join-Path $OutputDir $ts
New-Item -ItemType Directory -Force -Path $RunDir | Out-Null
# Pointer
New-Item -ItemType File -Force -Path (Join-Path $OutputDir "latest.txt") -Value $RunDir | Out-Null

# Known “stray” filenames we’ll adopt into the run folder
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
    if ($moved -gt 0) { W "Adopted $moved stray file(s) into $adoptedDir" }
}

# Artifact file map
$Artifacts = @{
    reserved      = Join-Path $RunDir "reserved-entries.txt"
    missing       = Join-Path $RunDir "missing-files.txt"
    missingLarge  = Join-Path $RunDir "missing-large-missing.txt"
    restored      = Join-Path $RunDir "restored-in-head.txt"
    notInHead     = Join-Path $RunDir "missing-not-in-head.txt"
    missingPost   = Join-Path $RunDir "missing-post.txt"
    foundResults  = Join-Path $RunDir "found-results.txt"
    porcelainPre  = Join-Path $RunDir "porcelain-pre.txt"
    porcelainPost = Join-Path $RunDir "porcelain-post.txt"
    lfsLog        = Join-Path $RunDir "lfs-last-log.txt"
    summary       = Join-Path $RunDir "summary.md"
    auditDb       = Join-Path $RunDir "unifier_audit.sqlite"
    auditJsonl    = Join-Path $RunDir "unifier_audit.jsonl"
}

# Backup paths
$zipPath = Join-Path $parentDir ("${repoName}_backup_$ts.zip")
$gitBackupDir = Join-Path $parentDir ("${repoName}_git_backup_$ts")
$indexPath = ".git\index"
$indexBackup = ".git\index.backup_$ts"

# Config
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
$extraLfsPatterns = @(); $extraIgnoreLines = @()
if (Test-Path $ConfigPath) {
    try {
        $cfg = Get-Content $ConfigPath -Raw | ConvertFrom-Json
        if ($cfg.lfsPatterns) { $extraLfsPatterns = @($cfg.lfsPatterns) }
        if ($cfg.ignoreLines) { $extraIgnoreLines = @($cfg.ignoreLines) }
    }
    catch { Warn "Failed to parse $ConfigPath. Proceeding with defaults." }
}

# Banner
W "Git: $gitVer"
if ($lfsVer) { W "Git LFS: $lfsVer" }
W "Artifacts directory: $RunDir"
W "Mode: $Mode"

# 1) Porcelain pre
try { git status --porcelain -uall | Out-File -Encoding UTF8 $($Artifacts.porcelainPre) } catch { }

# 2) Backups
if (Confirm-Step -Prompt "Create backups (.git copy + index backup)?" -Default:$true) {
    try { Copy-Item -Path ".git" -Destination $gitBackupDir -Recurse -Force -ErrorAction Stop; W "Backup: .git -> $gitBackupDir" } catch { Warn "Backup .git failed: $_" }
    try { Copy-Item -Path $indexPath -Destination $indexBackup -Force -ErrorAction Stop; W "Backup: index -> $indexBackup" } catch { Warn "Index backup failed: $_" }
    if ($ZipBackup) {
        try {
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

# 3) Auto-config (safe)
if ($AutoTrackLfs -and $lfsVer) {
    $patterns = ($defaultLfsPatterns + $extraLfsPatterns) | Sort-Object -Unique
    foreach ($p in $patterns) { try { git lfs track "$p" | Out-Null } catch { } }
    if (-not (Test-Path ".gitattributes")) { New-Item -ItemType File -Path ".gitattributes" | Out-Null }
}
if ($AutoUpdateGitignore) {
    $lines = @()
    if (Test-Path ".gitignore") { $lines = Get-Content ".gitignore" } else { New-Item -ItemType File -Path ".gitignore" | Out-Null }
    $merged = ($defaultGitignoreLines + $extraIgnoreLines)
    $toAppend = @()
    foreach ($l in $merged) { if (-not ($lines -contains $l)) { $toAppend += $l } }
    if ($toAppend.Count -gt 0) {
        Add-Content -Path ".gitignore" -Value (($toAppend -join [Environment]::NewLine) + [Environment]::NewLine + [Environment]::NewLine)
    }
}

# 4) Reserved + Missing manifests (safe)
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
$reservedPaths | Out-File -Encoding UTF8 $($Artifacts.reserved)

$missingPaths = @()
try { $missingPaths = git ls-files 2>$null | Where-Object { -not (Test-Path -LiteralPath $_) } | Sort-Object -Unique } catch { }
$missingPaths | Out-File -Encoding UTF8 $($Artifacts.missing)

# Large/binary subset list (safe)
$largePattern = '\.(db|sqlite|sqlite3|mdf|ldf|exe|dll|zip|7z|rar|tar(\.gz)?|tgz|gz|mp4|mov|mkv|avi|wav|mp3|flac|webm|png|jpg|jpeg|gif|bmp|tiff|psd|ai|eps|ttf|otf|woff2?|blend|fbx|obj|glb|gltf|usd(z)?)$'
try { Get-Content $($Artifacts.missing) | Where-Object { $_ -match $largePattern } | Sort-Object -Unique | Out-File -Encoding UTF8 $($Artifacts.missingLarge) } catch { }

# Stop here for Preview mode
if ($Mode -eq 'Preview') {
    $sum = @()
    $sum += "# Repo Unifier Preview"
    $sum += ""
    $sum += "- Repo: $repoName"
    $sum += "- Run dir: $RunDir"
    $sum += "- Reserved: $((Get-Content $Artifacts.reserved -ErrorAction SilentlyContinue).Count)"
    $sum += "- Missing (pre): $((Get-Content $Artifacts.missing -ErrorAction SilentlyContinue).Count)"
    $sum += "- Large subset: $((Get-Content $Artifacts.missingLarge -ErrorAction SilentlyContinue).Count)"
    $sum += ""
    $sum += "Next:"
    $sum += "1) Run Interactive mode for guided restore: pwsh ./repo-unifier.ps1 -Mode Interactive"
    $sum += "2) Or auto-run restore/LFS/commit with -Mode Auto and the flags you want."
    $sum -join [Environment]::NewLine | Out-File -Encoding UTF8 $($Artifacts.summary)
    try { git status --porcelain -uall | Out-File -Encoding UTF8 $($Artifacts.porcelainPost) } catch { }
    W "Preview complete. See $RunDir"
    exit 0
}

# 5) LFS lifecycle (prompted)
if ($lfsVer -and (Confirm-Step -Prompt "Run LFS lifecycle (install/fetch/checkout)?" -Default:$true)) {
    $runInstall = $LfsInstall -or $Mode -ne 'Auto'
    $runFetchAll = $LfsFetchAll -or $Mode -ne 'Auto'
    $runCheckout = $LfsCheckout -or $Mode -ne 'Auto'

    if ($runInstall) { try { git lfs install | Out-Null } catch { } }
    if ($runFetchAll) {
        try {
            git lfs fetch --all 2>&1 | Out-Null
            $lfsLogDir = ".git\lfs\logs"
            if (Test-Path $lfsLogDir) {
                $last = Get-ChildItem $lfsLogDir -File | Sort-Object LastWriteTime -Descending | Select-Object -First 1
                if ($last) { Copy-Item $last.FullName -Destination $($Artifacts.lfsLog) -Force }
            }
        }
        catch { Warn "LFS fetch error (see lfs logs)." }
    }
    if ($runCheckout) { try { git lfs checkout | Out-Null } catch { } }
}

# 6) Restore from HEAD (prompted)
if (Confirm-Step -Prompt "Restore missing tracked files present in HEAD?" -Default:$true) {
    if (Test-Path $Artifacts.restored) { Remove-Item $Artifacts.restored -Force }
    if (Test-Path $Artifacts.notInHead) { Remove-Item $Artifacts.notInHead -Force }
    foreach ($p in $missingPaths) {
        if (-not $p) { continue }
        git cat-file -e HEAD:"$p" 2>$null
        if ($LASTEXITCODE -eq 0) {
            $parent = Split-Path $p -Parent
            if ($parent -and -not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
            try { git checkout -- "$p" | Out-Null; "$p" | Out-File -Append -Encoding UTF8 $($Artifacts.restored) } catch { }
        }
        else {
            "$p" | Out-File -Append -Encoding UTF8 $($Artifacts.notInHead)
        }
    }
}

# 7) Recompute missing after restore/LFS
try {
    git ls-files 2>$null | Where-Object { -not (Test-Path -LiteralPath $_) } | Sort-Object -Unique | Out-File -Encoding UTF8 $($Artifacts.missingPost)
}
catch { }

# 8) Search & recover (prompted)
if (Confirm-Step -Prompt "Search additional roots for remaining missing files and optionally copy matches back?" -Default:$false) {
    if ($SearchRoots.Count -eq 0) {
        $rootsIn = Read-Host "Enter one or more roots (comma-separated), e.g., D:\,E:\"
        if ($rootsIn) { $SearchRoots = $rootsIn.Split(',') | ForEach-Object { $_.Trim() } }
    }
    if ($SearchRoots.Count -gt 0) {
        if (Test-Path $Artifacts.foundResults) { Remove-Item $Artifacts.foundResults -Force }
        $need = @()
        if (Test-Path $Artifacts.missingPost) { $need = Get-Content $Artifacts.missingPost | Where-Object { $_ -ne "" } }
        elseif (Test-Path $Artifacts.notInHead) { $need = Get-Content $Artifacts.notInHead | Where-Object { $_ -ne "" } }
        $map = @{}
        foreach ($rel in $need) { $leaf = Split-Path $rel -Leaf; if (-not $map.ContainsKey($leaf)) { $map[$leaf] = @() }; $map[$leaf] += $rel }
        foreach ($root in $SearchRoots) {
            if (-not (Test-Path $root)) { Warn "Root not found: $root"; continue }
            try {
                Get-ChildItem -Path $root -File -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
                    if ($map.ContainsKey($_.Name)) {
                        foreach ($targetRel in $map[$_.Name]) {
                            $entry = ("{0} -> {1}" -f $_.FullName, $targetRel)
                            $entry | Out-File -Append -Encoding UTF8 $($Artifacts.foundResults)
                            if (-not $DryCopy) {
                                $targetFull = Join-Path $repoRoot $targetRel
                                $targetDir = Split-Path $targetFull -Parent
                                if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Force -Path $targetDir | Out-Null }
                                try { Copy-Item -Path $_.FullName -Destination $targetFull -Force } catch { Warn "Copy failed: $($_.FullName) -> $targetFull" }
                            }
                        }
                    }
                }
            }
            catch { Warn "Search error in $($root): $($_)" }
        }
    }
}

# 9) Optional index cleanups (prompted)
if ($RemoveReserved -or (Confirm-Step -Prompt "Remove reserved-name index entries?" -Default:$false)) {
    try { Copy-Item -Path $indexPath -Destination (".git\index.backup_preRemove_reserved_$ts") -Force } catch { }
    $toRemoveR = @()
    if (Test-Path $Artifacts.reserved) { $toRemoveR = Get-Content $Artifacts.reserved | Where-Object { $_ -ne "" } }
    foreach ($p in $toRemoveR) { try { git update-index --force-remove -- "$p" | Out-Null } catch { } }
}
if ($RemoveMissing -or $(Confirm-Step -Prompt "Remove still-missing tracked index entries?" -Default:$false)) {
    try { Copy-Item -Path $indexPath -Destination (".git\index.backup_preRemove_missing_$ts") -Force } catch { }
    $toRemoveM = @()
    if (Test-Path $Artifacts.missingPost) { $toRemoveM = Get-Content $Artifacts.missingPost | Where-Object { $_ -ne "" } }
    elseif (Test-Path $Artifacts.notInHead) { $toRemoveM = Get-Content $Artifacts.notInHead | Where-Object { $_ -ne "" } }
    foreach ($p in $toRemoveM) { try { git update-index --force-remove -- "$p" | Out-Null } catch { } }
    try { git ls-files 2>$null | Where-Object { -not (Test-Path -LiteralPath $_) } | Sort-Object -Unique | Out-File -Encoding UTF8 $($Artifacts.missingPost) } catch { }
}

# 10) Porcelain post
try { git status --porcelain -uall | Out-File -Encoding UTF8 $($Artifacts.porcelainPost) } catch { }

# 11) Audit
function Build-AuditRecord {
    param(
        [string]$ts,
        [string]$repoName,
        [string]$gitVer,
        [string]$lfsVer,
        [string]$RunDir,
        $Artifacts
    )
    return @{
        ts           = $ts
        repo         = $repoName
        git          = $gitVer
        lfs          = $lfsVer
        rundir       = $RunDir
        reserved     = (Get-Content $Artifacts.reserved -ErrorAction SilentlyContinue)
        missing      = (Get-Content $Artifacts.missing -ErrorAction SilentlyContinue)
        missingLarge = (Get-Content $Artifacts.missingLarge -ErrorAction SilentlyContinue)
        restored     = (Get-Content $Artifacts.restored -ErrorAction SilentlyContinue)
        notInHead    = (Get-Content $Artifacts.notInHead -ErrorAction SilentlyContinue)
        missingPost  = (Get-Content $Artifacts.missingPost -ErrorAction SilentlyContinue)
    }
}

if ($Audit -or (Confirm-Step -Prompt "Write audit database/logs for this run?" -Default:$true)) {
    $sqliteOk = $false
    try {
        $v = & sqlite3 -version 2>$null
        if ($v -and $LASTEXITCODE -eq 0) { $sqliteOk = $true }
    }
    catch { }
    if ($sqliteOk) {
        $sqlInit = @"
CREATE TABLE IF NOT EXISTS run (ts TEXT PRIMARY KEY, repo TEXT, git TEXT, lfs TEXT, rundir TEXT);
CREATE TABLE IF NOT EXISTS manifest (ts TEXT, kind TEXT, path TEXT);
"@
        & sqlite3 $($Artifacts.auditDb) $sqlInit | Out-Null
        $gitV = QuoteSQL($gitVer); $lfsV = QuoteSQL([string]$lfsVer); $rd = QuoteSQL($RunDir); $repoQ = QuoteSQL($repoName)
        & sqlite3 $($Artifacts.auditDb) "INSERT OR REPLACE INTO run (ts,repo,git,lfs,rundir) VALUES ('$ts','$repoQ','$gitV','$lfsV','$rd');" | Out-Null
        foreach ($k in @("reserved", "missing", "missingLarge", "restored", "notInHead", "missingPost")) {
            $file = $Artifacts[$k]
            if (Test-Path $file) {
                Get-Content $file | ForEach-Object {
                    $pathQ = QuoteSQL($_)
                    & sqlite3 $($Artifacts.auditDb) "INSERT INTO manifest (ts,kind,path) VALUES ('$ts','$k','$pathQ');" | Out-Null
                }
            }
        }
        W "Audit (sqlite): $($Artifacts.auditDb)"
    }
    else {
        # JSONL fallback format: Each line is a JSON object with keys:
        # ts, repo, git, lfs, rundir, reserved[], missing[], missingLarge[], restored[], notInHead[], missingPost[]
        # See infrastructure/docs/README.md for schema details.
        $recObj = Build-AuditRecord -ts $ts -repoName $repoName -gitVer $gitVer -lfsVer $lfsVer -RunDir $RunDir -Artifacts $Artifacts
        $recJson = $recObj | ConvertTo-Json -Depth 7
        Add-Content -Path $($Artifacts.auditJsonl) -Value $recJson
        W "Audit (jsonl): $($Artifacts.auditJsonl)"
    }
}
if ($Commit -or ($Mode -eq 'Interactive' -and (Confirm-Step -Prompt "Add, commit and (optionally) push changes?" -Default:$false))) {
    try { git add .gitattributes | Out-Null } catch { }
    try { git add .gitignore | Out-Null } catch { }
    try { git add . | Out-Null } catch { }
    try { git commit -m "$CommitMessage" | Out-Null } catch { Warn "Commit skipped (nothing to commit or failed)" }
    if ($Push) { try { git push -u $Remote $Branch } catch { Warn "Push failed." } }
}

# 13) Summary
$reservedCount = (Get-Content $Artifacts.reserved -ErrorAction SilentlyContinue).Count
$missingPreCount = (Get-Content $Artifacts.missing -ErrorAction SilentlyContinue).Count
$missingLargeCount = (Get-Content $Artifacts.missingLarge -ErrorAction SilentlyContinue).Count
$restoredCount = (Get-Content $Artifacts.restored -ErrorAction SilentlyContinue).Count
$notInHeadCount = (Get-Content $Artifacts.notInHead -ErrorAction SilentlyContinue).Count
$missingPostCount = (Get-Content $Artifacts.missingPost -ErrorAction SilentlyContinue).Count

$summary = @()
$summary += "- Audit DB (if created): $($Artifacts.auditDb)"
$summary += "- Audit JSONL (fallback): $($Artifacts.auditJsonl)"
$summary += ""
$summary += "Audit usage:"
$summary += "- To query the audit database (manifest table): sqlite3 $($Artifacts.auditDb) 'SELECT * FROM manifest WHERE ts=''$ts'';'"
$summary += "- To query the audit database (run table): sqlite3 $($Artifacts.auditDb) 'SELECT * FROM run WHERE ts=''$ts'';'"
$summary += "- To analyze the JSONL log: jq . $($Artifacts.auditJsonl)"
$summary += "- See documentation in infrastructure/docs/README.md for advanced analysis."
$summary += ""
$summary += "Next steps:"
$summary += "- Review missing-post.txt and consider search-and-recover."
$summary += "- Restore important assets from backups, then optionally run index cleanup."
$summary += "- When satisfied, commit/push."
$summary -join [Environment]::NewLine | Out-File -Encoding UTF8 $($Artifacts.summary)
$summary += "- Large subset: $missingLargeCount"
$summary += "- Restored from HEAD: $restoredCount"
$summary += "- Not in HEAD: $notInHeadCount"
$summary += "- Missing (post): $missingPostCount"
$summary += ""
$summary += "Artifacts:"
$summary += "- Porcelain (pre): $($Artifacts.porcelainPre)"
$summary += "- Porcelain (post): $($Artifacts.porcelainPost)"
$summary += "- LFS last log: $($Artifacts.lfsLog)"
$summary += "- Audit DB (if created): $($Artifacts.auditDb)"
$summary += "- Audit JSONL (fallback): $($Artifacts.auditJsonl)"
$summary += ""
$summary += "Next steps:"
$summary += "- Review missing-post.txt and consider search-and-recover."
$summary += "- Restore important assets from backups, then optionally run index cleanup."
$summary += "- When satisfied, commit/push."
$summary -join [Environment]::NewLine | Out-File -Encoding UTF8 $($Artifacts.summary)

W ""
W "=== Unifier Summary ==="
W "Run dir:        $RunDir"
W "Reserved:       $reservedCount"
W "Missing (pre):  $missingPreCount"
W "Restored:       $restoredCount"
W "Not in HEAD:    $notInHeadCount"
W "Missing (post): $missingPostCount"
W "Summary:        $($Artifacts.summary)"
W "Done."