#!/bin/bash

# Production deployment script for StealHouse crawler
# This script builds and pushes the Docker image to Google Container Registry

# Set variables
PROJECT_ID=$(gcloud config get-value project)
IMAGE_NAME="stealhouse-crawler-prod"
GCR_PATH="gcr.io/$PROJECT_ID/$IMAGE_NAME"

# Build the production Docker image
echo "Building production Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME:latest -f Dockerfile.production .

# Tag the image for Google Container Registry
echo "Tagging image for Google Container Registry"
docker tag $IMAGE_NAME:latest $GCR_PATH:latest

# Push the image to Google Container Registry
echo "Pushing image to Google Container Registry"
docker push $GCR_PATH:latest

echo "Deployment image preparation complete"
echo "Image available at: $GCR_PATH:latest"
echo ""
echo "To deploy to Cloud Run, use:"
echo "gcloud run deploy stealhouse-crawler --image $GCR_PATH:latest --region=your-region --platform=managed --allow-unauthenticated=false" 