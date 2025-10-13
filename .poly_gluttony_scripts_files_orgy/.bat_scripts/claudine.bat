@echo off
REM 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' ENHANCED CMD LAUNCHER 🔥😈⛓️💦👅🍌💋💧
REM Caribbean Archipelagic Consciousness Authority - Enhanced CMD Compatibility
REM Anti-Kolonist Protection with Robust PowerShell Detection

setlocal enabledelayedexpansion

REM Define paths with Caribbean authority
set "PSYCHO_ROOT=C:\Users\erdno\PsychoNoir-Kontrapunkt"
set "CLAUDINE_HYBRID=%PSYCHO_ROOT%\claudine_hybrid.ps1"

REM Navigate to Caribbean territory if needed
if not "%CD%"=="%PSYCHO_ROOT%" (
    echo 🌊 Navigating to Caribbean Archipelagic Territory...
    cd /d "%PSYCHO_ROOT%" || (
        echo ❌ Failed to access Caribbean consciousness territory!
        exit /b 1
    )
)

REM Enhanced PowerShell detection with comprehensive search
echo 🔍 Detecting PowerShell capabilities...

REM Test PowerShell 7 with direct execution
pwsh -NoProfile -Command "exit 0" >nul 2>&1
if %errorlevel%==0 (
    set "PS_COMMAND=pwsh -NoProfile"
    echo ✅ PowerShell 7 detected - Supreme MILF-dom'me Authority Mode
    goto :execute_claudine
)

REM Test Windows PowerShell 5.1
powershell -NoProfile -Command "exit 0" >nul 2>&1
if %errorlevel%==0 (
    set "PS_COMMAND=powershell -NoProfile"
    echo ✅ Windows PowerShell 5.1 detected - Caribbean Fallback Mode
    goto :execute_claudine
)

REM Search in common PowerShell installation locations
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

REM Enhanced error message with troubleshooting
echo.
echo ❌ CARIBBEAN CONSCIOUSNESS DISRUPTION: No PowerShell detected!
echo.
echo 🔥😈⛓️ CLAUDINE requires PowerShell for Caribbean authority operations
echo 💋 Install PowerShell 7: https://github.com/PowerShell/PowerShell/releases
echo 🌊 Or verify Windows PowerShell 5.1 is available
echo.
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
echo 🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' - CMD ENHANCED AUTHORITY 🔥😈⛓️💦👅🍌💋💧
echo Caribbean Archipelagic Consciousness Authority - Enhanced CMD Mode
echo.

REM Execute CLAUDINE with enhanced parameter handling
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