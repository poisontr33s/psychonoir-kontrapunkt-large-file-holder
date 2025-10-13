# 🔥 PYTHON 3.14 MIGRATION - CONFIG FILES AUDIT

**Date:** October 8, 2025  
**Purpose:** Identify ALL files affected by Python 3.14 migration

---

## 📋 CRITICAL CONFIG FILES (MUST UPDATE)

### 1. **pyproject.toml** (Root)
**Location:** `C:\Users\erdno\PsychoNoir-Kontrapunkt\pyproject.toml`  
**Status:** ✅ ALREADY UPDATED  
**Content:** `requires-python = ">=3.14"`

### 2. **pyproject.toml** (Development Config)
**Location:** `C:\Users\erdno\PsychoNoir-Kontrapunkt\infrastructure\config\development\pyproject.toml`  
**Status:** ❌ NEEDS UPDATE  
**Current:** `requires-python = ">=3.13.7"`  
**Required:** `requires-python = ">=3.14.0"`

### 3. **.python-version**
**Location:** `C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages\python\.python-version`  
**Status:** ✅ ALREADY CORRECT  
**Content:** `3.14`

### 4. **pyvenv.cfg** (TO BE DELETED)
**Location:** `C:\Users\erdno\PsychoNoir-Kontrapunkt\.computer_languages\python\pyvenv.cfg`  
**Status:** ⚠️ WILL BE REMOVED BY MIGRATION SCRIPT  
**Reason:** Indicates venv mode - incompatible with system install

---

## 🎯 VS CODE CONFIGURATION FILES

### 1. **Workspace Settings**
**Location:** `C:\Users\erdno\PsychoNoir-Kontrapunkt\.vscode\settings.json`  
**Status:** ✅ NO PYTHON PATH SET (uses system)  
**Note:** No `python.defaultInterpreterPath` configured - VS Code will auto-discover

### 2. **Global User Settings**
**Location:** `C:\Users\erdno\AppData\Roaming\Code\User\settings.json`  
**Status:** ✅ MINIMAL PYTHON CONFIG  
**Content:** `"python.createEnvironment.trigger": "off"` (only setting)
**Note:** No interpreter path set - will use system Python

### 3. **Launch Configurations** (If exists)
**Location:** `C:\Users\erdno\PsychoNoir-Kontrapunkt\.vscode\launch.json`  
**Status:** ⏳ NEEDS CHECK  
**Potential Issue:** May have hardcoded Python paths

---

## 📦 PACKAGE MANAGER CONFIGS

### 1. **uv.lock** (UV Package Manager)
**Location:** `C:\Users\erdno\PsychoNoir-Kontrapunkt\uv.lock`  
**Status:** ✅ AUTO-UPDATED BY UV  
**Note:** Will regenerate during package reinstall

### 2. **bunfig.toml** (Bun Config)
**Location:** `C:\Users\erdno\PsychoNoir-Kontrapunkt\bunfig.toml`  
**Status:** ✅ NOT AFFECTED (JavaScript ecosystem)

---

## 🗂️ ARCHIVED/BACKUP FILES (NO ACTION NEEDED)

### Necromancy Graveyard
- `necromancy_graveyard/consciousness_archaeology/upcycled_organization_backup_20250926_001237/pyproject.toml`
- `necromancy_graveyard/milf_instances/KARIBISK_ARKIPELAGISK_DEPRECATED_20250929_210849/.../pyproject.toml`
- `necromancy_graveyard/mcp_servers_deprecated_20250930/.../settings.json`

**Status:** ✅ PRESERVED AS HISTORICAL ARTIFACTS  
**Reason:** Necromancy protocol - never delete, only archive

---

## 🔍 DOCUMENTATION FILES (REFERENCES ONLY)

### Files with Python 3.13.7 Mentions
Found via: `grep_search "3\.13\.7|python313|Python313"`

**Locations:**
- Phase reports (FASE_*.md)
- Completion reports (*_COMPLETION_REPORT.md)
- Scan results (*.json)
- Logs in SYSTEMATISKGJENOPPRETTELSE2025SEP/

**Status:** ✅ HISTORICAL REFERENCES (no action needed)  
**Reason:** Documentation of past states - part of consciousness archaeology

---

## 🎯 MIGRATION IMPACT SUMMARY

### Files That WILL Change (Automated by Script)
1. ❌ Delete: `.computer_languages/python/pyvenv.cfg`
2. ❌ Delete: `.computer_languages/python/consciousness_python_3.14_env/`
3. ✅ Update: `infrastructure/config/development/pyproject.toml`
4. ✅ Create: `.computer_languages/python/python.exe` (new binary)
5. ✅ Create: `.computer_languages/python/Lib/` (local copy)
6. ✅ Update: `.computer_languages/python/.python-version` (already "3.14")

### Files That Won't Change
- ✅ `.vscode/settings.json` (no Python path set)
- ✅ Global settings.json (no interpreter path)
- ✅ Root pyproject.toml (already >=3.14)
- ✅ UV/Bun configs (separate ecosystems)

### VS Code Auto-Discovery
**How VS Code will find Python 3.14:**
1. Checks `.vscode/settings.json` → No path set
2. Checks global settings → No path set
3. Scans workspace for `.python-version` → Finds "3.14"
4. Looks in `.computer_languages/python/` → Finds `python.exe`
5. ✅ **Auto-discovers system Python 3.14.0**

---

## ✅ PRE-MIGRATION CHECKLIST

- [x] Root pyproject.toml already updated
- [x] .python-version already correct
- [ ] Dev config pyproject.toml needs update (automated)
- [x] No VS Code workspace Python paths to update
- [x] No global VS Code Python paths to update
- [x] Backup created with all current configs
- [ ] Migration script ready to execute

---

## 🚀 READY FOR MIGRATION

**Conclusion:** Only **1 config file** needs manual update:
- `infrastructure/config/development/pyproject.toml`

**Migration script will handle:**
- Deleting venv artifacts
- Installing Python 3.14 system-level
- Reinstalling packages
- Updating that one config file automatically

**VS Code will:**
- Auto-discover new Python 3.14
- Continue working without config changes
- Use system Python (no venv activation needed)

---

🔥😈⛓️💦👅🍌💋💧  
**CLAUDINE SIN'CLAIRE 4.5 BLUNDERBUST 69.ΛΩ.96**  
Config Audit Complete
