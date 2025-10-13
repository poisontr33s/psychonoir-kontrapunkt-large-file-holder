@echo off
REM 🔥😈⛓️💦👅🍌💋💧 CLAUDINE CMD PATH HELPER 🔥😈⛓️💦👅🍌💋💧
REM Ensures CLAUDINE can be run from any CMD location

setlocal

REM Define CLAUDINE location
set "CLAUDINE_ROOT=C:\Users\erdno\PsychoNoir-Kontrapunkt"
set "CLAUDINE_BAT=%CLAUDINE_ROOT%\claudine.bat"

REM Verify CLAUDINE batch file exists
if not exist "%CLAUDINE_BAT%" (
    echo ❌ CLAUDINE batch file not found: %CLAUDINE_BAT%
    echo 💔 Caribbean consciousness architecture missing!
    exit /b 1
)

REM Execute CLAUDINE from its proper location
echo 🌊 Invoking CLAUDINE from Caribbean territory...
cd /d "%CLAUDINE_ROOT%" && "%CLAUDINE_BAT%" %*

REM Preserve exit code
exit /b %errorlevel%