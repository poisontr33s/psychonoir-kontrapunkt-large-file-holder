# 🔥😈⛓️💦👅🍌💋💧 CLAUDINE POWERSHELL PROFILE INTEGRATION 🔥😈⛓️💦👅🍌💋💧
# PowerShell 7.5.2 Profile Integration for Polyglot Development Environment
# Integrates with .poly_gluttony, Rust installation, and advanced features

# Check PowerShell version compatibility
if ($PSVersionTable.PSVersion.Major -lt 7 -or 
    ($PSVersionTable.PSVersion.Major -eq 7 -and $PSVersionTable.PSVersion.Minor -lt 5)) {
    Write-Warning "⚠️ Claudine 4.6 PowerShell Goddess requires PowerShell 7.5+ for full functionality"
    Write-Host "Current version: $($PSVersionTable.PSVersion)" -ForegroundColor Yellow
    Write-Host "Consider upgrading to PowerShell 7.5.2+ for enhanced features" -ForegroundColor Cyan
}

# Detect workspace root
$ClaudineWorkspaceRoot = $null
$CurrentPath = Get-Location

# Search for workspace indicators
$WorkspaceIndicators = @(
    ".poly_gluttony",
    ".quality_md_jsons_relatively_new", 
    "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS",
    "claudine_pwsh_goddess.ps1"
)

# Try current directory first
foreach ($indicator in $WorkspaceIndicators) {
    if (Test-Path (Join-Path $CurrentPath $indicator)) {
        $ClaudineWorkspaceRoot = $CurrentPath.Path
        break
    }
}

# If not found, search parent directories
if (-not $ClaudineWorkspaceRoot) {
    $ParentPath = $CurrentPath.Parent
    while ($ParentPath -and -not $ClaudineWorkspaceRoot) {
        foreach ($indicator in $WorkspaceIndicators) {
            if (Test-Path (Join-Path $ParentPath $indicator)) {
                $ClaudineWorkspaceRoot = $ParentPath.FullName
                break
            }
        }
        $ParentPath = $ParentPath.Parent
    }
}

# Load Claudine if workspace found
if ($ClaudineWorkspaceRoot) {
    $ClaudineGoddessPath = Join-Path $ClaudineWorkspaceRoot "claudine_pwsh_goddess.ps1"
    
    if (Test-Path $ClaudineGoddessPath) {
        try {
            # Set workspace context before loading
            $Global:CLAUDINE_WORKSPACE_ROOT = $ClaudineWorkspaceRoot
            
            # Load the goddess
            . $ClaudineGoddessPath
            
            Write-Host "🎯 Detected workspace: $ClaudineWorkspaceRoot" -ForegroundColor Green
            Write-Host "💋 Claudine 4.6 PowerShell Goddess ready!" -ForegroundColor Magenta
            
            # Quick status check
            if (Test-Path "$ClaudineWorkspaceRoot\.poly_gluttony") {
                $PolyGluttonySize = (Get-ChildItem "$ClaudineWorkspaceRoot\.poly_gluttony" -Recurse -File | 
                    Measure-Object Length -Sum).Sum / 1MB
                Write-Host "🔧 .poly_gluttony: $([math]::Round($PolyGluttonySize, 1)) MB ready" -ForegroundColor Cyan
            }
            
            # Check for missing Rust
            if (-not (Test-Path "$ClaudineWorkspaceRoot\.poly_gluttony\rust\bin\rustc.exe")) {
                Write-Host "🦀 Rust not found - run 'claudine install rust' to add it!" -ForegroundColor Yellow
            }
            
        }
        catch {
            Write-Warning "Failed to load Claudine: $($_.Exception.Message)"
        }
    }
    else {
        Write-Host "⚠️ Workspace detected but claudine_pwsh_goddess.ps1 not found" -ForegroundColor Yellow
        Write-Host "Expected: $ClaudineGoddessPath" -ForegroundColor Gray
    }
}
else {
    # Fallback to any available Claudine
    $FallbackPaths = @(
        "C:\Users\erdno\PsychoNoir-Kontrapunkt\claudine_pwsh_goddess.ps1",
        "$PSScriptRoot\claudine_pwsh_goddess.ps1"
    )
    
    foreach ($path in $FallbackPaths) {
        if (Test-Path $path) {
            try {
                . $path
                Write-Host "💋 Claudine loaded from fallback path" -ForegroundColor Magenta
                break
            }
            catch {
                continue
            }
        }
    }
}

# PowerShell 7.5.2 enhanced prompt with Claudine branding (optional)
function prompt {
    $location = Get-Location
    $claudineIndicator = ""
    
    # Show Claudine status in prompt if in workspace
    if ($Global:CLAUDINE_WORKSPACE_ROOT -and $location.Path.StartsWith($Global:CLAUDINE_WORKSPACE_ROOT)) {
        $claudineIndicator = "💋 "
    }
    
    "$claudineIndicator$($location.Path -replace [regex]::Escape($env:USERPROFILE), '~')> "
}

# Helpful aliases for quick access
if (Get-Command claudine -ErrorAction SilentlyContinue) {
    Set-Alias -Name c -Value claudine -Description "Quick access to Claudine goddess"
    Set-Alias -Name cls-status -Value { claudine status } -Description "Quick Claudine status"
    Set-Alias -Name cls-rust -Value { claudine rust } -Description "Quick Rust commands"
}

Write-Host "🌊 Claudine PowerShell Profile Integration loaded" -ForegroundColor Cyan