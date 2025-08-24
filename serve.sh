#!/bin/bash

# Local Jekyll development server script

# Set up gem paths for user installation
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"

echo "Starting Jekyll development server..."
echo "=================================="

# Check if Ruby is installed
if ! command -v ruby &> /dev/null; then
    echo "Ruby is not installed. Please install Ruby first:"
    echo "  sudo apt-get update"
    echo "  sudo apt-get install ruby-full build-essential zlib1g-dev"
    exit 1
fi

# Check if bundler is installed
if ! command -v bundle &> /dev/null; then
    echo "Installing bundler..."
    gem install bundler --user-install
fi

# Install dependencies if needed
if [ ! -f "Gemfile.lock" ]; then
    echo "Installing Jekyll dependencies..."
    bundle install
else
    echo "Updating Jekyll dependencies..."
    bundle update
fi

# Start Jekyll server
echo ""
echo "Starting Jekyll server..."
echo "Site will be available at: http://localhost:4000"
echo "Press Ctrl+C to stop the server"
echo ""

bundle exec jekyll serve --livereload --force_polling