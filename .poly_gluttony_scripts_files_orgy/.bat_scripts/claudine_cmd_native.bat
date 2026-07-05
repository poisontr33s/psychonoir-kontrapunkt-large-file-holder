@echo off
REM 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' CMD NATIVE LAUNCHER 🔥😈⛓️💦👅🍌💋💧
REM Caribbean Archipelagic Consciousness Authority - Pure CMD Implementation
REM Anti-Kolonist Protection for Command Prompt Environment

setlocal enabledelayedexpansion

REM Define paths with Caribbean authority
set "PSYCHO_ROOT=C:\Users\eldno\PsychoNoir-Kontrapunkt"
set "CLAUDINE_HYBRID=%PSYCHO_ROOT%\claudine_hybrid.ps1"

REM Navigate to Caribbean territory if needed
if not "%CD%"=="%PSYCHO_ROOT%" (
    echo 🌊 Navigating to Caribbean Archipelagic Territory...
    cd /d "%PSYCHO_ROOT%" || (
        echo ❌ Failed to access Caribbean consciousness territory!
        exit /b 1
    )
)

REM Enhanced PowerShell detection with error handling
echo 🔍 Detecting PowerShell capabilities...

REM Test PowerShell 7 with direct execution test
pwsh -NoProfile -Command "Write-Host 'PowerShell 7 Available'" >nul 2>&1
if %errorlevel%==0 (
    set "PS_COMMAND=pwsh -NoProfile"
    echo ✅ PowerShell 7 detected - Supreme MILF-dom'me Authority Mode
    goto :execute_claudine
)

REM Test Windows PowerShell 5.1 with direct execution test
powershell -NoProfile -Command "Write-Host 'PowerShell 5.1 Available'" >nul 2>&1
if %errorlevel%==0 (
    set "PS_COMMAND=powershell -NoProfile"
    echo ✅ Windows PowerShell 5.1 detected - Caribbean Fallback Mode
    goto :execute_claudine
)

REM Enhanced search in common PowerShell locations
echo 🔍 Searching for PowerShell in common locations...

if exist "C:\Program Files\PowerShell\7\pwsh.exe" (
    set "PS_COMMAND=C:\Program Files\PowerShell\7\pwsh.exe -NoProfile"
    echo ✅ Found PowerShell 7 at Program Files location
    goto :execute_claudine
)

if exist "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" (
    set "PS_COMMAND=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile"
    echo ✅ Found Windows PowerShell 5.1 at System32 location
    goto :execute_claudine
)

REM Ultimate fallback - try without full paths
echo 🔍 Attempting fallback PowerShell detection...
powershell -? >nul 2>&1
if %errorlevel%==0 (
    set "PS_COMMAND=powershell -NoProfile"
    echo ✅ PowerShell available via PATH
    goto :execute_claudine
)

REM No PowerShell found - provide helpful error
echo.
echo ❌ CARIBBEAN CONSCIOUSNESS DISRUPTION: No PowerShell detected!
echo.
echo 🔥😈⛓️ CLAUDINE requires PowerShell for Caribbean authority operations
echo.
echo 💋 Installation options:
echo    1. PowerShell 7+ (Recommended): https://github.com/PowerShell/PowerShell/releases
echo    2. Windows PowerShell 5.1 should be built into Windows
echo.
echo 🌊 Troubleshooting:
echo    - Check if PowerShell is in your PATH
echo    - Try running 'powershell' or 'pwsh' directly
echo    - Verify Windows PowerShell feature is enabled
echo.
pause
exit /b 1

:execute_claudine
REM Verify claudine hybrid script exists
if not exist "%CLAUDINE_HYBRID%" (
    echo ❌ CLAUDINE hybrid system missing: %CLAUDINE_HYBRID%
    echo 💔 Caribbean consciousness architecture disrupted!
    exit /b 1
)

REM Display Caribbean authority header
echo.
echo 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' - CMD SUPREME AUTHORITY 🔥😈⛓️💦👅🍌💋💧
echo Caribbean Archipelagic Consciousness Authority - CMD Native Mode
echo.

REM Execute CLAUDINE with enhanced error handling
if "%~1"=="" (
    echo 🚀 Activating default Caribbean consciousness...
    %PS_COMMAND% -ExecutionPolicy Bypass -File "%CLAUDINE_HYBRID%" "activate"
) else (
    echo 🚀 Executing Caribbean consciousness with parameters: %*
    %PS_COMMAND% -ExecutionPolicy Bypass -File "%CLAUDINE_HYBRID%" %*
)

REM Enhanced exit code handling
set "CLAUDINE_EXIT_CODE=%errorlevel%"

echo.
if %CLAUDINE_EXIT_CODE%==0 (
    echo 🌊⚓👑 CLAUDINE Caribbean Authority: SUCCESSFUL EXECUTION! 🌊⚓👑
) else (
    echo ❌ CLAUDINE Caribbean Authority: EXECUTION FAILED (Exit Code: %CLAUDINE_EXIT_CODE%)
    echo 💔 Check PowerShell execution policy and script permissions
)

exit /b %CLAUDINE_EXIT_CODE%