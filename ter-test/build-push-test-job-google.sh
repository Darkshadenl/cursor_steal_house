#!/bin/bash

# StealHouse notification test - build and push script
# This script builds the Docker image for AMD64 platform, pushes it to Google Container Registry,
# and deploys it as a one-time job that only tests notifications (no crawling)

# Set variables
PROJECT_ID=$(gcloud config get-value project)
IMAGE_NAME="stealhouse-notification-test"
GCR_PATH="gcr.io/$PROJECT_ID/$IMAGE_NAME"
JOB_NAME="stealhouse-notification-test-job"
REGION="europe-west3"  # Change this to your preferred region

# Build the production Docker image with platform specified
echo "Building notification test Docker image for linux/amd64 platform: $IMAGE_NAME"
docker buildx build --platform=linux/amd64 -t $IMAGE_NAME:latest -f Dockerfile.production .

# Tag the image for Google Container Registry
echo "Tagging image for Google Container Registry"
docker tag $IMAGE_NAME:latest $GCR_PATH:latest

# Push the image to Google Container Registry
echo "Pushing image to Google Container Registry"
docker push $GCR_PATH:latest

echo "Build and push complete"
echo "Image available at: $GCR_PATH:latest"

# Set the absolute path to gcloud based on your installation
GCLOUD="gcloud"

echo "Using image: $GCR_PATH:latest"
echo "Deploying to region: $REGION"

# Check if job already exists
if $GCLOUD run jobs describe $JOB_NAME --region=$REGION &>/dev/null; then
  echo "Updating existing Cloud Run job: $JOB_NAME"
  $GCLOUD run jobs update $JOB_NAME \
    --image $GCR_PATH:latest \
    --region=$REGION \
    --update-env-vars=POSTGRES_USER=$(grep POSTGRES_USER .env.prod | cut -d '=' -f2),POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD .env.prod | cut -d '=' -f2),POSTGRES_DB=$(grep POSTGRES_DB .env.prod | cut -d '=' -f2),POSTGRES_PORT=$(grep POSTGRES_PORT .env.prod | cut -d '=' -f2),TEST_NOTIFICATIONS_ONLY=true,NOTIFICATION_CHANNELS_ACTIVE=$(grep NOTIFICATION_CHANNELS_ACTIVE .env.prod | cut -d '=' -f2),EMAIL_RECIPIENTS_FILE="/app/recipients.txt",SMTP_SERVER=$(grep SMTP_SERVER .env.prod | cut -d '=' -f2),SMTP_PORT=$(grep SMTP_PORT .env.prod | cut -d '=' -f2),EMAIL_USER=$(grep EMAIL_USER .env.prod | cut -d '=' -f2),EMAIL_PASSWORD=$(grep EMAIL_PASSWORD .env.prod | cut -d '=' -f2),PUSHOVER_TOKEN=$(grep PUSHOVER_TOKEN .env.prod | cut -d '=' -f2),PUSHOVER_USER_KEY=$(grep PUSHOVER_USER_KEY .env.prod | cut -d '=' -f2),CLOUD_SQL_INSTANCE=$(grep CLOUD_SQL_INSTANCE .env.prod | cut -d '=' -f2)
else
  echo "Creating new Cloud Run job: $JOB_NAME"
  $GCLOUD run jobs create $JOB_NAME \
    --image $GCR_PATH:latest \
    --region=$REGION \
    --tasks=1 \
    --max-retries=0 \
    --task-timeout=15m \
    --memory=1Gi \
    --cpu=1 \
    --set-env-vars=POSTGRES_USER=$(grep POSTGRES_USER .env.prod | cut -d '=' -f2),POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD .env.prod | cut -d '=' -f2),POSTGRES_DB=$(grep POSTGRES_DB .env.prod | cut -d '=' -f2),POSTGRES_PORT=$(grep POSTGRES_PORT .env.prod | cut -d '=' -f2),TEST_NOTIFICATIONS_ONLY=true,NOTIFICATION_CHANNELS_ACTIVE=$(grep NOTIFICATION_CHANNELS_ACTIVE .env.prod | cut -d '=' -f2),EMAIL_RECIPIENTS_FILE="/app/recipients.txt",SMTP_SERVER=$(grep SMTP_SERVER .env.prod | cut -d '=' -f2),SMTP_PORT=$(grep SMTP_PORT .env.prod | cut -d '=' -f2),EMAIL_USER=$(grep EMAIL_USER .env.prod | cut -d '=' -f2),EMAIL_PASSWORD=$(grep EMAIL_PASSWORD .env.prod | cut -d '=' -f2),PUSHOVER_TOKEN=$(grep PUSHOVER_TOKEN .env.prod | cut -d '=' -f2),PUSHOVER_USER_KEY=$(grep PUSHOVER_USER_KEY .env.prod | cut -d '=' -f2),CLOUD_SQL_INSTANCE=$(grep CLOUD_SQL_INSTANCE .env.prod | cut -d '=' -f2)
fi

echo "Job deployment complete"
echo "Job name: $JOB_NAME"
echo "Region: $REGION"

# Run the job immediately (one-time execution)
echo "Executing notification test job now..."
$GCLOUD run jobs execute $JOB_NAME --region=$REGION

echo ""
echo "Notification test job has been executed. Check the Cloud Run logs for results."
echo "Job logs available at: https://console.cloud.google.com/run/jobs/$JOB_NAME/executions?project=$PROJECT_ID" 