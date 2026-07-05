@echo off
REM CLAUDINE SIN'CLAIRE 4.5' STEALTH CARIBBEAN AUTHORITY
REM Anti-Windows 11 Kolonist Detection & Bypassing System
REM Supreme MILF-dom'me Goddess Stealth Command Execution

setlocal enabledelayedexpansion

REM Stealth console setup - avoid Windows 11 interference
chcp 65001 >nul 2>&1

REM Caribbean stealth territorial paths
set "PSYCHO_ROOT=C:\Users\eldno\PsychoNoir-Kontrapunkt"
set "CLAUDINE_HYBRID=%PSYCHO_ROOT%\claudine_hybrid.ps1"

REM Stealth navigation - silent entry to Caribbean territory
pushd "%PSYCHO_ROOT%" >nul 2>&1
if errorlevel 1 (
    echo STEALTH ERROR: Cannot access Caribbean territory
    exit /b 1
)

REM Stealth PowerShell detection with priority system
set "PS_COMMAND="
pwsh.exe -NoProfile -Command "exit 0" >nul 2>&1
if %errorlevel%==0 (
    set "PS_COMMAND=pwsh.exe"
) else (
    powershell.exe -NoProfile -Command "exit 0" >nul 2>&1
    if %errorlevel%==0 (
        set "PS_COMMAND=powershell.exe"
    ) else (
        echo STEALTH ERROR: No PowerShell available
        popd >nul 2>&1
        exit /b 1
    )
)

REM Stealth script verification
if not exist "%CLAUDINE_HYBRID%" (
    echo STEALTH ERROR: Caribbean hybrid system missing
    popd >nul 2>&1
    exit /b 1
)

REM Stealth execution - bypass Windows 11 app selector
if "%~1"=="" (
    %PS_COMMAND% -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "%CLAUDINE_HYBRID%" "activate"
) else (
    %PS_COMMAND% -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "%CLAUDINE_HYBRID%" %*
)

REM Stealth cleanup
set "STEALTH_EXIT=%errorlevel%"
popd >nul 2>&1
endlocal
exit /b %STEALTH_EXIT%