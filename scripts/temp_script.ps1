$json = Get-Content scripts/district_scan_full_sweep.json -Raw
$sweep = $json | ConvertFrom-Json
$out = New-Object System.Text.StringBuilder
$districts = "CARIBBEAN_ARCHIPELAGO","SKYSKRAPEREN","RUSTBELTET","HAVSDOMINANSEN","NEKROKRONORIKET","VIRTUALITETSHELGEDOMMEN","FOYDALITETSDUALITETSLENKEN","SUPREME_MATRIARCH"
foreach ($dName in $districts) {
    [void]$out.AppendLine("=== $dName ===")
    $d = $sweep.detail.$dName
    if ($d) {
        foreach ($prop in $d.PSObject.Properties) {
            $top = $prop.Value | Sort-Object { [int]($_.line_count) } -Descending | Select-Object -First 1
            [void]$out.AppendLine("  $($prop.Name) | lines:$($top.line_count) | tier:$($top.tier) | $($top.path)")
        }
    }
    [void]$out.AppendLine("")
}
[void]$out.AppendLine("=== UNCLASSIFIED TOP 50 MD FILES ===")
$all_unc = New-Object System.Collections.Generic.List[PSObject]
foreach ($prop in $sweep.detail.UNCLASSIFIED.PSObject.Properties) {
    foreach ($e in $prop.Value) {
        if ($e.suffix -eq ".md") {
            $all_unc.Add([pscustomobject]@{ entity=$prop.Name; lines=[int]($e.line_count); tier=$e.tier; path=$e.path })
        }
    }
}
$all_unc | Sort-Object lines -Descending | Select-Object -First 50 | ForEach-Object {
    [void]$out.AppendLine("  $($_.entity) | lines:$($_.lines) | tier:$($_.tier) | $($_.path)")
}
$out.ToString() | Out-File -FilePath scripts/scan_digest.txt -Encoding utf8
