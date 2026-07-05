#!/usr/bin/env pwsh
<#
.SYNOPSIS
    PsychoNoir Polyglot Stack Verification Script

.DESCRIPTION
    Verifies that all components of the polyglot stack are properly installed and working.
#>

param(
    [switch]$Detailed
)

$ErrorActionPreference = "Stop"

function Write-Status {
    param([string]$Message, [string]$Color = "Cyan")
    Write-Host "[$((Get-Date).ToString('HH:mm:ss'))] $Message" -ForegroundColor $Color
}

function Write-Success {
    param([string]$Message)
    Write-Status "✓ $Message" "Green"
}

function Write-Error {
    param([string]$Message)
    Write-Status "✗ $Message" "Red"
}

function Write-Warning {
    param([string]$Message)
    Write-Status "! $Message" "Yellow"
}

function Test-Command {
    param([string]$Command, [array]$Arguments = @(), [string]$Name)

    try {
        $result = & $Command @Arguments 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Success "$Name is working"
            if ($Detailed) {
                Write-Host "  Output: $result" -ForegroundColor Gray
            }
            return $true
        }
        else {
            Write-Error "$Name failed (exit code: $LASTEXITCODE)"
            if ($Detailed) {
                Write-Host "  Output: $result" -ForegroundColor Red
            }
            return $false
        }
    }
    catch {
        Write-Error "$Name failed: $($_.Exception.Message)"
        return $false
    }
}

function Test-EnvironmentVariables {
    Write-Status "Checking environment variables..."

    $envVars = @(
        @{ Name = "RUBY_ROOT"; Required = $false }
        @{ Name = "RUSTUP_HOME"; Required = $false }
        @{ Name = "CARGO_HOME"; Required = $false }
        @{ Name = "PYTHON_HOME"; Required = $false }
    )

    foreach ($var in $envVars) {
        $value = [Environment]::GetEnvironmentVariable($var.Name, "User")
        if ($value) {
            Write-Success "$($var.Name) = $value"
        }
        elseif ($var.Required) {
            Write-Error "$($var.Name) is not set"
        }
        else {
            Write-Warning "$($var.Name) is not set (optional)"
        }
    }
}

function Test-DirectoryStructure {
    Write-Status "Checking directory structure..."

    $polyglotRoot = "C:\Users\eldno\PsychoNoir-Kontrapunkt\.scripting_coding_programming_languages"
    $directories = @("ruby", "rust", "python", "js_ts", "linters", "msys2")

    foreach ($dir in $directories) {
        $fullPath = Join-Path $polyglotRoot $dir
        if (Test-Path $fullPath) {
            Write-Success "Directory exists: $dir"
        }
        else {
            Write-Warning "Directory missing: $dir"
        }
    }
}

function Test-RubyGems {
    Write-Status "Testing Ruby gems installation..."

    try {
        $result = & gem env 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Success "RubyGems is working"
            if ($Detailed) {
                Write-Host "  Gem paths:" -ForegroundColor Gray
                $result | Select-String "GEM PATHS" -Context 0, 5 | ForEach-Object {
                    Write-Host "    $($_.Line)" -ForegroundColor Gray
                }
            }
            return $true
        }
        else {
            Write-Error "RubyGems failed"
            return $false
        }
    }
    catch {
        Write-Error "RubyGems test failed: $($_.Exception.Message)"
        return $false
    }
}

function Test-RustTools {
    Write-Status "Testing Rust toolchain..."

    $rustTests = @(
        @{ Command = "rustc"; Arguments = @("--version"); Name = "rustc" }
        @{ Command = "cargo"; Arguments = @("--version"); Name = "cargo" }
        @{ Command = "rustup"; Arguments = @("--version"); Name = "rustup" }
    )

    $allPassed = $true
    foreach ($test in $rustTests) {
        if (!(Test-Command -Command $test.Command -Arguments $test.Arguments -Name $test.Name)) {
            $allPassed = $false
        }
    }

    return $allPassed
}

function Test-PythonTools {
    Write-Status "Testing Python tools..."

    $pythonTests = @(
        @{ Command = "python"; Arguments = @("--version"); Name = "Python" }
        @{ Command = "uv"; Arguments = @("--version"); Name = "UV" }
        @{ Command = "ruff"; Arguments = @("--version"); Name = "Ruff" }
    )

    $allPassed = $true
    foreach ($test in $pythonTests) {
        if (!(Test-Command -Command $test.Command -Arguments $test.Arguments -Name $test.Name)) {
            $allPassed = $false
        }
    }

    return $allPassed
}

function Test-JSTools {
    Write-Status "Testing JavaScript/TypeScript tools..."

    $jsTests = @(
        @{ Command = "bun"; Arguments = @("--version"); Name = "Bun" }
        @{ Command = "bunx"; Arguments = @("--version"); Name = "Bunx" }
        @{ Command = "biome"; Arguments = @("--version"); Name = "Biome" }
    )

    $allPassed = $true
    foreach ($test in $jsTests) {
        if (!(Test-Command -Command $test.Command -Arguments $test.Arguments -Name $test.Name)) {
            $allPassed = $false
            if ($test.Name -eq "Biome") {
                Write-Warning "Biome installation may be corrupted. Try: bun add -g @biomejs/biome"
                Write-Warning "Or install standalone: https://github.com/biomejs/biome/releases"
            }
        }
    }

    return $allPassed
}

function Test-VSCodeSettings {
    Write-Status "Checking VSCode settings..."

    $vscodeSettingsPath = "C:\Users\eldno\PsychoNoir-Kontrapunkt\.vscode\settings.json"

    if (!(Test-Path $vscodeSettingsPath)) {
        Write-Warning "VSCode settings file not found"
        return $false
    }

    try {
        $settings = Get-Content $vscodeSettingsPath -Raw | ConvertFrom-Json

        $checks = @(
            @{ Path = "terminal.integrated.env.windows"; Name = "Terminal environment" }
            @{ Path = "python.defaultInterpreterPath"; Name = "Python interpreter" }
            @{ Path = "ruby.useLanguageServer"; Name = "Ruby language server" }
        )

        $allPassed = $true
        foreach ($check in $checks) {
            $value = $settings.PSObject.Properties[$check.Path].Value
            if ($null -eq $value) {
                # Try nested property access for complex paths
                try {
                    $value = Invoke-Expression "`$settings.$($check.Path)"
                }
                catch {
                    $value = $null
                }
            }

            if ($null -ne $value) {
                Write-Success "$($check.Name) configured"
            }
            else {
                Write-Warning "$($check.Name) not configured"
                $allPassed = $false
            }
        }

        return $allPassed
    }
    catch {
        Write-Error "Failed to parse VSCode settings: $($_.Exception.Message)"
        return $false
    }
}

# ============================================================================
# Main Verification
# ============================================================================

Write-Status "PsychoNoir Polyglot Stack Verification" "Magenta"
Write-Status "=====================================" "Magenta"
Write-Host ""

$results = @{}

# Test directory structure
Test-DirectoryStructure
Write-Host ""

# Test environment variables
Test-EnvironmentVariables
Write-Host ""

# Test all tools
$results.Ruby = Test-Command -Command "ruby" -Arguments @("-v") -Name "Ruby"
$results.RubyGems = Test-RubyGems
Write-Host ""

$results.Rust = Test-RustTools
Write-Host ""

$results.Python = Test-PythonTools
Write-Host ""

$results.JavaScript = Test-JSTools
Write-Host ""

$results.VSCode = Test-VSCodeSettings
Write-Host ""

# Summary
Write-Status "Verification Summary" "Magenta"
Write-Status "===================" "Magenta"

$passed = 0
$total = $results.Count

foreach ($component in $results.Keys) {
    if ($results[$component]) {
        Write-Success "$component"
        $passed++
    }
    else {
        Write-Error "$component"
    }
}

Write-Host ""
Write-Status "Results: $passed/$total components working" $(if ($passed -eq $total) { "Green" } else { "Yellow" })

if ($passed -eq $total) {
    Write-Success "All systems operational! 🎉"
}
else {
    Write-Warning "Some components need attention. Check the output above for details."
    Write-Status "Common fixes:"
    Write-Status "  - Restart terminal/VSCode for PATH changes"
    Write-Status "  - Run MSYS2 setup manually if Ruby gems fail"
    Write-Status "  - Check environment variables"
}