# Portable Stack: Skeleton and Headless MSYS2

This folder contains small, no-admin utilities to:
- Create the skeleton directory layout only (no installers, no GUI)
- Install MSYS2 headlessly (no GUI), then optionally the UCRT64 toolchain
- Consolidate an existing hub layout (detect/remove redundant files)

## 1) Create skeleton only

Use this when you want the hub layout without installing anything yet.

```powershell
# From repo root
pwsh -File .\tools\portable_stack\create_skeleton.ps1

# Or specify a custom hub path
pwsh -File .\tools\portable_stack\create_skeleton.ps1 -HubRoot "C:\\Users\\erdno\\PsychoNoir-Kontrapunkt\\.scripting_coding_programming_languages"
```

Minimal skeleton created:
- msys2\
- js_ts\ (subfolders created on demand)
- python\, python\Scripts\
- rust\cargo\bin\, rust\rustup\
- ruby\bin\
- linters\

## 2) Install MSYS2 headlessly

Download MSYS2 base archive (Manual install) from https://www.msys2.org/ → `msys2-base-x86_64-YYYYMMDD.tar.xz`.

```powershell
# Extract and initialize MSYS2 without GUI
pwsh -File .\tools\portable_stack\install_msys2_headless.ps1 -ArchivePath "C:\\path\\to\\msys2-base-x86_64-20250830.tar.xz"

# Optionally also install UCRT64 toolchain headlessly
pwsh -File .\tools\portable_stack\install_msys2_headless.ps1 -ArchivePath "C:\\path\\to\\msys2-base-x86_64-20250830.tar.xz" -InitToolchain
```

This performs:
- Extracts archive to a temp folder and syncs contents into `<hub>\msys2`
- Initializes pacman keyring and runs `pacman -Syu --noconfirm`
- If `-InitToolchain` is set: installs `base-devel` and `mingw-w64-ucrt-x86_64-toolchain`

## 3) Consolidate an existing hub layout

Use this to detect (default) or remove (`-Apply`) redundant MSYS2 installer leftovers and duplicate top-level directories.

```powershell
# Dry-run (report only)
pwsh -File .\tools\portable_stack\consolidate_hub_layout.ps1

# Apply removals with backup report
pwsh -File .\tools\portable_stack\consolidate_hub_layout.ps1 -Apply -Backup
```

The script flags and (optionally) removes examples like:
- Top-level `ucrt64/`, `mingw64/`, `usr/`, etc. that should be inside `msys2/`
- Installer artifacts at hub root (`msys2.exe`, `uninstall.exe`, `components.xml`, etc.)

## Recommended ladder (no surprises)
1. Run skeleton script → review/adjust layout (no installs)
2. Headless MSYS2 install (no GUI) → optionally UCRT toolchain
3. Then install languages headlessly (Python embeddable, Bun zip, Rust via rustup, Ruby via pacman)
4. Verify in VS Code integrated terminal (already wired in `.vscode/settings.json`)
