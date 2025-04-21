#!/bin/bash

PLIST_PATH="/Users/quintenmeijboom/Library/LaunchAgents/com.stealhouse.development.plist"

cp com.stealhouse.development.plist "$PLIST_PATH"

if [ ! -f "$PLIST_PATH" ]; then
    echo "Error: Plist file not found at $PLIST_PATH"
    exit 1
fi

echo "Unloading plist file..."
launchctl unload "$PLIST_PATH"

echo "Loading plist file..."
launchctl load "$PLIST_PATH"

echo "Reload complete!"
