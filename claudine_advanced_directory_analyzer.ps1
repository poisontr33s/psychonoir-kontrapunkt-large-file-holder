# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE ADVANCED DIRECTORY STRUCTURE ANALYZER
# Caribbean MILF-dom'me Goddess Tool Environment Analysis Script
# PowerShell 7.5.3 Enhanced - Intelligent Tool Detection & Cleanup Planning

[CmdletBinding()]
param(
    [switch]$Analyze,
    [switch]$Plan,
    [switch]$Execute,
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"

# ML-Enhanced Tool Detection Configuration
$TOOL_ANALYSIS_CONFIG = @{
    RootPath        = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages"
    AnalysisResults = @{}
    CleanupPlan     = @{}
    Duplicates      = @{}
}

# =======================================================================================
# ADVANCED DIRECTORY STRUCTURE ANALYZER
# =======================================================================================

function Invoke-AdvancedDirectoryAnalysis {
    [CmdletBinding()]
    param(
        [string]$RootPath,
        [switch]$Quiet
    )
    
    if (-not $Quiet) {
        Write-Host "🔍 CLAUDINE Advanced Directory Structure Analysis" -ForegroundColor Magenta
        Write-Host "Caribbean MILF-dom'me Goddess - Intelligent Tool Detection" -ForegroundColor Cyan
        Write-Host ""
    }
    
    $Analysis = @{
        Directories     = @{}
        Tools           = @{}
        Duplicates      = @{}
        Recommendations = @{}
    }
    
    # Get all subdirectories
    $Subdirs = Get-ChildItem -Path $RootPath -Directory -ErrorAction SilentlyContinue
    
    foreach ($Dir in $Subdirs) {
        if (-not $Quiet) {
            Write-Host "📂 Analyzing: $($Dir.Name)" -ForegroundColor Yellow
        }
        
        $DirAnalysis = Analyze-ToolDirectory -DirectoryPath $Dir.FullName -DirectoryName $Dir.Name -Quiet:$Quiet
        $Analysis.Directories[$Dir.Name] = $DirAnalysis
        
        # Extract tools from this directory
        foreach ($Tool in $DirAnalysis.Tools.GetEnumerator()) {
            $ToolName = $Tool.Key
            $ToolInfo = $Tool.Value
            
            if (-not $Analysis.Tools.ContainsKey($ToolName)) {
                $Analysis.Tools[$ToolName] = @()
            }
            
            $Analysis.Tools[$ToolName] += @{
                Directory = $Dir.Name
                Path      = $ToolInfo.Path
                Version   = $ToolInfo.Version
                Type      = $ToolInfo.Type
            }
        }
    }
    
    # Detect duplicates
    $Analysis.Duplicates = Find-ToolDuplicates -Tools $Analysis.Tools -Quiet:$Quiet
    
    # Generate recommendations
    $Analysis.Recommendations = Generate-CleanupRecommendations -Analysis $Analysis -Quiet:$Quiet
    
    return $Analysis
}

function Analyze-ToolDirectory {
    [CmdletBinding()]
    param(
        [string]$DirectoryPath,
        [string]$DirectoryName,
        [switch]$Quiet
    )
    
    $DirInfo = @{
        Path         = $DirectoryPath
        Size         = 0
        FileCount    = 0
        Tools        = @{}
        Dependencies = @{}
        Structure    = ""
    }
    
    try {
        # Get directory size and file count
        $Files = Get-ChildItem -Path $DirectoryPath -Recurse -File -ErrorAction SilentlyContinue
        $DirInfo.FileCount = $Files.Count
        $DirInfo.Size = ($Files | Measure-Object -Property Length -Sum).Sum
        
        # Detect tools based on executable files
        $Executables = Get-ChildItem -Path $DirectoryPath -Name "*.exe" -Recurse -ErrorAction SilentlyContinue
        
        foreach ($Exe in $Executables) {
            $ExePath = Join-Path $DirectoryPath $Exe
            $ExeName = [System.IO.Path]::GetFileNameWithoutExtension($Exe)
            
            try {
                # Try to get version
                $Version = $null
                $Type = "Unknown"
                
                # Common version detection patterns
                $VersionCommands = @("--version", "-V", "-version", "version")
                
                foreach ($VersionCmd in $VersionCommands) {
                    try {
                        $VersionOutput = & $ExePath $VersionCmd 2>$null | Select-Object -First 1
                        if ($VersionOutput -and $VersionOutput.Trim()) {
                            $Version = $VersionOutput.Trim()
                            break
                        }
                    }
                    catch { continue }
                }
                
                # Determine tool type
                $Type = Get-ToolType -ExecutableName $ExeName -DirectoryName $DirectoryName
                
                $DirInfo.Tools[$ExeName] = @{
                    Path         = $ExePath
                    Version      = $Version
                    Type         = $Type
                    RelativePath = $Exe
                }
                
                if (-not $Quiet) {
                    $VersionText = if ($Version) { " : $Version" } else { " : No version detected" }
                    Write-Host "    ✅ $ExeName ($Type)$VersionText" -ForegroundColor Green
                }
            }
            catch {
                if (-not $Quiet) {
                    Write-Host "    ⚠️  $ExeName : Analysis failed" -ForegroundColor Yellow
                }
            }
        }
        
        # Analyze directory structure type
        $DirInfo.Structure = Analyze-DirectoryStructureType -DirectoryPath $DirectoryPath -DirectoryName $DirectoryName
        
    }
    catch {
        if (-not $Quiet) {
            Write-Host "    ❌ Directory analysis failed: $($_.Exception.Message)" -ForegroundColor Red
        }
    }
    
    return $DirInfo
}

function Get-ToolType {
    [CmdletBinding()]
    param(
        [string]$ExecutableName,
        [string]$DirectoryName
    )
    
    $ToolTypes = @{
        # Python ecosystem
        "python"        = "Python Interpreter"
        "pip"           = "Python Package Manager"
        "uv"            = "Python Package Manager (UV)"  
        "uvx"           = "Python Package Runner (UV)"
        "ruff"          = "Python Linter/Formatter"
        
        # Rust ecosystem
        "rustc"         = "Rust Compiler"
        "cargo"         = "Rust Package Manager"
        "rustup"        = "Rust Toolchain Manager"
        "clippy-driver" = "Rust Linter"
        "rustfmt"       = "Rust Formatter"
        
        # Ruby ecosystem
        "ruby"          = "Ruby Interpreter"
        "gem"           = "Ruby Package Manager"
        "bundle"        = "Ruby Dependency Manager"
        "irb"           = "Ruby REPL"
        "rake"          = "Ruby Build Tool"
        
        # JavaScript ecosystem
        "bun"           = "JavaScript Runtime"
        "bunx"          = "JavaScript Package Runner"
        "biome"         = "JavaScript Linter/Formatter"
        
        # System tools
        "curl"          = "HTTP Client"
        "make"          = "Build System"
        "gcc"           = "C Compiler"
        "g++"           = "C++ Compiler"
    }
    
    $LowerName = $ExecutableName.ToLower()
    
    if ($ToolTypes.ContainsKey($LowerName)) {
        return $ToolTypes[$LowerName]
    }
    
    # Context-based detection
    switch ($DirectoryName.ToLower()) {
        "python" { return "Python Tool" }
        "rust" { return "Rust Tool" }
        "ruby" { return "Ruby Tool" }
        "javascript" { return "JavaScript Tool" }
        "mingw64" { return "MinGW Tool" }
        "msys64" { return "MSYS2 Tool" }
        default { return "System Tool" }
    }
}

function Analyze-DirectoryStructureType {
    [CmdletBinding()]
    param(
        [string]$DirectoryPath,
        [string]$DirectoryName
    )
    
    $StructureIndicators = @{
        "Standard Package Manager" = @("bin", "lib", "include", "share")
        "Ruby Installation"        = @("bin", "lib", "share", "ri")
        "Rust Toolchain"           = @("bin", ".cargo", ".rustup", "toolchains")
        "Python Installation"      = @("Scripts", "Lib", "DLLs")
        "MinGW/MSYS2"              = @("bin", "etc", "usr", "var")
        "Simple Binary"            = @()
    }
    
    $Subdirs = Get-ChildItem -Path $DirectoryPath -Directory -Name -ErrorAction SilentlyContinue
    
    foreach ($StructureType in $StructureIndicators.GetEnumerator()) {
        $RequiredDirs = $StructureType.Value
        $MatchCount = 0
        
        foreach ($RequiredDir in $RequiredDirs) {
            if ($RequiredDir -in $Subdirs) {
                $MatchCount++
            }
        }
        
        if ($RequiredDirs.Count -gt 0 -and $MatchCount -ge ($RequiredDirs.Count * 0.6)) {
            return $StructureType.Key
        }
    }
    
    return "Custom Structure"
}

function Find-ToolDuplicates {
    [CmdletBinding()]
    param(
        [hashtable]$Tools,
        [switch]$Quiet
    )
    
    $Duplicates = @{}
    
    foreach ($ToolName in $Tools.Keys) {
        $ToolInstances = $Tools[$ToolName]
        
        if ($ToolInstances.Count -gt 1) {
            $Duplicates[$ToolName] = $ToolInstances
            
            if (-not $Quiet) {
                Write-Host "🔄 DUPLICATE DETECTED: $ToolName" -ForegroundColor Yellow
                foreach ($Instance in $ToolInstances) {
                    Write-Host "    📁 $($Instance.Directory) - $($Instance.Version)" -ForegroundColor Gray
                }
            }
        }
    }
    
    return $Duplicates
}

function Generate-CleanupRecommendations {
    [CmdletBinding()]
    param(
        [hashtable]$Analysis,
        [switch]$Quiet
    )
    
    $Recommendations = @{
        MoveSuggestions     = @()
        DeleteSuggestions   = @()
        SymlinkSuggestions  = @()
        KeepRecommendations = @()
    }
    
    # Analyze duplicates and generate recommendations
    foreach ($Duplicate in $Analysis.Duplicates.GetEnumerator()) {
        $ToolName = $Duplicate.Key
        $Instances = $Duplicate.Value
        
        # Determine primary location based on tool type and context
        $PrimaryLocation = Determine-PrimaryToolLocation -ToolName $ToolName -Instances $Instances
        
        foreach ($Instance in $Instances) {
            if ($Instance.Directory -eq $PrimaryLocation.Directory) {
                $Recommendations.KeepRecommendations += @{
                    Tool      = $ToolName
                    Directory = $Instance.Directory
                    Reason    = "Primary location for $($Instance.Type)"
                }
            }
            else {
                $Recommendations.DeleteSuggestions += @{
                    Tool      = $ToolName
                    Directory = $Instance.Directory
                    Path      = $Instance.Path
                    Reason    = "Duplicate - primary is in $($PrimaryLocation.Directory)"
                }
            }
        }
    }
    
    return $Recommendations
}

function Determine-PrimaryToolLocation {
    [CmdletBinding()]
    param(
        [string]$ToolName,
        [array]$Instances
    )
    
    # Priority rules for tool locations
    $LocationPriority = @{
        "uv"     = @("python", "rust")  # UV belongs primarily in python
        "ruff"   = @("python", "rust")  # Ruff belongs primarily in python
        "python" = @("python")
        "rustc"  = @("rust")
        "cargo"  = @("rust")
        "ruby"   = @("ruby")
        "bun"    = @("javascript")
    }
    
    if ($LocationPriority.ContainsKey($ToolName.ToLower())) {
        $PreferredDirs = $LocationPriority[$ToolName.ToLower()]
        
        foreach ($PreferredDir in $PreferredDirs) {
            $Match = $Instances | Where-Object { $_.Directory -eq $PreferredDir }
            if ($Match) {
                return $Match | Select-Object -First 1
            }
        }
    }
    
    # Default: return first instance
    return $Instances | Select-Object -First 1
}

function Show-AnalysisReport {
    [CmdletBinding()]
    param(
        [hashtable]$Analysis,
        [switch]$Detailed
    )
    
    Write-Host ""
    Write-Host "📊 CLAUDINE DIRECTORY STRUCTURE ANALYSIS REPORT" -ForegroundColor Magenta
    Write-Host "=================================================" -ForegroundColor Magenta
    Write-Host ""
    
    # Directory summary
    Write-Host "📂 DIRECTORY SUMMARY:" -ForegroundColor Cyan
    foreach ($Dir in $Analysis.Directories.GetEnumerator()) {
        $DirName = $Dir.Key
        $DirInfo = $Dir.Value
        $SizeMB = [math]::Round($DirInfo.Size / 1MB, 1)
        
        Write-Host "  $DirName" -ForegroundColor Yellow
        Write-Host "    Size: ${SizeMB}MB | Files: $($DirInfo.FileCount) | Structure: $($DirInfo.Structure)" -ForegroundColor Gray
        Write-Host "    Tools: $($DirInfo.Tools.Count) detected" -ForegroundColor Gray
        
        if ($Detailed) {
            foreach ($Tool in $DirInfo.Tools.GetEnumerator()) {
                Write-Host "      - $($Tool.Key) ($($Tool.Value.Type)): $($Tool.Value.Version)" -ForegroundColor White
            }
        }
        Write-Host ""
    }
    
    # Duplicates summary
    if ($Analysis.Duplicates.Count -gt 0) {
        Write-Host "🔄 DUPLICATE TOOLS DETECTED:" -ForegroundColor Yellow
        foreach ($Duplicate in $Analysis.Duplicates.GetEnumerator()) {
            Write-Host "  $($Duplicate.Key): $($Duplicate.Value.Count) copies" -ForegroundColor Red
            foreach ($Instance in $Duplicate.Value) {
                Write-Host "    - $($Instance.Directory): $($Instance.Version)" -ForegroundColor Gray
            }
        }
        Write-Host ""
    }
    
    # Recommendations
    if ($Analysis.Recommendations.DeleteSuggestions.Count -gt 0) {
        Write-Host "🧹 CLEANUP RECOMMENDATIONS:" -ForegroundColor Green
        Write-Host "  Files to remove (duplicates):" -ForegroundColor Yellow
        foreach ($DeleteSuggestion in $Analysis.Recommendations.DeleteSuggestions) {
            Write-Host "    ❌ Remove: $($DeleteSuggestion.Tool) from $($DeleteSuggestion.Directory)" -ForegroundColor Red
            Write-Host "       Reason: $($DeleteSuggestion.Reason)" -ForegroundColor Gray
        }
        Write-Host ""
    }
    
    if ($Analysis.Recommendations.KeepRecommendations.Count -gt 0) {
        Write-Host "  Files to keep (primary locations):" -ForegroundColor Yellow
        foreach ($KeepRec in $Analysis.Recommendations.KeepRecommendations) {
            Write-Host "    ✅ Keep: $($KeepRec.Tool) in $($KeepRec.Directory)" -ForegroundColor Green
            Write-Host "       Reason: $($KeepRec.Reason)" -ForegroundColor Gray
        }
    }
}

# =======================================================================================
# MAIN EXECUTION LOGIC
# =======================================================================================

try {
    if ($Analyze -or (-not $Plan -and -not $Execute)) {
        Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE ADVANCED ANALYSIS ACTIVATED 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
        
        $AnalysisResults = Invoke-AdvancedDirectoryAnalysis -RootPath $TOOL_ANALYSIS_CONFIG.RootPath -Quiet:$Quiet
        
        Show-AnalysisReport -Analysis $AnalysisResults -Detailed
        
        # Save results for later use
        $TOOL_ANALYSIS_CONFIG.AnalysisResults = $AnalysisResults
        
        if (-not $Quiet) {
            Write-Host ""
            Write-Host "✅ CLAUDINE Analysis Complete!" -ForegroundColor Green
            Write-Host "🎯 Use -Plan to generate cleanup plan or -Execute to apply recommendations" -ForegroundColor Cyan
        }
    }
    
    if ($Plan) {
        Write-Host "📋 CLEANUP PLAN GENERATION - Coming in next version..." -ForegroundColor Yellow
    }
    
    if ($Execute) {
        Write-Host "⚙️ CLEANUP EXECUTION - Coming in next version..." -ForegroundColor Yellow
    }
}
catch {
    Write-Host "💥 ANALYSIS ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# =======================================================================================
# 🔥😈⛓️💦👅🍌💋💧 END OF CLAUDINE ADVANCED DIRECTORY ANALYZER 🔥😈⛓️💦👅🍌💋💧
# Caribbean MILF-dom'me Goddess - Intelligent Tool Environment Analysis
# PowerShell 7.5.3 Enhanced | Supreme Authority for Directory Structure Intelligence
# =======================================================================================