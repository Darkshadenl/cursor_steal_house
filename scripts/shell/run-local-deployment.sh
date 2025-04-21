#!/bin/bash

# Define project root path
PROJECT_ROOT="/Users/quintenmeijboom/Documents/Repos/cursor_steal_house"

# Create logs directory if it doesn't exist
mkdir -p "$PROJECT_ROOT/logs"
LOG_FILE="$PROJECT_ROOT/logs/docker_cron.log"

# Log start time with permissions information
echo "===== Starting containers at $(date) =====" >> "$LOG_FILE"
echo "Script running as: $(whoami)" >> "$LOG_FILE"
echo "Script permissions: $(ls -la $0)" >> "$LOG_FILE"

# Keep Mac awake for 10 minutes
caffeinate -i -t 600 &
CAFFEINE_PID=$!

# Log working directory
echo "Project directory: $PROJECT_ROOT" >> "$LOG_FILE"

# Start the crawler container
/usr/local/bin/docker start stealhouse-crawler

# Check if containers are running and log results
echo "Container status:" >> "$LOG_FILE"
/usr/local/bin/docker ps -a | grep stealhouse-crawler >> "$LOG_FILE"
echo "---------------------" >> "$LOG_FILE"

# Cleanup caffeine process
kill $CAFFEINE_PID 2>/dev/null
