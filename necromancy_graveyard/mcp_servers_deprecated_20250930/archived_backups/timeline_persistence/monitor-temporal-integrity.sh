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
