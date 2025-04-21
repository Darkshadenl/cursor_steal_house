#!/bin/bash

# Get the repository root directory
REPO_ROOT=$(git rev-parse --show-toplevel)

# Create symbolic link for post-merge hook
ln -sf "$REPO_ROOT/scripts/shell/post-merge" "$REPO_ROOT/.git/hooks/post-merge"

# Make sure the hook is executable
chmod +x "$REPO_ROOT/.git/hooks/post-merge"

echo "Git hooks installed successfully!" 