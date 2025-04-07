#!/bin/bash

# Production deployment script for StealHouse crawler as a Cloud Run job
# This script builds, pushes, and deploys the Docker image as a Google Cloud Run job

# Set the absolute path to gcloud based on your installation
GCLOUD="/Users/quintenmeijboom/Downloads/google-cloud-sdk/bin/gcloud"

# Set variables
PROJECT_ID=$($GCLOUD config get-value project)
IMAGE_NAME="stealhouse-crawler-prod"
GCR_PATH="gcr.io/$PROJECT_ID/$IMAGE_NAME"
JOB_NAME="stealhouse-crawler-job"
REGION="europe-west4"  # Change this to your preferred region

# Build the production Docker image
echo "Building production Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME:latest -f Dockerfile.production .

# Tag the image for Google Container Registry
echo "Tagging image for Google Container Registry"
docker tag $IMAGE_NAME:latest $GCR_PATH:latest

# Push the image to Google Container Registry
echo "Pushing image to Google Container Registry"
docker push $GCR_PATH:latest

# Check if job already exists
if $GCLOUD run jobs describe $JOB_NAME --region=$REGION &>/dev/null; then
  echo "Updating existing Cloud Run job: $JOB_NAME"
  $GCLOUD run jobs update $JOB_NAME \
    --image $GCR_PATH:latest \
    --region=$REGION \
    --update-env-vars=POSTGRES_USER=$(grep POSTGRES_USER .env.prod | cut -d '=' -f2),POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD .env.prod | cut -d '=' -f2),POSTGRES_DB=$(grep POSTGRES_DB .env.prod | cut -d '=' -f2),POSTGRES_HOST=$(grep POSTGRES_HOST .env.prod | cut -d '=' -f2),VESTEDA_EMAIL=$(grep VESTEDA_EMAIL .env.prod | cut -d '=' -f2),VESTEDA_PASSWORD=$(grep VESTEDA_PASSWORD .env.prod | cut -d '=' -f2),DEEPSEEK_API_KEY=$(grep DEEPSEEK_API_KEY .env.prod | cut -d '=' -f2),GOOGLE_API_KEY=$(grep GOOGLE_API_KEY .env.prod | cut -d '=' -f2),CRAWLER_VERBOSE=False
else
  echo "Creating new Cloud Run job: $JOB_NAME"
  $GCLOUD run jobs create $JOB_NAME \
    --image $GCR_PATH:latest \
    --region=$REGION \
    --tasks=1 \
    --max-retries=3 \
    --task-timeout=1h \
    --memory=2Gi \
    --cpu=1 \
    --set-env-vars=POSTGRES_USER=$(grep POSTGRES_USER .env.prod | cut -d '=' -f2),POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD .env.prod | cut -d '=' -f2),POSTGRES_DB=$(grep POSTGRES_DB .env.prod | cut -d '=' -f2),POSTGRES_HOST=$(grep POSTGRES_HOST .env.prod | cut -d '=' -f2),VESTEDA_EMAIL=$(grep VESTEDA_EMAIL .env.prod | cut -d '=' -f2),VESTEDA_PASSWORD=$(grep VESTEDA_PASSWORD .env.prod | cut -d '=' -f2),DEEPSEEK_API_KEY=$(grep DEEPSEEK_API_KEY .env.prod | cut -d '=' -f2),GOOGLE_API_KEY=$(grep GOOGLE_API_KEY .env.prod | cut -d '=' -f2),CRAWLER_VERBOSE=False
fi

echo "Job deployment complete"
echo "Job name: $JOB_NAME"
echo "Region: $REGION"
echo ""
echo "To run the job manually:"
echo "$GCLOUD run jobs execute $JOB_NAME --region=$REGION"
echo ""
echo "To set up a schedule (daily at 3:00 AM):"
echo "$GCLOUD scheduler jobs create http ${JOB_NAME}-trigger \\
  --location=$REGION \\
  --schedule=\"0 3 * * *\" \\
  --uri=\"https://${REGION}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${PROJECT_ID}/jobs/${JOB_NAME}:run\" \\
  --http-method=POST \\
  --oauth-service-account-email=${PROJECT_ID}@appspot.gserviceaccount.com" 