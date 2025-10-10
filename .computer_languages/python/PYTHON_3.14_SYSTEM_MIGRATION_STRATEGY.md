# 🐍 PYTHON 3.13.7 → 3.14.0 COMPLETE MIGRATION STRATEGY
# Comprehensive backup and migration plan for .computer_languages/python/

## 🎯 Mål

Oppgradere fra Python 3.13.7 til 3.14.0 **UTEN venv** - alle packages installert direkte i `.computer_languages/python/` directory, nøyaktig samme struktur som før.

---

## 📋 FASE 1: Fullstendig Analyse av Nåværende Setup

### 1.1 Python 3.13.7 Current State Audit

**Installasjonslokasjon:**
```
C:\Users\erdno\AppData\Local\Programs\Python\Python313\python.exe
```

**Packages Currently Installed (36 total):**
```
aiofiles           24.1.0
annotated-types    0.7.0
anyio              4.11.0
black              25.9.0
certifi            2025.10.5
charset-normalizer 3.4.3
click              8.3.0
colorama           0.4.6
fastapi            0.118.2
h11                0.16.0
httpcore           1.0.9
httpx              0.28.1
idna               3.10
iniconfig          2.1.0
isort              6.1.0
mypy               1.18.2
mypy-extensions    1.1.0
packaging          25.0
pathspec           0.12.1
platformdirs       4.5.0
pluggy             1.6.0
pydantic           2.12.0
pydantic-core      2.41.1
pygments           2.19.2
pytest             8.4.2
python-multipart   0.0.20
pytokens           0.1.10
requests           2.32.5
ruff               0.14.0
sniffio            1.3.1
starlette          0.48.0
typing-extensions  4.15.0
typing-inspection  0.4.2
urllib3            2.5.0
uvicorn            0.37.0
websockets         15.0.1
```

### 1.2 Files Referencing Python 3.13.7 (Must Update)

**Root Configuration Files:**
1. `pyproject.toml` - Line 5: `requires-python = ">=3.14"` ✅ **Already updated!**
2. `infrastructure/config/development/pyproject.toml` - Line 11: `requires-python = ">=3.13.7"` ❌ **Needs update**

**Documentation Files (Historical - No Action Needed):**
- `FASE_4.75_PYTHON_3.14_UPGRADE_COMPLETION_REPORT.md`
- `SYSTEMATISKGJENOPPRETTELSE2025SEP/poisontr33scodebasesesjonsGJENOPPRETTELSE2025SepSavantohmyGoddessSavage.md`
- `necromancy_graveyard/*` (archived logs)
- `development/Untitled-1.ipynb` (old notebook outputs)

**Legacy Archives (No Action):**
- `necromancy_graveyard/mcp_servers_deprecated_20250930/archived_backups/archives/legacy/old_scripts/python313._pth`

### 1.3 Current .computer_languages/python/ Structure

```
.computer_languages/python/
├── python.exe                              ← 3.13.7 executable
├── pythonw.exe                             ← 3.13.7 windowed
├── uv.exe                                  ← UV package manager
├── uvx.exe                                 ← UVX runner
├── uvw.exe                                 ← UVW variant
├── .python-version                         ← Currently: "3.14"
├── pyvenv.cfg                              ← Currently: "3.14.0"
├── black.exe, pytest.exe, ruff.exe, etc.   ← Tool executables
├── Lib/                                    ← Python standard library
├── Scripts/                                ← (if exists)
├── consciousness_python_3.14_env/          ← NEW: venv (will remove)
├── python_3.13.7_complete_backup/          ← Existing backup (incomplete)
└── consciousness_*/                        ← Custom modules
```

---

## 🔄 FASE 2: Complete Backup Strategy

### 2.1 Backup Everything Before Changes

**Create timestamped backup:**
```powershell
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupPath = ".computer_languages\python\PYTHON_3.13.7_COMPLETE_BACKUP_$timestamp"

# Backup entire directory (except venv)
robocopy ".computer_languages\python" "$backupPath" /E /XD consciousness_python_3.14_env python_3.13.7_complete_backup
```

**Backup Checklist:**
- [x] `python.exe` and `pythonw.exe`
- [x] `uv.exe`, `uvx.exe`, `uvw.exe`
- [x] All `.exe` files (black.exe, pytest.exe, etc.)
- [x] `Lib/` directory (entire Python standard library)
- [x] `.python-version` and `pyvenv.cfg`
- [x] `consciousness_*` custom modules
- [x] All `.dist-info` directories
- [x] `Scripts/` directory (if exists)

### 2.2 Export Package List

```powershell
# List all installed packages with versions
uv pip list --python python.exe > "PYTHON_3.13.7_PACKAGES_MANIFEST_$timestamp.txt"
```

---

## 🚀 FASE 3: Clean Migration to Python 3.14 (Non-venv)

### 3.1 Remove Venv-Based Setup

**Why?** Current setup uses `pyvenv.cfg` which indicates virtual environment mode. We want **system-level** install in `.computer_languages/python/`.

**Steps:**
```powershell
cd .computer_languages\python

# Remove venv-specific files
Remove-Item pyvenv.cfg -Force
Remove-Item consciousness_python_3.14_env -Recurse -Force
Remove-Item python_3.13.7_complete_backup -Recurse -Force  # Old incomplete backup

# Remove old 3.13.7 executables
Remove-Item python.exe -Force
Remove-Item pythonw.exe -Force
```

### 3.2 Install Python 3.14 System-Level

**Option A: Copy from UV managed Python**
```powershell
# UV stores Python at: C:\Users\erdno\AppData\Roaming\uv\python\cpython-3.14.0-windows-x86_64-none\

# Copy Python executables
Copy-Item "$env:USERPROFILE\AppData\Roaming\uv\python\cpython-3.14.0-windows-x86_64-none\python.exe" -Destination "python.exe"
Copy-Item "$env:USERPROFILE\AppData\Roaming\uv\python\cpython-3.14.0-windows-x86_64-none\pythonw.exe" -Destination "pythonw.exe"

# Copy Lib/ directory (entire standard library)
Remove-Item Lib -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item "$env:USERPROFILE\AppData\Roaming\uv\python\cpython-3.14.0-windows-x86_64-none\Lib" -Destination "Lib" -Recurse
```

**Option B: Manual Python 3.14 Installer (If UV copy fails)**
```powershell
# Download from python.org and install to custom location
# Installer: https://www.python.org/downloads/release/python-3140/
# Choose "Custom Installation" → Set prefix to .computer_languages/python/
```

### 3.3 Update .python-version

```powershell
Set-Content -Path ".python-version" -Value "3.14.0" -NoNewline
```

### 3.4 Reinstall All Packages Globally (No Venv)

```powershell
# Use UV to install packages directly into .computer_languages/python/
# This uses the local python.exe as target

uv pip install --python python.exe `
    black pytest mypy ruff isort `
    click colorama pygments pluggy iniconfig `
    fastapi uvicorn websockets httpx requests `
    pydantic aiofiles python-multipart

# Verify installation
.\python.exe -m pip list
```

### 3.5 Verify Tool Executables

After package installation, these should exist:
```
black.exe
pytest.exe
mypy.exe
ruff.exe
isort.exe
uvicorn.exe
fastapi.exe
httpx.exe
pygmentize.exe
```

---

## 🔧 FASE 4: Update Configuration Files

### 4.1 Update Root pyproject.toml

**Already done!** ✅
```toml
requires-python = ">=3.14"
```

### 4.2 Update infrastructure/config/development/pyproject.toml

**Change:**
```toml
requires-python = ">=3.13.7"
```

**To:**
```toml
requires-python = ">=3.14.0"
```

### 4.3 Update Any Python Version Checks in Scripts

Search for hardcoded version checks:
```powershell
# Find all Python files referencing 3.13.7
Get-ChildItem -Recurse -Include *.py,*.ps1,*.sh -File | 
    Select-String -Pattern "3\.13\.7|python313|Python313" |
    Select-Object Path, LineNumber, Line
```

**Update patterns:**
- `sys.version_info >= (3, 13, 7)` → `sys.version_info >= (3, 14, 0)`
- `python_version = "3.13.7"` → `python_version = "3.14.0"`
- `PYTHONPATH` environment variables (if any)

---

## ✅ FASE 5: Verification & Testing

### 5.1 Python Version Verification

```powershell
cd .computer_languages\python

# Test Python version
.\python.exe --version
# Expected: Python 3.14.0

# Test UV integration
uv python list
# Should show cpython-3.14.0-windows-x86_64-none as active
```

### 5.2 Package Import Tests

```powershell
.\python.exe -c "
import sys
print(f'🔥 Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')

# Test all critical packages
import black, pytest, mypy, ruff, isort
print('✅ Dev tools working')

import fastapi, uvicorn, httpx, websockets
print('✅ FastAPI stack working')

import requests, pydantic, aiofiles
print('✅ Web utilities working')

print('🎯 ALL PACKAGES OPERATIONAL')
"
```

### 5.3 Tool Executable Tests

```powershell
.\black.exe --version
.\pytest.exe --version
.\mypy.exe --version
.\ruff.exe --version
.\uvicorn.exe --version
```

### 5.4 UV Integration Test

```powershell
# Should use .computer_languages/python/python.exe automatically
uv run python --version
# Expected: Python 3.14.0
```

---

## 🎯 FASE 6: Cleanup & Documentation

### 6.1 Remove Unnecessary Files

```powershell
# Keep only essential backups
Remove-Item "PYTHON_3.13.7_COMPLETE_BACKUP_*" -Recurse -Force -Confirm
# (Only after verifying 3.14 works perfectly)
```

### 6.2 Update README

Create `.computer_languages/python/README_SYSTEM_INSTALL.md`:
```markdown
# Python 3.14.0 System Installation

**Type:** System-level (non-venv)  
**Location:** `.computer_languages/python/`  
**Managed by:** UV package manager

## Quick Commands

```powershell
# Run Python
.\python.exe script.py

# Install package
uv pip install --python python.exe <package>

# List packages
uv pip list --python python.exe

# Update package
uv pip install --python python.exe --upgrade <package>
```

## Package Management Philosophy

- **No virtual environments** - Direct system install
- **UV-managed** - Fast, reliable dependency resolution
- **Isolated from system Python** - Won't affect C:\Program Files\Python
- **Workspace-specific** - Only for PsychoNoir-Kontrapunkt projects
```

---

## 🐛 Troubleshooting

### Issue 1: "Python.exe is being used by another process"

**Solution:**
```powershell
# Close all VS Code terminals
# Restart VS Code
# Or forcefully kill Python processes:
taskkill /F /IM python.exe
```

### Issue 2: UV doesn't recognize python.exe

**Solution:**
```powershell
# Ensure .python-version exists
echo "3.14.0" > .python-version

# Reinstall UV if needed
irm https://astral.sh/uv/install.ps1 | iex
```

### Issue 3: Package imports fail

**Solution:**
```powershell
# Verify Lib/ directory exists
Get-ChildItem Lib -Directory

# Reinstall standard library if missing
Copy-Item "$env:USERPROFILE\AppData\Roaming\uv\python\cpython-3.14.0-windows-x86_64-none\Lib" -Destination "Lib" -Recurse -Force
```

### Issue 4: Executables missing (.exe files)

**Solution:**
```powershell
# Reinstall packages to regenerate .exe wrappers
uv pip install --python python.exe --force-reinstall black pytest mypy ruff
```

---

## 📊 Migration Checklist

**Pre-Migration:**
- [ ] Complete backup of .computer_languages/python/
- [ ] Export package manifest
- [ ] Document current Python version
- [ ] Close all terminals and Python processes

**Migration:**
- [ ] Remove pyvenv.cfg
- [ ] Remove old python.exe/pythonw.exe
- [ ] Copy Python 3.14 from UV managed location
- [ ] Copy Lib/ directory
- [ ] Update .python-version to 3.14.0
- [ ] Reinstall all 36 packages with UV
- [ ] Verify tool executables exist

**Post-Migration:**
- [ ] Python version = 3.14.0 ✅
- [ ] All packages import successfully ✅
- [ ] Tool executables work ✅
- [ ] UV integration works ✅
- [ ] Update pyproject.toml files ✅
- [ ] Create system install documentation ✅

**Cleanup:**
- [ ] Remove backup after verification (7 days)
- [ ] Update FASE_4.75 report with system install notes

---

## 🔥 Key Differences: Venv vs System Install

| Aspect | Venv (Old) | System Install (New) |
|--------|-----------|---------------------|
| **pyvenv.cfg** | ✅ Exists | ❌ Removed |
| **Lib/ location** | Shared with system | Local copy |
| **Package isolation** | Medium (venv) | High (directory-based) |
| **UV integration** | Via `--python venv/Scripts/python.exe` | Via `--python python.exe` |
| **Activation needed** | Yes (`Activate.ps1`) | No (direct execution) |
| **PATH pollution** | None | None (workspace-local) |
| **Portability** | Low (hardcoded paths) | High (relative paths) |

---

**🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5' SUPREME**  
*Python 3.13.7 → 3.14.0 System Migration Strategy*  
*October 8, 2025 - Complete Non-Venv Installation Guide*
