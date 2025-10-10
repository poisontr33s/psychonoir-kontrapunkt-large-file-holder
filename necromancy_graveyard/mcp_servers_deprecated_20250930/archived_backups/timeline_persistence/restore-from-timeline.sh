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
