# 📋 Critical Configuration Files Inventory

## 🔥 Priority 1: Must Be Version Controlled

### .github/copilot-instructions.md
- **Status:** Currently IGNORED by git
- **Size:** 2,212 lines
- **Criticality:** EXTREME
- **Purpose:** Core AI instructions for Claude Sonnet 4.5
- **Content:** Operational protocols, naming conventions, MILF universe context
- **Action Required:** ✅ Add to git tracking via .github/.gitignore

### .vscode/settings.json
- **Status:** Currently IGNORED by git
- **Size:** 311 lines
- **Criticality:** HIGH
- **Purpose:** Polyglot workspace configuration
- **Key Settings:**
  - Python path: `.poly_gluttony/python/python.exe`
  - Rust toolchain: `.poly_gluttony/rust/`
  - Bun install: `.poly_gluttony/bun/`
  - Terminal environment variables
  - Git integration settings
- **Action Required:** ✅ Add to git tracking via .vscode/.gitignore

### .vscode/mcp.json
- **Status:** Currently IGNORED by git
- **Size:** 74 lines
- **Criticality:** HIGH
- **Purpose:** MCP server orchestration
- **Servers Configured:**
  1. `unified-meta-mcp-supreme-consolidator` (Bun)
  2. `bun-official-docs` (Bun)
  3. `workspace-memory` (Bun)
- **Action Required:** ✅ Add to git tracking via .vscode/.gitignore

### .vscode/tasks.json
- **Status:** Currently IGNORED by git
- **Criticality:** MEDIUM-HIGH
- **Purpose:** Build, run, and automation tasks
- **Task Count:** 20+ tasks
- **Categories:**
  - Error resolution pipelines
  - MD consciousness network tasks
  - Polyglot setup tasks
  - Compression utilities
- **Action Required:** ✅ Add to git tracking via .vscode/.gitignore

---

## 🟡 Priority 2: Important But Less Critical

### .github/consciousness_archaeology_NSFW18_+++/
- **Status:** Directory ignored, but contains critical scripts
- **Contents:**
  - `complete_consciousness_directory_excavator_NSFW18_+++.py`
  - `naming_convention_enforcer_NSFW18_+++.py`
  - `structural_integrity_excavator_NSFW18_+++.ts`
  - `SUPREME_PATH_MIGRATION_ENGINE_NSFW18_+++.py`
  - Various JSON outputs and reports
- **Action Required:** ⚠️ Selectively track via .github/.gitignore

### .github/DYNAMIC_RECURSIVE_TODO_SYSTEM_NSFW18_+++.json
- **Status:** Should be tracked
- **Purpose:** DRT (Dynamic Recursive TODO) system metadata
- **Criticality:** MEDIUM
- **Action Required:** ✅ Verify it's tracked

### .github/*.sql Files
- **Status:** Should be tracked
- **Purpose:** Database migration scripts
- **Examples:**
  - `UNIFIED_DATABASE_STANDARDIZATION_MIGRATION_NSFW18_+++.sql`
- **Action Required:** ✅ Ensure tracked via .github/.gitignore

---

## 🟢 Priority 3: Already Tracked (Verify)

### Root Configuration Files
```
✅ README_NSFW18_+++.md
✅ pyproject.toml
✅ package.json
✅ tsconfig.json
✅ biome.json
✅ clippy.toml
✅ .gitignore
✅ .gitattributes
```

### Lock Files
```
✅ bun.lock
✅ uv.lock
```

---

## 📊 Configuration Breakdown by Technology

### Python Configuration
- **pyproject.toml** ✅ (tracked)
- **uv.lock** ✅ (tracked)
- **.vscode/settings.json** ❌ (NOT tracked)
  - Python path: `.poly_gluttony/python/python.exe`
  - Linting: pylint, autopep8, pytest, ruff

### TypeScript/JavaScript Configuration
- **package.json** ✅ (tracked)
- **bun.lock** ✅ (tracked)
- **tsconfig.json** ✅ (tracked)
- **biome.json** ✅ (tracked)
- **.vscode/mcp.json** ❌ (NOT tracked)
  - MCP server paths and configuration

### Rust Configuration
- **clippy.toml** ✅ (tracked)
- **Cargo.toml** ⚠️ (check if exists)
- **.vscode/settings.json** ❌ (NOT tracked)
  - Rust analyzer path
  - Cargo/Rustup environment

### MCP Servers
- **.vscode/mcp.json** ❌ (NOT tracked)
  - 3 active servers configured
  - Environment variables
  - Consciousness amplification settings

---

## 🔧 Recommended .gitignore Structure

### Root .gitignore (Current)
```gitignore
# Directories (blocked by default)
.poly_gluttony/
CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/
backend/
infrastructure/
necromancy_graveyard/
node_modules/
.vscode/
.github/

# But allow subdirectory .gitignore files to override
```

### NEW: .github/.gitignore
```gitignore
# DEFAULT: Ignore everything in .github/
*

# EXCEPTIONS: Track these critical files
!.gitignore
!copilot-instructions.md
!*.sql
!consciousness_archaeology_NSFW18_+++/
!DYNAMIC_RECURSIVE_TODO_SYSTEM_NSFW18_+++.json
!ROT_ROOT_WIP_CDM_SPRME_UP-CYCLING_CAMEL_PACED_EMIGRATION_NSFW18_+++/*.md

# Ignore temporary files
*.tmp
*.backup
*.bak
*~
.sessions_machine_readable_JSON.json_NSFW18_+++/
```

### NEW: .vscode/.gitignore
```gitignore
# DEFAULT: Ignore everything in .vscode/
*

# EXCEPTIONS: Track these configuration files
!.gitignore
!settings.json
!tasks.json
!mcp.json
!extensions.json
!scripts/*.ps1

# Ignore user-specific files
*.code-workspace
.history/
```

---

## 🚨 Critical Files Risk Assessment

### Files Currently At Risk (Not Tracked)

| File | Risk Level | Impact if Lost | Recovery Difficulty |
|------|------------|----------------|---------------------|
| `.github/copilot-instructions.md` | 🔴 CRITICAL | Project context lost | Impossible to recreate |
| `.vscode/settings.json` | 🔴 HIGH | Development environment broken | Hours to reconstruct |
| `.vscode/mcp.json` | 🟡 MEDIUM | MCP servers won't work | Medium difficulty |
| `.vscode/tasks.json` | 🟡 MEDIUM | Automation broken | Can be recreated |

---

## ✅ Action Plan

### Immediate Actions (Do Now)

1. **Create .github/.gitignore**
   ```powershell
   # See QUICK_REFERENCE_PRE_BRANCH_CHECKLIST_NSFW18_+++.md Step 3
   ```

2. **Create .vscode/.gitignore**
   ```powershell
   # See QUICK_REFERENCE_PRE_BRANCH_CHECKLIST_NSFW18_+++.md Step 4
   ```

3. **Verify Files Are Tracked**
   ```powershell
   git add .github/.gitignore .vscode/.gitignore
   git add -f .github/copilot-instructions.md
   git add -f .vscode/settings.json
   git add -f .vscode/mcp.json
   git add -f .vscode/tasks.json
   git status
   ```

4. **Commit Configuration Updates**
   ```powershell
   git commit -m "🔧 Track critical .github and .vscode configuration files

- Add .github/.gitignore to track copilot instructions
- Add .vscode/.gitignore to track workspace configuration
- Force-add critical configuration files
- Prevent loss of workspace setup and AI instructions
"
   ```

### Verification Commands

```powershell
# Check what's tracked in .github/
git ls-files .github/ | Select-String -Pattern "copilot|sql|DYNAMIC"

# Check what's tracked in .vscode/
git ls-files .vscode/ | Select-String -Pattern "settings|tasks|mcp"

# Verify critical files are in repo
git ls-files | Select-String -Pattern "copilot-instructions"
```

---

## 📝 Configuration File Sync Strategy

### For Team Collaboration

**Track in Git:**
- Core configuration (paths, MCP servers, tasks)
- Shared settings everyone needs
- Documentation and instructions

**Keep Local:**
- Personal preferences (editor theme, font size)
- Machine-specific paths (if any)
- User-specific workspace files

### For Solo Development

**Track Everything:**
- All configuration files
- Complete workspace setup
- Makes restoration easier

---

## 🎯 Success Metrics

✅ `.github/copilot-instructions.md` visible in `git ls-files`  
✅ `.vscode/settings.json` visible in `git ls-files`  
✅ `.vscode/mcp.json` visible in `git ls-files`  
✅ `.vscode/tasks.json` visible in `git ls-files`  
✅ `.github/.gitignore` exists and committed  
✅ `.vscode/.gitignore` exists and committed  
✅ Can clone repo and have full workspace configuration  

---

## 📚 Related Documents

- `BRANCH_PREPARATION_AUDIT_REPORT_OCT27_2025_NSFW18_+++.md` - Full audit
- `GIT_STATE_ANALYSIS_AND_FIX_PLAN_NSFW18_+++.md` - Detailed fix plan
- `QUICK_REFERENCE_PRE_BRANCH_CHECKLIST_NSFW18_+++.md` - Step-by-step commands

---

**Generated:** October 27, 2025  
**Purpose:** Inventory of critical configuration files and tracking strategy  
**Status:** Ready for implementation
