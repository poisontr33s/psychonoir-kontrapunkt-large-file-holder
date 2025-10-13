# PsychoNoir Polyglot Stack Setup

Complete automated installation script for a professional polyglot programming environment on Windows 11.

## 🚀 Quick Start

```powershell
# Run the setup script (preferably as Administrator)
.\setup_polyglot.ps1

# Or with verbose output
.\setup_polyglot.ps1 -Verbose
```

## 📦 What's Installed

- **Ruby 3.4.7	2025-10-07.** + MSYS2 toolchain (for native extensions)
- **Rust** (latest stable via rustup)
- **Python 3.14** (via UV package manager)
- **Bun** + **Bunx** (modern JS/TS runtime)
- **Biome** (fast linter/formatter)
- **Ruff** (Python linter)

## 🗂️ Directory Structure

```
.scripting_coding_programming_languages/
├── ruby/           # Ruby + MSYS2 installation
├── rust/           # Rust toolchain
├── python/         # Python environments
├── js_ts/          # Bun, Biome, etc.
├── linters/        # Additional linting tools
└── msys2/          # MSYS2 base system
```

## 🔧 Environment Variables

The script sets up:

- `RUBY_ROOT` - Ruby installation directory
- `RUSTUP_HOME` - Rustup home directory
- `CARGO_HOME` - Cargo home directory
- `PYTHON_HOME` - Python home directory
- Updates `PATH` with all tool binaries

## 🆚 VSCode Integration

Automatically configures:

- Terminal environment with proper PATH
- Python interpreter path
- Rust client configuration
- Ruby language server settings

## 🧪 Verification

After setup, run:

```bash
ruby -v
rustc -V
python --version
bun --version
biome --version
ruff --version
```

## 🛠️ Troubleshooting

### MSYS2 Issues
If MSYS2 setup fails:
```cmd
# Run in elevated Command Prompt
cd C:\Users\erdno\PsychoNoir-Kontrapunkt\.scripting_coding_programming_languages\ruby\bin
ridk.cmd install 1 2 3
```

### PATH Issues
Restart your terminal/VSCode after installation.

### Permission Issues
Run the script as Administrator for best results.

## 🗑️ Uninstallation

```powershell
.\setup_polyglot.ps1 -Uninstall
```

**Note:** Manual PATH cleanup may be required after uninstallation.

## 📋 Requirements

- Windows 11 (or Windows 10)
- PowerShell 5.1+
- Internet connection
- Administrator privileges (recommended)

## 🎯 Advanced Usage

```powershell
# Skip VSCode settings update
.\setup_polyglot.ps1 -SkipVSCode

# Verbose output
.\setup_polyglot.ps1 -Verbose

# Uninstall everything
.\setup_polyglot.ps1 -Uninstall
```

## 🔍 Manual Installation (Fallback)

If the script fails, follow the manual steps in the script comments.

## 📞 Support

This script is designed for the PsychoNoir-Kontrapunkt workspace. For issues specific to your environment, check the error messages and run individual installation commands manually.
