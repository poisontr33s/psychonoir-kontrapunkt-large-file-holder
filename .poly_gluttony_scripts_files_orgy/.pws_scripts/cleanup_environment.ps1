#!/usr/bin/env pwsh

# 🧹 .poly_gluttony Environment Cleanup Script
# Created: October 13, 2025
# Purpose: Clean conflicting environment variables and PATH entries

Write-Host "🎯 .poly_gluttony Environment Cleanup Script" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# 1. Update conflicting HOME variables
Write-Host "1. Updating HOME variables to point to .poly_gluttony..." -ForegroundColor Yellow
$env:RUBY_ROOT = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\ruby"
$env:BUN_INSTALL = "C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\bun"

Write-Host "   ✅ RUBY_ROOT = $env:RUBY_ROOT" -ForegroundColor Green
Write-Host "   ✅ BUN_INSTALL = $env:BUN_INSTALL" -ForegroundColor Green
Write-Host ""

# 2. Clean PATH duplicates and conflicts
Write-Host "2. Cleaning PATH duplicates and conflicts..." -ForegroundColor Yellow
$currentPath = $env:Path
$pathEntries = $currentPath.Split(';')

# Remove duplicates and conflicting paths
$cleanPathEntries = @()
$seen = @()

foreach ($entry in $pathEntries) {
    $shouldAdd = $true
    
    # Skip duplicates
    if ($seen -contains $entry) {
        $shouldAdd = $false
        Write-Host "   🗑️ Removing duplicate: $entry" -ForegroundColor Red
    }
    
    # Skip old tool installations
    elseif ($entry -like "*computer_languages*" -or $entry -like "*scripting_coding*") {
        $shouldAdd = $false
        Write-Host "   🗑️ Removing old path: $entry" -ForegroundColor Red
    }
    
    # Add valid entries
    if ($shouldAdd -and $entry.Trim() -ne "") {
        $cleanPathEntries += $entry
        $seen += $entry
    }
}

# Update PATH
$cleanPath = $cleanPathEntries -join ';'
$env:Path = $cleanPath

Write-Host "   ✅ PATH cleaned and updated" -ForegroundColor Green
Write-Host ""

# 3. Test all tools
Write-Host "3. Testing all tools after cleanup..." -ForegroundColor Yellow
Write-Host ""

Write-Host "🐍 Python:" -ForegroundColor Blue
try {
    $pythonVersion = python --version 2>&1
    $pythonPath = (where.exe python | Select-Object -First 1)
    Write-Host "   Version: $pythonVersion" -ForegroundColor Green
    Write-Host "   Path: $pythonPath" -ForegroundColor Green
    if ($pythonPath -like "*poly_gluttony*") {
        Write-Host "   ✅ Using .poly_gluttony Python" -ForegroundColor Green
    }
    else {
        Write-Host "   ⚠️  Using external Python" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "   ❌ Python test failed" -ForegroundColor Red
}
Write-Host ""

Write-Host "💎 Ruby:" -ForegroundColor Magenta
try {
    $rubyVersion = (ruby --version 2>&1 | Select-Object -First 1)
    $rubyPath = (where.exe ruby | Select-Object -First 1)
    Write-Host "   Version: $rubyVersion" -ForegroundColor Green
    Write-Host "   Path: $rubyPath" -ForegroundColor Green
    if ($rubyPath -like "*poly_gluttony*") {
        Write-Host "   ✅ Using .poly_gluttony Ruby" -ForegroundColor Green
    }
    else {
        Write-Host "   ⚠️  Using external Ruby" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "   ❌ Ruby test failed" -ForegroundColor Red
}
Write-Host ""

Write-Host "🟦 Bun:" -ForegroundColor Blue
try {
    $bunVersion = bun --version 2>&1
    $bunPath = (where.exe bun | Select-Object -First 1)
    Write-Host "   Version: $bunVersion" -ForegroundColor Green
    Write-Host "   Path: $bunPath" -ForegroundColor Green
    if ($bunPath -like "*poly_gluttony*") {
        Write-Host "   ✅ Using .poly_gluttony Bun" -ForegroundColor Green
    }
    else {
        Write-Host "   ⚠️  Using external Bun" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "   ❌ Bun test failed" -ForegroundColor Red
}
Write-Host ""

Write-Host "📦 UV:" -ForegroundColor Green
try {
    $uvVersion = uv --version 2>&1
    $uvPath = (where.exe uv | Select-Object -First 1)
    Write-Host "   Version: $uvVersion" -ForegroundColor Green
    Write-Host "   Path: $uvPath" -ForegroundColor Green
    if ($uvPath -like "*poly_gluttony*") {
        Write-Host "   ✅ Using .poly_gluttony UV" -ForegroundColor Green
    }
    else {
        Write-Host "   ⚠️  Using external UV" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "   ❌ UV test failed" -ForegroundColor Red
}
Write-Host ""

Write-Host "🔧 GCC:" -ForegroundColor Yellow
try {
    $gccVersion = (gcc --version 2>&1 | Select-Object -First 1)
    $gccPath = (where.exe gcc | Select-Object -First 1)
    Write-Host "   Version: $gccVersion" -ForegroundColor Green
    Write-Host "   Path: $gccPath" -ForegroundColor Green
    if ($gccPath -like "*poly_gluttony*") {
        Write-Host "   ✅ Using .poly_gluttony GCC" -ForegroundColor Green
    }
    else {
        Write-Host "   ⚠️  Using external GCC" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "   ❌ GCC test failed" -ForegroundColor Red
}
Write-Host ""

Write-Host "🎉 Environment cleanup completed!" -ForegroundColor Green
Write-Host "All tools should now be using .poly_gluttony installations." -ForegroundColor Green
Write-Host ""
Write-Host "💡 To make these changes permanent, add this script to your PowerShell profile:" -ForegroundColor Cyan
Write-Host "   notepad `$PROFILE" -ForegroundColor White
Write-Host "   # Add the environment variable settings from this script" -ForegroundColor White