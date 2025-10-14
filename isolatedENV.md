# Isolated Development Environment (Workspace‑Scoped)

This repository is wired to use a fully isolated, workspace‑scoped toolchain under `.poly_gluttony`. Nothing here requires global PATH edits.

## Overview

**Philosophy:** "Isolation Without Compromise"  
All development tools are self-contained within `.poly_gluttony`, providing a reproducible environment that doesn't pollute system PATH or registry. This enables:
- Multi-language development (Python, JavaScript/TypeScript, Rust, C/C++, Ruby)
- Version pinning per project
- Zero interference with system installations
- Portable across machines (copy `.poly_gluttony` directory)

## Tool Inventory

| Tool | Version | Purpose | Path |
|------|---------|---------|------|
| **UV** | 0.9.2 | Python toolchain manager | `.poly_gluttony\uv\bin\uv.exe` |
| **UV CPython** | 3.14.0 | UV-managed Python runtime | `.poly_gluttony\uv_python\cpython-3.14.0-windows-x86_64-none\python.exe` |
| **Portable Python** | 3.14.0 | Standalone Python (editor/debug) | `.poly_gluttony\python\python.exe` |
| **Bun** | 1.3.0+ | JavaScript runtime & toolchain | `.poly_gluttony\bun\bin\bun.exe` |
| **Biome** | 2.2.5 | JS/TS linter & formatter | (via Bun) |
| **Ruby** | 3.4.7 | Ruby interpreter | `.poly_gluttony\ruby\bin\ruby.exe` |
| **Rust** | latest | Rust toolchain (cargo, rustc) | `.poly_gluttony\rust\bin\` |
| **MSYS2** | ucrt64 | Unix tools & GCC toolchain | `.poly_gluttony\msys64\ucrt64\bin\` |
| **Ruff** | latest | Fast Python linter | `.poly_gluttony\tools\bin\ruff.exe` |

## Quick Paths (Absolute)

- **uv toolchain** (still a work in progress):
  - uv: `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\uv\bin\uv.exe`
  - uvw: `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\uv\bin\uvw.exe`
  - uvx: `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\uv\bin\uvx.exe`
- **uv CPython** (used by `uv run`):
  - `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\uv_python\cpython-3.14.0-windows-x86_64-none\python.exe`
- **Portable Python 3.14** (non‑uv):
  - `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\python\python.exe`
- **Bun**:
  - `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\bun\bin\bun.exe`
- **Ruby**:
  - `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\ruby\bin\ruby.exe`
- **MSYS2** (ucrt64 toolchain):
  - root: `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\msys64`
  - bin:  `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\msys64\ucrt64\bin`
- **Rust toolchain** (isolated):
  - bin:  `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\rust\bin` (cargo, rustc, rustup)
- **Ruff** (local binary):
  - `C:\Users\erdno\PsychoNoir-Kontrapunkt\.poly_gluttony\tools\bin\ruff.exe`

## Directory Structure

```
PsychoNoir-Kontrapunkt/
├── .poly_gluttony/              # Isolated toolchain root
│   ├── uv/                      # UV toolchain manager
│   │   └── bin/                 # uv.exe, uvx.exe, uvw.exe
│   ├── uv_python/               # UV-managed CPython (3.14.0)
│   │   └── cpython-3.14.0-windows-x86_64-none/
│   │       └── python.exe       # Used implicitly by `uv run`
│   ├── python/                  # Portable Python (3.14.0)
│   │   ├── python.exe           # VS Code editor/debugger
│   │   └── Scripts/             # pip, etc.
│   ├── bun/                     # Bun JavaScript runtime
│   │   └── bin/bun.exe
│   ├── ruby/                    # Ruby interpreter
│   │   └── bin/ruby.exe
│   ├── rust/                    # Rust toolchain
│   │   └── bin/                 # cargo, rustc, rustup
│   ├── msys64/                  # MSYS2 Unix environment
│   │   ├── ucrt64/bin/          # GCC, make, bash, etc.
│   │   └── usr/bin/             # Core Unix tools
│   ├── tools/                   # Additional binaries
│   │   └── bin/ruff.exe
│   └── activate_polyglot.ps1    # Environment activation script
├── .vscode/
│   └── settings.json            # Workspace-scoped configuration
└── ...
```

## VS Code integration (key settings)

File: `.vscode/settings.json`

- Terminal env PATH (excerpt — order matters):
  - `...;${workspaceFolder}\\.poly_gluttony\\msys64\\ucrt64\\bin;${workspaceFolder}\\.poly_gluttony\\msys64\\usr\\bin;${workspaceFolder}\\.poly_gluttony\\python;${workspaceFolder}\\.poly_gluttony\\python\\Scripts;${workspaceFolder}\\.poly_gluttony\\bun\\bin;${workspaceFolder}\\.poly_gluttony\\rust\\bin;${workspaceFolder}\\.poly_gluttony\\uv\\bin;${workspaceFolder}\\.poly_gluttony\\tools\\bin;${env:PATH}`
- Python interpreter for editor/debug (keeps non‑uv as default):
  - `"python.defaultInterpreterPath": "${workspaceFolder}\\.poly_gluttony\\python\\python.exe"`
- Ruff integration:
  - `"ruff.path": ["${workspaceFolder}\\.poly_gluttony\\tools\\bin\\ruff.exe"]`
- Integrated terminal profile runs the activator:
  - PowerShell profile uses: `-NoExit -ExecutionPolicy Bypass -File ${workspaceFolder}\\.poly_gluttony\\activate_polyglot.ps1`

Tip: Open a new Integrated Terminal to inherit these settings (existing terminals don’t reload PATH automatically). If needed: Command Palette → “Developer: Reload Window”.

## Activation and usage

- New terminal: the activation script runs via the profile. If you need to apply manually in a session:
  - PowerShell: `. .\.poly_gluttony\activate_polyglot.ps1`

- Verify tools:
  - `uv -V`
  - `uv run python -V`   (uv’s CPython)
  - `python -V`          (portable Python)
  - `uvx ruff -V` or `ruff --version`

## Recommended workflow (separation of concerns)

- Keep `uv` on PATH; keep the uv CPython directory off PATH.
  - Plain `python` → portable Python (editor/debug consistency)
  - `uv run ...`       → uv CPython runtime
- If you prefer the editor/debugger to use uv’s CPython, set:
  - `"python.defaultInterpreterPath": "${workspaceFolder}\\.poly_gluttony\\uv_python\\cpython-3.14.0-windows-x86_64-none\\python.exe"`
  - Do not add that folder to PATH unless you want it to replace `python` globally in the terminal.

## PYTHONHOME note

- If `PYTHONHOME` is set for the portable Python, `uv` may complain. Options:
  - Easiest: remove `PYTHONHOME` from `terminal.integrated.env.windows`.
  - Or call uv via the sanitized wrapper (clears PYTHONHOME for the call):
    - `uvs` (defined by the activation scripts) → behaves like `uv`, without PYTHONHOME interference.

## Troubleshooting

- `uv` not found:
  - Open a new terminal or reload the VS Code window; the PATH from settings only applies to new sessions.
  - Absolute check: `\.poly_gluttony\uv\bin\uv.exe -V`
  - Dot‑source activator: `. .\.poly_gluttony\activate_polyglot.ps1`
- PATH shadowing (MSYS2 vs Windows tools):
  - Activation defines Windows‑native aliases where necessary to avoid MSYS2 shadowing.
- Rustup/ruff not resolving:
  - Ensure `${workspaceFolder}\\.poly_gluttony\\rust\\bin` and `${workspaceFolder}\\.poly_gluttony\\tools\\bin` precede system entries.

## Quick checklist

- New terminal → `uv -V` shows version (0.9.2)
- `uv run python -V` reports 3.14.0 (uv CPython)
- `python -V` reports 3.14.x from portable Python
- `bun -v` shows Bun version (1.3.0+)
- `cargo --version` shows Rust toolchain
- `ruff --version` works (local binary)
- Optional: switch editor/debug interpreter to uv CPython if you want full alignment with `uv run`

## Common Workflows

### Python: UV vs Portable

**UV workflow (fast, isolated):**
```powershell
uv run script.py              # Execute with UV's Python
uv run python -m module       # Run Python module
uvx tool                      # Run tool without install
```

**Portable Python workflow (editor consistency):**
```powershell
python script.py              # Direct execution
python -m pytest              # Run tests
pip install package           # Install to portable env
```

### JavaScript/TypeScript with Bun

```powershell
bun run script.ts             # Execute TypeScript
bun install                   # Install dependencies
bunx biome check .            # Lint/format
```

### Rust Development

```powershell
cargo build                   # Build project
cargo run                     # Run project
cargo test                    # Run tests
```

### C/C++ with MSYS2

```powershell
gcc program.c -o program.exe  # Compile
make                          # Build with Makefile
bash script.sh                # Run shell script
```

## Advanced: PYTHONHOME & PATH Mitigations

### uvs Wrapper (sanitized UV)

If PYTHONHOME conflicts with `uv run`, use the `uvs` wrapper:
```powershell
uvs run script.py             # Clears PYTHONHOME before calling uv
```

### win-tools Aliases

The activation script provides Windows-native aliases to avoid MSYS2 shadowing:
- `win-python` → Portable Python (`.poly_gluttony\python\python.exe`)
- `win-bun` → Bun (`.poly_gluttony\bun\bin\bun.exe`)

### Health Check

Run comprehensive system status:
```powershell
.\system_status_report.ps1
```

## Additional Resources

- **Polyglot Fortress README:** `claudine_polyglot_fortress_readme.md`
- **Setup Documentation:** Root-level setup scripts and guides
- **CLAUDINE Supreme Nexus:** `CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/` (advanced tools)

---

**Philosophy:** "Isolation Without Compromise"

This document reflects the current isolated setup for this workspace on Windows (PowerShell).