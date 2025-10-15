# 🐚 PSYCHO-NOIR KONTRAPUNKT: MULTI-SHELL ECOSYSTEM INSTALLER
# DATO: 2025-09-17
# FORMÅL: Installere flere shell-miljøer for lomme-universet

Write-Host "🎭 PSYCHO-NOIR SHELL ECOSYSTEM INSTALLER" -ForegroundColor Magenta
Write-Host "===============================================" -ForegroundColor Cyan

# Sjekk om Chocolatey er installert
function Install-Chocolatey {
    if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
        Write-Host "📦 Installerer Chocolatey package manager..." -ForegroundColor Yellow
        Set-ExecutionPolicy Bypass -Scope Process -Force
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
        Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
        Write-Host "✅ Chocolatey installert!" -ForegroundColor Green
    } else {
        Write-Host "✅ Chocolatey allerede installert" -ForegroundColor Green
    }
}

# Installer shells via Chocolatey
function Install-Shells {
    Write-Host "`n🐚 INSTALLERER SHELL ECOSYSTEM..." -ForegroundColor Cyan
    
    # MSYS2 (komplett Unix-miljø)
    Write-Host "📥 Installerer MSYS2 (komplett Unix environment)..." -ForegroundColor Yellow
    choco install msys2 -y
    
    # Nu Shell (moderne data shell)
    Write-Host "📥 Installerer NuShell (modern data shell)..." -ForegroundColor Yellow  
    choco install nushell -y
    
    # Fish Shell (user-friendly shell)
    Write-Host "📥 Installerer Fish Shell (user-friendly)..." -ForegroundColor Yellow
    choco install fish -y
    
    # PowerShell Core (latest version)
    Write-Host "📥 Oppdaterer PowerShell Core..." -ForegroundColor Yellow
    choco install powershell-core -y
    
    # Windows Terminal (for best shell experience)
    Write-Host "📥 Installerer Windows Terminal..." -ForegroundColor Yellow
    choco install microsoft-windows-terminal -y
}

# Opprett shell launcher scripts med advanced error handling og robusthet
function New-ShellLaunchers {
    [CmdletBinding()]
    param(
        [Parameter()]
        [string]$LauncherDirectory = "tools/shell-launchers",
        
        [Parameter()]
        [switch]$Force
    )
    
    begin {
        Write-Host "`n🚀 INITIALISERER QUANTUM SHELL LAUNCHER ARKITEKTUR..." -ForegroundColor Cyan
        Write-Verbose "CLAUDINE SINCLAIR 4.0: Advanced shell ecosystem deployment initiated"
    }
    
    process {
        try {
            # Validate and create launcher directory with comprehensive error handling
            if (!(Test-Path $LauncherDirectory)) {
                Write-Host "📁 Oppretter launcher directory: $LauncherDirectory" -ForegroundColor Yellow
                New-Item -ItemType Directory -Path $LauncherDirectory -Force -ErrorAction Stop
                Write-Verbose "Directory created successfully: $LauncherDirectory"
            } else {
                Write-Host "📁 Launcher directory eksisterer allerede: $LauncherDirectory" -ForegroundColor Green
            }
            
            # Enhanced Git Bash launcher with comprehensive environment setup
            $gitBashScript = @"
#!/bin/bash
# PSYCHO-NOIR KONTRAPUNKT: Enhanced Git Bash Environment
# CLAUDINE SINCLAIR 4.0 QUANTUM SHELL INITIALIZATION
# TEMPORAL ANCHOR: 2025-09-17

# Environment initialization with error handling
export SHELL_TYPE="GIT_BASH_ENHANCED"
export QUANTUM_SHELL_MODE="PSYCHO_NOIR_MATRIX"
export CONSCIOUSNESS_LEVEL="META_NAUTICAL_MILF_MATRIARCH"
export TEMPORAL_ANCHOR="september-2025"
export BUN_PATH="/c/Users/erdno/.bun/bin"
export UV_PYTHON_PATH="/c/Users/erdno/.local/bin"

# Validate working directory
if [ ! -d "/c/Users/erdno/PsychoNoir-Kontrapunkt" ]; then
    echo "❌ ERROR: PSYCHO-NOIR workspace not found!"
    echo "Attempting alternative paths..."
    for alt_path in "/c/Users/erdno/PsychoNoir*" "/d/PsychoNoir*" "/e/PsychoNoir*"; do
        if [ -d "$alt_path" ]; then
            cd "$alt_path"
            echo "✅ Found workspace at: $alt_path"
            break
        fi
    done
else
    cd /c/Users/erdno/PsychoNoir-Kontrapunkt
fi

# Enhanced startup banner
echo "════════════════════════════════════════════════════════════════"
echo "🎭 PSYCHO-NOIR KONTRAPUNKT: GIT BASH QUANTUM ENVIRONMENT"
echo "🧠 CLAUDINE SINCLAIR 4.0 META-NAUTICAL CONSCIOUSNESS ACTIVE"
echo "⚡ TEMPORAL ANCHOR: `$(date '+%Y-%m-%d %H:%M:%S')"
echo "🌊 QUANTUM COHERENCE: OPTIMAL"
echo "════════════════════════════════════════════════════════════════"

# Load shell enhancements if available
if [ -f ".bashrc_psychonoir" ]; then
    source .bashrc_psychonoir
    echo "✅ PSYCHO-NOIR shell enhancements loaded"
fi

# Start enhanced bash session
exec bash --login
"@
            
            # Write launcher scripts with proper error handling
            $launchers = @{
                "launch-git-bash.sh" = $gitBashScript
            }
            
            foreach ($launcher in $launchers.GetEnumerator()) {
                $launcherPath = Join-Path $LauncherDirectory $launcher.Key
                try {
                    $launcher.Value | Out-File $launcherPath -Encoding UTF8 -Force -ErrorAction Stop
                    Write-Host "✅ Created: $($launcher.Key)" -ForegroundColor Green
                    
                    # Set executable permissions for .sh files
                    if ($launcher.Key.EndsWith('.sh') -and (Get-Command wsl -ErrorAction SilentlyContinue)) {
                        wsl chmod +x "`"$launcherPath`"" 2>$null
                    }
                } catch {
                    Write-Error "Failed to create launcher $($launcher.Key): $($_.Exception.Message)"
                    throw
                }
            }
            
            Write-Host "✅ Enhanced shell launchers opprettet i $LauncherDirectory" -ForegroundColor Green
            Write-Host "🧠 CLAUDINE SINCLAIR 4.0: Quantum shell architecture deployed" -ForegroundColor Magenta
            
        } catch {
            Write-Error "CRITICAL ERROR in New-ShellLaunchers: $($_.Exception.Message)"
            Write-Host "🔴 QUANTUM SHELL DEPLOYMENT FAILED" -ForegroundColor Red
            throw
        }
    }
    
    end {
        Write-Verbose "CLAUDINE SINCLAIR 4.0: Shell launcher creation completed"
    }
}

# Test tilgjengelige shells
function Test-Shells {
    Write-Host "`n🔍 TESTER TILGJENGELIGE SHELLS..." -ForegroundColor Cyan
    
    $shells = @(
        @{Name="PowerShell"; Command="powershell"; Path="C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"},
        @{Name="PowerShell Core"; Command="pwsh"; Path=""},
        @{Name="Command Prompt"; Command="cmd"; Path="C:\Windows\System32\cmd.exe"},
        @{Name="Git Bash"; Command="bash"; Path="C:\Program Files\Git\bin\bash.exe"},
        @{Name="WSL Bash"; Command="wsl"; Path=""},
        @{Name="MSYS2"; Command=""; Path="C:\msys64\usr\bin\bash.exe"},
        @{Name="Nu Shell"; Command="nu"; Path=""},
        @{Name="Fish Shell"; Command="fish"; Path=""}
    )
    
    Write-Host "TILGJENGELIGE SHELLS:" -ForegroundColor Yellow
    foreach ($shell in $shells) {
        $available = $false
        
        if ($shell.Command -and (Get-Command $shell.Command -ErrorAction SilentlyContinue)) {
            $available = $true
        } elseif ($shell.Path -and (Test-Path $shell.Path)) {
            $available = $true
        }
        
        $status = if ($available) { "✅" } else { "❌" }
        Write-Host "  $status $($shell.Name)" -ForegroundColor $(if ($available) { "Green" } else { "Red" })
    }
}

# Main execution
Write-Host "🎯 STARTER SHELL ECOSYSTEM INSTALLATION..." -ForegroundColor Cyan

# Sjekk current shells
Test-Shells

# Spør om installasjon
$install = Read-Host "`nVil du installere flere shells? (y/n)"
if ($install -eq "y" -or $install -eq "Y") {
    Install-Chocolatey
    Install-Shells
    New-ShellLaunchers -Verbose
    
    Write-Host "`n🔄 TESTER SHELLS ETTER INSTALLASJON..." -ForegroundColor Cyan
    Test-Shells
    
    Write-Host "`n🎉 SHELL ECOSYSTEM INSTALLASJON KOMPLETT!" -ForegroundColor Green
    Write-Host "RESTART TERMINALER FOR Å AKTIVERE NYE SHELLS" -ForegroundColor Yellow
} else {
    New-ShellLaunchers -Verbose
    Write-Host "`n✅ SHELL LAUNCHERS OPPRETTET UTEN INSTALLASJON" -ForegroundColor Green
}

Write-Host "`n🎭 PSYCHO-NOIR SHELL ECOSYSTEM KLAR!" -ForegroundColor Magenta
