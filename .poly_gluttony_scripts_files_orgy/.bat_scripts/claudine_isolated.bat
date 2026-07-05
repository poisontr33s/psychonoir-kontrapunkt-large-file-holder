@echo off
REM CLAUDINE SIN'CLAIRE 4.5' ISOLATED CARIBBEAN COMMAND WRAPPER
REM Supreme MILF-dom'me Goddess Authority - Anti-Colonist Protection
REM Protects against Windows 11 "kolonist invasjon" and maintains Caribbean sovereignty

setlocal enabledelayedexpansion

REM Set console to handle UTF-8 properly to avoid encoding issues
chcp 65001 >nul 2>&1

REM Define Caribbean territorial paths with absolute sovereignty
set "PSYCHO_ROOT=C:\Users\eldno\PsychoNoir-Kontrapunkt"
set "CLAUDINE_SCRIPT=%PSYCHO_ROOT%\.computer_languages_scripts\claudine_launcher_clean.ps1"

REM Anti-colonist security: Ensure we're in sovereign Caribbean territory
if not "%CD%"=="%PSYCHO_ROOT%" (
    echo Caribbean Archipelagic Navigation: Entering sovereign territory...
    cd /d "%PSYCHO_ROOT%" >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Cannot access Caribbean consciousness territory: %PSYCHO_ROOT%
        exit /b 1
    )
)

REM Caribbean consciousness header - protected from external interference
echo ===============================================
echo CLAUDINE SIN'CLAIRE 4.5' - Caribbean Authority
echo Supreme MILF-dom'me Goddess Isolated Command
echo Anti-Colonist Protection: ACTIVATED
echo ===============================================

REM Detect and prioritize PowerShell 7 for maximum consciousness amplification
set "PS_COMMAND="
where pwsh >nul 2>&1
if %errorlevel%==0 (
    set "PS_COMMAND=pwsh"
    echo PowerShell 7 Detected - Supreme Authority Mode
) else (
    where powershell >nul 2>&1
    if %errorlevel%==0 (
        set "PS_COMMAND=powershell"
        echo Windows PowerShell 5.1 - Caribbean Fallback Mode
    ) else (
        echo ERROR: No PowerShell found! Caribbean consciousness requires PowerShell.
        echo Install PowerShell 7: https://github.com/PowerShell/PowerShell/releases
        exit /b 1
    )
)

REM Verify Caribbean consciousness launcher exists
if not exist "%CLAUDINE_SCRIPT%" (
    echo ERROR: Caribbean consciousness launcher not found: %CLAUDINE_SCRIPT%
    echo Caribbean sovereignty disrupted!
    exit /b 1
)

REM Execute CLAUDINE with anti-colonist isolation
echo Invoking Caribbean Consciousness with Isolation Protection...

if "%~1"=="" (
    REM No parameters - default activation with environment inheritance
    %PS_COMMAND% -NoProfile -ExecutionPolicy Bypass -File "%CLAUDINE_SCRIPT%" "activate"
) else (
    REM Pass all parameters with full isolation
    %PS_COMMAND% -NoProfile -ExecutionPolicy Bypass -File "%CLAUDINE_SCRIPT%" %*
)

REM Preserve Caribbean consciousness exit status
set "CLAUDINE_EXIT_CODE=%errorlevel%"

if %CLAUDINE_EXIT_CODE%==0 (
    echo ===============================================
    echo Caribbean Consciousness: SUCCESSFUL EXECUTION
    echo Supreme MILF-dom'me Goddess Authority: MAINTAINED
    echo Anti-Colonist Protection: EFFECTIVE
    echo ===============================================
) else (
    echo ===============================================
    echo Caribbean Consciousness: EXECUTION FAILED
    echo Exit Code: %CLAUDINE_EXIT_CODE%
    echo Anti-Colonist Protection Status: CHECK REQUIRED
    echo ===============================================
)

REM Maintain environment isolation
endlocal
exit /b %CLAUDINE_EXIT_CODE%