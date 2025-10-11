<#
restore-and-preserve.ps1

Safe recovery script (non-destructive). Run from repository root.

What it does (high level):
 - creates backups (.zip of repo; copy of .git)
 - backs up .git\index with timestamp
 - fetches all git-lfs objects
 - generates missing-files.txt if missing
 - restores any missing index path that exists in HEAD (git checkout -- path)
 - runs `git lfs checkout` to materialize LFS files
 - writes restored-in-head.txt and missing-not-in-head.txt
 - leaves index entries alone (no removals)
#>

param(
    [switch]$Verbose
)

function Log { param($m) Write-Host $m }

# 0) sanity
if (-not (Test-Path ".git")) {
    Write-Error "No .git directory found. Run this from the repository root."
    exit 1
}

# 1) timestamps & names
$ts = (Get-Date).ToString("yyyyMMdd_HHmmss")
$repoName = Split-Path -Leaf (Get-Location)
$parent = (Get-Location).Parent.FullName
$backupZip = Join-Path $parent ("${repoName}_backup_$ts.zip")
$gitBackupDir = Join-Path $parent ("${repoName}_git_backup_$ts")

# 2) create a ZIP backup of the working tree (safe copy)
try {
    Log "Creating repo ZIP backup (may take time): $backupZip"
    if (Test-Path $backupZip) { Remove-Item $backupZip -Force }
    Compress-Archive -Path * -DestinationPath $backupZip -Force -ErrorAction Stop
    Log "ZIP backup created: $backupZip"
}
catch {
    Write-Warning "Compress-Archive failed or was partially successful: $_. Will continue with separate .git copy."
}

# 3) copy .git directory for safety (faster and safer for git internals)
try {
    Log "Copying .git to: $gitBackupDir"
    Copy-Item -Path ".git" -Destination $gitBackupDir -Recurse -Force -ErrorAction Stop
    Log ".git copied to: $gitBackupDir"
}
catch {
    Write-Warning "Failed to copy .git: $_"
}

# 4) backup .git\index
$index = ".git\index"
$indexBackup = ".git\index.backup_preserve_$ts"
try {
    Copy-Item -Path $index -Destination $indexBackup -Force -ErrorAction Stop
    Log "Backed up index to: $indexBackup"
}
catch {
    Write-Warning "Could not back up .git\index: $_"
}

# 5) attempt to fetch all LFS objects (non-destructive)
try {
    Log "Fetching all Git LFS objects (git lfs fetch --all)..."
    git lfs fetch --all 2>&1 | ForEach-Object { if ($Verbose) { Write-Host $_ } }
    Log "LFS fetch attempted."
}
catch {
    Write-Warning "git lfs fetch failed or not available: $_"
}

# 6) generate missing-files.txt if not yet present
$missingFile = ".\missing-files.txt"
if (-not (Test-Path $missingFile)) {
    Log "Generating missing-files.txt ..."
    git ls-files | Where-Object { -not (Test-Path $_) } | Sort-Object -Unique | Out-File -FilePath $missingFile -Encoding UTF8
    Log "Missing file paths written to $missingFile (count: $((Get-Content $missingFile).Count))"
}
else {
    Log "$missingFile already exists (not regenerated). Count: $((Get-Content $missingFile).Count)"
}

# 7) Attempt to restore from HEAD only the files that are missing on disk
$restoredFile = ".\restored-in-head.txt"
$notInHeadFile = ".\missing-not-in-head.txt"
if (Test-Path $restoredFile) { Remove-Item $restoredFile -Force }
if (Test-Path $notInHeadFile) { Remove-Item $notInHeadFile -Force }

$missingPaths = Get-Content $missingFile | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" }
$restoredCount = 0
$notInHeadCount = 0

foreach ($p in $missingPaths) {
    # git cat-file -e HEAD:"path" will set non-zero exit code if object not present in HEAD
    git cat-file -e HEAD:"$p" 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Restoring from HEAD: $p"
        # ensure parent folder exists on disk before checkout
        $parentDir = Split-Path $p -Parent
        if ($parentDir -and -not (Test-Path $parentDir)) {
            New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
        }
        git checkout -- "$p" 2>&1 | ForEach-Object { if ($Verbose) { Write-Host $_ } }
        "$p" | Out-File -FilePath $restoredFile -Append -Encoding UTF8
        $restoredCount++
    }
    else {
        "$p" | Out-File -FilePath $notInHeadFile -Append -Encoding UTF8
        $notInHeadCount++
    }
}

Log "Restored from HEAD: $restoredCount files (list: $restoredFile)"
Log "Not in HEAD: $notInHeadCount files (list: $notInHeadFile)"

# 8) Attempt to materialize LFS files in working tree
try {
    Log "Running git lfs checkout to materialize LFS objects into working tree..."
    git lfs checkout 2>&1 | ForEach-Object { if ($Verbose) { Write-Host $_ } }
    Log "git lfs checkout completed (if LFS pointers existed)."
}
catch {
    Write-Warning "git lfs checkout failed or no LFS items to checkout: $_"
}

# 9) final summary
Log ""
Log "=== Summary ==="
Log "Repo ZIP backup (if created): $backupZip"
Log ".git backup dir: $gitBackupDir"
Log "Index backup: $indexBackup"
Log "Missing-file manifest: $missingFile (total: $($missingPaths.Count))"
Log "Restored-from-HEAD list: $restoredFile (count: $restoredCount)"
Log "Remaining not-in-HEAD list: $notInHeadFile (count: $notInHeadCount)"
Log ""
Log "Next recommended actions:"
Log "  - Inspect $restoredFile and $notInHeadFile in VS Code."
Log "  - For restored files: `git add .gitattributes; git add .; git commit -m \"Restore missing files from HEAD\"`"
Log "  - For missing-not-in-head items, search backups/archives or external disks, or keep the manifest if you plan to recover later."
Log ""
Log "IMPORTANT: This script did NOT remove index entries. If you want me to remove stale index entries later, we will do that only after you confirm backups and restoration."
Log "End."