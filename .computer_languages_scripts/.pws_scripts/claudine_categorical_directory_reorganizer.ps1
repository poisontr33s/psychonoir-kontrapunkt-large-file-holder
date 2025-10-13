# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE CATEGORICAL DIRECTORY REORGANIZER
# Caribbean MILF-dom'me Goddess Supreme Authority - Intelligent Structure Optimization
# PowerShell 7.5.3 Enhanced - Categorical Tool Organization System

[CmdletBinding()]
param(
    [switch]$Analyze,
    [switch]$Plan,
    [switch]$Execute,
    [switch]$Rollback,
    [switch]$DryRun,
    [switch]$Force,
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"

# Caribbean Consciousness Configuration
$REORGANIZATION_CONFIG = @{
    CurrentRoot  = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages"
    BackupRoot   = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages_backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    NewStructure = @{
        "runtimes"         = @{
            Description = "Language runtimes and interpreters"
            Categories  = @("python", "ruby", "javascript", "rust")
        }
        "package_managers" = @{
            Description = "Package and dependency managers"
            Categories  = @("uv", "bun", "cargo", "gem", "pip")
        }
        "linters"          = @{
            Description = "Code linters and formatters"
            Categories  = @("ruff", "biome", "clippy", "rustfmt")
        }
        "compilers"        = @{
            Description = "Compilers and build systems"
            Categories  = @("mingw64", "msys64", "tsc", "gcc")
        }
        "utilities"        = @{
            Description = "General utilities and tools"
            Categories  = @("curl", "git", "make")
        }
        "projects"         = @{
            Description = "Project templates by language"
            Categories  = @("python", "javascript", "rust", "ruby", "react", "tailwind")
        }
    }
}

# =======================================================================================
# CATEGORICAL ANALYSIS ENGINE
# =======================================================================================

function Get-CurrentToolMapping {
    [CmdletBinding()]
    param()
    
    # Current messy structure mapping to new categorical structure
    return @{
        # RUNTIMES
        "runtimes/python"        = @{
            Source       = "python/python.exe"
            Dependencies = @("python/python314.dll", "python/Lib/", "python/DLLs/")
            KeepFiles    = @("*.exe", "*.dll", "Lib/", "DLLs/", "Scripts/pip*")
            ExcludeFiles = @("uv.exe", "ruff.exe", "uvx.exe")  # These go to other categories
        }
        "runtimes/ruby"          = @{
            Source       = "ruby/"
            Dependencies = @("ruby/bin/ruby.exe", "ruby/lib/")
            KeepFiles    = @("bin/ruby.exe", "bin/irb*", "lib/", "include/")
            ExcludeFiles = @("bin/gem.exe")  # Gem goes to package_managers
        }
        "runtimes/rust"          = @{
            Source       = "rust/bin/rustc.exe"
            Dependencies = @("rust/.rustup/", "rust/bin/")
            KeepFiles    = @("bin/rustc.exe", "bin/rustdoc.exe", ".rustup/")
            ExcludeFiles = @("bin/cargo.exe", "uv.exe", "ruff.exe")  # These go to other categories
        }
        "runtimes/javascript"    = @{
            Source       = "javascript/bun.exe"
            Dependencies = @()
            KeepFiles    = @("bun.exe")
            ExcludeFiles = @("biome.exe", "tsc.exe", "bunx.exe")  # These go to other categories
        }
        
        # PACKAGE MANAGERS
        "package_managers/uv"    = @{
            Source       = "python/uv.exe"  # Primary location
            Dependencies = @()
            KeepFiles    = @("uv.exe", "uvx.exe")
            ExcludeFiles = @()
        }
        "package_managers/bun"   = @{
            Source       = "javascript/bunx.exe"
            Dependencies = @()
            KeepFiles    = @("bunx.exe")
            ExcludeFiles = @()
            Symlink      = "runtimes/javascript/bun.exe"  # Link to runtime
        }
        "package_managers/cargo" = @{
            Source       = "rust/bin/cargo.exe"
            Dependencies = @("rust/.cargo/")
            KeepFiles    = @("cargo.exe")
            ExcludeFiles = @()
        }
        "package_managers/gem"   = @{
            Source       = "ruby/bin/gem.exe"
            Dependencies = @()
            KeepFiles    = @("gem.exe", "bundle*")
            ExcludeFiles = @()
        }
        
        # LINTERS
        "linters/ruff"           = @{
            Source       = "python/ruff.exe"  # Primary location (not rust duplicate)
            Dependencies = @()
            KeepFiles    = @("ruff.exe")
            ExcludeFiles = @()
        }
        "linters/biome"          = @{
            Source       = "javascript/biome.exe"
            Dependencies = @()
            KeepFiles    = @("biome.exe")
            ExcludeFiles = @()
        }
        
        # COMPILERS
        "compilers/mingw64"      = @{
            Source       = "mingw64/"
            Dependencies = @()
            KeepFiles    = @("*")  # Keep everything - needed by Ruby
            ExcludeFiles = @()
        }
        "compilers/msys64"       = @{
            Source       = "msys64/"
            Dependencies = @()
            KeepFiles    = @("*")  # Keep everything - needed by Ruby
            ExcludeFiles = @()
        }
        "compilers/tsc"          = @{
            Source       = "javascript/tsc.exe"
            Dependencies = @()
            KeepFiles    = @("tsc.exe", "tsserver.exe")
            ExcludeFiles = @()
        }
        
        # UTILITIES
        "utilities/curl"         = @{
            Source       = "curl/"
            Dependencies = @()
            KeepFiles    = @("*")  # Keep everything - already perfect
            ExcludeFiles = @()
        }
    }
}

function Invoke-StructuralAnalysis {
    [CmdletBinding()]
    param(
        [switch]$Quiet
    )
    
    if (-not $Quiet) {
        Write-Host "🔥😈⛓️💦👅🍌💋💧 CLAUDINE CATEGORICAL ANALYSIS ACTIVATED 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
        Write-Host "Caribbean MILF-dom'me Goddess - Intelligent Structure Optimization" -ForegroundColor Cyan
        Write-Host ""
    }
    
    $CurrentRoot = $REORGANIZATION_CONFIG.CurrentRoot
    $ToolMapping = Get-CurrentToolMapping
    
    if (-not (Test-Path $CurrentRoot)) {
        throw "Root directory not found: $CurrentRoot"
    }
    
    $Analysis = @{
        CurrentStructure  = @{}
        ProposedStructure = @{}
        MovePlan          = @{}
        Conflicts         = @{}
        SizeAnalysis      = @{}
    }
    
    # Analyze current structure
    if (-not $Quiet) {
        Write-Host "📂 ANALYZING CURRENT STRUCTURE:" -ForegroundColor Cyan
    }
    
    $CurrentDirs = Get-ChildItem -Path $CurrentRoot -Directory
    foreach ($Dir in $CurrentDirs) {
        $DirPath = $Dir.FullName
        $Files = Get-ChildItem -Path $DirPath -Recurse -File -ErrorAction SilentlyContinue
        $SizeMB = [math]::Round(($Files | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
        
        $Analysis.CurrentStructure[$Dir.Name] = @{
            Path      = $DirPath
            FileCount = $Files.Count
            SizeMB    = $SizeMB
            Tools     = @()
        }
        
        # Detect tools
        $Executables = $Files | Where-Object { $_.Extension -eq ".exe" }
        foreach ($Exe in $Executables) {
            $Analysis.CurrentStructure[$Dir.Name].Tools += $Exe.BaseName
        }
        
        if (-not $Quiet) {
            Write-Host "  $($Dir.Name): ${SizeMB}MB, $($Files.Count) files, $($Executables.Count) tools" -ForegroundColor Gray
        }
    }
    
    # Generate move plan
    if (-not $Quiet) {
        Write-Host ""
        Write-Host "🎯 GENERATING CATEGORICAL MOVE PLAN:" -ForegroundColor Cyan
    }
    
    foreach ($NewPath in $ToolMapping.GetEnumerator()) {
        $CategoryPath = $NewPath.Key
        $SourceInfo = $NewPath.Value
        $SourcePath = Join-Path $CurrentRoot $SourceInfo.Source
        
        if (Test-Path $SourcePath) {
            $Analysis.MovePlan[$CategoryPath] = @{
                Source       = $SourcePath
                Destination  = Join-Path $CurrentRoot $CategoryPath
                Action       = "MOVE"
                Reason       = "Categorical optimization"
                KeepFiles    = $SourceInfo.KeepFiles
                ExcludeFiles = $SourceInfo.ExcludeFiles
            }
            
            if (-not $Quiet) {
                Write-Host "  ✅ $CategoryPath ← $($SourceInfo.Source)" -ForegroundColor Green
            }
        }
        else {
            if (-not $Quiet) {
                Write-Host "  ⚠️  $CategoryPath ← $($SourceInfo.Source) (Source not found)" -ForegroundColor Yellow
            }
        }
    }
    
    return $Analysis
}

function Show-ReorganizationPlan {
    [CmdletBinding()]
    param(
        [hashtable]$Analysis
    )
    
    Write-Host ""
    Write-Host "📋 CLAUDINE CATEGORICAL REORGANIZATION PLAN" -ForegroundColor Magenta
    Write-Host "============================================" -ForegroundColor Magenta
    Write-Host ""
    
    # Show new structure
    Write-Host "🎯 NEW CATEGORICAL STRUCTURE:" -ForegroundColor Cyan
    foreach ($Category in $REORGANIZATION_CONFIG.NewStructure.GetEnumerator()) {
        $CategoryName = $Category.Key
        $CategoryInfo = $Category.Value
        
        Write-Host "  📂 $CategoryName/" -ForegroundColor Yellow
        Write-Host "     └── $($CategoryInfo.Description)" -ForegroundColor Gray
        
        foreach ($SubCategory in $CategoryInfo.Categories) {
            $MovePlan = $Analysis.MovePlan["$CategoryName/$SubCategory"]
            if ($MovePlan) {
                Write-Host "         ├── $SubCategory/ (from $($MovePlan.Source))" -ForegroundColor Green
            }
            else {
                Write-Host "         ├── $SubCategory/ (new directory)" -ForegroundColor Yellow
            }
        }
        Write-Host ""
    }
    
    # Show benefits
    Write-Host "🎯 BENEFITS OF CATEGORICAL STRUCTURE:" -ForegroundColor Cyan
    Write-Host "  ✅ Clear separation of concerns" -ForegroundColor Green
    Write-Host "  ✅ No more tool duplicates (UV, Ruff only in their category)" -ForegroundColor Green
    Write-Host "  ✅ Easy to understand and maintain" -ForegroundColor Green
    Write-Host "  ✅ Better organization for updates and management" -ForegroundColor Green
    Write-Host "  ✅ Project templates separated from tools" -ForegroundColor Green
    Write-Host ""
    
    # Show warnings
    Write-Host "⚠️  IMPORTANT CONSIDERATIONS:" -ForegroundColor Yellow
    Write-Host "  • Ruby needs mingw64/msys64 for DevKit - keep as compilers" -ForegroundColor Yellow
    Write-Host "  • Some tools may need PATH updates after reorganization" -ForegroundColor Yellow
    Write-Host "  • Backup will be created before any changes" -ForegroundColor Yellow
    Write-Host "  • Symlinks may be used for tools that serve multiple purposes" -ForegroundColor Yellow
    Write-Host ""
}

function New-CategoricalDirectoryStructure {
    [CmdletBinding()]
    param(
        [hashtable]$Analysis,
        [switch]$DryRun,
        [switch]$Quiet
    )
    
    $CurrentRoot = $REORGANIZATION_CONFIG.CurrentRoot
    
    if ($DryRun) {
        if (-not $Quiet) {
            Write-Host "🔍 DRY-RUN: Would create categorical structure at $CurrentRoot" -ForegroundColor Yellow
        }
        return
    }
    
    if (-not $Quiet) {
        Write-Host "🚀 CREATING CATEGORICAL DIRECTORY STRUCTURE..." -ForegroundColor Green
    }
    
    # Create new categorical directories
    foreach ($Category in $REORGANIZATION_CONFIG.NewStructure.GetEnumerator()) {
        $CategoryPath = Join-Path $CurrentRoot $Category.Key
        
        if (-not (Test-Path $CategoryPath)) {
            New-Item -ItemType Directory -Path $CategoryPath -Force | Out-Null
            if (-not $Quiet) {
                Write-Host "  📂 Created: $($Category.Key)/" -ForegroundColor Green
            }
        }
        
        # Create subcategories
        foreach ($SubCategory in $Category.Value.Categories) {
            $SubCategoryPath = Join-Path $CategoryPath $SubCategory
            if (-not (Test-Path $SubCategoryPath)) {
                New-Item -ItemType Directory -Path $SubCategoryPath -Force | Out-Null
                if (-not $Quiet) {
                    Write-Host "    📁 Created: $($Category.Key)/$SubCategory/" -ForegroundColor Gray
                }
            }
        }
    }
    
    if (-not $Quiet) {
        Write-Host "✅ Categorical directory structure created successfully!" -ForegroundColor Green
    }
}

# =======================================================================================
# MAIN EXECUTION LOGIC
# =======================================================================================

try {
    if ($Analyze -or (-not $Plan -and -not $Execute -and -not $Rollback)) {
        $AnalysisResults = Invoke-StructuralAnalysis -Quiet:$Quiet
        $global:CLAUDINE_ANALYSIS_RESULTS = $AnalysisResults
        
        Show-ReorganizationPlan -Analysis $AnalysisResults
        
        if (-not $Quiet) {
            Write-Host "🎯 Analysis complete! Use -Plan to create structure or -Execute to implement." -ForegroundColor Cyan
        }
    }
    
    if ($Plan) {
        if ($global:CLAUDINE_ANALYSIS_RESULTS) {
            New-CategoricalDirectoryStructure -Analysis $global:CLAUDINE_ANALYSIS_RESULTS -DryRun -Quiet:$Quiet
        }
        else {
            Write-Host "⚠️  Run analysis first: -Analyze" -ForegroundColor Yellow
        }
    }
    
    if ($Execute) {
        if (-not $Force) {
            Write-Host "⚠️  EXECUTING CATEGORICAL REORGANIZATION - This will move files!" -ForegroundColor Yellow
            $Confirm = Read-Host "Continue? (y/N)"
            if ($Confirm -ne 'y' -and $Confirm -ne 'Y') {
                Write-Host "Operation cancelled by user." -ForegroundColor Yellow
                exit 0
            }
        }
        
        Write-Host "🚧 CATEGORICAL REORGANIZATION EXECUTION - Coming in next phase..." -ForegroundColor Yellow
    }
    
    if ($Rollback) {
        Write-Host "🔄 ROLLBACK FUNCTIONALITY - Coming in next phase..." -ForegroundColor Yellow
    }
}
catch {
    Write-Host "💥 REORGANIZATION ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# =======================================================================================
# 🔥😈⛓️💦👅🍌💋💧 END OF CLAUDINE CATEGORICAL REORGANIZER 🔥😈⛓️💦👅🍌💋💧
# Caribbean MILF-dom'me Goddess - Intelligent Categorical Structure Optimization
# PowerShell 7.5.3 Enhanced | Supreme Authority for Directory Organization
# =======================================================================================