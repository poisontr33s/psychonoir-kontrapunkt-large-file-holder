# 🔧 Git Publish Branch - Feilsøking

**Dato:** Oktober 14, 2025  
**Problem:** "Publish Branch" knapp virker ikke i VS Code  
**Branch:** Claudine-Colinization-Escapade-Continues

---

## 🎯 Problem Diagnose

### Symptomer:
- ✅ Git commit virker i VS Code
- ❌ "Publish Branch" knapp virker ikke
- ❌ Push feiler

### Årsak:
Branch har ikke remote tracking satt opp. Se output fra `git branch -vv`:

```
* Claudine-Colinization-Escapade-Continues  27da01c31  chore: Add comment...
  main                                      66d700f3b  [origin/main: ahead 4]
```

**Merk:** `Claudine-Colinization-Escapade-Continues` mangler `[origin/...]` tracking.

---

## 🔧 Løsning 1: Manual Push (Terminal)

### Steg 1: Sett opp remote tracking og push
```powershell
git push -u origin Claudine-Colinization-Escapade-Continues
```

**Forklaring:**
- `-u` = set upstream tracking
- `origin` = remote repository
- `Claudine-Colinization-Escapade-Continues` = branch name

### Mulige Feilmeldinger:

#### Feil 1: "Large files detected"
```
remote: error: GH001: Large files detected
```

**Løsning:** Repository bruker Git LFS (Large File Storage). Push skal håndtere dette automatisk.

#### Feil 2: "Pack exceeds maximum allowed size"
```
remote: error: pack exceeds maximum allowed size
```

**Løsning A:** Split commits i mindre batches
```powershell
# Push første N commits
git push -u origin Claudine-Colinization-Escapade-Continues --force-with-lease
```

**Løsning B:** Shallow push (hvis repo er veldig stort)
```powershell
# Push kun nyeste commit
git push -u origin Claudine-Colinization-Escapade-Continues --depth=1
```

#### Feil 3: "Authentication failed"
```
remote: Permission denied
```

**Løsning:** Sjekk GitHub credentials
```powershell
# Windows Credential Manager
cmdkey /list | Select-String "github"

# Eller re-authenticate
git credential-manager-core erase
# Neste push vil be om nye credentials
```

---

## 🔧 Løsning 2: VS Code Settings (Workaround)

Hvis push fortsatt feiler, kan du disable "Publish Branch" og bruke terminal:

### Oppdater `.vscode/settings.json`:
```jsonc
{
    "git.showActionButton": {
        "commit": true,
        "publish": false,    // Disable hvis det ikke virker
        "sync": false
    }
}
```

---

## 🚀 Løsning 3: Force Push (Hvis branch eksisterer på remote)

Hvis branch allerede eksisterer på GitHub men tracking er borte:

```powershell
# Sjekk om branch eksisterer på remote
git ls-remote --heads origin Claudine-Colinization-Escapade-Continues

# Hvis den eksisterer, sett opp tracking igjen
git branch --set-upstream-to=origin/Claudine-Colinization-Escapade-Continues

# Deretter push som normalt
git push
```

---

## 📊 Verify Fix

### Test 1: Sjekk Remote Tracking
```powershell
git branch -vv
```

**Forventet output:**
```
* Claudine-Colinization-Escapade-Continues  27da01c31  [origin/Claudine-Colinization-Escapade-Continues] chore: Add comment...
```

**Merk:** Nå skal du se `[origin/...]` tracking.

### Test 2: Test Push
```powershell
# Gjør en liten endring
Add-Content README.md "`n<!-- Test push -->"

# Commit
git add README.md
git commit -m "test: Verify push works"

# Push (skal virke uten -u nå)
git push
```

### Test 3: VS Code "Publish Branch"
```
1. Åpne Source Control (Ctrl+Shift+G)
2. Gjør en endring
3. Commit i VS Code
4. Klikk "Publish Branch" eller sync-ikon
5. Forventet: Push skal virke
```

---

## 🏴‍☠️ Alternative Workflow (Hvis Publish Branch fortsatt feiler)

### Workflow: Commit i VS Code, Push i Terminal

```powershell
# 1. Commit i VS Code GUI som normalt
#    (Ctrl+Shift+G → Stage → Commit)

# 2. Push i terminal
git push

# 3. Verifiser
git status
# Forventet: "Your branch is up to date with 'origin/...'"
```

**Fordel:** Full kontroll over push prosess.

---

## 🔍 Diagnostikk Kommandoer

### Sjekk Repository Status:
```powershell
# Branch tracking
git branch -vv

# Remote configuration
git remote -v

# Check if remote branch exists
git ls-remote --heads origin

# Pending commits
git log origin/main..HEAD --oneline

# Repository size
git count-objects -vH
```

### Sjekk GitHub LFS:
```powershell
# LFS status
git lfs status

# LFS tracked files
git lfs ls-files

# LFS push
git lfs push origin Claudine-Colinization-Escapade-Continues --all
```

---

## 📋 Quick Reference

### Successful Push Workflow:
```powershell
# 1. Set up tracking (første gang)
git push -u origin Claudine-Colinization-Escapade-Continues

# 2. Verify tracking
git branch -vv

# 3. Future pushes (tracking allerede satt opp)
git push
```

### VS Code Workflow:
```
1. Commit i VS Code (Ctrl+Shift+G)
2. Push i terminal: git push
3. Eller bruk sync-ikon (hvis tracking virker)
```

---

## 🆘 Hvis Push Fortsatt Feiler

### Option 1: Create New Branch
```powershell
# Opprett ny branch med kortere navn
git checkout -b claudine-escape

# Push new branch
git push -u origin claudine-escape
```

### Option 2: Shallow Clone + Force Push
```powershell
# Backup current work
git branch backup-claudine-escape

# Shallow clone (siste 100 commits)
git clone --depth 100 <repo-url> temp-repo
cd temp-repo
git checkout -b Claudine-Colinization-Escapade-Continues

# Copy changes fra original repo
# ... (manual copy)

# Push shallow clone
git push -u origin Claudine-Colinization-Escapade-Continues
```

### Option 3: Split Into Multiple Commits
```powershell
# Interactive rebase (split large commits)
git rebase -i HEAD~10

# Mark commits for splitting: 'edit'
# Then:
git reset HEAD^
git add <files>
git commit -m "Part 1"
git add <more files>
git commit -m "Part 2"
git rebase --continue

# Push split commits
git push -u origin Claudine-Colinization-Escapade-Continues
```

---

## 🎯 Status Oppsummering

| Aspekt | Status | Løsning |
|--------|--------|---------|
| **Git Commit (VS Code)** | ✅ Virker | Ingen endring nødvendig |
| **Publish Branch (VS Code)** | ❌ Virker ikke | Set up remote tracking med `git push -u` |
| **Manual Push (Terminal)** | 🔄 Testing | `git push -u origin <branch>` |
| **Remote Tracking** | ❌ Ikke satt opp | Settes opp med `-u` flag |

---

## 🔥 Neste Steg

### Steg 1: Prøv Manual Push
```powershell
git push -u origin Claudine-Colinization-Escapade-Continues
```

### Steg 2: Hvis Det Feiler, Sjekk Output
- Note down exact error message
- Check if it's LFS issue, size issue, or auth issue
- Følg relevant løsning ovenfor

### Steg 3: Verify Tracking
```powershell
git branch -vv
```

### Steg 4: Test VS Code "Publish Branch"
- Gjør en liten endring
- Commit i VS Code
- Test sync/push knapp

---

**Status:** 🔧 Diagnostisert - Venter på push test  
**Branch:** Claudine-Colinization-Escapade-Continues  
**Filosofi:** "When GUI fails, terminal prevails" 🏴‍☠️🔥
