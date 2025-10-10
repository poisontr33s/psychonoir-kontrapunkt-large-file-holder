#!/usr/bin/env ruby
# MSYS2 RbConfig Path Conversion Patch
# Converts Windows paths in RbConfig to MSYS Unix paths for native extension compilation

require 'rbconfig'

# Only patch if we're in MSYS2 environment
if ENV['MSYSTEM']
  require 'open3'

  # Function to convert Windows path to MSYS path
  def convert_to_msys_path(path)
    return path unless path =~ /^[A-Za-z]:/

    begin
      stdout, stderr, status = Open3.capture3('cygpath', '-u', path)
      if status.success?
        stdout.strip
      else
        # Fallback: manual conversion
        path.sub(/^([A-Za-z]):/, '/\1').gsub('\\', '/').downcase
      end
    rescue
      # Fallback: manual conversion
      path.sub(/^([A-Za-z]):/, '/\1').gsub('\\', '/').downcase
    end
  end

  # Patch the CONFIG hash
  original_config = RbConfig::CONFIG.dup

  # Convert key paths that are used in Makefiles
  %w[
    rubyhdrdir
    rubyarchhdrdir
    libdir
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
      RbConfig::CONFIG[key] = convert_to_msys_path(original_config[key])
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
end

# Test the patch
if __FILE__ == $0
  puts "Testing RbConfig patch..."
  puts "rubyhdrdir: #{RbConfig::CONFIG['rubyhdrdir']}"
  puts "rubyarchhdrdir: #{RbConfig::CONFIG['rubyarchhdrdir']}"
  puts "libdir: #{RbConfig::CONFIG['libdir']}"
end