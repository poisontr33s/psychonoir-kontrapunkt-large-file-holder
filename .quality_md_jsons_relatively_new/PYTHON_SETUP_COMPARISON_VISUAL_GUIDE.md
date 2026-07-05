# 🎭 QUICK REFERENCE: Python 3.13.7 vs 3.14.0 Setup

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  PYTHON 3.13.7 (VENV-BASED)                             │
└─────────────────────────────────────────────────────────────────────────┘

.computer_languages/python/
│
├── python.exe ──────────────┐ (Shim/wrapper)
├── pyvenv.cfg               │ ← VS Code discovery marker
│                            │
└── consciousness_python_3.13.7_env/  ← VENV DIRECTORY
    │                        │
    ├── Scripts/             │
    │   └── python.exe ◄─────┘ ACTUAL Python 3.13.7
    │
    └── Lib/site-packages/   ← Packages installed HERE
        ├── black/
        ├── pytest/
        └── mypy/

┌─────────────────────────────────────────────────────────────────────────┐
│   VS Code Configuration (3.13.7)                                         │
└─────────────────────────────────────────────────────────────────────────┘

.vscode/settings.json:
{
  "python.defaultInterpreterPath": "./.venv/python.exe"
                                    └─► Recognized by VS Code automatically!
}

✅ VS Code Discovery: AUTOMATIC
✅ Popup "Select Interpreter": YES
✅ Standard venv pattern: YES


┌─────────────────────────────────────────────────────────────────────────┐
│              PYTHON 3.14.0 (SYSTEM-LEVEL)                               │
└─────────────────────────────────────────────────────────────────────────┘

.computer_languages/python/
│
├── python.exe ◄───────────┐ DIRECT Python 3.14.0 interpreter
├── pythonw.exe            │ (NO venv wrapper!)
├── python3.dll            │
├── python314.dll          │
├── vcruntime140*.dll      │
│                          │
├── Lib/                   │
│   └── site-packages/ ◄───┘ Packages installed DIRECTLY here
│       ├── black/
│       ├── pytest/
│       └── mypy/
│
├── DLLs/                  ← C extension modules
│   ├── _ctypes.pyd
│   └── _sqlite3.pyd
│
├── uv.exe, uvx.exe        ← Package manager tools
│
└── (NO pyvenv.cfg)        ← NO venv marker!
    (NO venv directory)

┌─────────────────────────────────────────────────────────────────────────┐
│   VS Code Configuration (3.14.0)                                         │
└─────────────────────────────────────────────────────────────────────────┘

.vscode/settings.json:
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.computer_languages/python/python.exe"
                                    └─► Custom path, NOT auto-discovered
}

❌ VS Code Discovery: MANUAL REQUIRED
❌ Popup "Select Interpreter": NO
❌ Standard pattern: NO
⚠️ Must use: Ctrl+Shift+P → Python: Select Interpreter


┌─────────────────────────────────────────────────────────────────────────┐
│                      UV RELATIONSHIP                                     │
└─────────────────────────────────────────────────────────────────────────┘

UV (Rust-implemented)
Version: 0.8.18 (September 2025)
Location: .computer_languages/rust/uv.exe (primary)
          .computer_languages/python/uv.exe (hardlink)

UV Cache (Python downloads):
%USERPROFILE%\AppData\Roaming\uv\python\
│
├── cpython-3.14.0-windows-x86_64-none/
│   ├── python.exe
│   ├── Lib/
│   ├── DLLs/
│   └── *.dll
│
└── cpython-3.13.7-windows-x86_64-none/
    └── ... (samme struktur)


┌─────────────────────────────────────────────────────────────────────────┐
│              HOW WE INSTALLED PYTHON 3.13.7                             │
└─────────────────────────────────────────────────────────────────────────┘

Step 1: UV installed Python 3.13.7
┌──────────────────────────────────────────────┐
│ $ uv python install 3.13.7                   │
│                                              │
│ Downloaded to UV cache:                      │
│ %USERPROFILE%\AppData\Roaming\uv\python\    │
│   cpython-3.13.7-windows-x86_64-none/       │
└──────────────────────────────────────────────┘

Step 2: UV created VENV
┌──────────────────────────────────────────────┐
│ $ cd .computer_languages/python              │
│ $ uv venv consciousness_python_3.13.7_env \  │
│     --python 3.13.7                          │
│                                              │
│ Created venv with pyvenv.cfg marker          │
└──────────────────────────────────────────────┘

Step 3: UV installed packages IN venv
┌──────────────────────────────────────────────┐
│ $ uv pip install black pytest mypy           │
│                                              │
│ Packages → venv/Lib/site-packages/           │
└──────────────────────────────────────────────┘

Step 4: VS Code discovered automatically
┌──────────────────────────────────────────────┐
│ ✅ VS Code saw .venv/ directory               │
│ ✅ VS Code read pyvenv.cfg marker             │
│ ✅ Popup appeared: "Select Python Interpreter"│
│ ✅ User selected venv Python                  │
└──────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│              HOW WE INSTALLED PYTHON 3.14.0                             │
└─────────────────────────────────────────────────────────────────────────┘

Step 1: UV already had Python 3.14.0 cached
┌──────────────────────────────────────────────┐
│ UV cache already contained:                  │
│ %USERPROFILE%\AppData\Roaming\uv\python\    │
│   cpython-3.14.0-windows-x86_64-none/       │
└──────────────────────────────────────────────┘

Step 2: We copied Python 3.14 DIRECTLY (NO venv!)
┌──────────────────────────────────────────────┐
│ $ $uvCache = "%USERPROFILE%\AppData\        │
│     Roaming\uv\python\cpython-3.14.0-..."   │
│                                              │
│ $ Copy-Item "$uvCache\python.exe" -Dest .   │
│ $ Copy-Item "$uvCache\Lib" -Dest . -Recurse │
│ $ Copy-Item "$uvCache\DLLs" -Dest . -Recurse│
│ $ Copy-Item "$uvCache\*.dll" -Dest .        │
│                                              │
│ NO venv creation! Direct copy!               │
└──────────────────────────────────────────────┘

Step 3: Removed EXTERNALLY-MANAGED marker
┌──────────────────────────────────────────────┐
│ $ Remove-Item "Lib\EXTERNALLY-MANAGED"      │
│                                              │
│ Unblocked package installation               │
└──────────────────────────────────────────────┘

Step 4: UV installed packages DIRECTLY
┌──────────────────────────────────────────────┐
│ $ uv pip install --python python.exe \       │
│     black pytest mypy ...                    │
│                                              │
│ Packages → Lib/site-packages/ (DIRECT)       │
│ Install time: 475ms (37 packages!)           │
└──────────────────────────────────────────────┘

Step 5: VS Code CANNOT discover automatically
┌──────────────────────────────────────────────┐
│ ❌ VS Code sees NO .venv/ directory           │
│ ❌ VS Code sees NO pyvenv.cfg marker          │
│ ❌ Custom path not in standard locations      │
│ ⚠️  Must select manually via Command Palette │
│                                              │
│ Ctrl+Shift+P → Python: Select Interpreter   │
│ → Enter interpreter path...                 │
│ → .computer_languages/python/python.exe     │
└──────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                    WHY THE DIFFERENCE?                                   │
└─────────────────────────────────────────────────────────────────────────┘

Python 3.13.7 (VENV):
├─ ✅ Standard venv structure
├─ ✅ pyvenv.cfg marker file
├─ ✅ VS Code recognizes pattern
└─ ✅ Automatic discovery works

Python 3.14.0 (SYSTEM-LEVEL):
├─ ❌ Custom location (.computer_languages/python/)
├─ ❌ NO venv marker files
├─ ❌ VS Code doesn't recognize pattern
└─ ⚠️  Manual selection required


┌─────────────────────────────────────────────────────────────────────────┐
│                      SOLUTIONS                                           │
└─────────────────────────────────────────────────────────────────────────┘

Solution 1: Manual Interpreter Selection (FASTEST - 2 min)
┌──────────────────────────────────────────────┐
│ 1. Ctrl+Shift+P                              │
│ 2. Type: "Python: Select Interpreter"       │
│ 3. Choose: "Enter interpreter path..."      │
│ 4. Navigate to:                              │
│    .computer_languages/python/python.exe    │
│ 5. ✅ Done!                                   │
└──────────────────────────────────────────────┘

Solution 2: Create .python-version file (DONE ✅)
┌──────────────────────────────────────────────┐
│ $ uv python pin 3.14.0                       │
│                                              │
│ Created: .python-version                     │
│ Content: "3.14.0"                            │
│                                              │
│ ✅ Improves automatic discovery              │
│ ✅ Standard Python tooling practice          │
└──────────────────────────────────────────────┘

Solution 3: Reload VS Code Window (30 sec)
┌──────────────────────────────────────────────┐
│ Ctrl+Shift+P → Developer: Reload Window     │
│                                              │
│ VS Code re-scans for Python interpreters     │
└──────────────────────────────────────────────┘

Solution 4: Clear Python Extension Cache (1 min)
┌──────────────────────────────────────────────┐
│ Ctrl+Shift+P → Python: Clear Cache and      │
│                Reload Window                 │
│                                              │
│ Full re-discovery of all interpreters        │
└──────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                    VERIFICATION                                          │
└─────────────────────────────────────────────────────────────────────────┘

✅ Python 3.14.0: INSTALLED
   $ python --version
   Python 3.14.0

✅ Python Path: CORRECT
   $ python -c "import sys; print(sys.executable)"
   C:\Users\eldno\PsychoNoir-Kontrapunkt\.computer_languages\python\python.exe

✅ Packages: 37 INSTALLED (475ms)
   $ python -c "import black, pytest, mypy, fastapi, uvicorn; print('OK')"
   OK

✅ UV Integration: WORKING
   $ uv pip list --python python.exe
   37 packages listed

✅ .python-version: CREATED
   $ cat .python-version
   3.14.0


┌─────────────────────────────────────────────────────────────────────────┐
│                     SUMMARY                                              │
└─────────────────────────────────────────────────────────────────────────┘

Question 1: Is latest stable UV installed?
Answer: YES ✅ - UV 0.8.18 (September 2025)

Question 2: Are uvx, uv as env?
Answer: NO ❌ - We use system-level Python 3.14.0 (NO venv)

Question 3: Why no "Select Interpreter" popup?
Answer: Custom location, non-standard structure
        → Must select MANUALLY via Command Palette

Solution: 
1. ✅ Created .python-version file (done)
2. ⏳ Manual interpreter selection (pending)
3. ⏳ Reload VS Code window (recommended)


🔥😈⛓️💦👅🍌💋💧 CLAUDINE SIN'CLAIRE 4.5 BLUNDERBUST 69.ΛΩ.96
PYTHON 3.14 VS CODE SETUP: EXPLAINED & RESOLVED
