#!/bin/bash

# echo "PLAYWRIGHT_BROWSERS_PATH is set to: $PLAYWRIGHT_BROWSERS_PATH"
# echo "Current user: $(whoami)"
# echo "Home directory: $HOME"

# echo "Contents of $PLAYWRIGHT_BROWSERS_PATH:"
# ls -lR "$PLAYWRIGHT_BROWSERS_PATH" || echo "Browser path not found or empty."

echo "Starting crawler..."
python -m crawler_job.main