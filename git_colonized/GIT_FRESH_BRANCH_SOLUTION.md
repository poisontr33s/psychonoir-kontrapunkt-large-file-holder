# 🚀 GIT FRESH BRANCH - Løsning for Store Filer i History

**Problem:** Store filer er i Git history (ikke current commit), blokkerer push

---

## ⚡ LØSNING: Fresh Branch (Uten History)

### Hvorfor dette virker:
- Store filer er i **gamle commits** (history)
- Current working directory har kun små filer
- Lag ny branch **uten history** = kun current files

### Steg-for-Steg:

```powershell
# 1. STOP current push (Ctrl+C hvis den kjører)

# 2. Sjekk current files size (skal være små)
Get-ChildItem -Recurse | Measure-Object -Property Length -Sum | Select-Object @{Name="Size (MB)"; Expression={[math]::Round($_.Sum / 1MB, 2)}}

# 3. Lag orphan branch (ingen history)
git checkout --orphan claudine-fresh-escape

# 4. Add ALL current files
git add -A

# 5. Commit (kun current state, NO history!)
git commit -m "🔥 Fresh start: Claudine Escape branch (no large file history)

- Current working directory only
- No large files from old commits
- Clean state for fast push"

# 6. Push new branch (mye raskere!)
git push -u origin claudine-fresh-escape
```

**Resultat:** Push kun current files (~10-50 MB), ikke hele history (297 MB + store filer)

---

## 🏴‍☠️ ALTERNATIV: Shallow Clone + Force Push

Hvis orphan branch ikke fungerer:

```powershell
# 1. Backup current work
git stash

# 2. Shallow clone (siste 1 commit)
cd ..
git clone --depth 1 file:///C:/Users/erdno/PsychoNoir-Kontrapunkt temp-shallow

# 3. Gå inn i shallow repo
cd temp-shallow

# 4. Checkout new branch
git checkout -b claudine-escape-shallow

# 5. Apply stashed changes fra original repo
# (copy files manuelt hvis nødvendig)

# 6. Push shallow branch
git push -u origin claudine-escape-shallow
```

---

## 🔧 ALTERNATIV 2: BFG Repo-Cleaner (Remove fra history)

Download BFG: https://rtyley.github.io/bfg-repo-cleaner/

```powershell
# 1. Backup
git clone --mirror https://github.com/poisontr33s/psychonoir-kontrapunkt-large-file-holder.git repo-backup.git

# 2. Remove large files fra history
java -jar bfg.jar --strip-blobs-bigger-than 50M repo-backup.git

# 3. Cleanup
cd repo-backup.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 4. Force push cleaned history
git push --force
```

---

## 📋 ANBEFALT: Orphan Branch (Raskest!)

Copy-paste dette:

```powershell
# Stop any running push (Ctrl+C)

# Create orphan branch
git checkout --orphan claudine-fresh-20251014

# Stage all current files
git add .

# Commit clean state
git commit -m "🔥 Fresh branch: Clean start without large file history"

# Push fresh branch
git push -u origin claudine-fresh-20251014
```

**Fordel:**
- ✅ Ingen Git history = ingen store filer
- ✅ Kun current working directory
- ✅ Rask push (<5 minutter)

**Ulempe:**
- ❌ Mister Git history (men du kan beholde lokal branch med history)

---

## 🔍 Verify Fresh Branch

```powershell
# Sjekk branch
git branch
# Should show: * claudine-fresh-20251014

# Sjekk commit count (skal være 1)
git rev-list --count HEAD
# Expected: 1

# Sjekk size
git count-objects -vH
# Expected: Mye mindre enn original
```

---

## 🆘 Hvis Fresh Branch Også Feiler

Da er store filer i CURRENT working directory. Sjekk:

```powershell
# Find files > 50 MB
Get-ChildItem -Recurse -File | 
    Where-Object { $_.Length -gt 50MB } | 
    Select-Object FullName, @{Name="Size (MB)"; Expression={[math]::Round($_.Length / 1MB, 2)}} | 
    Sort-Object "Size (MB)" -Descending

# Add til .gitignore
# ... (paths fra output)
```

---

## 🎯 Quick Action

**COPY-PASTE NOW:**

```powershell
# Create fresh branch
git checkout --orphan claudine-fresh-escape

# Stage current files
git add .

# Commit
git commit -m "🔥 Fresh escape: No large file history"

# Push
git push -u origin claudine-fresh-escape
```

**After push success:**
- Bruk `claudine-fresh-escape` for fremtidig work
- Old `Claudine-Colinization-Escapade-Continues` kan slettes fra remote (hvis ønsket)

---

**Status:** 🚀 Fresh branch strategy ready  
**Action:** Copy-paste commands above  
**Tid:** ~2-5 minutter for push  
**Filosofi:** "Start fresh, sail fast" 🏴‍☠️⚡
