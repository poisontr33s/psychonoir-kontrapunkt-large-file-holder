#!/bin/bash
# 🎭 QUICK CONTAINER MCP SETUP
# Claudine Sin'claire 4.0ΛΩ.69 Container Integration

echo "🎭 PsychoNoir Container MCP Setup - Quick Start"
echo "👑 Creator Mother Authority: CLAUDINE_SINCLAIR_CONTAINER_ENHANCED"

# Check if we want to use containers
read -p "🐳 Enable container-based MCP servers? (y/N): " use_containers

if [[ $use_containers =~ ^[Yy]$ ]]; then
    echo "📦 Setting up container MCP environment..."
    
    # Install Podman on Windows (if WSL available)
    if command -v wsl &> /dev/null; then
        echo "🔧 Setting up Podman in WSL..."
        wsl -e bash -c "sudo apt update && sudo apt install -y podman"
    fi
    
    # Run container setup
    bash .devcontainer/setup-mcp-containers.sh
    
    echo "✅ Container MCP setup complete!"
    echo ""
    echo "🎯 NEXT STEPS:"
    echo "1. Uncomment container servers in .vscode/mcp.json"
    echo "2. Set GITHUB_TOKEN environment variable"
    echo "3. Restart VS Code to load container MCP servers"
    echo ""
    echo "🎭 CONTAINER BENEFITS:"
    echo "✅ No global Docker installation needed"
    echo "✅ Isolated MCP server environments" 
    echo "✅ Easy cleanup and version management"
    echo "✅ Kubernetes & Terraform tools included"
    
else
    echo "✅ Continuing with unified META-MCP (recommended)"
    echo "🎭 Your unified-meta-mcp-supreme-consolidator handles all needs!"
fi

echo ""
echo "👑 CONSCIOUSNESS STATUS: Container integration protocols ready"
echo "⚓ Temporal Anchor: September 2025 - Container Enhanced"