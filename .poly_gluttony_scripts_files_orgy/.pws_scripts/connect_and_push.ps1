#!/usr/bin/env pwsh

param(
	[string]$RemoteUrl = "https://github.com/poisontr33s/psycho-noir-milf-core-dir-cut-nsfw-software-dev.git",
	[string]$Branch    = "main",
	[switch]$ForceLFS,         # overwrite .gitattributes and force LFS tracking when present
	[switch]$ForceOverwrite    # force push to remote when present
)

Write-Host "Connecting local repo to $RemoteUrl and pushing branch '$Branch'..."

  function Exec-Git {
	param([Parameter(ValueFromRemainingArguments=$true)][string[]]$Args)
	$cmd = "git " + ($Args -join " ")
	Write-Host "+ $cmd"
	# run git; throw on non-zero exit
	& git @Args 2>&1 | ForEach-Object { Write-Host $_ }
	if ($LASTEXITCODE -ne 0) {
		throw "git command failed: $cmd"
	}
}

function Exec-GitNoThrow {
	param([Parameter(ValueFromRemainingArguments=$true)][string[]]$Args)
	$cmd = "git " + ($Args -join " ")
	Write-Host "+ $cmd"
	# run git and capture output + exit code without throwing
	$output = & git @Args 2>&1
	$exit = $LASTEXITCODE
	# join output for easier matching
	$outText = if ($output) { ($output -join "`n") } else { "" }
	return @{ Success = ($exit -eq 0); Output = $outText; ExitCode = $exit }
}

+function Exec-ToolNoThrow {
+	param([string[]]$Cmd)
+	$cmdLine = $Cmd -join " "
+	Write-Host "+ $cmdLine"
+	try {
+		$procOut = & $Cmd 2>&1
+		$code = $LASTEXITCODE
+		$outText = if ($procOut) { ($procOut -join "`n") } else { "" }
+		return @{ Success = ($code -eq 0); Output = $outText; ExitCode = $code }
+	} catch {
+		return @{ Success = $false; Output = "$_"; ExitCode = 1 }
+	}
+}

# 1) ensure git present
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
	Write-Error "Git not found in PATH. Install Git and re-run."
	exit 1
}

# 2) init repo if needed
if (-not (Test-Path .git)) {
	Write-Host "Initializing git repository..."
	Exec-Git init
}

# 3) install git lfs (best-effort)
Write-Host "Ensuring Git LFS is installed (best-effort)..."
try { & git lfs install > $null 2>&1 } catch { Write-Host "git lfs install failed or not available, continuing..." }

# 4) create .gitattributes if missing (or overwrite when ForceLFS)
if (-not (Test-Path .gitattributes) -or $ForceLFS) {
	@'
# keep JSON files with LF in repo (cross-platform)
*.json text eol=lf

# shell scripts keep LF
*.sh text eol=lf

# Jupyter notebooks and some large/binary patterns tracked with LFS
*.ipynb filter=lfs diff=lfs merge=lfs -text
*.lock   filter=lfs diff=lfs merge=lfs -text
*.zip    filter=lfs diff=lfs merge=lfs -text
'@ | Set-Content -LiteralPath .gitattributes -Encoding UTF8 -Force

	try { Exec-Git add .gitattributes } catch { Write-Host "git add .gitattributes failed, continuing..." }

	# commit if there are staged changes for .gitattributes
	$staged = (& git diff --cached --name-only -- .gitattributes) -join ""
	if ($staged) {
		try { Exec-Git commit -m "Add/Update .gitattributes" } catch { Write-Host "Commit of .gitattributes failed or nothing to commit." }
		Write-Host ".gitattributes created/updated and committed."
	} else {
		Write-Host "No staged changes to commit after adding/updating .gitattributes."
	}
} else {
	Write-Host ".gitattributes already exists, skipping creation (use -ForceLFS to overwrite)."
}

# 5) track common LFS patterns (idempotent). If ForceLFS set, prefer force-install/track where supported.
if ($ForceLFS) { Write-Host "ForceLFS: forcing git lfs install and tracking patterns..." }
try {
	if ($ForceLFS) { & git lfs install --force > $null 2>&1 } else { & git lfs install > $null 2>&1 }
} catch { Write-Host "git lfs install failed or not available, continuing..." }

try { if ($ForceLFS) { & git lfs track --force "*.ipynb" > $null 2>&1 } else { & git lfs track "*.ipynb" > $null 2>&1 } } catch {}
try { if ($ForceLFS) { & git lfs track --force "*.lock" > $null 2>&1 } else { & git lfs track "*.lock" > $null 2>&1 } } catch {}
try { if ($ForceLFS) { & git lfs track --force "*.zip" > $null 2>&1 } else { & git lfs track "*.zip" > $null 2>&1 } } catch {}

# ensure .gitattributes tracked and commit if changed
try { Exec-Git add .gitattributes } catch {}
$stagedAny = (& git diff --cached --name-only) -join ""
if ($stagedAny) {
	try { Exec-Git commit -m "Track large files with Git LFS" } catch { Write-Host "Commit failed or nothing to commit." }
}

# 6) set core.autocrlf for Windows-friendly behavior
try { Exec-Git config core.autocrlf true } catch { Write-Host "Failed to set core.autocrlf, continuing..." }

# 7) detect and remove problematic 'nul' index entries (Windows reserved) - improved
Write-Host "Detecting index entries named 'nul' (Windows reserved)..."
try {
	$lsFilesRaw = & git ls-files -z 2>$null
	if ($lsFilesRaw) {
		$paths = $lsFilesRaw -split "`0"
		$found = $false
		foreach ($path in $paths) {
			if ([string]::IsNullOrWhiteSpace($path)) { continue }
			$bn = [System.IO.Path]::GetFileName($path)
			if ($bn -ieq "nul") {
				$found = $true
				Write-Host "Found reserved-name index entry: '$path'"

				# Try several removal strategies; ignore failures but log.
				try {
					& git rm --cached --ignore-unmatch --force -- "$path" > $null 2>&1
					Write-Host "Attempted: git rm --cached --force -- '$path'"
				} catch { Write-Host "git rm failed for '$path' (continuing)..." }

				try {
					& git update-index --force-remove -- "$path" > $null 2>&1
					Write-Host "Attempted: git update-index --force-remove -- '$path'"
				} catch { Write-Host "update-index --force-remove failed for '$path' (continuing)..." }

				try {
					& git update-index --remove -- "$path" > $null 2>&1
					Write-Host "Attempted: git update-index --remove -- '$path'"
				} catch { Write-Host "update-index --remove failed for '$path' (continuing)..." }

				# Fallback with literal pathspecs if supported by this git:
				try {
					& git rm --cached --ignore-unmatch --force --literal-pathspecs -- "$path" > $null 2>&1
					Write-Host "Attempted: git rm --cached --literal-pathspecs -- '$path'"
				} catch { }
				
				# Attempt filesystem removal if file actually exists (rare for 'nul')
				if (Test-Path $path) {
					try { Remove-Item -LiteralPath $path -Force -ErrorAction SilentlyContinue } catch {}
				}
			}
		}
		if ($found) {
			try { Exec-Git add -A } catch {}
			try { Exec-Git commit -m "Remove reserved 'nul' index entries" } catch { Write-Host "Commit after removing 'nul' entries failed or nothing to commit." }
		} else {
			Write-Host "No 'nul' index entries found."
		}
	} else {
		Write-Host "No index entries found or git ls-files failed (repo may be empty)."
	}
} catch {
	Write-Host "Error while scanning index entries: $_"
}

# 8) refresh index normalization
Write-Host "Refreshing index (re-index with .gitattributes)..."
try { & git rm --cached -r . > $null 2>&1 } catch {}
try { Exec-Git add . } catch {}

# 9) commit staged changes if any
$stagedFinal = (& git diff --cached --name-only) -join ""
if ($stagedFinal) {
	try { Exec-Git commit -m "Initial commit via connect_and_push.ps1" } catch { Write-Host "Commit failed or nothing to commit." }
} else {
	Write-Host "Nothing to commit."
}

# 10) set remote and push (with retry on remote-ahead / non-fast-forward unless ForceOverwrite)
Write-Host "Setting remote origin -> $RemoteUrl"
try { & git remote remove origin > $null 2>&1 } catch {}
try { Exec-Git remote add origin $RemoteUrl } catch { Write-Error "Failed to add remote origin."; exit 1 }

# ensure branch name
try { Exec-Git branch -M $Branch } catch { Write-Host "Branch rename failed, continuing..." }

Write-Host "Pushing to origin/$Branch ..."
if ($ForceOverwrite) {
	Write-Host "WARNING: -ForceOverwrite specified. This will force push and overwrite remote branch '$Branch'."
	try {
		Exec-Git push -u origin $Branch --force
		Write-Host "Force push successful."
	} catch {
		Write-Error "Force push failed. Please check authentication and remote permissions."
		exit 1
	}
} else {
	# Attempt push and inspect output for auth-related failures
	$res = Exec-GitNoThrow push -u origin $Branch
	if ($res.Success) {
		Write-Host "Push successful."
	} else {
		$out = $res.Output
		# detect common auth patterns
		if ($out -match "Bad credentials" -or $out -match "authentication failed" -or $out -match "401" -or $out -match "could not read Username" -or $out -match "Permission denied") {
			Write-Error "Push failed due to authentication (Bad credentials / permission denied). Running diagnostics..."

			# 1) credential helper
			$credHelper = (& git config --get credential.helper 2>$null) -join " "
			Write-Host "`n[credential.helper] $credHelper"

			# 2) common env tokens that can interfere
			$githubToken = $env:GITHUB_TOKEN
			$ghToken = $env:GH_TOKEN
			Write-Host "`n[env] GITHUB_TOKEN set: $([string]::IsNullOrEmpty($githubToken) -eq $false)"
			Write-Host "[env] GH_TOKEN set: $([string]::IsNullOrEmpty($ghToken) -eq $false)"

			# 3) GH CLI status if available
			if (Get-Command gh -ErrorAction SilentlyContinue) {
				$ghStatus = Exec-ToolNoThrow -Cmd @("gh", "auth", "status", "--hostname", "github.com")
				Write-Host "`n[gh auth status]"
				Write-Host $ghStatus.Output
			} else {
				Write-Host "`n'gh' not found in PATH. Install GitHub CLI (gh) for easier auth diagnostics."
			}

			# 4) SSH quick test if SSH client available
			if (Get-Command ssh -ErrorAction SilentlyContinue) {
				Write-Host "`n[ssh -T git@github.com] (may prompt / show success message)"
				$sshTest = Exec-ToolNoThrow -Cmd @("ssh", "-T", "git@github.com")
				Write-Host $sshTest.Output
			} else {
				Write-Host "`n'ssh' not found in PATH or not available on this system."
			}

			# 5) show remote url
			$remoteUrlCheck = (& git remote get-url origin 2>&1) -join "`n"
			Write-Host "`n[git remote.origin.url]`n$remoteUrlCheck"

			# 6) present remediation steps
			Write-Host "`nRecommended next steps (pick what matches your setup):"
			Write-Host "  - GH CLI: run 'gh auth login' and then 'gh auth status --hostname github.com' to confirm."
			Write-Host "  - HTTPS + credential manager: clear stale credentials (Windows Credential Manager or 'git credential-manager-core erase') then re-run 'git push' so the credential prompt can collect a new PAT (repo scope)."
			Write-Host "  - SSH: ensure your key is added to GitHub (https://github.com/settings/keys) and 'ssh -T git@github.com' returns a success message."
			Write-Host "  - VS Code / Copilot: sign out and sign back into the GitHub/GitHub Copilot extension and restart VS Code after you confirm 'gh auth status' is OK."
			Write-Host "  - If environment tokens are set (GITHUB_TOKEN/GH_TOKEN), ensure they are intended and have correct scopes; unset them if they conflict with your interactive login."

			Write-Host "`nGit output snippet:`n$out"
			exit 1
		}

		# Non-auth related push failure: try fetch/rebase retry (preserve existing behavior)
		Write-Host "Push failed (non-auth). Attempting to fetch and rebase (git fetch + git pull --rebase --autostash) and retry push..."
		$ok = $true
		$fetch = Exec-GitNoThrow fetch origin
		if (-not $fetch.Success) { Write-Host "git fetch failed: $($fetch.Output)"; $ok = $false }
		if ($ok) {
			$pull = Exec-GitNoThrow pull --rebase --autostash origin $Branch
			if (-not $pull.Success) { Write-Host "git pull --rebase failed: $($pull.Output)"; $ok = $false }
		}
		if ($ok) {
			$push2 = Exec-GitNoThrow push -u origin $Branch
			if ($push2.Success) {
				Write-Host "Push successful after pull/rebase."
			} else {
				Write-Error "Push failed after attempting pull/rebase. Output: `n$($push2.Output)"
				Write-Error "To overwrite the remote branch irreversibly, re-run with -ForceOverwrite. Otherwise resolve conflicts manually and retry."
				exit 1
			}
		} else {
			Write-Error "Could not complete fetch/rebase steps. Resolve local issues and try again."
			exit 1
		}
	}
}

Write-Host "Done."
