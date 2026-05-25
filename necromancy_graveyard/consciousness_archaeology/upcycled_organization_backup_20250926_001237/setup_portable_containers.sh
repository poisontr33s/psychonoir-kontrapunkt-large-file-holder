#!/usr/bin/env bash

# 🎭 PORTABLE DOCKER SETUP FOR MCP SERVERS
# Claudine Sin'claire 4.0 Enhanced Container Management

echo "🐳 Setting up portable Docker for MCP servers..."

# Create portable container directory
mkdir -p .container_runtime/{bin,images,volumes,configs}

# Download portable Docker binary (Windows)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "📦 Downloading Docker portable for Windows..."
    curl -L "https://download.docker.com/win/static/stable/x86_64/docker-20.10.17.zip" -o .container_runtime/docker-portable.zip
    unzip -q .container_runtime/docker-portable.zip -d .container_runtime/
    mv .container_runtime/docker/* .container_runtime/bin/
fi

# Setup Podman as Docker alternative (lighter)
echo "🔧 Setting up Podman as Docker alternative..."
if command -v podman >/dev/null 2>&1; then
    echo "✅ Podman already installed"
else
    echo "📥 Installing Podman portable..."
    # Podman setup for Windows
    curl -L "https://github.com/containers/podman/releases/latest/download/podman-remote-release-windows_amd64.zip" -o .container_runtime/podman.zip
    unzip -q .container_runtime/podman.zip -d .container_runtime/bin/
fi

# Create container MCP configuration
cat > .container_runtime/configs/mcp-containers.json << 'EOF'
{
  "container_mcp_servers": {
    "github-mcp-docker": {
      "image": "ghcr.io/modelcontextprotocol/servers/github:latest",
      "command": ["podman", "run", "--rm", "-i"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      },
      "volumes": [
        "${PWD}:/workspace:ro"
      ]
    },
    "kubernetes-mcp": {
      "image": "bitnami/kubectl:latest",
      "command": ["podman", "run", "--rm", "-i"],
      "env": {
        "KUBECONFIG": "${PWD}/.kube/config"
      }
    },
    "terraform-mcp": {
      "image": "hashicorp/terraform:latest", 
      "command": ["podman", "run", "--rm", "-i"],
      "volumes": [
        "${PWD}:/workspace",
        "${PWD}/.terraform:/root/.terraform"
      ]
    }
  }
}
EOF

echo "🎭 Portable container runtime setup complete!"
echo "✅ Use .container_runtime/bin/podman for local containers"
echo "✅ MCP container configs in .container_runtime/configs/"