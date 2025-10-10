#!/usr/bin/env ruby
# MSYS2 RbConfig Path Conversion Patch
# Converts Windows paths in RbConfig to MSYS Unix paths for native extension compilation

puts "MSYS2 RbConfig patch loading... MSYSTEM: #{ENV['MSYSTEM']}"

require 'rbconfig'

# Only patch if we're in MSYS2 environment
if ENV['MSYSTEM']
  puts "MSYS2 environment detected, applying patch..."
  require 'open3'

  # Function to convert Windows path to MSYS path
  def convert_to_msys_path(path)
    return path unless path =~ /^[A-Za-z]:/

    begin
      stdout, stderr, status = Open3.capture3('cygpath', '-u', path)
      if status.success?
        stdout.strip
      else
        # Fallback: manual conversion with lowercase drive letter
        path.sub(/^([A-Za-z]):/, '/\1').gsub('\\', '/').downcase
      end
    rescue
      # Fallback: manual conversion with lowercase drive letter
      path.sub(/^([A-Za-z]):/, '/\1').gsub('\\', '/').downcase
    end
  end

  # Patch the CONFIG hash
  original_config = RbConfig::CONFIG.dup

  # Convert key paths that are used in Makefiles and file checks
  # Use Windows paths for includes and headers since MSYS GCC needs them
  # Keep libdir as Windows path for MSYS GCC compatibility
  %w[
    prefix
    rubylibdir
    archdir
    sitedir
    sitelibdir
    sitearchdir
    vendordir
    vendorlibdir
    vendorarchdir
  ].each do |key|
    if original_config[key] && original_config[key] =~ /^[A-Za-z]:/
      puts "Original #{key}: #{original_config[key]}"
      RbConfig::CONFIG[key] = convert_to_msys_path(original_config[key])
      puts "Patched #{key}: #{RbConfig::CONFIG[key]}"
    end
  end

  # Also patch MAKEFILE_CONFIG which mkmf.rb uses
  makefile_config = RbConfig::MAKEFILE_CONFIG.dup
  %w[
    prefix
    rubylibdir
    archdir
    sitedir
    sitelibdir
    sitearchdir
    vendordir
    vendorlibdir
    vendorarchdir
  ].each do |key|
    if makefile_config[key] && makefile_config[key] =~ /^[A-Za-z]:/
      RbConfig::MAKEFILE_CONFIG[key] = convert_to_msys_path(makefile_config[key])
    end
  end

  # Keep header and include paths as Windows paths for MSYS GCC compatibility
  %w[
    rubyhdrdir
    rubyarchhdrdir
    includedir
    archincludedir
    sitearchincludedir
    oldincludedir
    vendorarchhdrdir
    sitearchhdrdir
    vendorhdrdir
    sitehdrdir
  ].each do |key|
    if original_config[key] && original_config[key] =~ /^[A-Za-z]:/
      puts "Keeping Windows path for #{key}: #{original_config[key]}"
      # Keep as Windows path for MSYS GCC
    end
  end

  # Convert compiler commands to use MSYS GCC directly
  %w[CC CXX].each do |key|
    if original_config[key]
      puts "Original #{key}: #{original_config[key]}"
      # Use MSYS GCC directly (not through bash wrapper)
      msys_gcc = ENV['MSYS2_PATH'] ? "#{ENV['MSYS2_PATH']}/ucrt64/bin/#{original_config[key]}.exe" : "#{original_config[key]}.exe"
      RbConfig::CONFIG[key] = msys_gcc
      puts "Patched #{key}: #{RbConfig::CONFIG[key]}"
    end
  end

  # Convert compiler and linker flags that contain paths
  %w[
    CPPFLAGS
    CFLAGS
    LDFLAGS
    LIBRUBYARG
  ].each do |key|
    if original_config[key]
      RbConfig::CONFIG[key] = original_config[key].gsub(/([A-Za-z]:[^\s"']*)/) do |match|
        convert_to_msys_path(match)
      end
    end
  end

  # Set MAKE to use MSYS mingw32-make (should be in PATH)
  if original_config['MAKE'].nil? || original_config['MAKE'].empty?
    RbConfig::CONFIG['MAKE'] = 'mingw32-make.exe'
    RbConfig::MAKEFILE_CONFIG['MAKE'] = 'mingw32-make.exe'
    puts "Set MAKE: #{RbConfig::CONFIG['MAKE']}"
  end
else
  puts "MSYS2 environment not detected, skipping patch"
end

# Test the patch
if __FILE__ == $0
  puts "Testing RbConfig patch..."
  puts "rubyhdrdir: #{RbConfig::CONFIG['rubyhdrdir']}"
  puts "rubyarchhdrdir: #{RbConfig::CONFIG['rubyarchhdrdir']}"
  puts "libdir: #{RbConfig::CONFIG['libdir']}"
end