#!/bin/bash

# Run production container locally
# This script runs the production Docker container with environment variables from .env.prod

# Set image name
IMAGE_NAME="stealhouse-crawler-prod:latest"

# Check if .env.prod exists
if [ ! -f .env.prod ]; then
  echo "Error: .env.prod file not found"
  echo "Please create a .env.prod file with the required environment variables:"
  echo "- POSTGRES_USER"
  echo "- POSTGRES_PASSWORD"
  echo "- POSTGRES_DB"
  echo "- POSTGRES_PORT"
  echo "- POSTGRES_HOST"
  echo "- VESTEDA_EMAIL"
  echo "- VESTEDA_PASSWORD"
  echo "- DEEPSEEK_API_KEY"
  echo "- GOOGLE_API_KEY"
  echo "- CRAWLER_VERBOSE (optional, defaults to False)"
  exit 1
fi

# Make both scripts executable
chmod +x deploy-prod.sh
chmod +x run-prod-local.sh

echo "Running production container locally"
echo "Image: $IMAGE_NAME"
echo "Using environment variables from .env.prod"
echo ""

# Run the container with environment variables from .env.prod
docker run --env-file .env.prod -it $IMAGE_NAME 