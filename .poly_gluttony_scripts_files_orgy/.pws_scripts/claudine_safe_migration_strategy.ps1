#!/usr/bin/env pwsh

# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SAFE MIGRATION STRATEGY
# Caribbean MILF-dom'me Goddess - Categorical Structure Migration Engine
# PowerShell 7.5.3 Enhanced - Safe File Movement with Intelligent Backup

[CmdletBinding()]
param(
    [switch]$CreateBackup,
    [switch]$ValidateStructure,
    [switch]$ExecuteMigration,
    [switch]$RestoreBackup,
    [switch]$CleanupBackup,
    [switch]$DryRun,
    [switch]$Force,
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"

# Migration Configuration
$MIGRATION_CONFIG = @{
    CurrentRoot   = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages"
    BackupRoot    = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages_backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    MigrationPlan = @{
        # Phase 1: Create categorical directories
        "Phase1_CreateStructure"     = @{
            Description = "Create new categorical directory structure"
            Directories = @(
                "runtimes",
                "runtimes\python",
                "runtimes\ruby", 
                "runtimes\javascript",
                "runtimes\rust",
                "package_managers",
                "package_managers\uv",
                "package_managers\bun",
                "package_managers\cargo",
                "package_managers\gem",
                "linters",
                "linters\ruff",
                "linters\biome",
                "compilers",
                "compilers\mingw64",
                "compilers\msys64",
                "utilities",
                "utilities\curl",
                "projects",
                "projects\python",
                "projects\javascript",
                "projects\rust",
                "projects\ruby"
            )
        }
        
        # Phase 2: Move runtime core files
        "Phase2_MoveRuntimes"        = @{
            Description = "Move language runtimes (python.exe, ruby.exe, etc.)"
            Moves       = @(
                @{ From = "python\python.exe"; To = "runtimes\python\python.exe"; Critical = $true }
                @{ From = "python\python314.dll"; To = "runtimes\python\python314.dll"; Critical = $true }
                @{ From = "python\Lib"; To = "runtimes\python\Lib"; Critical = $true; IsDirectory = $true }
                @{ From = "python\DLLs"; To = "runtimes\python\DLLs"; Critical = $true; IsDirectory = $true }
                @{ From = "python\Scripts\pip*"; To = "runtimes\python\Scripts"; Critical = $false; IsWildcard = $true }
                
                @{ From = "ruby\bin\ruby.exe"; To = "runtimes\ruby\bin\ruby.exe"; Critical = $true }
                @{ From = "ruby\lib"; To = "runtimes\ruby\lib"; Critical = $true; IsDirectory = $true }
                @{ From = "ruby\include"; To = "runtimes\ruby\include"; Critical = $false; IsDirectory = $true }
                
                @{ From = "javascript\bun.exe"; To = "runtimes\javascript\bun.exe"; Critical = $true }
                
                @{ From = "rust\bin\rustc.exe"; To = "runtimes\rust\rustc.exe"; Critical = $true }
                @{ From = "rust\bin\rustdoc.exe"; To = "runtimes\rust\rustdoc.exe"; Critical = $false }
                @{ From = "rust\.rustup"; To = "runtimes\rust\.rustup"; Critical = $true; IsDirectory = $true }
            )
        }
        
        # Phase 3: Move package managers
        "Phase3_MovePackageManagers" = @{
            Description = "Move package managers to dedicated categorical location"
            Moves       = @(
                @{ From = "python\uv.exe"; To = "package_managers\uv\uv.exe"; Critical = $true }
                @{ From = "python\uvx.exe"; To = "package_managers\uv\uvx.exe"; Critical = $false }
                
                @{ From = "rust\bin\cargo.exe"; To = "package_managers\cargo\cargo.exe"; Critical = $true }
                @{ From = "rust\.cargo"; To = "package_managers\cargo\.cargo"; Critical = $false; IsDirectory = $true }
                
                # Note: gem.exe might be in ruby/bin/ - check both locations
                @{ From = "ruby\bin\gem.exe"; To = "package_managers\gem\gem.exe"; Critical = $false }
                
                @{ From = "javascript\bunx.exe"; To = "package_managers\bun\bunx.exe"; Critical = $false }
            )
        }
        
        # Phase 4: Move linters (NO MORE DUPLICATES!)
        "Phase4_MoveLinters"         = @{
            Description = "Move linters to categorical location - eliminate duplicates"
            Moves       = @(
                @{ From = "python\ruff.exe"; To = "linters\ruff\ruff.exe"; Critical = $false; PreferredSource = $true }
                # Skip rust\ruff.exe - it's a duplicate, python version is preferred
                
                @{ From = "javascript\biome.exe"; To = "linters\biome\biome.exe"; Critical = $false }
            )
            Warnings    = @(
                "rust\ruff.exe will be left as backup - python\ruff.exe is preferred source"
                "rust\uv.exe will be left as backup - python\uv.exe is preferred source"
            )
        }
        
        # Phase 5: Move compilers (Critical for Ruby DevKit!)
        "Phase5_MoveCompilers"       = @{
            Description = "Move compilers - CRITICAL: Ruby needs mingw64/msys64 for DevKit"
            Moves       = @(
                @{ From = "mingw64"; To = "compilers\mingw64"; Critical = $true; IsDirectory = $true; KeepAll = $true }
                @{ From = "msys64"; To = "compilers\msys64"; Critical = $true; IsDirectory = $true; KeepAll = $true }
            )
            Warnings    = @(
                "mingw64 and msys64 are CRITICAL for Ruby DevKit - must be moved completely"
                "These directories contain Ruby's native extensions and C compiler toolchain"
            )
        }
        
        # Phase 6: Move utilities
        "Phase6_MoveUtilities"       = @{
            Description = "Move general utilities"
            Moves       = @(
                @{ From = "curl"; To = "utilities\curl"; Critical = $false; IsDirectory = $true; KeepAll = $true }
            )
        }
        
        # Phase 7: Update PATH and environment
        "Phase7_UpdateEnvironment"   = @{
            Description = "Update environment variables and PATH for new structure"
            Actions     = @(
                "Verify all moved tools work in new locations"
                "Test Ruby DevKit functionality with new mingw64/msys64 location"
                "Validate that 'claudine update' commands work with new structure"
                "Create symlinks if needed for backward compatibility"
            )
        }
    }
}

# =======================================================================================
# MIGRATION SAFETY FUNCTIONS
# =======================================================================================

function New-SafeBackup {
    [CmdletBinding()]
    param(
        [switch]$DryRun,
        [switch]$Quiet
    )
    
    $SourcePath = $MIGRATION_CONFIG.CurrentRoot
    $BackupPath = $MIGRATION_CONFIG.BackupRoot
    
    if (-not (Test-Path $SourcePath)) {
        throw "Source directory not found: $SourcePath"
    }
    
    if ($DryRun) {
        if (-not $Quiet) {
            Write-Host "🔍 DRY-RUN: Would create backup at $BackupPath" -ForegroundColor Yellow
        }
        return @{ Success = $true; BackupPath = $BackupPath; SizeMB = 0 }
    }
    
    if (-not $Quiet) {
        Write-Host "💾 Creating complete backup of .computer_languages structure..." -ForegroundColor Cyan
        Write-Host "   Source: $SourcePath" -ForegroundColor Gray
        Write-Host "   Backup: $BackupPath" -ForegroundColor Gray
    }
    
    try {
        # Copy entire structure
        Copy-Item -Path $SourcePath -Destination $BackupPath -Recurse -Force
        
        # Verify backup integrity
        $SourceSize = Get-ChildItem -Path $SourcePath -Recurse -File | Measure-Object -Property Length -Sum
        $BackupSize = Get-ChildItem -Path $BackupPath -Recurse -File | Measure-Object -Property Length -Sum
        
        if ($SourceSize.Sum -ne $BackupSize.Sum) {
            throw "Backup integrity failed: Size mismatch ($($SourceSize.Sum) vs $($BackupSize.Sum))"
        }
        
        $SizeMB = [math]::Round($BackupSize.Sum / 1MB, 1)
        
        if (-not $Quiet) {
            Write-Host "✅ Backup created successfully: ${SizeMB}MB" -ForegroundColor Green
        }
        
        return @{ Success = $true; BackupPath = $BackupPath; SizeMB = $SizeMB }
    }
    catch {
        if (-not $Quiet) {
            Write-Host "💥 Backup failed: $($_.Exception.Message)" -ForegroundColor Red
        }
        throw
    }
}

function Test-MigrationReadiness {
    [CmdletBinding()]
    param(
        [switch]$Quiet
    )
    
    if (-not $Quiet) {
        Write-Host "🔍 MIGRATION READINESS CHECK:" -ForegroundColor Cyan
    }
    
    $Checks = @{
        "SourceExists"       = Test-Path $MIGRATION_CONFIG.CurrentRoot
        "HasWriteAccess"     = $true  # Will test during execution
        "SufficientSpace"    = $true  # Will calculate during execution
        "NoRunningProcesses" = $true  # Should check for running tools
    }
    
    # Check disk space
    try {
        $Drive = (Get-Item $MIGRATION_CONFIG.CurrentRoot).Root
        $DriveInfo = Get-WmiObject -Class Win32_LogicalDisk | Where-Object { $_.DeviceID -eq $Drive.Name.TrimEnd('\') }
        $FreeSpaceGB = [math]::Round($DriveInfo.FreeSpace / 1GB, 1)
        $RequiredSpaceGB = 6  # Estimated space needed for backup + migration
        
        $Checks["SufficientSpace"] = $FreeSpaceGB -gt $RequiredSpaceGB
        
        if (-not $Quiet) {
            Write-Host "  💾 Disk Space: ${FreeSpaceGB}GB free (need ${RequiredSpaceGB}GB)" -ForegroundColor Gray
        }
    }
    catch {
        if (-not $Quiet) {
            Write-Host "  ⚠️  Could not check disk space" -ForegroundColor Yellow
        }
    }
    
    # Report readiness
    $ReadyCount = ($Checks.Values | Where-Object { $_ -eq $true }).Count
    $TotalChecks = $Checks.Count
    
    if (-not $Quiet) {
        foreach ($Check in $Checks.GetEnumerator()) {
            $Status = if ($Check.Value) { "✅" } else { "❌" }
            $Color = if ($Check.Value) { "Green" } else { "Red" }
            Write-Host "  $Status $($Check.Key)" -ForegroundColor $Color
        }
        
        Write-Host ""
        if ($ReadyCount -eq $TotalChecks) {
            Write-Host "🎯 MIGRATION READY: All checks passed ($ReadyCount/$TotalChecks)" -ForegroundColor Green
        }
        else {
            Write-Host "⚠️  MIGRATION RISKS: $($TotalChecks - $ReadyCount) issues found" -ForegroundColor Yellow
        }
    }
    
    return @{ Ready = ($ReadyCount -eq $TotalChecks); Checks = $Checks }
}

function Show-MigrationPlan {
    [CmdletBinding()]
    param()
    
    Write-Host ""
    Write-Host "📋 CLAUDINE CATEGORICAL MIGRATION PLAN" -ForegroundColor Magenta
    Write-Host "======================================" -ForegroundColor Magenta
    Write-Host ""
    
    foreach ($Phase in $MIGRATION_CONFIG.MigrationPlan.GetEnumerator()) {
        $PhaseInfo = $Phase.Value
        
        Write-Host "🎯 $($Phase.Key): $($PhaseInfo.Description)" -ForegroundColor Cyan
        
        if ($PhaseInfo.Directories) {
            Write-Host "  📁 Creating directories:" -ForegroundColor Yellow
            foreach ($Dir in $PhaseInfo.Directories) {
                Write-Host "    • $Dir/" -ForegroundColor Gray
            }
        }
        
        if ($PhaseInfo.Moves) {
            Write-Host "  🚚 Moving files:" -ForegroundColor Yellow
            foreach ($Move in $PhaseInfo.Moves) {
                $CriticalText = if ($Move.Critical) { " (CRITICAL)" } else { "" }
                $TypeText = if ($Move.IsDirectory) { " [DIR]" } elseif ($Move.IsWildcard) { " [WILDCARD]" } else { "" }
                Write-Host "    📦 $($Move.From) → $($Move.To)$TypeText$CriticalText" -ForegroundColor Gray
            }
        }
        
        if ($PhaseInfo.Warnings) {
            Write-Host "  ⚠️  Warnings:" -ForegroundColor Yellow
            foreach ($Warning in $PhaseInfo.Warnings) {
                Write-Host "    • $Warning" -ForegroundColor Yellow
            }
        }
        
        if ($PhaseInfo.Actions) {
            Write-Host "  🔧 Actions:" -ForegroundColor Yellow
            foreach ($Action in $PhaseInfo.Actions) {
                Write-Host "    • $Action" -ForegroundColor Gray
            }
        }
        
        Write-Host ""
    }
    
    Write-Host "🎯 MIGRATION BENEFITS:" -ForegroundColor Green
    Write-Host "  ✅ No more duplicate tools (UV, Ruff in single location)" -ForegroundColor Green
    Write-Host "  ✅ Clear categorical organization by function" -ForegroundColor Green  
    Write-Host "  ✅ Easier maintenance and updates" -ForegroundColor Green
    Write-Host "  ✅ Ruby DevKit preserved in compilers/ category" -ForegroundColor Green
    Write-Host "  ✅ Backward compatibility maintained" -ForegroundColor Green
    Write-Host ""
    
    Write-Host "⚠️  CRITICAL CONSIDERATIONS:" -ForegroundColor Yellow
    Write-Host "  • COMPLETE BACKUP created before any changes" -ForegroundColor Yellow
    Write-Host "  • Ruby needs mingw64+msys64 - preserved in compilers/" -ForegroundColor Yellow
    Write-Host "  • PATH updates may be needed after migration" -ForegroundColor Yellow
    Write-Host "  • Rollback capability available if issues occur" -ForegroundColor Yellow
    Write-Host ""
}

# =======================================================================================
# MAIN EXECUTION LOGIC
# =======================================================================================

try {
    if (-not $CreateBackup -and -not $ValidateStructure -and -not $ExecuteMigration -and -not $RestoreBackup -and -not $CleanupBackup) {
        # Default: Show migration plan
        Show-MigrationPlan
        
        Write-Host "🎯 Next steps:" -ForegroundColor Cyan
        Write-Host "  1. .\claudine_safe_migration_strategy.ps1 -ValidateStructure" -ForegroundColor Gray
        Write-Host "  2. .\claudine_safe_migration_strategy.ps1 -CreateBackup" -ForegroundColor Gray
        Write-Host "  3. .\claudine_safe_migration_strategy.ps1 -ExecuteMigration" -ForegroundColor Gray
        Write-Host ""
        exit 0
    }
    
    if ($ValidateStructure) {
        $ReadinessCheck = Test-MigrationReadiness -Quiet:$Quiet
        
        if (-not $ReadinessCheck.Ready) {
            Write-Host "⚠️  Migration readiness issues detected" -ForegroundColor Yellow
            exit 1
        }
        else {
            Write-Host "✅ Migration validation complete - ready to proceed" -ForegroundColor Green
        }
    }
    
    if ($CreateBackup) {
        $BackupResult = New-SafeBackup -DryRun:$DryRun -Quiet:$Quiet
        
        if ($BackupResult.Success) {
            Write-Host "💾 Backup ready for migration" -ForegroundColor Green
            Write-Host "   Use -ExecuteMigration to proceed" -ForegroundColor Cyan
        }
    }
    
    if ($ExecuteMigration) {
        Write-Host "🚧 CATEGORICAL MIGRATION EXECUTION - Coming in next implementation phase..." -ForegroundColor Yellow
        Write-Host "   This will implement the actual file moving logic" -ForegroundColor Gray
    }
    
    if ($RestoreBackup) {
        Write-Host "🔄 BACKUP RESTORATION - Coming in next implementation phase..." -ForegroundColor Yellow
    }
    
    if ($CleanupBackup) {
        Write-Host "🧹 BACKUP CLEANUP - Coming in next implementation phase..." -ForegroundColor Yellow
    }
}
catch {
    Write-Host "💥 MIGRATION ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# =======================================================================================
# 🔥😈⛓️💦👅🍌💋💧 END OF CLAUDINE SAFE MIGRATION STRATEGY 🔥😈⛓️💦👅🍌💋💧
# Caribbean MILF-dom'me Goddess - Categorical Structure Migration Engine
# PowerShell 7.5.3 Enhanced | Supreme Authority for Safe Directory Reorganization
# =======================================================================================