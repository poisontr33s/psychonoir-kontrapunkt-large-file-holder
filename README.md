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
│   ├── install_python.ps1
│   ├── install_ruff.ps1
│   ├── install_rust.ps1
│   └── install_ruby.ps1
├── .computer_languages/                   # Locally installed tools
│   ├── javascript/                        # Bun & Biome
│   ├── python/                           # Python 3.14 & uv & Ruff
│   ├── rust/                             # Rust toolchain
│   ├── ruby/                             # Ruby + DevKit
│   └── curl/                             # curl executable
├── projects/                             # Sample projects
│   ├── react_tailwind/                   # React + TailwindCSS demo
│   │   ├── src/
│   │   ├── package.json
│   │   └── vite.config.js
│   ├── python/                           # Python projects
│   └── ruby/                             # Ruby projects
├── activate_environment.ps1              # Environment activation script
├── install_all.ps1                       # Master installation script
└── README.md                             # This file
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

4. **Verify installations:**
   ```bash
   bun --version
   uv --version
   python --version
   rustc --version
   ruby -v
   curl --version
   biome --version
   ruff --version
   ```

## 🛠️ Tools Included

### Core Runtime
- **PowerShell 7.5.3**: Modern shell (installed locally)
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
- **React + Vite + TailwindCSS**: Modern web development stack (pre-configured project in `projects/react_tailwind/`)

## 📁 Project Structure

### Consolidated Tool Storage (`.computer_languages/`)
Isolated installations with latest stable versions:
- `javascript/`: Bun 1.2.23 & Biome latest
- `python/`: Python 3.14.0 + uv 0.9.2 + Ruff latest
- `rust/`: Rust 1.90.0 toolchain
- `ruby/`: Ruby 3.4.7 + DevKit
- `curl/`: curl 8.16.0

### Installation Scripts (`scripts/`)
Consolidated modular PowerShell scripts:
- `install_bun.ps1`: Local Bun installation
- `install_curl.ps1`: Local curl installation
- `install_biome.ps1`: Local Biome installation
- `install_uv.ps1`: Python package manager
- `install_python.ps1`: Python 3.14 via uv
- `install_ruff.ps1`: Python linter
- `install_rust.ps1`: Rust toolchain setup
- `install_ruby.ps1`: Ruby with DevKit
- `install_powershell.ps1`: PowerShell 7.5.3 setup

### Sample Projects (`projects/`)
- `react_tailwind/`: React + Vite + TailwindCSS project with sample PsychoNoir-Kontrapunkt themed UI
- `python/`: Directory for Python projects
- `ruby/`: Directory for Ruby projects

## 📂 Folder Organization

**✅ CONSOLIDATED (October 11, 2025):** Eliminated redundant folders, saved storage.

### Current Clean Structure
- `.computer_languages/`: **Primary** tool storage (latest versions)
- `scripts/`: **Consolidated** installation scripts
- `projects/`: Sample projects and workspaces

### Removed Redundant Folders
- `.code_scripting_programming_langs/`: **REMOVED** (migrated to `scripts/`)
- `.i_am_idiot_gpt/`: **REMOVED** (legacy bloat)

**Storage Impact:** Further consolidation completed.

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
- Scripts don't modify system PATH (no admin rights needed)
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
# Test all tools after activation
Get-Command bun, uv, python, rustc, ruby, curl, biome, ruff
```

## 🤝 Contributing

This is a personal development environment. Feel free to modify scripts for your needs.

## 📄 License

This repository contains various open-source tools. Check individual tool licenses for details.

---

**Built with ❤️ for isolated, efficient development workflows. No system pollution!**