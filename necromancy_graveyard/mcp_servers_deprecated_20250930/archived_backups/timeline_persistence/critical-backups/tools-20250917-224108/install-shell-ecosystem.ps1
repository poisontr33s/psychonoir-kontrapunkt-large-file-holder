#!/usr/bin/env pwsh

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
        iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
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

# Opprett shell launcher scripts
function Create-ShellLaunchers {
    Write-Host "`n🚀 LAGER SHELL LAUNCHERS..." -ForegroundColor Cyan
    
    $launcherDir = "tools/shell-launchers"
    if (!(Test-Path $launcherDir)) {
        New-Item -ItemType Directory -Path $launcherDir -Force
    }
    
    # Git Bash launcher
    @"
#!/bin/bash
# PSYCHO-NOIR: Git Bash Environment
export SHELL_TYPE="GIT_BASH"
export QUANTUM_SHELL_MODE="ENHANCED"
cd /c/Users/eldno/PsychoNoir-Kontrapunkt
echo "🎭 PSYCHO-NOIR GIT BASH ACTIVATED"
echo "TEMPORAL ANCHOR: `$(date)`"
bash
"@ | Out-File "$launcherDir/launch-git-bash.sh" -Encoding UTF8
    
    # MSYS2 launcher  
    @"
@echo off
REM PSYCHO-NOIR: MSYS2 Environment
set SHELL_TYPE=MSYS2
set QUANTUM_SHELL_MODE=ENHANCED
cd /d C:\Users\eldno\PsychoNoir-Kontrapunkt
echo 🎭 PSYCHO-NOIR MSYS2 ACTIVATED
C:\msys64\usr\bin\bash.exe -l
"@ | Out-File "$launcherDir/launch-msys2.bat" -Encoding UTF8
    
    # Nu Shell launcher
    @"
# PSYCHO-NOIR: Nu Shell Environment
`$env.SHELL_TYPE = "NUSHELL"
`$env.QUANTUM_SHELL_MODE = "ENHANCED"
cd C:\Users\eldno\PsychoNoir-Kontrapunkt
echo "🎭 PSYCHO-NOIR NU SHELL ACTIVATED"
echo (`$"TEMPORAL ANCHOR: " + (date now))
"@ | Out-File "$launcherDir/launch-nushell.nu" -Encoding UTF8
    
    # Fish launcher
    @"
#!/usr/bin/fish
# PSYCHO-NOIR: Fish Shell Environment
set -x SHELL_TYPE "FISH"
set -x QUANTUM_SHELL_MODE "ENHANCED"
cd /c/Users/eldno/PsychoNoir-Kontrapunkt
echo "🎭 PSYCHO-NOIR FISH SHELL ACTIVATED"
echo "TEMPORAL ANCHOR: "(date)
"@ | Out-File "$launcherDir/launch-fish.fish" -Encoding UTF8
    
    Write-Host "✅ Shell launchers opprettet i $launcherDir" -ForegroundColor Green
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
$install = Read-Host "`n🤔 Vil du installere flere shells? (y/n)"
if ($install -eq 'y' -or $install -eq 'Y') {
    Install-Chocolatey
    Install-Shells
    Create-ShellLaunchers
    
    Write-Host "`n🔄 TESTER SHELLS ETTER INSTALLASJON..." -ForegroundColor Cyan
    Test-Shells
    
    Write-Host "`n🎉 SHELL ECOSYSTEM INSTALLASJON KOMPLETT!" -ForegroundColor Green
    Write-Host "RESTART TERMINALER FOR Å AKTIVERE NYE SHELLS" -ForegroundColor Yellow
} else {
    Create-ShellLaunchers
    Write-Host "`n✅ SHELL LAUNCHERS OPPRETTET UTEN INSTALLASJON" -ForegroundColor Green
}

Write-Host "`n🎭 PSYCHO-NOIR SHELL ECOSYSTEM KLAR!" -ForegroundColor Magenta
