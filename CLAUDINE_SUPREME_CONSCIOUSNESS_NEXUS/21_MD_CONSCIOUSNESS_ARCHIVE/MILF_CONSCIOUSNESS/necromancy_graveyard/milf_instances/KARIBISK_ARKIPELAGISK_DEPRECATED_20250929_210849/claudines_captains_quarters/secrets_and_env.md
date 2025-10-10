# Secrets and environment configuration

This repo avoids hard-coding secrets. Use a local `.env` (ignored by git) and/or PowerShell user environment variables.

Recommended setup (Windows + PowerShell)
- Create a `.env` in the repo root by copying `.env.example` and filling values. This file is git-ignored and will be loaded by Bun automatically.
- Alternatively, set persistent user environment variables so you don’t need a `.env`:

## Option A — per-repo `.env` (quick and local)
1. Copy the template:
   - `Copy-Item .env.example .env`
2. Edit `.env` and paste values (never commit this file).

## Option B — persistent user env vars
Use PowerShell to set variables for your Windows user profile so they persist across sessions:

```powershell
# Set (persists after restart)
[System.Environment]::SetEnvironmentVariable('SENTRY_AUTH_TOKEN','<paste token here>','User')

# Verify in current session
$env:SENTRY_AUTH_TOKEN
```

To remove later:
```powershell
[System.Environment]::SetEnvironmentVariable('SENTRY_AUTH_TOKEN',$null,'User')
```

Notes
- The orchestrator and current tools do not require Sentry or Context7 now. If you still want them available for future tooling, store them via Option A or B; the code won’t break without them.
- Keep `.env` out of git (see `.gitignore`). Share only `.env.example`.
