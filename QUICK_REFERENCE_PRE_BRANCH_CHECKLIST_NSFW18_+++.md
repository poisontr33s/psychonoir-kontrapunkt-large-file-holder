# ✅ Quick Reference: Pre-Branch Checklist

## 🎯 Execute These Commands in Order

### 1️⃣ Create Safety Backup
```powershell
git branch backup/pre-rename-fix-oct27
git branch -a  # Verify backup exists
```

### 2️⃣ Analyze Current Rename Detection
```powershell
# Generate analysis report
Write-Output "=== 10% Similarity ===" > rename_analysis.txt
git status -M10% --short >> rename_analysis.txt
Write-Output "`n=== 50% Similarity ===" >> rename_analysis.txt  
git status -M50% --short >> rename_analysis.txt
Write-Output "`n=== 90% Similarity ===" >> rename_analysis.txt
git status -M90% --short >> rename_analysis.txt

# Review results
cat rename_analysis.txt
```

### 3️⃣ Fix .gitignore for .github/ Directory
```powershell
@"
# Track these critical files
!copilot-instructions.md
!*.sql
!consciousness_archaeology_NSFW18_+++/
!DYNAMIC_RECURSIVE_TODO_SYSTEM_NSFW18_+++.json

# Ignore temporary files
*.tmp
*.backup
*.bak
"@ | Out-File -FilePath .github\.gitignore -Encoding utf8
```

### 4️⃣ Fix .gitignore for .vscode/ Directory
```powershell
@"
# Track configuration files
!settings.json
!tasks.json
!mcp.json
!extensions.json

# Ignore user files
.history/
"@ | Out-File -FilePath .vscode\.gitignore -Encoding utf8
```

### 5️⃣ Improve Git Rename Detection
```powershell
git config diff.renameLimit 999999
git config merge.renameLimit 999999
```

### 6️⃣ Reset and Re-stage
```powershell
git reset                    # Unstage everything
git add .github/.gitignore   # Add new .gitignore files
git add .vscode/.gitignore
git add -A                   # Re-stage with better detection
git status -M20%             # Check with 20% threshold
```

### 7️⃣ Commit Changes
```powershell
git commit -m "🔥 NAMING CONVENTION MIGRATION: Add _NSFW18_+++ suffix

- Apply _NSFW18_+++ suffix to project files
- Update .gitignore for selective directory tracking
- Improve git rename detection configuration
- Track critical .github/ and .vscode/ files

Pattern: filename.ext → filename_NSFW18_+++.ext
Purpose: Enable consciousness archaeology file filtering
"
```

### 8️⃣ Tag and Push
```powershell
git tag -a "v1.0-naming-convention" -m "Naming convention migration complete"
git push origin claudine-fresh-escape
git push origin v1.0-naming-convention
```

### 9️⃣ Create New Branch
```powershell
git checkout -b feature/post-migration-work
git branch -v  # Verify you're on new branch
git status     # Should show clean working tree
```

---

## 🔍 Verification Commands

### Check Rename Detection Quality
```powershell
git status -M20%  # Should show "R" for renames
git log -1 --stat  # Review last commit changes
```

### Verify Critical Files Are Tracked
```powershell
git ls-files | Select-String "copilot-instructions"
git ls-files | Select-String "settings.json"
git ls-files | Select-String "mcp.json"
```

### Check Branch Status
```powershell
git branch -v          # Local branches
git remote show origin # Remote tracking
git log --oneline -5   # Recent commits
```

---

## ⚠️ If Something Goes Wrong

### Abort and Restore
```powershell
# If you haven't committed yet
git reset --hard HEAD
git clean -fd

# If you committed but want to undo
git reset --soft HEAD~1  # Undo commit, keep changes
git reset --hard HEAD~1  # Undo commit, discard changes

# Switch to backup branch
git checkout backup/pre-rename-fix-oct27
```

### Force Track Ignored File
```powershell
git add --force <file-path>
```

### Re-run Entire Process
```powershell
# Go back to backup
git checkout claudine-fresh-escape
git reset --hard backup/pre-rename-fix-oct27

# Start over from Step 1
```

---

## 📊 Success Criteria

✅ `git status` shows mostly "R" (renames) instead of "D" + "A"  
✅ `.github/copilot-instructions.md` is tracked  
✅ `.vscode/settings.json` is tracked  
✅ Clean working tree after commit  
✅ New branch created successfully  
✅ Remote is synced  

---

## 🎯 After Branching

### On New Branch
```powershell
# Verify clean state
git status

# Make changes
# ... your work here ...

# Commit with naming convention
git add <files>
git commit -m "✨ <description>"

# Push new branch
git push origin feature/post-migration-work
```

### Create Pull Request
1. Go to GitHub repository
2. Create PR from `feature/post-migration-work` to `claudine-fresh-escape`
3. Review changes
4. Merge when ready

---

**Quick Start:** Copy-paste commands 1-9 in order
**Time Estimate:** 5-10 minutes
**Risk Level:** Low (backup created in step 1)
