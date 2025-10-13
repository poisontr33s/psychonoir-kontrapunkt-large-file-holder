# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE CLEAN INSTALLATION STRATEGY
# Caribbean MILF-dom'me Goddess - Fresh Clean Installation of Core Tools
# PowerShell 7.5.3 Enhanced - Start Fresh, Do It Right

[CmdletBinding()]
param(
    [switch]$InstallUVPython,
    [switch]$InstallBunWithNPX,
    [switch]$CleanDuplicates,
    [switch]$VerifyInstallation,
    [switch]$FullCleanInstall,
    [switch]$DryRun,
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"

# Clean Installation Configuration
$CLEAN_INSTALL_CONFIG = @{
    BaseRoot = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages"
    
    # Clean UV Python Installation
    UVPython = @{
        InstallDir       = "python_clean"
        UVInstallCommand = "powershell -c ""irm https://astral.sh/uv/install.ps1 | iex"""
        ExpectedTools    = @("uv.exe", "python.exe", "pip.exe")
        PythonVersion    = "3.14"  # Stable, well-supported version
        Description      = "Clean UV-managed Python installation with CPython"
    }
    
    # Clean Bun Installation with NPX compatibility
    BunClean = @{
        InstallDir        = "javascript_clean"
        BunInstallCommand = "powershell -c ""irm bun.sh/install.ps1 | iex"""
        ExpectedTools     = @("bun.exe", "bunx.exe")
        NPXCompatibility  = $true
        Description       = "Clean Bun installation with NPX compatibility for Playwright"
    }
    
    # Tools to remove (duplicates and broken installations)
    ToClean  = @{
        UVDuplicates   = @(
            "rust\uv.exe",
            "rust\uvx.exe"
        )
        RuffDuplicates = @(
            "rust\ruff.exe"  # Keep python\ruff.exe (newer version)
        )
        BrokenRuby     = @(
            "ruby\bin\gem.exe"  # Missing, needs complete reinstall
        )
    }
}

# =======================================================================================
# CLEAN INSTALLATION FUNCTIONS  
# =======================================================================================

function Install-CleanUVPython {
    [CmdletBinding()]
    param([switch]$DryRun, [switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🐍 INSTALLING CLEAN UV PYTHON:" -ForegroundColor Cyan
        Write-Host "===============================" -ForegroundColor Cyan
    }
    
    $Config = $CLEAN_INSTALL_CONFIG.UVPython
    $InstallPath = Join-Path $CLEAN_INSTALL_CONFIG.BaseRoot $Config.InstallDir
    
    if ($DryRun) {
        if (-not $Quiet) {
            Write-Host "🔍 DRY-RUN: Would install UV Python to $InstallPath" -ForegroundColor Yellow
            Write-Host "   Command: $($Config.UVInstallCommand)" -ForegroundColor Gray
        }
        return @{ Success = $true; DryRun = $true }
    }
    
    try {
        # Create clean installation directory
        if (Test-Path $InstallPath) {
            if (-not $Quiet) {
                Write-Host "🧹 Removing existing installation at $InstallPath" -ForegroundColor Yellow
            }
            Remove-Item -Path $InstallPath -Recurse -Force
        }
        
        New-Item -ItemType Directory -Path $InstallPath -Force | Out-Null
        
        if (-not $Quiet) {
            Write-Host "📥 Installing UV package manager..." -ForegroundColor Yellow
        }
        
        # Install UV using official installer
        $UVInstallProcess = Start-Process -FilePath "powershell" -ArgumentList "-c", "irm https://astral.sh/uv/install.ps1 | iex" -Wait -PassThru -NoNewWindow
        
        if ($UVInstallProcess.ExitCode -ne 0) {
            throw "UV installation failed with exit code: $($UVInstallProcess.ExitCode)"
        }
        
        # UV installs to user profile by default, we need to move it to our custom location
        $UserUVPath = "$env:USERPROFILE\.cargo\bin\uv.exe"
        if (Test-Path $UserUVPath) {
            Copy-Item -Path $UserUVPath -Destination "$InstallPath\uv.exe" -Force
            if (-not $Quiet) {
                Write-Host "✅ UV copied to custom location" -ForegroundColor Green
            }
        }
        
        # Install clean Python using UV
        if (-not $Quiet) {
            Write-Host "🐍 Installing Python $($Config.PythonVersion) using UV..." -ForegroundColor Yellow
        }
        
        $env:PATH = "$InstallPath;$env:PATH"  # Temporarily add to PATH
        
        $PythonInstallProcess = Start-Process -FilePath "$InstallPath\uv.exe" -ArgumentList "python", "install", $Config.PythonVersion -Wait -PassThru -NoNewWindow
        
        if ($PythonInstallProcess.ExitCode -ne 0) {
            throw "Python installation via UV failed with exit code: $($PythonInstallProcess.ExitCode)"
        }
        
        # UV installs Python to its cache, we need to create symlinks to our location
        $UVPythonPath = & "$InstallPath\uv.exe" python find $Config.PythonVersion 2>$null
        if ($UVPythonPath -and (Test-Path $UVPythonPath)) {
            $PythonDir = Split-Path $UVPythonPath -Parent
            
            # Create symlinks for Python executable
            New-Item -ItemType SymbolicLink -Path "$InstallPath\python.exe" -Target $UVPythonPath -Force | Out-Null
            
            # Create symlink for pip if it exists
            $PipPath = Join-Path $PythonDir "Scripts\pip.exe"
            if (Test-Path $PipPath) {
                New-Item -ItemType SymbolicLink -Path "$InstallPath\pip.exe" -Target $PipPath -Force | Out-Null
            }
            
            if (-not $Quiet) {
                Write-Host "✅ Python symlinks created" -ForegroundColor Green
            }
        }
        
        # Verify installation
        $VerifyResults = @{}
        foreach ($Tool in $Config.ExpectedTools) {
            $ToolPath = Join-Path $InstallPath $Tool
            if (Test-Path $ToolPath) {
                try {
                    $Version = & $ToolPath --version 2>$null | Select-Object -First 1
                    $VerifyResults[$Tool] = @{ Success = $true; Version = $Version }
                    if (-not $Quiet) {
                        Write-Host "  ✅ $Tool : $Version" -ForegroundColor Green
                    }
                }
                catch {
                    $VerifyResults[$Tool] = @{ Success = $false; Error = $_.Exception.Message }
                    if (-not $Quiet) {
                        Write-Host "  ❌ $Tool : Not functional" -ForegroundColor Red
                    }
                }
            }
            else {
                $VerifyResults[$Tool] = @{ Success = $false; Error = "Not found" }
                if (-not $Quiet) {
                    Write-Host "  ❌ $Tool : Not found" -ForegroundColor Red
                }
            }
        }
        
        $SuccessCount = ($VerifyResults.Values | Where-Object { $_.Success -eq $true }).Count
        $TotalCount = $VerifyResults.Count
        
        if (-not $Quiet) {
            Write-Host ""
            Write-Host "🎯 UV PYTHON INSTALLATION: $SuccessCount/$TotalCount tools working" -ForegroundColor Cyan
        }
        
        return @{ 
            Success       = ($SuccessCount -eq $TotalCount)
            InstallPath   = $InstallPath
            VerifyResults = $VerifyResults
        }
    }
    catch {
        if (-not $Quiet) {
            Write-Host "💥 UV Python installation failed: $($_.Exception.Message)" -ForegroundColor Red
        }
        return @{ Success = $false; Error = $_.Exception.Message }
    }
}

function Install-CleanBunWithNPX {
    [CmdletBinding()]
    param([switch]$DryRun, [switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🟡 INSTALLING CLEAN BUN WITH NPX COMPATIBILITY:" -ForegroundColor Cyan
        Write-Host "===============================================" -ForegroundColor Cyan
    }
    
    $Config = $CLEAN_INSTALL_CONFIG.BunClean
    $InstallPath = Join-Path $CLEAN_INSTALL_CONFIG.BaseRoot $Config.InstallDir
    
    if ($DryRun) {
        if (-not $Quiet) {
            Write-Host "🔍 DRY-RUN: Would install Bun with NPX to $InstallPath" -ForegroundColor Yellow
        }
        return @{ Success = $true; DryRun = $true }
    }
    
    try {
        # Create clean installation directory
        if (Test-Path $InstallPath) {
            if (-not $Quiet) {
                Write-Host "🧹 Removing existing installation at $InstallPath" -ForegroundColor Yellow
            }
            Remove-Item -Path $InstallPath -Recurse -Force
        }
        
        New-Item -ItemType Directory -Path $InstallPath -Force | Out-Null
        
        if (-not $Quiet) {
            Write-Host "📥 Installing Bun runtime..." -ForegroundColor Yellow
        }
        
        # Install Bun using official installer
        $BunInstallProcess = Start-Process -FilePath "powershell" -ArgumentList "-c", "irm bun.sh/install.ps1 | iex"  -Wait -PassThru -NoNewWindow
        
        if ($BunInstallProcess.ExitCode -ne 0) {
            throw "Bun installation failed with exit code: $($BunInstallProcess.ExitCode)"
        }
        
        # Bun installs to user profile by default, copy to our custom location
        $UserBunPath = "$env:USERPROFILE\.bun\bin\bun.exe"
        if (Test-Path $UserBunPath) {
            Copy-Item -Path $UserBunPath -Destination "$InstallPath\bun.exe" -Force
            if (-not $Quiet) {
                Write-Host "✅ Bun copied to custom location" -ForegroundColor Green
            }
        }
        
        # Create bunx (Bun's npx equivalent) 
        $BunxPath = "$env:USERPROFILE\.bun\bin\bunx.exe"
        if (Test-Path $BunxPath) {
            Copy-Item -Path $BunxPath -Destination "$InstallPath\bunx.exe" -Force
            if (-not $Quiet) {
                Write-Host "✅ Bunx copied to custom location" -ForegroundColor Green
            }
        }
        else {
            # Create bunx as symlink to bun if not found
            New-Item -ItemType SymbolicLink -Path "$InstallPath\bunx.exe" -Target "$InstallPath\bun.exe" -Force | Out-Null
            if (-not $Quiet) {
                Write-Host "✅ Bunx created as symlink to bun" -ForegroundColor Green
            }
        }
        
        # Create NPX compatibility (for Playwright and other tools expecting NPX)
        if (-not $Quiet) {
            Write-Host "🔗 Creating NPX compatibility for Playwright..." -ForegroundColor Yellow
        }
        
        # Create npx.cmd that calls bunx
        $NPXScript = @"
@echo off
"$InstallPath\bunx.exe" %*
"@
        $NPXPath = Join-Path $InstallPath "npx.cmd"
        $NPXScript | Out-File -FilePath $NPXPath -Encoding ASCII
        
        if (-not $Quiet) {
            Write-Host "✅ NPX compatibility script created" -ForegroundColor Green
        }
        
        # Verify installation
        $VerifyResults = @{}
        foreach ($Tool in $Config.ExpectedTools) {
            $ToolPath = Join-Path $InstallPath $Tool
            if (Test-Path $ToolPath) {
                try {
                    $Version = & $ToolPath --version 2>$null | Select-Object -First 1
                    $VerifyResults[$Tool] = @{ Success = $true; Version = $Version }
                    if (-not $Quiet) {
                        Write-Host "  ✅ $Tool : $Version" -ForegroundColor Green
                    }
                }
                catch {
                    $VerifyResults[$Tool] = @{ Success = $false; Error = $_.Exception.Message }
                    if (-not $Quiet) {
                        Write-Host "  ❌ $Tool : Not functional" -ForegroundColor Red
                    }
                }
            }
            else {
                $VerifyResults[$Tool] = @{ Success = $false; Error = "Not found" }
                if (-not $Quiet) {
                    Write-Host "  ❌ $Tool : Not found" -ForegroundColor Red
                }
            }
        }
        
        # Test NPX compatibility
        $NPXPath = Join-Path $InstallPath "npx.cmd"
        if (Test-Path $NPXPath) {
            try {
                $NPXTest = & $NPXPath --version 2>$null
                $VerifyResults["npx.cmd"] = @{ Success = $true; Version = "Bunx compatibility: $NPXTest" }
                if (-not $Quiet) {
                    Write-Host "  ✅ npx.cmd : Bunx compatibility working" -ForegroundColor Green
                }
            }
            catch {
                $VerifyResults["npx.cmd"] = @{ Success = $false; Error = "NPX compatibility failed" }
                if (-not $Quiet) {
                    Write-Host "  ❌ npx.cmd : NPX compatibility failed" -ForegroundColor Red
                }
            }
        }
        
        $SuccessCount = ($VerifyResults.Values | Where-Object { $_.Success -eq $true }).Count
        $TotalCount = $VerifyResults.Count
        
        if (-not $Quiet) {
            Write-Host ""
            Write-Host "🎯 BUN WITH NPX INSTALLATION: $SuccessCount/$TotalCount tools working" -ForegroundColor Cyan
        }
        
        return @{ 
            Success       = ($SuccessCount -ge 2)  # At least bun and bunx should work
            InstallPath   = $InstallPath
            VerifyResults = $VerifyResults
        }
    }
    catch {
        if (-not $Quiet) {
            Write-Host "💥 Bun installation failed: $($_.Exception.Message)" -ForegroundColor Red
        }
        return @{ Success = $false; Error = $_.Exception.Message }
    }
}

function Remove-DuplicateTools {
    [CmdletBinding()]
    param([switch]$DryRun, [switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🧹 REMOVING DUPLICATE TOOLS:" -ForegroundColor Cyan
        Write-Host "=============================" -ForegroundColor Cyan
    }
    
    $Config = $CLEAN_INSTALL_CONFIG.ToClean
    $BaseRoot = $CLEAN_INSTALL_CONFIG.BaseRoot
    $RemovedCount = 0
    
    # Remove UV duplicates
    foreach ($UVDupe in $Config.UVDuplicates) {
        $FullPath = Join-Path $BaseRoot $UVDupe
        if (Test-Path $FullPath) {
            if ($DryRun) {
                if (-not $Quiet) {
                    Write-Host "🔍 DRY-RUN: Would remove UV duplicate: $UVDupe" -ForegroundColor Yellow
                }
            }
            else {
                Remove-Item -Path $FullPath -Force
                $RemovedCount++
                if (-not $Quiet) {
                    Write-Host "  🗑️  Removed UV duplicate: $UVDupe" -ForegroundColor Gray
                }
            }
        }
    }
    
    # Remove Ruff duplicates (keep python version - newer)
    foreach ($RuffDupe in $Config.RuffDuplicates) {
        $FullPath = Join-Path $BaseRoot $RuffDupe
        if (Test-Path $FullPath) {
            if ($DryRun) {
                if (-not $Quiet) {
                    Write-Host "🔍 DRY-RUN: Would remove Ruff duplicate: $RuffDupe" -ForegroundColor Yellow
                }
            }
            else {
                Remove-Item -Path $FullPath -Force
                $RemovedCount++
                if (-not $Quiet) {
                    Write-Host "  🗑️  Removed Ruff duplicate: $RuffDupe (keeping python version - newer)" -ForegroundColor Gray
                }
            }
        }
    }
    
    if (-not $Quiet) {
        if ($DryRun) {
            Write-Host "🔍 DRY-RUN: Would remove $($Config.UVDuplicates.Count + $Config.RuffDuplicates.Count) duplicate files" -ForegroundColor Yellow
        }
        else {
            Write-Host "✅ Removed $RemovedCount duplicate files" -ForegroundColor Green
        }
    }
    
    return @{ Success = $true; RemovedCount = $RemovedCount }
}

# =======================================================================================
# MAIN EXECUTION LOGIC
# =======================================================================================

try {
    if ($FullCleanInstall -or (-not $InstallUVPython -and -not $InstallBunWithNPX -and -not $CleanDuplicates -and -not $VerifyInstallation)) {
        # Default: Full clean installation workflow
        if (-not $Quiet) {
            Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE CLEAN INSTALLATION 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
            Write-Host "Caribbean MILF-dom'me Goddess - Fresh Clean Tool Installation" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "🎯 STRATEGY: Start fresh with clean installations" -ForegroundColor Cyan
            Write-Host "  • Clean UV Python (CPython via UV package manager)" -ForegroundColor Gray
            Write-Host "  • Clean Bun with NPX compatibility (fixes Playwright)" -ForegroundColor Gray  
            Write-Host "  • Remove duplicates (UV, Ruff)" -ForegroundColor Gray
            Write-Host "  • Skip Ruby DevKit (too complex, fix later)" -ForegroundColor Gray
            Write-Host ""
        }
        
        # Step 1: Install clean UV Python
        $UVResult = Install-CleanUVPython -DryRun:$DryRun -Quiet:$Quiet
        
        # Step 2: Install clean Bun with NPX
        $BunResult = Install-CleanBunWithNPX -DryRun:$DryRun -Quiet:$Quiet
        
        # Step 3: Clean duplicates
        $CleanResult = Remove-DuplicateTools -DryRun:$DryRun -Quiet:$Quiet
        
        # Summary
        if (-not $Quiet) {
            Write-Host ""
            Write-Host "🎯 CLEAN INSTALLATION SUMMARY:" -ForegroundColor Cyan
            
            $UVStatus = if ($UVResult.Success) { "✅" } else { "❌" }
            $BunStatus = if ($BunResult.Success) { "✅" } else { "❌" }
            $CleanStatus = if ($CleanResult.Success) { "✅" } else { "❌" }
            
            Write-Host "  $UVStatus UV Python: $($UVResult.Success)" -ForegroundColor Gray
            Write-Host "  $BunStatus Bun + NPX: $($BunResult.Success)" -ForegroundColor Gray
            Write-Host "  $CleanStatus Duplicates: Cleaned" -ForegroundColor Gray
            
            if ($UVResult.Success -and $BunResult.Success) {
                Write-Host ""
                Write-Host "✅ CORE TOOLS READY - Playwright should now work!" -ForegroundColor Green
                Write-Host "   Python: $($UVResult.InstallPath)" -ForegroundColor Gray
                Write-Host "   Bun+NPX: $($BunResult.InstallPath)" -ForegroundColor Gray
            }
            else {
                Write-Host ""
                Write-Host "⚠️  Some installations failed - check logs above" -ForegroundColor Yellow
            }
        }
    }
    
    if ($InstallUVPython) {
        $UVOnlyResult = Install-CleanUVPython -DryRun:$DryRun -Quiet:$Quiet
        $global:CLAUDINE_UV_RESULT = $UVOnlyResult
    }
    
    if ($InstallBunWithNPX) {
        $BunOnlyResult = Install-CleanBunWithNPX -DryRun:$DryRun -Quiet:$Quiet
        $global:CLAUDINE_BUN_RESULT = $BunOnlyResult
    }
    
    if ($CleanDuplicates) {
        $CleanOnlyResult = Remove-DuplicateTools -DryRun:$DryRun -Quiet:$Quiet
        $global:CLAUDINE_CLEAN_RESULT = $CleanOnlyResult
    }
}
catch {
    Write-Host "💥 CLEAN INSTALLATION ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# =======================================================================================
# 🔥😈⛓️💦👅🍌💋💧 END OF CLAUDINE CLEAN INSTALLATION 🔥😈⛓️💦👅🍌💋💧
# Caribbean MILF-dom'me Goddess - Fresh Clean Tool Installation Strategy
# PowerShell 7.5.3 Enhanced | Supreme Authority for Clean Development Environment
# =======================================================================================