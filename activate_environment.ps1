# Activate the PsychoNoir-Kontrapunkt development environment
# This script sets up PATH and environment variables for the session

param(
    [switch]$Permanent
)

# Get the repository root directory
$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

Write-Host "=== Activating PsychoNoir-Kontrapunkt Development Environment ===" -ForegroundColor Cyan
Write-Host "Repository: $RepoRoot" -ForegroundColor Gray
Write-Host ""

# Define tool paths
$ToolPaths = @(
    # JavaScript tools
    @{ Path = ".computer_languages\javascript"; Description = "Bun & Biome" },

    # Python tools
    @{ Path = ".computer_languages\python"; Description = "Python, uv & Ruff" },

    # Rust tools
    @{ Path = ".computer_languages\rust\.cargo\bin"; Description = "Rust toolchain" },

    # Ruby tools
    @{ Path = ".computer_languages\ruby\bin"; Description = "Ruby runtime" },

    # curl
    @{ Path = ".computer_languages\curl"; Description = "curl executable" },

    # PowerShell
    @{ Path = ".computer_languages\powershell"; Description = "PowerShell 7.5.3" }
)

# Add paths to environment
$AddedPaths = @()
foreach ($Tool in $ToolPaths) {
    $FullPath = Join-Path $RepoRoot $Tool.Path

    if (Test-Path $FullPath) {
        if ($env:PATH -notlike "*$FullPath*") {
            $env:PATH = "$FullPath;$env:PATH"
            $AddedPaths += $Tool.Description
            Write-Host "✓ Added $($Tool.Description) to PATH" -ForegroundColor Green
        }
        else {
            Write-Host "~ $($Tool.Description) already in PATH" -ForegroundColor Gray
        }
    }
    else {
        Write-Host "⚠ $($Tool.Description) not found at $FullPath" -ForegroundColor Yellow
    }
}

Write-Host ""

# Set environment variables
$env:PSYCHONOR_KONTRAPUNKT_ROOT = $RepoRoot
Write-Host "✓ Set PSYCHONOR_KONTRAPUNKT_ROOT=$RepoRoot" -ForegroundColor Green

# Make permanent if requested
if ($Permanent) {
    Write-Host ""
    Write-Host "Making changes permanent..." -ForegroundColor Yellow

    # Add to user PATH permanently
    $CurrentUserPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    foreach ($Tool in $ToolPaths) {
        $FullPath = Join-Path $RepoRoot $Tool.Path
        if (Test-Path $FullPath -and $CurrentUserPath -notlike "*$FullPath*") {
            $CurrentUserPath = "$FullPath;$CurrentUserPath"
        }
    }

    [Environment]::SetEnvironmentVariable("PATH", $CurrentUserPath, "User")
    [Environment]::SetEnvironmentVariable("PSYCHONOR_KONTRAPUNKT_ROOT", $RepoRoot, "User")

    Write-Host "✓ Environment variables set permanently" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== Environment Activated ===" -ForegroundColor Cyan

if ($AddedPaths.Count -gt 0) {
    Write-Host "Added to PATH: $($AddedPaths -join ', ')" -ForegroundColor Green
}
else {
    Write-Host "All tools already available in PATH" -ForegroundColor Green
}

Write-Host ""
Write-Host "Test your environment:" -ForegroundColor Yellow
Write-Host "bun --version          # JavaScript runtime" -ForegroundColor White
Write-Host "uv --version           # Python package manager" -ForegroundColor White
Write-Host "python --version       # Python interpreter" -ForegroundColor White
Write-Host "ruff --version         # Python linter" -ForegroundColor White
Write-Host "rustc --version        # Rust compiler" -ForegroundColor White
Write-Host "ruby -v                # Ruby interpreter" -ForegroundColor White
Write-Host "curl --version         # Data transfer tool" -ForegroundColor White
Write-Host "biome --version        # JS/TS linter" -ForegroundColor White

Write-Host ""
Write-Host "Happy coding in your isolated environment! 🚀" -ForegroundColor Green