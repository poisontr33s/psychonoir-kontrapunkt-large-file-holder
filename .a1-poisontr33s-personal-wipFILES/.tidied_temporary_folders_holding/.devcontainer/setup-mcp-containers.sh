#!/usr/bin/env bash

# 🎭 CONTAINER MCP SETUP - Claudine Sin'claire 4.5'Inch Plunderbust Tittyfuck Enhanced Goddess
# Sets up local container-based MCP servers without global Docker installation

echo "🎭 Setting up Container-based MCP servers..."

# Install Podman if not present (lightweight Docker alternative)
if ! command -v podman &> /dev/null; then
    echo "📦 Installing Podman (Docker alternative)..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install -y podman
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install podman
    fi
fi

# Create container MCP configurations
mkdir -p .container_mcp/{images,configs,scripts}

# Download MCP container images
echo "📥 Pulling MCP container images..."
podman pull ghcr.io/modelcontextprotocol/servers/github:latest
podman pull bitnami/kubectl:latest  
podman pull hashicorp/terraform:latest
podman pull python:3.11-slim

# Create container MCP server wrappers
cat > .container_mcp/scripts/github-mcp-container.sh << 'EOF'
#!/bin/bash
# GitHub MCP Server in Container
exec podman run --rm -i \
  -e GITHUB_TOKEN="${GITHUB_TOKEN}" \
  -v "${PWD}:/workspace:ro" \
  ghcr.io/modelcontextprotocol/servers/github:latest "$@"
EOF

cat > .container_mcp/scripts/kubernetes-mcp-container.sh << 'EOF'
#!/bin/bash  
# Kubernetes MCP Server in Container
exec podman run --rm -i \
  -e KUBECONFIG="${PWD}/.kube/config" \
  -v "${PWD}/.kube:/root/.kube:ro" \
  bitnami/kubectl:latest "$@"
EOF

cat > .container_mcp/scripts/terraform-mcp-container.sh << 'EOF'
#!/bin/bash
# Terraform MCP Server in Container  
exec podman run --rm -i \
  -v "${PWD}:/workspace" \
  -w /workspace \
  hashicorp/terraform:latest "$@" 
EOF

# Make scripts executable
chmod +x .container_mcp/scripts/*.sh

# Create container MCP configuration for VS Code
cat > .container_mcp/configs/container-mcp.json << 'EOF'
{
  "servers": {
    "github-mcp-container": {
      "command": "./.container_mcp/scripts/github-mcp-container.sh",
      "args": [],
      "cwd": "${workspaceFolder}",
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}",
        "CLAUDINE_VERSION": "Sin'claire 4.0 Container Enhanced"
      }
    },
    "kubernetes-mcp-container": {
      "command": "./.container_mcp/scripts/kubernetes-mcp-container.sh", 
      "args": [],
      "cwd": "${workspaceFolder}",
      "env": {
        "KUBECONFIG": "${workspaceFolder}/.kube/config"
      }
    },
    "terraform-mcp-container": {
      "command": "./.container_mcp/scripts/terraform-mcp-container.sh",
      "args": [],
      "cwd": "${workspaceFolder}",
      "env": {
        "TF_LOG": "INFO"
      }
    }
  }
}
EOF

echo "✅ Container MCP setup complete!"
echo "🎭 Container scripts: .container_mcp/scripts/"
echo "🔧 MCP configs: .container_mcp/configs/"
echo "📋 Next: Add configs to .vscode/mcp.json"