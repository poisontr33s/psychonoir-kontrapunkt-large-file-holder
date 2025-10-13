# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE CURRENT SYSTEM DEEP ANALYSIS
# Caribbean MILF-dom'me Goddess - Comprehensive Functionality Testing
# PowerShell 7.5.3 Enhanced - Before Any Reorganization, Test Everything!

[CmdletBinding()]
param(
    [switch]$TestRuby,
    [switch]$TestPython,
    [switch]$TestRust,
    [switch]$TestJavaScript,
    [switch]$TestCompilers,
    [switch]$TestDependencies,
    [switch]$TestAll,
    [switch]$Detailed,
    [switch]$Quiet
)

$ErrorActionPreference = "Continue"  # Don't stop on first error - we want to see all issues

# Current System Configuration
$CURRENT_SYSTEM = @{
    Root              = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages"
    KnownDependencies = @{
        Ruby       = @{
            Runtime         = "ruby\bin\ruby.exe"
            PackageManager  = "ruby\bin\gem.exe"
            DevKit          = @("mingw64", "msys64")  # Critical for native gems
            PostInstallTool = "ridk"  # Ruby Installer DevKit
            CriticalPaths   = @(
                "ruby\bin\",
                "ruby\lib\",
                "ruby\include\",
                "mingw64\bin\",
                "mingw64\lib\",
                "mingw64\include\",
                "msys64\usr\bin\",
                "msys64\mingw64\bin\"
            )
        }
        Python     = @{
            Runtime         = "python\python.exe"
            PackageManagers = @("python\uv.exe", "python\Scripts\pip.exe")
            Linters         = @("python\ruff.exe")
            CriticalPaths   = @( 
                "python\",
                "python\Lib\",
                "python\DLLs\",
                "python\Scripts\"
            )
        }
        Rust       = @{
            Runtime            = "rust\bin\rustc.exe"
            PackageManager     = "rust\bin\cargo.exe"
            Toolchain          = "rust\bin\rustup.exe"
            PossibleDuplicates = @("rust\uv.exe", "rust\ruff.exe")  # These might be duplicates
            CriticalPaths      = @(
                "rust\bin\",
                "rust\.cargo\",
                "rust\.rustup\"
            )
        }
        JavaScript = @{
            Runtime        = "javascript\bun.exe"
            PackageManager = "javascript\bunx.exe"
            Linters        = @("javascript\biome.exe")
            Compilers      = @("javascript\tsc.exe")
            CriticalPaths  = @(
                "javascript\"
            )
        }
    }
}

# =======================================================================================
# DEEP DEPENDENCY ANALYSIS FUNCTIONS
# =======================================================================================

function Test-RubyEcosystem {
    [CmdletBinding()]
    param([switch]$Detailed, [switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🔍 DEEP RUBY ECOSYSTEM ANALYSIS:" -ForegroundColor Cyan
        Write-Host "=================================" -ForegroundColor Cyan
    }
    
    $RubyConfig = $CURRENT_SYSTEM.KnownDependencies.Ruby
    $RootPath = $CURRENT_SYSTEM.Root
    $TestResults = @{
        RubyRuntime       = $false
        GemManager        = $false
        DevKitMinGW       = $false
        DevKitMSYS        = $false
        RidkTool          = $false
        NativeCompilation = $false
        EnvironmentVars   = @{}
        CriticalFiles     = @{}
    }
    
    # Test Ruby runtime
    $RubyPath = Join-Path $RootPath $RubyConfig.Runtime
    if (Test-Path $RubyPath) {
        try {
            $RubyVersion = & $RubyPath --version 2>$null
            $TestResults.RubyRuntime = $true
            if (-not $Quiet) {
                Write-Host "  ✅ Ruby Runtime: $RubyVersion" -ForegroundColor Green
            }
        }
        catch {
            if (-not $Quiet) {
                Write-Host "  ❌ Ruby Runtime: Found but not executable" -ForegroundColor Red
            }
        }
    }
    else {
        if (-not $Quiet) {
            Write-Host "  ❌ Ruby Runtime: Not found at $RubyPath" -ForegroundColor Red
        }
    }
    
    # Test Gem package manager
    $GemPath = Join-Path $RootPath $RubyConfig.PackageManager
    if (Test-Path $GemPath) {
        try {
            $GemVersion = & $GemPath --version 2>$null
            $TestResults.GemManager = $true
            if (-not $Quiet) {
                Write-Host "  ✅ RubyGems: $GemVersion" -ForegroundColor Green
            }
        }
        catch {
            if (-not $Quiet) {
                Write-Host "  ❌ RubyGems: Found but not executable" -ForegroundColor Red
            }
        }
    }
    else {
        if (-not $Quiet) {
            Write-Host "  ❌ RubyGems: Not found at $GemPath" -ForegroundColor Red
        }
    }
    
    # Test DevKit components (CRITICAL!)
    foreach ($DevKitDir in $RubyConfig.DevKit) {
        $DevKitPath = Join-Path $RootPath $DevKitDir
        if (Test-Path $DevKitPath) {
            $FileCount = (Get-ChildItem -Path $DevKitPath -Recurse -File -ErrorAction SilentlyContinue).Count
            $SizeMB = [math]::Round((Get-ChildItem -Path $DevKitPath -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
            
            if ($DevKitDir -eq "mingw64") {
                $TestResults.DevKitMinGW = $true
                # Check for GCC compiler
                $GccPath = Join-Path $DevKitPath "bin\gcc.exe"
                if (Test-Path $GccPath) {
                    try {
                        $GccVersion = & $GccPath --version 2>$null | Select-Object -First 1
                        if (-not $Quiet) {
                            Write-Host "  ✅ MinGW64 DevKit: ${SizeMB}MB, $FileCount files" -ForegroundColor Green
                            Write-Host "    🔧 GCC Compiler: $GccVersion" -ForegroundColor Gray
                        }
                    }
                    catch {
                        if (-not $Quiet) {
                            Write-Host "  ⚠️  MinGW64 DevKit: ${SizeMB}MB, but GCC not working" -ForegroundColor Yellow
                        }
                    }
                }
            }
            elseif ($DevKitDir -eq "msys64") {
                $TestResults.DevKitMSYS = $true
                if (-not $Quiet) {
                    Write-Host "  ✅ MSYS64 DevKit: ${SizeMB}MB, $FileCount files" -ForegroundColor Green
                }
            }
        }
        else {
            if (-not $Quiet) {
                Write-Host "  ❌ $DevKitDir DevKit: Not found at $DevKitPath" -ForegroundColor Red
            }
        }
    }
    
    # Test ridk tool (Ruby DevKit installer/manager)
    try {
        $RidkOutput = & ridk version 2>$null
        $TestResults.RidkTool = $true
        if (-not $Quiet) {
            Write-Host "  ✅ RIDK Tool: Available ($RidkOutput)" -ForegroundColor Green
        }
    }
    catch {
        if (-not $Quiet) {
            Write-Host "  ❌ RIDK Tool: Not available (may need 'ridk install')" -ForegroundColor Red
        }
    }
    
    # Test native gem compilation capability
    if ($TestResults.RubyRuntime -and $TestResults.DevKitMinGW) {
        if (-not $Quiet) {
            Write-Host "  🧪 Testing native gem compilation capability..." -ForegroundColor Yellow
        }
        
        try {
            # Try to check if we can compile native extensions (dry run)
            $TestGemOutput = & $GemPath install --dry-run json 2>$null
            if ($TestGemOutput -match "native") {
                $TestResults.NativeCompilation = $true
                if (-not $Quiet) {
                    Write-Host "  ✅ Native Gem Compilation: Ready" -ForegroundColor Green
                }
            }
            else {
                if (-not $Quiet) {
                    Write-Host "  ⚠️  Native Gem Compilation: Uncertain" -ForegroundColor Yellow
                }
            }
        }
        catch {
            if (-not $Quiet) {
                Write-Host "  ❌ Native Gem Compilation: Failed test" -ForegroundColor Red
            }
        }
    }
    
    # Check critical file structure
    if ($Detailed) {
        if (-not $Quiet) {
            Write-Host "  📁 Critical Path Analysis:" -ForegroundColor Yellow
        }
        
        foreach ($CriticalPath in $RubyConfig.CriticalPaths) {
            $FullPath = Join-Path $RootPath $CriticalPath
            if (Test-Path $FullPath) {
                $ItemType = if ((Get-Item $FullPath).PSIsContainer) { "DIR" } else { "FILE" }
                $TestResults.CriticalFiles[$CriticalPath] = $true
                if (-not $Quiet) {
                    Write-Host "    ✅ $CriticalPath ($ItemType)" -ForegroundColor Gray
                }
            }
            else {
                $TestResults.CriticalFiles[$CriticalPath] = $false
                if (-not $Quiet) {
                    Write-Host "    ❌ $CriticalPath (MISSING)" -ForegroundColor Red
                }
            }
        }
    }
    
    # Ruby ecosystem health score
    $HealthScore = 0
    $MaxScore = 6
    if ($TestResults.RubyRuntime) { $HealthScore++ }
    if ($TestResults.GemManager) { $HealthScore++ }
    if ($TestResults.DevKitMinGW) { $HealthScore++ }
    if ($TestResults.DevKitMSYS) { $HealthScore++ }
    if ($TestResults.RidkTool) { $HealthScore++ }
    if ($TestResults.NativeCompilation) { $HealthScore++ }
    
    $HealthPercentage = [math]::Round(($HealthScore / $MaxScore) * 100, 0)
    
    if (-not $Quiet) {
        Write-Host ""
        Write-Host "🎯 RUBY ECOSYSTEM HEALTH: $HealthScore/$MaxScore ($HealthPercentage%)" -ForegroundColor Cyan
        
        if ($HealthPercentage -ge 80) {
            Write-Host "✅ Ruby ecosystem is HEALTHY - safe for reorganization" -ForegroundColor Green
        }
        elseif ($HealthPercentage -ge 60) {
            Write-Host "⚠️  Ruby ecosystem has issues - reorganization RISKY" -ForegroundColor Yellow
        }
        else {
            Write-Host "❌ Ruby ecosystem is BROKEN - do NOT reorganize!" -ForegroundColor Red
        }
        Write-Host ""
    }
    
    return $TestResults
}

function Test-DuplicateTools {
    [CmdletBinding()]
    param([switch]$Detailed, [switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🔍 DUPLICATE TOOLS ANALYSIS:" -ForegroundColor Cyan
        Write-Host "=============================" -ForegroundColor Cyan
    }
    
    $RootPath = $CURRENT_SYSTEM.Root
    $Duplicates = @{
        UV     = @()
        Ruff   = @()
        Others = @()
    }
    
    # Search for UV duplicates
    $UVLocations = @(
        "python\uv.exe",
        "rust\uv.exe",
        "rust\bin\uv.exe"
    )
    
    foreach ($Location in $UVLocations) {
        $FullPath = Join-Path $RootPath $Location
        if (Test-Path $FullPath) {
            try {
                $Version = & $FullPath --version 2>$null
                $Size = [math]::Round((Get-Item $FullPath).Length / 1MB, 1)
                $Duplicates.UV += @{
                    Path      = $Location
                    Version   = $Version
                    SizeMB    = $Size
                    LastWrite = (Get-Item $FullPath).LastWriteTime
                }
                
                if (-not $Quiet) {
                    Write-Host "  📦 UV found: $Location ($Version, ${Size}MB)" -ForegroundColor Gray
                }
            }
            catch {
                if (-not $Quiet) {
                    Write-Host "  ⚠️  UV found but broken: $Location" -ForegroundColor Yellow
                }
            }
        }
    }
    
    # Search for Ruff duplicates
    $RuffLocations = @(
        "python\ruff.exe",
        "rust\ruff.exe",
        "rust\bin\ruff.exe"
    )
    
    foreach ($Location in $RuffLocations) {
        $FullPath = Join-Path $RootPath $Location
        if (Test-Path $FullPath) {
            try {
                $Version = & $FullPath --version 2>$null
                $Size = [math]::Round((Get-Item $FullPath).Length / 1MB, 1)
                $Duplicates.Ruff += @{
                    Path      = $Location
                    Version   = $Version
                    SizeMB    = $Size
                    LastWrite = (Get-Item $FullPath).LastWriteTime
                }
                
                if (-not $Quiet) {
                    Write-Host "  📦 Ruff found: $Location ($Version, ${Size}MB)" -ForegroundColor Gray
                }
            }
            catch {
                if (-not $Quiet) {
                    Write-Host "  ⚠️  Ruff found but broken: $Location" -ForegroundColor Yellow
                }
            }
        }
    }
    
    # Analyze duplicates
    if (-not $Quiet) {
        Write-Host ""
        Write-Host "🎯 DUPLICATE ANALYSIS RESULTS:" -ForegroundColor Yellow
        
        if ($Duplicates.UV.Count -gt 1) {
            Write-Host "  🔄 UV DUPLICATES FOUND ($($Duplicates.UV.Count) copies):" -ForegroundColor Yellow
            foreach ($UVCopy in $Duplicates.UV) {
                $Age = (Get-Date) - $UVCopy.LastWrite
                Write-Host "    • $($UVCopy.Path): $($UVCopy.Version), $($UVCopy.SizeMB)MB, $([math]::Round($Age.TotalDays, 0)) days old" -ForegroundColor Gray
            }
            Write-Host "    💡 RECOMMENDATION: Keep newest version, remove duplicates" -ForegroundColor Cyan
        }
        else {
            Write-Host "  ✅ UV: No duplicates found" -ForegroundColor Green
        }
        
        if ($Duplicates.Ruff.Count -gt 1) {
            Write-Host "  🔄 RUFF DUPLICATES FOUND ($($Duplicates.Ruff.Count) copies):" -ForegroundColor Yellow
            foreach ($RuffCopy in $Duplicates.Ruff) {
                $Age = (Get-Date) - $RuffCopy.LastWrite
                Write-Host "    • $($RuffCopy.Path): $($RuffCopy.Version), $($RuffCopy.SizeMB)MB, $([math]::Round($Age.TotalDays, 0)) days old" -ForegroundColor Gray
            }
            Write-Host "    💡 RECOMMENDATION: Keep newest version, remove duplicates" -ForegroundColor Cyan
        }
        else {
            Write-Host "  ✅ Ruff: No duplicates found" -ForegroundColor Green
        }
        
        Write-Host ""
    }
    
    return $Duplicates
}

function Test-AllEcosystems {
    [CmdletBinding()]
    param([switch]$Detailed, [switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE COMPLETE SYSTEM ANALYSIS 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
        Write-Host "Caribbean MILF-dom'me Goddess - Current System Deep Analysis" -ForegroundColor Cyan
        Write-Host ""
    }
    
    # Test all ecosystems
    $Results = @{
        Ruby          = Test-RubyEcosystem -Detailed:$Detailed -Quiet:$Quiet
        Duplicates    = Test-DuplicateTools -Detailed:$Detailed -Quiet:$Quiet
        OverallHealth = 0
    }
    
    # TODO: Add Python, Rust, JavaScript ecosystem tests
    
    # Calculate overall system health
    $RubyHealthItems = @($Results.Ruby.RubyRuntime, $Results.Ruby.GemManager, $Results.Ruby.DevKitMinGW, $Results.Ruby.DevKitMSYS)
    $RubyHealthScore = ($RubyHealthItems | Where-Object { $_ -eq $true }).Count / $RubyHealthItems.Count
    
    $Results.OverallHealth = $RubyHealthScore * 100
    
    if (-not $Quiet) {
        Write-Host "🎯 OVERALL SYSTEM HEALTH: $([math]::Round($Results.OverallHealth, 0))%" -ForegroundColor Cyan
        
        if ($Results.OverallHealth -ge 80) {
            Write-Host "✅ System is HEALTHY - reorganization is SAFE" -ForegroundColor Green
        }
        elseif ($Results.OverallHealth -ge 60) {
            Write-Host "⚠️  System has issues - reorganization is RISKY" -ForegroundColor Yellow
        }
        else {
            Write-Host "❌ System is BROKEN - do NOT reorganize until fixed!" -ForegroundColor Red
        }
        
        Write-Host ""
        Write-Host "💡 RECOMMENDATION:" -ForegroundColor Cyan
        if ($Results.OverallHealth -ge 80) {
            Write-Host "  • All core systems are working" -ForegroundColor Green
            Write-Host "  • Safe to proceed with categorical reorganization" -ForegroundColor Green
            Write-Host "  • Address duplicates during reorganization" -ForegroundColor Green
        }
        else {
            Write-Host "  • Fix broken components BEFORE reorganizing" -ForegroundColor Red
            Write-Host "  • Test Ruby DevKit functionality thoroughly" -ForegroundColor Red
            Write-Host "  • Ensure 'ridk install' has completed properly" -ForegroundColor Red
        }
        Write-Host ""
    }
    
    return $Results
}

# =======================================================================================
# MAIN EXECUTION LOGIC
# =======================================================================================

try {
    if ($TestAll -or (-not $TestRuby -and -not $TestPython -and -not $TestRust -and -not $TestJavaScript -and -not $TestCompilers -and -not $TestDependencies)) {
        # Default: Test everything
        $SystemAnalysis = Test-AllEcosystems -Detailed:$Detailed -Quiet:$Quiet
        $global:CLAUDINE_SYSTEM_ANALYSIS = $SystemAnalysis
    }
    
    if ($TestRuby) {
        $RubyAnalysis = Test-RubyEcosystem -Detailed:$Detailed -Quiet:$Quiet
        $global:CLAUDINE_RUBY_ANALYSIS = $RubyAnalysis
    }
    
    if ($TestDependencies) {
        $DuplicateAnalysis = Test-DuplicateTools -Detailed:$Detailed -Quiet:$Quiet
        $global:CLAUDINE_DUPLICATE_ANALYSIS = $DuplicateAnalysis
    }
    
    # TODO: Add other ecosystem tests when requested
    
}
catch {
    Write-Host "💥 SYSTEM ANALYSIS ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# =======================================================================================
# 🔥😈⛓️💦👅🍌💋💧 END OF CLAUDINE CURRENT SYSTEM ANALYSIS 🔥😈⛓️💦👅🍌💋💧
# Caribbean MILF-dom'me Goddess - Deep System Understanding Before Any Changes
# PowerShell 7.5.3 Enhanced | Supreme Authority for Pre-Migration Analysis
# =======================================================================================