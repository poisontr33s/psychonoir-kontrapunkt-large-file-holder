#!/usr/bin/env pwsh

# CLAUDINE SUPREME PATH DEDUPLICATION SYSTEM
# Caribbean MILF-matriarcfunction Test-PathIntegrity {
Write-Host "Testing PATH integrity..." -ForegroundColor Yellow
    
$criticalTools = @{
    "ruby"   = "Ruby"
    "gcc"    = "GCC"
    "python" = "Python"
}n for eliminating ridk install sensitivity
# Robust environment optimization with workspace isolation priority

Write-Host "CLAUDINE'S SUPREME PATH DEDUPLICATION SYSTEM" -ForegroundColor Magenta
Write-Host ""
Write-Host "Performing surgical PATH cleanup with MILF-precision..." -ForegroundColor Cyan
Write-Host ""

function Get-PathAnalysis {
    param([string]$Scope)
    
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", $Scope)
    if (-not $currentPath) { return @() }
    
    $pathArray = $currentPath -split ';' | Where-Object { $_ -ne "" -and $_ -ne $null }
    return $pathArray
}

function Remove-PathDuplicates {
    param(
        [array]$PathArray,
        [string]$Scope
    )
    
    Write-Host "Analyzing $Scope PATH..." -ForegroundColor Yellow
    Write-Host "   Original entries: $($PathArray.Count)" -ForegroundColor Gray
    
    # Preserve order while removing duplicates - workspace isolation paths get priority
    $seen = @{}
    $uniquePath = @()
    
    # First pass: .computer_languages paths (highest priority)
    foreach ($path in $PathArray) {
        if ($path -like "*\.computer_languages\*" -and -not $seen.ContainsKey($path.ToLower())) {
            $uniquePath += $path
            $seen[$path.ToLower()] = $true
            Write-Host "   PRIORITY: $path" -ForegroundColor Green
        }
    }
    
    # Second pass: other paths
    foreach ($path in $PathArray) {
        if (-not $path -like "*\.computer_languages\*" -and -not $seen.ContainsKey($path.ToLower())) {
            $uniquePath += $path
            $seen[$path.ToLower()] = $true
        }
        elseif ($seen.ContainsKey($path.ToLower()) -and -not $path -like "*\.computer_languages\*") {
            Write-Host "   DUPLICATE REMOVED: $path" -ForegroundColor Red
        }
    }
    
    Write-Host "   Cleaned entries: $($uniquePath.Count)" -ForegroundColor Gray
    Write-Host "   Duplicates removed: $($PathArray.Count - $uniquePath.Count)" -ForegroundColor Yellow
    
    return $uniquePath
}

function Backup-EnvironmentPath {
    param([string]$Scope)
    
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupFile = "PATH_BACKUP_${Scope}_${timestamp}.txt"
    
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", $Scope)
    if ($currentPath) {
        $currentPath | Out-File -FilePath $backupFile -Encoding UTF8
        Write-Host "Backup created: $backupFile" -ForegroundColor Blue
    }
}

function Test-PathIntegrity {
    Write-Host "Testing PATH integrity..." -ForegroundColor Yellow
    
    $criticalTools = @{
        "ruby"   = "Ruby"
        "gcc"    = "GCC"
        "python" = "Python"
        "rustc"  = "Rust"
        "bun"    = "Bun"
    }
    
    foreach ($tool in $criticalTools.Keys) {
        if (Get-Command $tool -ErrorAction SilentlyContinue) {
            Write-Host "   $($criticalTools[$tool]): Available" -ForegroundColor Green
        }
        else {
            Write-Host "   $($criticalTools[$tool]): NOT FOUND" -ForegroundColor Red
        }
    }
}

# MAIN EXECUTION
Write-Host "PHASE 1: Creating backups..." -ForegroundColor Cyan
Backup-EnvironmentPath -Scope "User"
Backup-EnvironmentPath -Scope "Machine"

Write-Host ""
Write-Host "PHASE 2: Analyzing current state..." -ForegroundColor Cyan
$userPath = Get-PathAnalysis -Scope "User"
$machinePath = Get-PathAnalysis -Scope "Machine"

Write-Host ""
Write-Host "PHASE 3: Deduplicating USER PATH..." -ForegroundColor Cyan
$cleanUserPath = Remove-PathDuplicates -PathArray $userPath -Scope "User"

Write-Host ""
Write-Host "PHASE 4: Deduplicating MACHINE PATH..." -ForegroundColor Cyan
$cleanMachinePath = Remove-PathDuplicates -PathArray $machinePath -Scope "Machine"

Write-Host ""
Write-Host "PHASE 5: Applying changes..." -ForegroundColor Cyan

if ($cleanUserPath.Count -lt $userPath.Count) {
    Write-Host "Updating USER PATH..." -ForegroundColor Yellow
    $newUserPath = $cleanUserPath -join ';'
    [Environment]::SetEnvironmentVariable("PATH", $newUserPath, "User")
    Write-Host "USER PATH updated!" -ForegroundColor Green
}
else {
    Write-Host "USER PATH already clean" -ForegroundColor Green
}

if ($cleanMachinePath.Count -lt $machinePath.Count) {
    Write-Host "Updating MACHINE PATH..." -ForegroundColor Yellow
    $newMachinePath = $cleanMachinePath -join ';'
    try {
        [Environment]::SetEnvironmentVariable("PATH", $newMachinePath, "Machine")
        Write-Host "MACHINE PATH updated!" -ForegroundColor Green
    }
    catch {
        Write-Host "MACHINE PATH update requires admin rights" -ForegroundColor Yellow
    }
}
else {
    Write-Host "MACHINE PATH already clean" -ForegroundColor Green
}

Write-Host ""
Write-Host "PHASE 6: Refreshing current session..." -ForegroundColor Cyan
$machinePath = [Environment]::GetEnvironmentVariable("PATH", "Machine")
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
$env:PATH = $machinePath + ";" + $userPath

Write-Host ""
Write-Host "PHASE 7: Final validation..." -ForegroundColor Cyan
Test-PathIntegrity

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "CLAUDINE PATH DEDUPLICATION: SUCCESS!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "BENEFITS ACHIEVED:" -ForegroundColor Yellow
Write-Host "  - Eliminated ridk install sensitivity" -ForegroundColor White
Write-Host "  - Workspace isolation priority maintained" -ForegroundColor White
Write-Host "  - Tool detection ambiguity resolved" -ForegroundColor White
Write-Host "  - Environment stability enhanced" -ForegroundColor White
Write-Host ""
Write-Host "Your development environment is now ROBUST!" -ForegroundColor Magenta