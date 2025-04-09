#!/bin/bash

# StealHouse crawler - Cloud Run job creation/update script
# This script creates or updates a Cloud Run job using an existing image and runs it immediately

# Set the absolute path to gcloud based on your installation
GCLOUD="/Users/quintenmeijboom/Downloads/google-cloud-sdk/bin/gcloud"

# Set variables
PROJECT_ID=$($GCLOUD config get-value project)
IMAGE_NAME="stealhouse-crawler-prod"
GCR_PATH="gcr.io/$PROJECT_ID/$IMAGE_NAME"
JOB_NAME="stealhouse-crawler-job"
REGION="europe-west4"  # Change this to your preferred region

echo "Using image: $GCR_PATH:latest"
echo "Deploying to region: $REGION"

# Check if job already exists
if $GCLOUD run jobs describe $JOB_NAME --region=$REGION &>/dev/null; then
  echo "Updating existing Cloud Run job: $JOB_NAME"
  $GCLOUD run jobs update $JOB_NAME \
    --image $GCR_PATH:latest \
    --region=$REGION \
    --update-env-vars=POSTGRES_USER=$(grep POSTGRES_USER .env.prod | cut -d '=' -f2),POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD .env.prod | cut -d '=' -f2),POSTGRES_DB=$(grep POSTGRES_DB .env.prod | cut -d '=' -f2),POSTGRES_PORT=$(grep POSTGRES_PORT .env.prod | cut -d '=' -f2),VESTEDA_EMAIL=$(grep VESTEDA_EMAIL .env.prod | cut -d '=' -f2),VESTEDA_PASSWORD=$(grep VESTEDA_PASSWORD .env.prod | cut -d '=' -f2),DEEPSEEK_API_KEY=$(grep DEEPSEEK_API_KEY .env.prod | cut -d '=' -f2),GOOGLE_API_KEY=$(grep GOOGLE_API_KEY .env.prod | cut -d '=' -f2),CRAWLER_VERBOSE=False,CLOUD_SQL_INSTANCE=$(grep CLOUD_SQL_INSTANCE .env.prod | cut -d '=' -f2)
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
    --set-env-vars=POSTGRES_USER=$(grep POSTGRES_USER .env.prod | cut -d '=' -f2),POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD .env.prod | cut -d '=' -f2),POSTGRES_DB=$(grep POSTGRES_DB .env.prod | cut -d '=' -f2),POSTGRES_PORT=$(grep POSTGRES_PORT .env.prod | cut -d '=' -f2),VESTEDA_EMAIL=$(grep VESTEDA_EMAIL .env.prod | cut -d '=' -f2),VESTEDA_PASSWORD=$(grep VESTEDA_PASSWORD .env.prod | cut -d '=' -f2),DEEPSEEK_API_KEY=$(grep DEEPSEEK_API_KEY .env.prod | cut -d '=' -f2),GOOGLE_API_KEY=$(grep GOOGLE_API_KEY .env.prod | cut -d '=' -f2),CRAWLER_VERBOSE=False,CLOUD_SQL_INSTANCE=$(grep CLOUD_SQL_INSTANCE .env.prod | cut -d '=' -f2)
fi

echo "Job deployment complete"
echo "Job name: $JOB_NAME"
echo "Region: $REGION"

# Run the job immediately
echo "Executing job..."
$GCLOUD run jobs execute $JOB_NAME --region=$REGION

echo ""
echo "Note: This job was executed manually and is not scheduled to run automatically."
echo "To set up a schedule in the future, use the Cloud Console or gcloud scheduler commands." 