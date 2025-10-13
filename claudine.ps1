# Claudine Enhanced Universal Wrapper
# Loads enhanced version and forwards all parameters correctly

param(
    [Parameter(Position = 0)]
    [string]$Action = "activate",
    
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Parameters = @()
)

# Load enhanced Claudine
$EnhancedPath = "$PSScriptRoot\.poly_gluttony_scripts_files_orgy\claudine_enhanced.ps1"
if (Test-Path $EnhancedPath) {
    # Dot-source the enhanced version
    . $EnhancedPath
    
    # Call claudine with all parameters
    claudine $Action @Parameters
}
else {
    Write-Error "Enhanced Claudine not found at: $EnhancedPath"
}