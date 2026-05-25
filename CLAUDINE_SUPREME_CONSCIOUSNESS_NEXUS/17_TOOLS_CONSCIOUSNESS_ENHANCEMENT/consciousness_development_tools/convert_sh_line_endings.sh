#!/usr/bin/env bash

# PSYCHO-NOIR KONTRAPUNKT: BASH SCRIPT LINE ENDING CONVERTER
# DATO: 2025-09-17
# FORMÅL: Konverterer alle .sh filer fra Windows til Unix line endings

echo "🔧 KONVERTERER .SH FILER TIL UNIX FORMAT..."
echo "TEMPORAL ANCHOR: $(date)"

# Tell antall filer
TOTAL_FILES=$(find . -name "*.sh" | wc -l)
echo "📊 FANT $TOTAL_FILES .sh filer"

# Konverter alle .sh filer
CONVERTED=0
for file in $(find . -name "*.sh"); do
    echo "🔄 Konverterer: $file"
    
    # Backup original
    cp "$file" "$file.bak"
    
    # Konverter line endings (fjern \r)
    tr -d '\r' < "$file.bak" > "$file"
    
    # Sett executable permissions
    chmod +x "$file"
    
    CONVERTED=$((CONVERTED + 1))
done

echo "✅ KONVERTERT: $CONVERTED av $TOTAL_FILES filer"
echo "💾 BACKUPS: Originale filer lagret som .bak"
echo "🎭 PSYCHO-NOIR BASH SCRIPTS ER NÅ UNIX-KOMPATIBLE!"
