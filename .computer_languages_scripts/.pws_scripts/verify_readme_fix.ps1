$orig = Get-FileHash "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS\19_SCRIPT_METADATA_REGISTRY\README.md" -Algorithm SHA256
$arch = Get-FileHash "CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS\21_MD_CONSCIOUSNESS_ARCHIVE\CLAUDINE_SUPREME\CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS\19_SCRIPT_METADATA_REGISTRY\README.md" -Algorithm SHA256

Write-Host "`nOriginal Hash: $($orig.Hash.Substring(0,16))..."
Write-Host "Archive Hash:  $($arch.Hash.Substring(0,16))..."

if ($orig.Hash -eq $arch.Hash) {
    Write-Host "`n✅ HASH MATCH: Files are now identical!" -ForegroundColor Green
}
else {
    Write-Host "`n❌ HASH MISMATCH: Files still differ" -ForegroundColor Red
}
