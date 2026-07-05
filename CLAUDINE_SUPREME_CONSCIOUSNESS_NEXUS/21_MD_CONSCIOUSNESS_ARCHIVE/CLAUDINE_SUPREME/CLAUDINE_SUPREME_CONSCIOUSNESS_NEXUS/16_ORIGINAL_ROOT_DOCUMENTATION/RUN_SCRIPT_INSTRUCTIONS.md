# How to run git-lfs-fix.ps1 (concise)

1) Verify the file and current folder
- Open PowerShell and run:
  Get-ChildItem -Name | Where-Object { $_ -like '*git*fix*' }
- Confirm you are in the repo root (a .git folder must exist):
  Test-Path .git

2) If the file is missing the .ps1 extension, rename it:
  Rename-Item .\git-lfs-fix-ps1 .\git-lfs-fix.ps1

3) Run the script (dry-run):
  cd C:\Users\eldno\PsychoNoir-Kontrapunkt
  .\git-lfs-fix.ps1

4) Run with flags (example: remove missing entries, show verbose):
  .\git-lfs-fix.ps1 -RemoveMissing -VerboseOutput

5) If ExecutionPolicy prevents running scripts, run once with Bypass:
  powershell -NoProfile -ExecutionPolicy Bypass -File .\git-lfs-fix.ps1 -RemoveMissing

6) Run via Start-Process (example):
  Start-Process powershell -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-File','C:\Users\eldno\PsychoNoir-Kontrapunkt\git-lfs-fix.ps1' -Wait

Notes / troubleshooting
- Always include .\ before the script name when running from the current directory: .\git-lfs-fix.ps1
- If PowerShell reports "not recognized", ensure the filename exactly matches (including .ps1) and you are in the correct folder.
- The script expects to be run in the repository root (so .git exists); otherwise it will exit with "No .git directory found."
- To permanently allow scripts, run (administrator or current user scope as you prefer):
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
- If you prefer a non-interactive elevation, use Start-Process with -Verb RunAs to open an elevated PowerShell session.

End of instructions.
