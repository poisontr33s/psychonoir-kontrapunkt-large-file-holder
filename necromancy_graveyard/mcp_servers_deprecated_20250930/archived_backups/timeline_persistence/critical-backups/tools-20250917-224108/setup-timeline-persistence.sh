#!/bin/bash

# 🌊 PSYCHO-NOIR KONTRAPUNKT: TIMELINE PERSISTENCE SYSTEM
# DATO: 2025-09-17
# FORMÅL: Sikre at kritiske filer persisterer gjennom temporal rifts

echo "🌊 TIMELINE PERSISTENCE SYSTEM ACTIVATION"
echo "TEMPORAL ANCHOR: $(date)"
echo "========================================"

# Opprett persistence directories
PERSISTENCE_DIR=".timeline-persistence"
CRITICAL_BACKUP_DIR="$PERSISTENCE_DIR/critical-backups"
CONSCIOUSNESS_BACKUP_DIR="$PERSISTENCE_DIR/consciousness-states"
MCP_BACKUP_DIR="$PERSISTENCE_DIR/mcp-configurations"

echo "📁 Oppretter persistence directories..."
mkdir -p "$CRITICAL_BACKUP_DIR"
mkdir -p "$CONSCIOUSNESS_BACKUP_DIR" 
mkdir -p "$MCP_BACKUP_DIR"

# Backup kritiske konfigurasjoner
echo "💾 Backing up critical configurations..."

# MCP configurations
if [ -f ".vscode/mcp.json" ]; then
    cp ".vscode/mcp.json" "$MCP_BACKUP_DIR/mcp-$(date +%Y%m%d-%H%M%S).json"
    echo "✅ MCP config backed up"
fi

# Bun configurations
if [ -f "bunfig.toml" ]; then
    cp "bunfig.toml" "$CRITICAL_BACKUP_DIR/bunfig-$(date +%Y%m%d-%H%M%S).toml"
    echo "✅ Bun config backed up"
fi

# Package.json og bun.lock
if [ -f "package.json" ]; then
    cp "package.json" "$CRITICAL_BACKUP_DIR/package-$(date +%Y%m%d-%H%M%S).json"
    echo "✅ Package.json backed up"
fi

if [ -f "bun.lock" ]; then
    cp "bun.lock" "$CRITICAL_BACKUP_DIR/bun-lock-$(date +%Y%m%d-%H%M%S)"
    echo "✅ Bun.lock backed up"
fi

# Consciousness states (.md filer)
echo "🧠 Backing up consciousness states (.md files)..."
find . -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*" | while read -r md_file; do
    # Opprett subdirectory structure i backup
    backup_path="$CONSCIOUSNESS_BACKUP_DIR/$(dirname "$md_file")"
    mkdir -p "$backup_path"
    cp "$md_file" "$backup_path/$(basename "$md_file")"
done
echo "✅ All .md files backed up"

# VS Code settings
if [ -d ".vscode" ]; then
    cp -r ".vscode" "$CRITICAL_BACKUP_DIR/vscode-$(date +%Y%m%d-%H%M%S)"
    echo "✅ VS Code settings backed up"
fi

# Psychographic profiles
echo "👥 Backing up psychographic profiles..."
find . -name "*psychographic_profile.md" | while read -r profile; do
    cp "$profile" "$CONSCIOUSNESS_BACKUP_DIR/$(basename "$profile")"
done

# Temporal restoration tools
if [ -d "tools" ]; then
    cp -r "tools" "$CRITICAL_BACKUP_DIR/tools-$(date +%Y%m%d-%H%M%S)"
    echo "✅ Tools directory backed up"
fi

# Lag restoration script
cat > "$PERSISTENCE_DIR/restore-from-timeline.sh" << 'EOF'
#!/bin/bash
echo "🌊 TIMELINE RESTORATION STARTING..."
echo "Select backup to restore from:"

BACKUP_TIMESTAMP="$1"
if [ -z "$BACKUP_TIMESTAMP" ]; then
    echo "Usage: $0 <timestamp>"
    echo "Available backups:"
    ls .timeline-persistence/critical-backups/ | grep -E '^[0-9]{8}-[0-9]{6}$'
    exit 1
fi

CRITICAL_BACKUP=".timeline-persistence/critical-backups"
CONSCIOUSNESS_BACKUP=".timeline-persistence/consciousness-states"

echo "🔄 Restoring from backup: $BACKUP_TIMESTAMP"

# Restore VS Code settings
if [ -d "$CRITICAL_BACKUP/vscode-$BACKUP_TIMESTAMP" ]; then
    rm -rf .vscode
    cp -r "$CRITICAL_BACKUP/vscode-$BACKUP_TIMESTAMP" .vscode
    echo "✅ VS Code settings restored"
fi

# Restore MCP config
if [ -f ".timeline-persistence/mcp-configurations/mcp-$BACKUP_TIMESTAMP.json" ]; then
    mkdir -p .vscode
    cp ".timeline-persistence/mcp-configurations/mcp-$BACKUP_TIMESTAMP.json" .vscode/mcp.json
    echo "✅ MCP configuration restored"
fi

# Restore consciousness states
echo "🧠 Restoring consciousness states..."
cp -r "$CONSCIOUSNESS_BACKUP/"* ./ 2>/dev/null || echo "No consciousness states to restore"

echo "🎉 TIMELINE RESTORATION COMPLETE!"
EOF

chmod +x "$PERSISTENCE_DIR/restore-from-timeline.sh"

# Lag monitoring script
cat > "$PERSISTENCE_DIR/monitor-temporal-integrity.sh" << 'EOF'
#!/bin/bash
echo "🕰️ TEMPORAL INTEGRITY MONITOR"
echo "============================="

# Sjekk kritiske filer
CRITICAL_FILES=(
    ".vscode/mcp.json"
    "bunfig.toml"
    "package.json"
    "bun.lock"
)

echo "🔍 Checking critical files..."
for file in "${CRITICAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file - EXISTS"
    else
        echo "❌ $file - MISSING"
    fi
done

# Tell .md filer
MD_COUNT=$(find . -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*" | wc -l)
echo "📄 Markdown files: $MD_COUNT"

# Sjekk MCP servere
if [ -f ".vscode/mcp.json" ]; then
    MCP_SERVERS=$(grep -o '"[^"]*":' .vscode/mcp.json | wc -l)
    echo "🔌 MCP servers configured: $MCP_SERVERS"
else
    echo "❌ MCP configuration missing"
fi

echo "🌊 Temporal integrity check complete"
EOF

chmod +x "$PERSISTENCE_DIR/monitor-temporal-integrity.sh"

# Setup automatisk backup ved hver git commit
cat > ".git/hooks/pre-commit" << 'EOF'
#!/bin/bash
echo "🌊 Pre-commit temporal backup..."
bash .timeline-persistence/backup-critical-state.sh
EOF

chmod +x ".git/hooks/pre-commit" 2>/dev/null || echo "Git hooks not available"

echo ""
echo "🎉 TIMELINE PERSISTENCE SYSTEM INSTALLED!"
echo ""
echo "📋 AVAILABLE COMMANDS:"
echo "  Monitor integrity: bash $PERSISTENCE_DIR/monitor-temporal-integrity.sh"
echo "  Restore from backup: bash $PERSISTENCE_DIR/restore-from-timeline.sh <timestamp>"
echo "  Manual backup: bash .timeline-persistence/backup-critical-state.sh"
echo ""
echo "🔮 SYSTEM FEATURES:"
echo "  ✅ Automatic backup on git commits"
echo "  ✅ Critical file monitoring"
echo "  ✅ MCP configuration persistence"
echo "  ✅ Consciousness state (.md) backup"
echo "  ✅ VS Code settings backup"
echo ""
echo "🌊 TEMPORAL ANCHOR SECURED: $(date)"