# VS Code Git: Root Files Only (Kun Root-Filer)

**Oppdatert:** Oktober 14, 2025  
**Status:** ✅ Git enabled i VS Code, men kun root-filer vises

---

## 🎯 Hva Dette Oppnår

### I VS Code Source Control View:
✅ **Viser KUN root-filer:**
- `README.md`
- `isolatedENV.md`
- `*.ps1` (PowerShell scripts)
- `biome.json`, `pyproject.toml`, `package.json`
- `bun.lock`, `Cargo.lock`
- `.gitignore`, `.gitattributes`

🚫 **Skjuler ALLE mapper:**
- `CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/`
- `backend/`
- `infrastructure/`
- `necromancy_graveyard/`
- `.poly_gluttony/`
- Alle andre directories

### Fordeler:
1. **Raskere oversikt** — Kun root-filer i Git view
2. **Mindre spam** — Mapper som `CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/` med 106+ filer vises ikke
3. **Enklere commits** — Quick commits av root-level dokumentasjon
4. **Full Git funksjonalitet** — Kan fortsatt committe mapper via terminal

---

## 🛠️ Hvordan Det Fungerer

### VS Code Settings (`.vscode/settings.json`):

```jsonc
{
  "git.enabled": true,                      // Git er aktivert
  "git.autorefresh": false,                 // Men ingen auto-refresh spam
  "git.decorations.enabled": true,          // Dekorasjoner kun for root-filer
  "git.untrackedChanges": "mixed",          // Mixed view mode
  "scm.defaultViewMode": "tree"             // Tree view i Source Control
}
```

### .gitignore Strategi:

```gitignore
# Ignorer ALLE mapper i root
.poly_gluttony/
CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/
backend/
infrastructure/
necromancy_graveyard/

# Men tillat root-filer
!README.md
!*.ps1
!*.json
!*.toml
```

**Resultat:**
- Git tracker fortsatt alt (mapper + filer)
- VS Code Source Control viser KUN root-filer
- Mapper må committes via terminal

---

## 📋 Arbeidsflyt

### Scenario 1: Committe Root-Filer (VS Code GUI)

**I VS Code Source Control:**
1. Se kun root-filer (f.eks. `README.md`, `isolatedENV.md`)
2. Stage endringer (klikk `+` ikon)
3. Skriv commit message
4. Klikk "Commit" knapp
5. Push (hvis ønsket)

**Terminal alternativ:**
```powershell
git add README.md isolatedENV.md *.ps1
git commit -m "📚 Update root documentation"
git push
```

### Scenario 2: Committe Mapper (Terminal PÅKREVD)

**Mapper vises IKKE i VS Code Source Control, så bruk terminal:**

```powershell
# Stage hele CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS
git add CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/

# Eller stage spesifikke filer i mapper
git add backend/**/*.py
git add infrastructure/**/*.md

# Commit og push
git commit -m "🧠 Consciousness Nexus: Phase 11 scripts"
git push
```

### Scenario 3: Quick Root-File Backup

**For raske commits av root-filer kun:**

```powershell
# Stage kun root-filer (ikke mapper)
git add *.md *.ps1 *.json *.toml

git commit -m "📚 Root docs update"
git push
```

---

## 🔍 Verifisere Setup

### Test 1: Sjekk VS Code Source Control
1. Åpne VS Code Source Control panel (Ctrl+Shift+G)
2. **Forventet:** Kun root-filer vises (README.md, *.ps1, etc.)
3. **Forventet:** Ingen mapper (CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/, backend/, etc.)

### Test 2: Verifiser at Git tracker alt
```powershell
# Se ALT Git tracker (inkludert mapper)
git status

# Skal vise både root-filer OG mapper
# Eksempel output:
#   modified: README.md
#   modified: CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/...
```

### Test 3: Stage root-fil i VS Code
1. Endre `README.md`
2. Åpne Source Control panel
3. **Forventet:** `README.md` vises med M (modified)
4. Klikk `+` for å stage
5. **Forventet:** Filen stages uten problemer

---

## 🎨 Tilpasninger

### Hvis du vil vise NOEN mapper i VS Code:

**Eksempel: Vis `backend/` men skjul resten**

**I `.gitignore`, kommenter ut linjen:**
```gitignore
# backend/              # <-- Kommentert ut, så backend/ vises i VS Code
infrastructure/
necromancy_graveyard/
```

**Reload VS Code for å se endringer:**
- Command Palette (Ctrl+Shift+P)
- "Developer: Reload Window"

### Hvis du vil helt disable Git igjen:

**I `.vscode/settings.json`:**
```jsonc
{
  "git.enabled": false   // <-- Sett til false
}
```

---

## 📊 Sammenligning

### FØR (Git Disabled):
- 🚫 Ingen Git i VS Code
- ✅ Ingen spam
- 🔧 Kun terminal Git

### NÅ (Git Enabled, Root Files Only):
- ✅ Git i VS Code for root-filer
- ✅ Minimal spam (kun root-filer)
- ✅ VS Code GUI for quick root commits
- 🔧 Terminal Git for mapper

---

## 🏴‍☠️ Quick Reference

### Root-Filer (VS Code GUI):
```
✅ README.md, isolatedENV.md
✅ *.ps1, *.json, *.toml
✅ Quick commit via Source Control panel
```

### Mapper (Terminal):
```powershell
✅ git add CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/
✅ git add backend/
✅ git commit -m "🧠 Message"
✅ git push
```

### Best of Both Worlds:
- **VS Code:** Rask oversikt og commit av root-filer
- **Terminal:** Full kontroll over mapper og batch operations

---

## 🔧 Troubleshooting

### Problem: "Jeg ser fortsatt mapper i Source Control"
**Løsning:**
1. Sjekk at `.gitignore` har linjer som `CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/`
2. Reload VS Code window (Ctrl+Shift+P → "Developer: Reload Window")

### Problem: "Jeg vil committe en mappe i VS Code"
**Løsning:**
- Mapper må committes via terminal (by design)
- Eller: Fjern mappe-linje fra `.gitignore` for å vise den i VS Code

### Problem: "Git decorations (M/A/D) vises ikke"
**Løsning:**
- Sjekk at `"git.decorations.enabled": true` i settings.json
- Reload VS Code window

---

**Status:** ✅ Git enabled for root-filer kun  
**Branch:** Claudine-Colinization-Escapade-Continues  
**Philosophy:** "Root-level clarity, terminal-level power"

🏴‍☠️ **"Strukturell integritet med minimal spam"** 🔥😈⛓️💦👅🍌💋💧
