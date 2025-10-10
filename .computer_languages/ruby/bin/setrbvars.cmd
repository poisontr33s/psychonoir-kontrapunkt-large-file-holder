@ECHO OFF
REM Determine where is RUBY_BIN (where this script is)
PUSHD %~dp0.
SET RUBY_BIN=%CD%
POPD

REM Add RUBY_BIN to the PATH
REM RUBY_BIN takes higher priority to avoid other tools
REM conflict with our own (mainly the DevKit)
SET PATH=%RUBY_BIN%;%PATH%

REM Load MSYS2 RbConfig patch if MSYS2 is detected
IF NOT "%MSYSTEM%"=="" (
    SET RUBYOPT=-r"%RUBY_BIN%\..\lib\ruby\site_ruby\3.4.0\msys2_rbconfig_patch.rb"
)

SET RUBY_BIN=

REM Display Ruby version
ruby.exe -v
