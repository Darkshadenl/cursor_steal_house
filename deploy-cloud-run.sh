#!/bin/bash
set -e

# Configuration
PROJECT_ID="steal-house-project"  # Replace with your actual Google Cloud project ID
REGION="europe-west4"             # Replace with your preferred region
SERVICE_NAME="steal-house-crawler"
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME:latest"

# Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Push the image to Google Container Registry
echo "Pushing image to GCR..."
docker push $IMAGE_NAME

# Deploy to Cloud Run with environment variables from .env file
echo "Deploying to Cloud Run..."

# Read environment variables from .env file
if [ -f .env ]; then
  ENV_VARS=""
  while IFS= read -r line || [[ -n "$line" ]]; do
    # Skip comments and empty lines
    [[ $line =~ ^\s*# ]] && continue
    [[ -z "$line" ]] && continue
    
    # Extract variable name and value
    if [[ $line =~ ^([^=]+)=(.*)$ ]]; then
      VAR_NAME="${BASH_REMATCH[1]}"
      VAR_VALUE="${BASH_REMATCH[2]}"
      
      # Add to env vars string, properly escaped
      ENV_VARS="$ENV_VARS,${VAR_NAME}=${VAR_VALUE}"
    fi
  done < .env
  
  # Remove leading comma
  ENV_VARS="${ENV_VARS:1}"
  
  echo "Loaded environment variables from .env file"
else
  echo "Error: .env file not found!"
  exit 1
fi

# Deploy to Cloud Run
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --set-env-vars "$ENV_VARS" \
  --memory 2Gi \
  --cpu 1 \
  --timeout 3600 \
  --no-allow-unauthenticated \
  --max-instances 1

echo "Deployment complete!" 