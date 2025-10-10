param(
  [string[]]$Tools = @('uv','bun','ruff'),
  [switch]$Apply
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Write-Step($msg){ Write-Host "==> $msg" -ForegroundColor Cyan }
function Write-Info($msg){ Write-Host "    $msg" -ForegroundColor DarkGray }
function New-TempDir(){
  $d = Join-Path $PSScriptRoot (".tmp_" + [Guid]::NewGuid()); New-Item -ItemType Directory -Force -Path $d | Out-Null; return $d
}
function Invoke-Download($Url,$OutFile){
  Write-Info "Download $Url"
  $ProgressPreference='SilentlyContinue'
  Invoke-WebRequest -Headers @{ 'User-Agent'='Mozilla/5.0' } -Uri $Url -OutFile $OutFile
}

$repoRoot = (Resolve-Path "$PSScriptRoot\..\").Path.TrimEnd('\\','/')
$paths = [ordered]@{
  Python = Join-Path $repoRoot ".computer_languages/python"
  JS     = Join-Path $repoRoot ".computer_languages/javascript"
  Rust   = Join-Path $repoRoot ".computer_languages/rust"
}
foreach($p in $paths.Values){ New-Item -ItemType Directory -Force -Path $p | Out-Null }

function Update-Uv(){
  Write-Step "UV: fetch latest release (astral-sh/uv)"
  $resp = Invoke-WebRequest -Headers @{ 'User-Agent'='Mozilla/5.0' } https://api.github.com/repos/astral-sh/uv/releases/latest
  $json = $resp.Content | ConvertFrom-Json
  $tag = $json.tag_name
  $assets = @($json.assets)
  $uvAsset  = $assets | Where-Object { $_.name -match '^uv-x86_64-pc-windows-msvc(\.zip|\.exe)$' } | Select-Object -First 1
  $uvxAsset = $assets | Where-Object { $_.name -match '^uvx-x86_64-pc-windows-msvc(\.zip|\.exe)$' } | Select-Object -First 1
  if(-not $uvAsset){ throw "Could not find uv Windows asset in $tag" }
  $tmp = New-TempDir
  try{
    $uvDest  = Join-Path $tmp $uvAsset.name
    Invoke-Download $uvAsset.browser_download_url $uvDest
    if($uvDest -like '*.zip'){
      Expand-Archive -Path $uvDest -DestinationPath $tmp -Force
      $uvExe = Get-ChildItem -Path $tmp -Filter uv.exe -Recurse | Select-Object -First 1
    } else { $uvExe = Get-Item $uvDest }
    if($uvExe){
      Copy-Item $uvExe.FullName (Join-Path $paths.Python 'uv.exe') -Force
      Copy-Item $uvExe.FullName (Join-Path $paths.Rust   'uv.exe') -Force
    }
    if($uvxAsset){
      $uvxDest = Join-Path $tmp $uvxAsset.name
      Invoke-Download $uvxAsset.browser_download_url $uvxDest
      if($uvxDest -like '*.zip'){
        Expand-Archive -Path $uvxDest -DestinationPath $tmp -Force
        $uvxExe = Get-ChildItem -Path $tmp -Filter uvx.exe -Recurse | Select-Object -First 1
      } else { $uvxExe = Get-Item $uvxDest }
      if($uvxExe){
        Copy-Item $uvxExe.FullName (Join-Path $paths.Python 'uvx.exe') -Force
        Copy-Item $uvxExe.FullName (Join-Path $paths.Rust   'uvx.exe') -Force
      }
    }
    Write-Host "UV updated to $tag" -ForegroundColor Green
  } finally { Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue }
}

function Update-Bun(){
  Write-Step "Bun: fetch latest release tag (oven-sh/bun)"
  $resp = Invoke-WebRequest -Headers @{ 'User-Agent'='Mozilla/5.0' } https://api.github.com/repos/oven-sh/bun/releases/latest
  $json = $resp.Content | ConvertFrom-Json
  $tag = $json.tag_name # e.g. bun-v1.2.23
  $zipUrl = "https://github.com/oven-sh/bun/releases/download/$tag/bun-windows-x64.zip"
  $tmp = New-TempDir
  try{
    $zip = Join-Path $tmp 'bun.zip'
    Invoke-Download $zipUrl $zip
    Expand-Archive -Path $zip -DestinationPath $tmp -Force
    $bunExe = Get-ChildItem -Path $tmp -Filter bun.exe -Recurse | Select-Object -First 1
    if(-not $bunExe){ throw "bun.exe not found in archive $zipUrl" }
    Copy-Item $bunExe.FullName (Join-Path $paths.JS 'bun.exe') -Force
    Write-Host "Bun updated to $tag" -ForegroundColor Green
  } finally { Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue }
}

function Update-Ruff(){
  Write-Step "Ruff: fetch latest release (astral-sh/ruff)"
  $resp = Invoke-WebRequest -Headers @{ 'User-Agent'='Mozilla/5.0' } https://api.github.com/repos/astral-sh/ruff/releases/latest
  $json = $resp.Content | ConvertFrom-Json
  $tag = $json.tag_name
  $asset = @($json.assets) | Where-Object { $_.name -match '^ruff-x86_64-pc-windows-msvc(\.zip|\.exe)$' } | Select-Object -First 1
  if(-not $asset){ throw "Could not find ruff Windows asset in $tag" }
  $tmp = New-TempDir
  try{
    $dest = Join-Path $tmp $asset.name
    Invoke-Download $asset.browser_download_url $dest
    if($dest -like '*.zip'){
      Expand-Archive -Path $dest -DestinationPath $tmp -Force
      $exe = Get-ChildItem -Path $tmp -Filter ruff.exe -Recurse | Select-Object -First 1
    } else { $exe = Get-Item $dest }
    if(-not $exe){ throw "ruff.exe not found in asset $($asset.name)" }
    Copy-Item $exe.FullName (Join-Path $paths.Python 'ruff.exe') -Force
    Write-Host "Ruff updated to $tag" -ForegroundColor Green
  } finally { Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue }
}

Write-Step "Planned updates: $($Tools -join ', ')"; if(-not $Apply){ Write-Info "(dry-run) add --Apply to perform updates" }

foreach($t in $Tools){
  switch ($t.ToLower()){
    'uv'   { if($Apply){ Update-Uv } else { Write-Info "uv -> .computer_languages/python & /rust" } }
    'bun'  { if($Apply){ Update-Bun } else { Write-Info "bun -> .computer_languages/javascript" } }
    'ruff' { if($Apply){ Update-Ruff } else { Write-Info "ruff -> .computer_languages/python" } }
    default { Write-Warning "Unknown tool: $t" }
  }
}

Write-Host "Done." -ForegroundColor Cyan
