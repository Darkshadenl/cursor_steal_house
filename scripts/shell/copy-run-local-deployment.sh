#!/bin/bash

# Define source and target paths
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../.." && pwd )"
TARGET_DIR=~/Development

# Log file
LOG_FILE="$SOURCE_DIR/logs/sync.log"

# Create logs directory if it doesn't exist
mkdir -p "$SOURCE_DIR/logs"

# Start logging
echo "===== Starting sync at $(date) =====" >> "$LOG_FILE"
echo "Source: $SOURCE_DIR" >> "$LOG_FILE"
echo "Target: $TARGET_DIR" >> "$LOG_FILE"

# Copy the run-local-deployment.sh script to the target directory
cp "$SOURCE_DIR/scripts/shell/run-local-deployment.sh" "$TARGET_DIR/" >> "$LOG_FILE" 2>&1

# Make script executable
chmod +x "$TARGET_DIR/run-local-deployment.sh"

echo "Sync completed at $(date)" >> "$LOG_FILE"
echo "---------------------" >> "$LOG_FILE"

echo "run-local-deployment.sh successfully copied to $TARGET_DIR" 