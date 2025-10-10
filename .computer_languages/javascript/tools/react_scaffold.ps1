param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectName,
    [switch]$UseVite
)

$bunPath = Join-Path $PSScriptRoot "..\bun.exe"
$bunxPath = Join-Path $PSScriptRoot "..\bunx.exe"

if (-not (Test-Path $bunPath) -or -not (Test-Path $bunxPath)) {
    Write-Error "Bun runtime missing. Expected $bunPath and $bunxPath."
    exit 1
}

$arguments = if ($UseVite.IsPresent) {
    @($bunxPath, "create-vite@latest", $ProjectName, "--", "--template", "react-swc")
} else {
    @($bunxPath, "create-next-app@latest", $ProjectName, "--turbo", "--ts", "--app")
}

# Leverage bunx to scaffold React project with either Turbopack (Next.js) or React SWC (Vite) presets.
$bunCommand = @($bunPath, "run") + $arguments

Write-Host "Scaffolding project '$ProjectName'..."
$process = Start-Process -FilePath $bunCommand[0] -ArgumentList $bunCommand[1..($bunCommand.Length - 1)] -NoNewWindow -Wait -PassThru
if ($process.ExitCode -ne 0) {
    Write-Error "Project scaffolding failed with exit code $($process.ExitCode)."
    exit $process.ExitCode
}

Write-Host "Project '$ProjectName' scaffold complete."
