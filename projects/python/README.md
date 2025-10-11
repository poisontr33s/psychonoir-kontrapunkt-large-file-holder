# Python Projects

This directory contains Python projects using the locally installed Python 3.14 and development tools.

## Getting Started

1. **Activate the environment:**
   ```powershell
   cd ..\..\
   .\activate_environment.ps1
   ```

2. **Verify Python setup:**
   ```bash
   python --version    # Should show Python 3.14.x
   uv --version       # Python package manager
   ruff --version     # Python linter
   ```

3. **Create a new project:**
   ```bash
   cd projects/python
   uv init my-project
   cd my-project
   uv add requests     # Add dependencies
   ```

## Available Tools

- **Python 3.14**: Latest Python interpreter
- **uv**: Fast Python package manager and virtual environment tool
- **ruff**: Lightning-fast Python linter and formatter

## Example Project Structure

```
my-project/
├── pyproject.toml    # Project configuration
├── src/
│   └── my_project/
│       └── __init__.py
├── tests/
│   └── test_example.py
└── README.md
```

## Quick Commands

```bash
# Create and activate virtual environment
uv venv
source .venv/Scripts/activate  # Windows

# Install dependencies
uv add requests pandas

# Run linting
ruff check .

# Format code
ruff format .

# Run Python script
python src/my_project/main.py
```