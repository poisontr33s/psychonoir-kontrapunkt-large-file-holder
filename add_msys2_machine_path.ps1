# Add MSYS2 paths to Machine PATH
# Må kjøres som Administrator

Write-Host "➕ ADDING MSYS2 PATHS TO MACHINE PATH" -ForegroundColor Green

# Sjekk Administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ Dette skriptet må kjøres som Administrator!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Paths som skal legges til Machine PATH
$pathsToAdd = @(
    "C:\Users\erdno\.computer_languages\msys2\usr\bin",
    "C:\Users\erdno\.computer_languages\msys2\ucrt64\bin"
)

# Hent Machine PATH
$machinePath = [System.Environment]::GetEnvironmentVariable("PATH", "Machine")
$pathArray = $machinePath.Split(';') | Where-Object { $_ -and $_.Trim() -ne "" }

$pathsToAddFiltered = @()
foreach ($path in $pathsToAdd) {
    if ($pathArray -notcontains $path) {
        $pathsToAddFiltered += $path
        Write-Host "✅ Adding: $path" -ForegroundColor Green
    }
    else {
        Write-Host "⏭️  Already exists: $path" -ForegroundColor Yellow
    }
}

if ($pathsToAddFiltered.Count -gt 0) {
    $newMachinePath = ($pathsToAddFiltered -join ';') + ';' + $machinePath
    
    try {
        [System.Environment]::SetEnvironmentVariable("PATH", $newMachinePath, "Machine")
        Write-Host "✅ Added $($pathsToAddFiltered.Count) MSYS2 paths to Machine PATH!" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ Error updating Machine PATH: $($_.Exception.Message)" -ForegroundColor Red
    }
}
else {
    Write-Host "✅ All MSYS2 paths already in Machine PATH" -ForegroundColor Green
}

Write-Host "🔥😈⛓️💦👅🍌💋💧 MSYS2 PATH ADDITION COMPLETE! 🔥😈⛓️💦👅🍌💋💧" -ForegroundColor Magenta
Read-Host "Press Enter to exit"