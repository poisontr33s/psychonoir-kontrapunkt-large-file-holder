# Emergency: push local project to remote GitHub

Important: make a full filesystem backup (ZIP) of C:\Users\eldno\PsychoNoir-Kontrapunkt\ before running destructive git commands.

1) Open PowerShell in the project root:
- cd "C:\Users\eldno\PsychoNoir-Kontrapunkt"

2) Inspect current git state:
- git status
- git branch --show-current
- git remote -v

3) If repository NOT initialized locally:
- git init
- git add .
- git commit -m "Restore local project - emergency commit"

4) Add / update remote to your GitHub repo:
- git remote remove origin 2>$null || echo "no existing origin"
- git remote add origin https://github.com/poisontr33s/poisontr33s-milfografisk-nsfw18-psycho-noir-kontrapunkt-directors-cut-gamedev.git

5) If you want to preserve remote and push your local snapshot to a separate branch (safe):
- git checkout -b restore-local
- git push -u origin restore-local

6) If you intend to overwrite the remote with your local (destructive). First BACKUP remote:
- git clone --mirror https://github.com/poisontr33s/poisontr33s-milfografisk-nsfw18-psycho-noir-kontrapunkt-directors-cut-gamedev.git ../remote-backup.git

Then force-push local main (use only if you understand it replaces remote history):
- git branch -M main
- git push -u origin main --force

7) If large assets exist, enable Git LFS BEFORE committing them:
- git lfs install
- git lfs track "*.png"
- git lfs track "*.jpg"
- git add .gitattributes
- git add <large files>
- git commit -m "Add large assets via LFS"
- git push origin main

8) Authentication options:
- Recommended: gh auth login (GitHub CLI) then git push.
- Or use HTTPS + PAT when prompted, or configure SSH keys and use an SSH remote.

9) Verify on GitHub: open your repo URL after push.

Troubleshooting quick tips:
- "remote: Permission denied" → authenticate (gh auth login or PAT) or use SSH.
- Uncommitted changes blocking push → git add . && git commit -m "WIP restore"
- If you accidentally force-pushed and need help restoring remote, stop and make a local mirror backup and ask for assistance.