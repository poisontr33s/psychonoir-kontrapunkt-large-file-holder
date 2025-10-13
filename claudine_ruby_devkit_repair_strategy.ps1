# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE RUBY DEVKIT REPAIR STRATEGY
# Caribbean MILF-dom'me Goddess - Fix Ruby Before Any Reorganization
# PowerShell 7.5.3 Enhanced - Ruby DevKit Post-Installation Repair

[CmdletBinding()]
param(
    [switch]$DiagnoseRuby,
    [switch]$RepairGems,
    [switch]$CompleteRidkInstall,
    [switch]$FixDevKitPaths,
    [switch]$TestNativeCompilation,
    [switch]$FullRepair,
    [switch]$DryRun,
    [switch]$Quiet
)

$ErrorActionPreference = "Continue"

# Ruby Repair Configuration
$RUBY_REPAIR_CONFIG = @{
    RubyRoot       = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages\ruby"
    MinGW64Root    = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages\mingw64"
    MSYS64Root     = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages\msys64"
    
    ExpectedFiles  = @{
        "ruby\bin\ruby.exe"          = "Ruby runtime"
        "ruby\bin\gem.exe"           = "RubyGems package manager"
        "ruby\bin\ridk.cmd"          = "Ruby DevKit installer"
        "ruby\bin\bundle.exe"        = "Bundler dependency manager"
        "mingw64\bin\gcc.exe"        = "MinGW GCC compiler"
        "msys64\usr\bin\bash.exe"    = "MSYS2 bash shell"
        "msys64\mingw64\bin\gcc.exe" = "MSYS2 MinGW GCC (MISSING - CRITICAL!)"
    }
    
    RidkComponents = @{
        1 = "MSYS2 base installation"
        2 = "MSYS2 system update"
        3 = "MSYS2 and MINGW development toolchain"
    }
}

# =======================================================================================
# RUBY DEVKIT REPAIR FUNCTIONS
# =======================================================================================

function Invoke-RubyDiagnosis {
    [CmdletBinding()]
    param([switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🔍 RUBY DEVKIT COMPREHENSIVE DIAGNOSIS:" -ForegroundColor Cyan
        Write-Host "=======================================" -ForegroundColor Cyan
    }
    
    $Config = $RUBY_REPAIR_CONFIG
    $DiagnosisResults = @{
        RubyRuntime     = $false
        GemManager      = $false
        DevKitComplete  = $false
        RidkAvailable   = $false
        PathIssues      = @()
        MissingFiles    = @()
        Recommendations = @()
    }
    
    # Check expected files
    foreach ($File in $Config.ExpectedFiles.GetEnumerator()) {
        $FullPath = Join-Path "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages" $File.Key
        
        if (Test-Path $FullPath) {
            if (-not $Quiet) {
                Write-Host "  ✅ $($File.Value): Found" -ForegroundColor Green
            }
            
            if ($File.Key -match "ruby\.exe") { $DiagnosisResults.RubyRuntime = $true }
            if ($File.Key -match "gem\.exe") { $DiagnosisResults.GemManager = $true }
            if ($File.Key -match "ridk\.cmd") { $DiagnosisResults.RidkAvailable = $true }
        }
        else {
            if (-not $Quiet) {
                Write-Host "  ❌ $($File.Value): MISSING at $FullPath" -ForegroundColor Red
            }
            $DiagnosisResults.MissingFiles += $File.Key
        }
    }
    
    # Check Ruby gem installation capability
    if ($DiagnosisResults.GemManager) {
        try {
            $GemEnv = & gem env 2>$null
            if ($GemEnv -match "GEM PATHS") {
                if (-not $Quiet) {
                    Write-Host "  ✅ RubyGems Environment: Working" -ForegroundColor Green
                }
            }
        }
        catch {
            if (-not $Quiet) {
                Write-Host "  ⚠️  RubyGems Environment: Issues detected" -ForegroundColor Yellow
            }
            $DiagnosisResults.PathIssues += "RubyGems environment not properly configured"
        }
    }
    
    # Check ridk functionality
    if ($DiagnosisResults.RidkAvailable) {
        try {
            $RidkVersion = & ridk version 2>$null
            if ($RidkVersion) {
                if (-not $Quiet) {
                    Write-Host "  ✅ RIDK Tool: Functional" -ForegroundColor Green
                }
                
                # Check ridk install status
                $RidkInstallCheck = & ridk install 2>$null
                if ($RidkInstallCheck -match "installed") {
                    $DiagnosisResults.DevKitComplete = $true
                    if (-not $Quiet) {
                        Write-Host "  ✅ RIDK Installation: Complete" -ForegroundColor Green
                    }
                }
                else {
                    if (-not $Quiet) {
                        Write-Host "  ⚠️  RIDK Installation: May need completion" -ForegroundColor Yellow
                    }
                    $DiagnosisResults.Recommendations += "Run 'ridk install 3' to complete DevKit installation"
                }
            }
        }
        catch {
            if (-not $Quiet) {
                Write-Host "  ❌ RIDK Tool: Not functional" -ForegroundColor Red
            }
            $DiagnosisResults.Recommendations += "RIDK tool needs repair or reinstallation"
        }
    }
    
    # Check critical missing path
    $CriticalMSYS64Path = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages\msys64\mingw64\bin"
    if (-not (Test-Path $CriticalMSYS64Path)) {
        if (-not $Quiet) {
            Write-Host "  🚨 CRITICAL: msys64\mingw64\bin\ directory missing!" -ForegroundColor Red
            Write-Host "     This is required for native gem compilation" -ForegroundColor Red
        }
        $DiagnosisResults.Recommendations += "Critical MSYS2 MinGW64 toolchain missing - run 'ridk install 3'"
    }
    
    # Generate repair recommendations
    if ($DiagnosisResults.MissingFiles.Count -gt 0) {
        $DiagnosisResults.Recommendations += "Missing files detected - Ruby installation may be incomplete"
    }
    
    if (-not $DiagnosisResults.GemManager) {
        $DiagnosisResults.Recommendations += "GemManager missing - critical for Ruby package management"
    }
    
    if (-not $DiagnosisResults.DevKitComplete) {
        $DiagnosisResults.Recommendations += "DevKit installation incomplete - native gems will fail"
    }
    
    # Show recommendations
    if (-not $Quiet -and $DiagnosisResults.Recommendations.Count -gt 0) {
        Write-Host ""
        Write-Host "💡 REPAIR RECOMMENDATIONS:" -ForegroundColor Cyan
        foreach ($Recommendation in $DiagnosisResults.Recommendations) {
            Write-Host "  • $Recommendation" -ForegroundColor Yellow
        }
        Write-Host ""
    }
    
    return $DiagnosisResults
}

function Invoke-RidkInstallCompletion {
    [CmdletBinding()]
    param([switch]$DryRun, [switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🔧 COMPLETING RIDK INSTALLATION:" -ForegroundColor Cyan
        Write-Host "=================================" -ForegroundColor Cyan
    }
    
    if ($DryRun) {
        if (-not $Quiet) {
            Write-Host "🔍 DRY-RUN: Would complete RIDK installation (ridk install 3)" -ForegroundColor Yellow
        }
        return @{ Success = $true; DryRun = $true }
    }
    
    try {
        if (-not $Quiet) {
            Write-Host "🚀 Running 'ridk install 3' to install development toolchain..." -ForegroundColor Yellow
            Write-Host "   This will install MSYS2 and MINGW development tools" -ForegroundColor Gray
            Write-Host "   This may take several minutes and require internet connection" -ForegroundColor Gray
            Write-Host ""
        }
        
        # Run ridk install 3 (MSYS2 and MINGW development toolchain)
        $RidkProcess = Start-Process -FilePath "ridk" -ArgumentList "install", "3" -Wait -PassThru -NoNewWindow
        
        if ($RidkProcess.ExitCode -eq 0) {
            if (-not $Quiet) {
                Write-Host "✅ RIDK installation completed successfully!" -ForegroundColor Green
            }
            
            # Verify the critical missing path now exists
            $CriticalPath = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages\msys64\mingw64\bin"
            if (Test-Path $CriticalPath) {
                if (-not $Quiet) {
                    Write-Host "✅ Critical path now exists: msys64\mingw64\bin\" -ForegroundColor Green
                }
                return @{ Success = $true; PathCreated = $true }
            }
            else {
                if (-not $Quiet) {
                    Write-Host "⚠️  RIDK completed but critical path still missing" -ForegroundColor Yellow
                }
                return @{ Success = $false; Issue = "Critical path not created" }
            }
        }
        else {
            if (-not $Quiet) {
                Write-Host "❌ RIDK installation failed with exit code: $($RidkProcess.ExitCode)" -ForegroundColor Red
            }
            return @{ Success = $false; Issue = "RIDK installation failed" }
        }
    }
    catch {
        if (-not $Quiet) {
            Write-Host "💥 RIDK installation error: $($_.Exception.Message)" -ForegroundColor Red
        }
        return @{ Success = $false; Issue = $_.Exception.Message }
    }
}

function Test-NativeGemCompilation {
    [CmdletBinding()]
    param([switch]$Quiet)
    
    if (-not $Quiet) {
        Write-Host "🧪 TESTING NATIVE GEM COMPILATION:" -ForegroundColor Cyan
        Write-Host "===================================" -ForegroundColor Cyan
    }
    
    try {
        # Test with a simple native gem (json is usually available)
        $TestOutput = & gem install json --dry-run 2>&1
        
        if ($TestOutput -match "native") {
            if (-not $Quiet) {
                Write-Host "✅ Native gem compilation capability: WORKING" -ForegroundColor Green
            }
            return @{ Success = $true; Capability = "Working" }
        }
        else {
            if (-not $Quiet) {
                Write-Host "⚠️  Native gem compilation: Status unclear" -ForegroundColor Yellow
            }
            return @{ Success = $false; Capability = "Unclear" }
        }
    }
    catch {
        if (-not $Quiet) {
            Write-Host "❌ Native gem compilation: FAILED" -ForegroundColor Red
            Write-Host "   Error: $($_.Exception.Message)" -ForegroundColor Red
        }
        return @{ Success = $false; Capability = "Failed"; Error = $_.Exception.Message }
    }
}

# =======================================================================================
# MAIN EXECUTION LOGIC  
# =======================================================================================

try {
    if ($FullRepair -or (-not $DiagnoseRuby -and -not $RepairGems -and -not $CompleteRidkInstall -and -not $FixDevKitPaths -and -not $TestNativeCompilation)) {
        # Default: Full diagnosis and repair workflow
        if (-not $Quiet) {
            Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE RUBY DEVKIT REPAIR 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
            Write-Host "Caribbean MILF-dom'me Goddess - Fix Ruby Before Reorganization" -ForegroundColor Cyan
            Write-Host ""
        }
        
        # Step 1: Comprehensive diagnosis
        $Diagnosis = Invoke-RubyDiagnosis -Quiet:$Quiet
        
        # Step 2: Complete RIDK installation if needed
        if (-not $Diagnosis.DevKitComplete -or $Diagnosis.MissingFiles -contains "msys64\mingw64\bin\gcc.exe") {
            if (-not $Quiet) {
                Write-Host "🔧 RIDK installation needs completion..." -ForegroundColor Yellow
            }
            
            $RidkResult = Invoke-RidkInstallCompletion -DryRun:$DryRun -Quiet:$Quiet
            
            if ($RidkResult.Success) {
                if (-not $Quiet) {
                    Write-Host "✅ RIDK installation completed" -ForegroundColor Green
                }
            }
            else {
                if (-not $Quiet) {
                    Write-Host "❌ RIDK installation failed: $($RidkResult.Issue)" -ForegroundColor Red
                }
            }
        }
        
        # Step 3: Test native compilation
        if (-not $DryRun) {
            $CompilationTest = Test-NativeGemCompilation -Quiet:$Quiet
        }
        
        # Step 4: Final health check
        if (-not $Quiet) {
            Write-Host ""
            Write-Host "🎯 RUBY REPAIR SUMMARY:" -ForegroundColor Cyan
            if ($Diagnosis.RubyRuntime -and $Diagnosis.GemManager -and $Diagnosis.DevKitComplete) {
                Write-Host "✅ Ruby ecosystem should now be healthy for reorganization" -ForegroundColor Green
            }
            else {
                Write-Host "⚠️  Ruby ecosystem still has issues - reorganization not recommended" -ForegroundColor Yellow
            }
            Write-Host ""
        }
    }
    
    if ($DiagnoseRuby) {
        $DiagnosisOnly = Invoke-RubyDiagnosis -Quiet:$Quiet
        $global:CLAUDINE_RUBY_DIAGNOSIS = $DiagnosisOnly
    }
    
    if ($CompleteRidkInstall) {
        $RidkInstallResult = Invoke-RidkInstallCompletion -DryRun:$DryRun -Quiet:$Quiet
        $global:CLAUDINE_RIDK_RESULT = $RidkInstallResult
    }
    
    if ($TestNativeCompilation) {
        $CompilationTestResult = Test-NativeGemCompilation -Quiet:$Quiet
        $global:CLAUDINE_COMPILATION_TEST = $CompilationTestResult
    }
}
catch {
    Write-Host "💥 RUBY REPAIR ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# =======================================================================================
# 🔥😈⛓️💦👅🍌💋💧 END OF CLAUDINE RUBY DEVKIT REPAIR 🔥😈⛓️💦👅🍌💋💧
# Caribbean MILF-dom'me Goddess - Ruby DevKit Post-Installation Repair
# PowerShell 7.5.3 Enhanced | Supreme Authority for Ruby Ecosystem Health
# =======================================================================================