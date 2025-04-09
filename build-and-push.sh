#!/bin/bash

# StealHouse crawler - build and push script
# This script builds the Docker image for AMD64 platform and pushes it to Google Container Registry

# Set variables
PROJECT_ID=$(gcloud config get-value project)
IMAGE_NAME="stealhouse-crawler-prod"
GCR_PATH="gcr.io/$PROJECT_ID/$IMAGE_NAME"

# Build the production Docker image with platform specified
echo "Building production Docker image for linux/amd64 platform: $IMAGE_NAME"
docker buildx build --platform=linux/amd64 -t $IMAGE_NAME:latest -f Dockerfile.production .

# Tag the image for Google Container Registry
echo "Tagging image for Google Container Registry"
docker tag $IMAGE_NAME:latest $GCR_PATH:latest

# Push the image to Google Container Registry
echo "Pushing image to Google Container Registry"
docker push $GCR_PATH:latest

echo "Build and push complete"
echo "Image available at: $GCR_PATH:latest"
echo ""
echo "You can now use create-new-job.sh to deploy this image as a Cloud Run job" 