#!/usr/bin/env pwsh

<#
Synopsis:
  Detect reserved-device basenames in Git index and list index entries missing from disk.
  Optionally remove missing or reserved index entries after backing up .git/index.

Usage examples:
  # Dry-run report (default)
  .\git-lfs-fix.ps1

  # Remove missing index entries after backup (non-interactive)
  .\git-lfs-fix.ps1 -RemoveMissing

  # Remove reserved-device basename entries (if any) after backup
  .\git-lfs-fix.ps1 -RemoveReserved

  # Combine flags (removes both missing + reserved after backing up)
  .\git-lfs-fix.ps1 -RemoveMissing -RemoveReserved

Notes:
  - The script only modifies the index when you pass -RemoveMissing and/or -RemoveReserved.
  - Before any destructive change, it saves .git\index to .git\index.backup.
  - Review ./missing-files.txt and ./reserved-entries.txt before removing.
  - Run in the repository root.

#>

param(
  [switch]$RemoveMissing,
  [switch]$RemoveReserved,
  [switch]$VerboseOutput
)

function Write-Log {
  param($m)
  Write-Host $m
}

# Ensure we are in a git repo
if (-not (Test-Path ".git")) {
  Write-Error "No .git directory found. Run this script from the repository root."
  exit 1
}

# 1) Detect reserved-device basenames in index (robust parsing)
$reservedPattern = '^(nul|con|prn|aux|clock\$|com[1-9]|lpt[1-9])$'
$reservedOutput = @()
git ls-files -s 2>$null | ForEach-Object {
  # git ls-files -s lines contain a tab before the path; split by tab to get the path robustly
  $parts = $_ -split "`t", 2
  if ($parts.Length -ge 2) {
    $path = $parts[1].Trim()
    if ($path -ne "") {
      $leaf = Split-Path $path -Leaf
      if ($leaf -match $reservedPattern) {
        $reservedOutput += $path
      }
    }
  }
}

# Write reserved entries
$reservedFile = ".\reserved-entries.txt"
$reservedOutput | Sort-Object -Unique | Out-File -FilePath $reservedFile -Encoding UTF8
if ($reservedOutput.Count -gt 0) {
  Write-Log "Found reserved-name index entries (written to $reservedFile):"
  $reservedOutput | ForEach-Object { Write-Host "  $_" }
} else {
  Write-Log "No reserved-device basenames found in index. ($reservedFile created but empty)"
}

# 2) Detect index entries missing on disk
$missingFile = ".\missing-files.txt"
$missing = git ls-files 2>$null | Where-Object { -not (Test-Path $_) } | Sort-Object -Unique
$missing | Out-File -FilePath $missingFile -Encoding UTF8
Write-Log "Missing index entries (written to $missingFile). Count: $($missing.Count)"
if ($missing.Count -le 40) {
  $missing | ForEach-Object { Write-Host "  $_" }
} else {
  Write-Log "Large list. Open $missingFile to review the full list."
}

# If no removal requested, exit with instructions
if (-not $RemoveMissing -and -not $RemoveReserved) {
  Write-Log ""
  Write-Log "No removal flags passed. Review the files and then re-run with -RemoveMissing and/or -RemoveReserved if you want the script to remove index entries."
  Write-Log "Example: .\\git-lfs-fix.ps1 -RemoveMissing"
  Write-Log ""
  Write-Log "Next recommended steps:"
  Write-Log "  1) Inspect ./reserved-entries.txt and ./missing-files.txt in VS Code."
  Write-Log "  2) Restore any important missing files to the paths in missing-files.txt if you want them kept and tracked by LFS."
  Write-Log "  3) If you decide to remove stale entries, re-run this script with -RemoveMissing (and/or -RemoveReserved)."
  exit 0
}

# 3) Back up .git/index before destructive operations
$indexPath = ".git\index"
$indexBackup = ".git\index.backup_script_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
try {
  Copy-Item -Path $indexPath -Destination $indexBackup -Force
  Write-Log "Backed up index to: $indexBackup"
} catch {
  Write-Error "Failed to back up .git/index: $_"
  exit 2
}

# 4) Remove missing entries if requested
if ($RemoveMissing) {
  if ($missing.Count -eq 0) {
    Write-Log "No missing index entries to remove."
  } else {
    Write-Log "Removing missing index entries from index..."
    foreach ($p in $missing) {
      if ($p -and $p.Trim() -ne "") {
        Write-Host "  Removing: $p"
        # Use -- to ensure proper handling of paths that start with '-' etc.
        git update-index --force-remove -- "$p" 2>&1 | ForEach-Object { if ($VerboseOutput) { Write-Host $_ } }
      }
    }
    Write-Log "Removal of missing entries complete."
  }
}

# 5) Remove reserved entries if requested
if ($RemoveReserved) {
  $reservedToRemove = Get-Content $reservedFile | Where-Object { $_ -ne "" } | Sort-Object -Unique
  if ($reservedToRemove.Count -eq 0) {
    Write-Log "No reserved entries found to remove."
  } else {
    Write-Log "Removing reserved-name entries from index..."
    foreach ($p in $reservedToRemove) {
      Write-Host "  Removing reserved entry: $p"
      git update-index --force-remove -- "$p" 2>&1 | ForEach-Object { if ($VerboseOutput) { Write-Host $_ } }
    }
    Write-Log "Removal of reserved entries complete."
  }
}

# 6) Re-generate lists after removals
$newMissing = git ls-files 2>$null | Where-Object { -not (Test-Path $_) } | Sort-Object -Unique
$newReserved = git ls-files -s 2>$null | ForEach-Object { $parts = $_ -split "`t", 2; if ($parts.Length -ge 2) { $p = $parts[1]; $leaf = Split-Path $p -Leaf; if ($leaf -match $reservedPattern) { $p } } } | Sort-Object -Unique

$newMissing | Out-File -FilePath $missingFile -Encoding UTF8
$newReserved | Out-File -FilePath $reservedFile -Encoding UTF8

Write-Log "Post-change summary:"
Write-Log "  missing-files.txt count: $($newMissing.Count)"
Write-Log "  reserved-entries.txt count: $($newReserved.Count)"
Write-Log ""
Write-Log "If counts are zero you can now run:"
Write-Host "  git add .gitattributes"
Write-Host "  git add ."
Write-Host "  git commit -m 'Initial dump: enable Git LFS and add workspace contents'"
Write-Host "  git push -u origin main"
Write-Log ""
Write-Log "If anything unexpected occurred, you can restore the previous index with:"
Write-Host "  copy `"$indexBackup`" .git\index"
Write-Log "End of script."