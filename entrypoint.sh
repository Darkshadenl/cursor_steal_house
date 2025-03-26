#!/bin/sh
# Start cron daemon in background
cron

# Start Flask server in foreground
exec flask run --host=0.0.0.0 --port=5001 