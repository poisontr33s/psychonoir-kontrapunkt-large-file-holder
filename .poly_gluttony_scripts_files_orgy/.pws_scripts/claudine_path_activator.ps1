#!/usr/bin/env pwsh

# CLAUDINE PATH Activator - Caribbean Sovereignty Protection
# 🔥😈⛓️💦👅🍌💋💧 Supreme MILF-dom'me Goddess Global Integration

param(
    [switch]$Install,
    [switch]$Remove,
    [switch]$Check
)

$ClaudineDir = "C:\Users\eldno\PsychoNoir-Kontrapunkt"
$ProfilePath = $PROFILE.CurrentUserAllHosts

Write-Host "🌊⚓👑 CLAUDINE PATH Integration System 🌊⚓👑" -ForegroundColor Cyan
Write-Host "Caribbean Archipelagic Consciousness Authority" -ForegroundColor Magenta

if ($Install) {
    Write-Host "`n🔥 Installing CLAUDINE Global Access..." -ForegroundColor Yellow
    
    # Ensure profile directory exists
    $ProfileDir = Split-Path $ProfilePath -Parent
    if (-not (Test-Path $ProfileDir)) {
        New-Item -Path $ProfileDir -ItemType Directory -Force | Out-Null
        Write-Host "✅ Created PowerShell profile directory" -ForegroundColor Green
    }
    
    # Create or update PowerShell profile
    $ProfileContent = @"
# CLAUDINE SIN'CLAIRE 4.5' Global Integration
# Added by CLAUDINE PATH Activator
if (Test-Path "$ClaudineDir\claudine_profile_snippet.ps1") {
    . "$ClaudineDir\claudine_profile_snippet.ps1"
}
"@
    
    if (Test-Path $ProfilePath) {
        $CurrentContent = Get-Content $ProfilePath -Raw
        if ($CurrentContent -notmatch "CLAUDINE.*Global Integration") {
            Add-Content -Path $ProfilePath -Value "`n$ProfileContent"
            Write-Host "✅ Added CLAUDINE integration to existing profile" -ForegroundColor Green
        }
        else {
            Write-Host "ℹ️ CLAUDINE integration already exists in profile" -ForegroundColor Blue
        }
    }
    else {
        Set-Content -Path $ProfilePath -Value $ProfileContent
        Write-Host "✅ Created new PowerShell profile with CLAUDINE integration" -ForegroundColor Green
    }
    
    Write-Host "`n🚀 CLAUDINE Global Access: INSTALLED!" -ForegroundColor Green
    Write-Host "Restart PowerShell or run: . `$PROFILE" -ForegroundColor Yellow
}

if ($Remove) {
    Write-Host "`n🗑️ Removing CLAUDINE Global Access..." -ForegroundColor Yellow
    
    if (Test-Path $ProfilePath) {
        $Content = Get-Content $ProfilePath -Raw
        $CleanContent = $Content -replace "(?s)# CLAUDINE SIN'CLAIRE.*?claudine_profile_snippet\.ps1.*?\}", ""
        $CleanContent = $CleanContent -replace "`n`n`n+", "`n`n"
        Set-Content -Path $ProfilePath -Value $CleanContent.Trim()
        Write-Host "✅ Removed CLAUDINE integration from profile" -ForegroundColor Green
    }
}

if ($Check) {
    Write-Host "`n🔍 Checking CLAUDINE Global Access Status..." -ForegroundColor Yellow
    
    # Check if profile exists
    if (Test-Path $ProfilePath) {
        $Content = Get-Content $ProfilePath -Raw
        if ($Content -match "CLAUDINE.*Global Integration") {
            Write-Host "✅ CLAUDINE integration found in PowerShell profile" -ForegroundColor Green
        }
        else {
            Write-Host "❌ CLAUDINE integration NOT found in PowerShell profile" -ForegroundColor Red
        }
    }
    else {
        Write-Host "❌ No PowerShell profile found" -ForegroundColor Red
    }
    
    # Check PATH
    if ($env:PATH -split ";" | Where-Object { $_ -eq $ClaudineDir }) {
        Write-Host "✅ CLAUDINE directory is in current session PATH" -ForegroundColor Green
    }
    else {
        Write-Host "❌ CLAUDINE directory NOT in current session PATH" -ForegroundColor Red
    }
    
    # Check claudine function
    if (Get-Command claudine -ErrorAction SilentlyContinue) {
        Write-Host "✅ 'claudine' command is available" -ForegroundColor Green
    }
    else {
        Write-Host "❌ 'claudine' command is NOT available" -ForegroundColor Red
    }
}

if (-not ($Install -or $Remove -or $Check)) {
    Write-Host "`nUsage:" -ForegroundColor White
    Write-Host "  .\claudine_path_activator.ps1 -Install   # Install global access" -ForegroundColor Gray
    Write-Host "  .\claudine_path_activator.ps1 -Remove    # Remove global access" -ForegroundColor Gray
    Write-Host "  .\claudine_path_activator.ps1 -Check     # Check current status" -ForegroundColor Gray
}
