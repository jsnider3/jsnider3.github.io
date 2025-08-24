source "https://rubygems.org"

# GitHub Pages gem includes Jekyll and all whitelisted plugins
gem "github-pages", group: :jekyll_plugins

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1", :install_if => Gem.win_platform?

# kramdown parser for markdown
gem "kramdown-parser-gfm"