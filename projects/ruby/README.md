# Ruby Projects

This directory contains Ruby projects using the locally installed Ruby and development tools.

## Getting Started

1. **Activate the environment:**
   ```powershell
   cd ..\..\
   .\activate_environment.ps1
   ```

2. **Verify Ruby setup:**
   ```bash
   ruby -v           # Should show Ruby version
   gem -v            # RubyGems package manager
   ridk version      # Ruby DevKit (if installed)
   ```

3. **Create a new project:**
   ```bash
   cd projects/ruby
   mkdir my-project
   cd my-project
   gem init          # Create Gemfile
   ```

## Available Tools

- **Ruby**: Dynamic programming language
- **RubyGems**: Package manager for Ruby
- **DevKit**: Development toolkit with native extensions support
- **MSYS2**: Unix-like environment for Windows

## Example Project Structure

```
my-project/
├── Gemfile         # Dependency specification
├── Gemfile.lock    # Locked dependencies
├── lib/
│   └── my_project.rb
├── spec/
│   └── my_project_spec.rb
└── README.md
```

## Quick Commands

```bash
# Install dependencies
bundle install

# Add a gem dependency
echo 'gem "httparty"' >> Gemfile
bundle install

# Run Ruby script
ruby lib/my_project.rb

# Install global gem
gem install rails

# List installed gems
gem list

# Update gems
bundle update
```

## Common Ruby Frameworks

- **Rails**: Full-stack web framework
- **Sinatra**: Lightweight web framework
- **Jekyll**: Static site generator
- **RSpec**: Testing framework