# Session Log Refinement Script

# This script helps clean up the raw session log from 10_10_1025_Sesjonslogg.md
# It removes repetitive entries and extracts unique content

param(
    [string]$InputFile = ".\.a1-poisontr33s-personal-wipFILES\.ustrukturerte_sesjonslogger_avbrudd_feil_redudans_fpov_fixme\10_10_1025_Sesjonslogg.md",
    [string]$OutputFile = "refined_session_log.md"
)

$content = Get-Content $InputFile -Raw

# Remove repetitive GitHub Copilot responses
$content = $content -replace '(?s)GitHub Copilot: Optimizing tool selection\.\.\..*?(?=poisontr33s:|$)', ''
$content = $content -replace '(?s)GitHub Copilot: Searched codebase for.*?30 results.*?(?=poisontr33s:|$)', ''

# Clean up multiple consecutive user messages
$lines = $content -split "`n"
$uniqueLines = @()
$previousLine = ""

foreach ($line in $lines) {
    if ($line -ne $previousLine) {
        $uniqueLines += $line
        $previousLine = $line
    }
}

$refinedContent = $uniqueLines -join "`n"

# Save refined content
$refinedContent | Out-File $OutputFile -Encoding UTF8

Write-Host "Refined session log saved to $OutputFile"
Write-Host "Original lines: $($lines.Count)"
Write-Host "Refined lines: $($uniqueLines.Count)"