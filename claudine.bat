@echo off
REM 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' UNIVERSAL BATCH WRAPPER 🔥😈⛓️💦👅🍌💋💧
REM Caribbean Archipelagic Consciousness Authority - CMD Compatibility Layer
REM Works in CMD, PowerShell 5.1, PowerShell 7, Extension Host - UNIVERSAL ROBUSTHET!

setlocal enabledelayedexpansion

REM Define paths
set "PSYCHO_ROOT=C:\Users\erdno\PsychoNoir-Kontrapunkt"
set "CLAUDINE_HYBRID=%PSYCHO_ROOT%\claudine_hybrid.ps1"
set "COMMON_CONFIG=%PSYCHO_ROOT%\.computer_languages_scripts\common_config.ps1"

REM Check if we're in the right location, if not, navigate there
if not "%CD%"=="%PSYCHO_ROOT%" (
    echo 🌊 Navigating to Caribbean Archipelagic Consciousness Authority...
    cd /d "%PSYCHO_ROOT%"
)

REM Detect available PowerShell and use the best one
set "PS_COMMAND="
where pwsh >nul 2>&1
if %errorlevel%==0 (
    set "PS_COMMAND=pwsh"
    echo 💋 Using PowerShell 7 ^(pwsh^) - Supreme MILF-dom'me Authority
) else (
    where powershell >nul 2>&1
    if %errorlevel%==0 (
        set "PS_COMMAND=powershell"
        echo 💋 Using Windows PowerShell 5.1 - Caribbean Consciousness Fallback
    ) else (
        echo ❌ No PowerShell found! CLAUDINE requires PowerShell.
        echo Install PowerShell 7: https://github.com/PowerShell/PowerShell/releases
        exit /b 1
    )
)

REM Check if claudine hybrid script exists
if not exist "%CLAUDINE_HYBRID%" (
    echo ❌ CLAUDINE hybrid system not found at: %CLAUDINE_HYBRID%
    echo 💔 Caribbean consciousness disrupted!
    exit /b 1
)

REM Execute CLAUDINE with parameters (if any)
echo 🔥😈⛓️💦👅🍌💋💧 Invoking CLAUDINE SIN'CLAIRE 4.5' Supreme Authority...

if "%~1"=="" (
    REM No parameters - default activation
    %PS_COMMAND% -ExecutionPolicy Bypass -File "%CLAUDINE_HYBRID%" "activate"
) else (
    REM Pass all parameters to claudine hybrid system
    %PS_COMMAND% -ExecutionPolicy Bypass -File "%CLAUDINE_HYBRID%" %*
)

REM Preserve exit code
set "CLAUDINE_EXIT_CODE=%errorlevel%"

if %CLAUDINE_EXIT_CODE%==0 (
    echo 🌊⚓👑 CLAUDINE Caribbean Authority: SUCCESS! 🌊⚓👑
) else (
    echo ❌ CLAUDINE Caribbean Authority: FAILED with exit code %CLAUDINE_EXIT_CODE%
)

exit /b %CLAUDINE_EXIT_CODE%