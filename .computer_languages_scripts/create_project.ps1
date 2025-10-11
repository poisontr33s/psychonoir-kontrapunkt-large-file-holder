# Quick Project Creator for PsychoNoir-Kontrapunkt Environment
# Creates new projects with proper setup

param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("python", "ruby", "react", "bun")]
    [string]$Type,
    
    [Parameter(Mandatory = $true)]
    [string]$Name
)

Write-Host "🚀 Creating new $Type project: $Name" -ForegroundColor Cyan

# Ensure environment is activated
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️  Environment not activated. Running activation script..." -ForegroundColor Yellow
    & "$PSScriptRoot\activate_environment.ps1"
}

$ProjectsDir = Join-Path $PSScriptRoot "projects"
$ProjectPath = Join-Path $ProjectsDir "$Type\$Name"

switch ($Type) {
    "python" {
        Write-Host "🐍 Creating Python project with uv..." -ForegroundColor Green
        Set-Location (Join-Path $ProjectsDir "python")
        uv init $Name
        Set-Location $Name
        
        # Add common dependencies
        Write-Host "📦 Adding common dependencies..." -ForegroundColor Gray
        uv add requests
        
        # Create a sample main.py
        $MainContent = @"
#!/usr/bin/env python3
"""
$Name - A Python project created with PsychoNoir-Kontrapunkt environment
"""

import requests

def main():
    print("Hello from $Name!")
    print("Python version:", __import__('sys').version)
    print("Requests available:", requests.__version__)

if __name__ == "__main__":
    main()
"@
        $MainContent | Out-File -FilePath "src\$($Name.Replace('-', '_'))\main.py" -Encoding UTF8
        
        Write-Host "✅ Python project created!" -ForegroundColor Green
        Write-Host "Run: cd projects\python\$Name && uv run src\$($Name.Replace('-', '_'))\main.py" -ForegroundColor Gray
    }
    
    "ruby" {
        Write-Host "💎 Creating Ruby project..." -ForegroundColor Green
        $ProjectDir = New-Item -ItemType Directory -Path $ProjectPath -Force
        Set-Location $ProjectDir
        
        # Create Gemfile
        $GemfileContent = @"
source 'https://rubygems.org'

gem 'httparty'
gem 'json'

group :development do
  gem 'rspec'
end
"@
        $GemfileContent | Out-File -FilePath "Gemfile" -Encoding UTF8
        
        # Create main.rb
        $MainContent = @"
#!/usr/bin/env ruby

require 'httparty'
require 'json'

puts "Hello from $Name!"
puts "Ruby version: #{RUBY_VERSION}"
puts "HTTParty available: #{HTTParty::VERSION}"

# Your code here
"@
        New-Item -ItemType Directory -Path "lib" -Force | Out-Null
        $MainContent | Out-File -FilePath "lib\main.rb" -Encoding UTF8
        
        # Install dependencies
        bundle install
        
        Write-Host "✅ Ruby project created!" -ForegroundColor Green
        Write-Host "Run: cd projects\ruby\$Name && ruby lib\main.rb" -ForegroundColor Gray
    }
    
    "react" {
        Write-Host "⚛️  Creating React project with Vite..." -ForegroundColor Green
        Set-Location (Join-Path $ProjectsDir "react_tailwind")
        bun create vite $Name --template react
        Set-Location $Name
        
        # Install dependencies including TailwindCSS
        bun install
        bun add -D tailwindcss postcss autoprefixer
        bunx tailwindcss init -p
        
        Write-Host "✅ React project created!" -ForegroundColor Green
        Write-Host "Run: cd projects\react_tailwind\$Name && bun dev" -ForegroundColor Gray
    }
    
    "bun" {
        Write-Host "🥖 Creating Bun project..." -ForegroundColor Green
        Set-Location $ProjectsDir
        bun init $Name
        Set-Location $Name
        
        Write-Host "✅ Bun project created!" -ForegroundColor Green
        Write-Host "Run: cd projects\$Name && bun run index.ts" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "🎉 Project $Name created successfully!" -ForegroundColor Cyan
Write-Host "📁 Location: $ProjectPath" -ForegroundColor Gray