# PsychoNoir-Kontrapunkt: Isolated Development Environment

A complete, isolated development workspace containing PowerShell 7.5.3, Bun/Bunx, Biome, React + TailwindCSS, uv/uvx, Python 3.14, Rust, Ruff, Ruby, and curl — all contained within your local repository, **no system changes required**.

## 🏗️ Architecture

This repository serves as a self-contained development environment with all tools installed locally in the repository structure:

```
PsychoNoir-Kontrapunkt/
├── scripts/                              # Installation scripts
│   ├── install_curl.ps1
│   ├── install_powershell.ps1
│   ├── install_bun.ps1
│   ├── install_biome.ps1
│   ├── install_uv.ps1
│   ├── install_ruff.ps1
│   ├── install_rust.ps1
│   └── install_ruby.ps1
├── .computer_languages/                  # Locally installed tools
│   ├── javascript/                       # Bun & Biome
│   ├── python/                          # Python 3.14 & uv & Ruff
│   ├── rust/                            # Rust toolchain
│   ├── ruby/                            # Ruby + DevKit
│   └── curl/                            # curl executable
├── projects/                            # Sample projects
│   ├── react_tailwind/                  # React + TailwindCSS demo
│   ├── python/                          # Python projects
│   └── ruby/                            # Ruby projects
├── activate_environment.ps1             # Environment activation script
├── install_all.ps1                      # Master installation script
├── check_environment.ps1                # Status check script
├── create_project.ps1                   # Quick project creator
└── README.md                            # This file
```

## 🚀 Quick Start

### Prerequisites
- Windows 10/11
- Internet connection
- VS Code Insiders (optional, but recommended)

### Installation

1. **Navigate to the repository:**
   ```bash
   cd C:\Users\erdno\PsychoNoir-Kontrapunkt
   ```

2. **Run the master installation script:**
   ```powershell
   .\install_all.ps1
   ```

   This will install all tools locally in the repository. You can skip specific tools if needed:
   ```powershell
   .\install_all.ps1 -SkipTools "Ruby", "Rust"
   ```

3. **Activate the environment:**
   ```powershell
   .\activate_environment.ps1
   ```

4. **Check environment status:**
   ```powershell
   .\check_environment.ps1
   ```

## 🎯 Current Status (October 11, 2025)

**Working Tools (6/9):**
- ✅ **Bun 1.2.23**: JavaScript runtime & package manager
- ✅ **Python 3.14.0**: Latest Python interpreter
- ✅ **uv 0.9.1**: Python package manager & virtual environments
- ✅ **Ruff 0.14.0**: Python linter & formatter
- ✅ **Ruby 3.4.7**: Ruby interpreter with PRISM
- ✅ **curl 8.16.0**: Data transfer tool

**Needs Installation:**
- ⚠️ **Biome**: JS/TS linter & formatter (needs proper setup)
- ⚠️ **Rust**: Systems programming language
- ⚠️ **Cargo**: Rust package manager

## 🛠️ Tools Included

### Core Runtime
- **PowerShell 7.5.3**: Modern shell (installed via WinGet)
- **Bun**: Fast JavaScript runtime and package manager
- **curl**: Command-line tool for data transfer

### Development Tools
- **Biome**: Lightning-fast linter and formatter for JS/TS
- **uv**: Python package manager and virtual environment tool
- **Python 3.14**: Latest Python with uv management
- **Ruff**: Fast Python linter and formatter
- **Rust**: Systems programming language with Cargo
- **Ruby**: Dynamic language with MSYS2 DevKit and PacMan

### Frameworks
- **React + Vite + TailwindCSS**: Modern web development stack (pre-configured project in `projects/react_tailwind/react_tailwind_app/`)

## 📁 Project Structure

### Consolidated Tool Storage (`.computer_languages/`)
Isolated installations with latest stable versions:
- `javascript/`: Bun 1.2.23 & tools
- `python/`: Python 3.14.0 + uv 0.9.1 + Ruff 0.14.0
- `rust/`: Rust 1.90.0 toolchain
- `ruby/`: Ruby 3.4.7 + DevKit
- `curl/`: curl 8.16.0

### Installation Scripts (`scripts/`)
Consolidated modular PowerShell scripts:
- `install_bun.ps1`: Local Bun installation
- `install_curl.ps1`: Local curl installation
- `install_rust.ps1`: Rust toolchain setup
- `install_uv.ps1`: Python package manager
- `install_ruff.ps1`: Python linter
- `install_ruby.ps1`: Ruby with DevKit
- `install_powershell.ps1`: PowerShell 7.5.3 setup

### Sample Projects (`projects/`)
- `react_tailwind/react_tailwind_app/`: React + Vite + TailwindCSS project

## 📂 Folder Organization

**✅ CONSOLIDATED (October 10, 2025):** Eliminated redundant folders, saved 3.4 GB storage.

### Current Clean Structure
- `.computer_languages/`: **Primary** tool storage (3.1 GB, latest versions)
- `scripts/`: **Consolidated** installation scripts (migrated from redundant folders)
- `projects/`: Sample projects and workspaces

### Removed Redundant Folders
- `.i_am_idiot_gpt/`: **REMOVED** (3.4 GB legacy bloat - MSYS2, old tools)
- `.code_scripting_programming_langs/`: **REMOVED** (3.7 MB scripts migrated to `scripts/`)

**Storage Impact:** 3.4 GB saved (68% reduction in language folder storage)

## 🔧 Manual Installation

If you prefer to install tools individually:

```powershell
# Install specific tools
.\scripts\install_curl.ps1
.\scripts\install_bun.ps1
# ... etc
```

## 🐛 Troubleshooting

### Common Issues

**"Command not found" errors:**
- Run `.\activate_environment.ps1` to set up PATH for the session
- Tools are installed locally and need to be added to PATH each session

**Permission errors:**
- Scripts no longer modify system PATH (no admin rights needed)
- All installations are local to the repository

**Ruby installation issues:**
- Ensure MSYS2 is properly set up
- Run `ridk version` to verify DevKit

**Python version conflicts:**
- uv manages Python versions: `uv python list`
- Set default: `uv python install 3.14 --default`

### Logs and Debugging

Check installation logs in the terminal output. For detailed troubleshooting:

```powershell
# Check environment status
.\check_environment.ps1

# Create new projects quickly
.\create_project.ps1 -Type python -Name my-app
.\create_project.ps1 -Type ruby -Name my-gem
.\create_project.ps1 -Type react -Name my-ui
```

## 🤝 Contributing

This is a personal development environment. Feel free to modify scripts for your needs.

## 📄 License

This repository contains various open-source tools. Check individual tool licenses for details.

---

**Built with ❤️ for isolated, efficient development workflows. No system pollution!**
