#!/bin/bash

# Start the development environment
echo "Starting StealHouse development environment..."

# Build and start the containers
docker compose -f docker-compose-dev.yml build
docker compose -f docker-compose-dev.yml up

# Note: Use Ctrl+C to stop the development environment 