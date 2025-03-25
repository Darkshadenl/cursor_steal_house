#!/bin/bash
set -e

# Configuration
PROJECT_ID="steal-house-project"  # Replace with your actual Google Cloud project ID

# Check if .env file exists
if [ ! -f .env ]; then
  echo "Error: .env file not found!"
  exit 1
fi

# Create secrets from .env file
echo "Creating secrets in Google Cloud Secret Manager..."

# Set up secret storage
create_secret_from_env() {
  local SECRET_NAME=$1
  local SECRET_VALUE=$2
  
  # Check if secret already exists
  if gcloud secrets describe $SECRET_NAME --project=$PROJECT_ID >/dev/null 2>&1; then
    echo "Secret $SECRET_NAME already exists. Updating..."
    echo -n "$SECRET_VALUE" | gcloud secrets versions add $SECRET_NAME --data-file=- --project=$PROJECT_ID
  else
    echo "Creating new secret $SECRET_NAME..."
    echo -n "$SECRET_VALUE" | gcloud secrets create $SECRET_NAME --data-file=- --project=$PROJECT_ID
  fi
}

# Process each line in .env file
while IFS= read -r line || [[ -n "$line" ]]; do
  # Skip comments and empty lines
  [[ $line =~ ^\s*# ]] && continue
  [[ -z "$line" ]] && continue
  
  # Extract variable name and value
  if [[ $line =~ ^([^=]+)=(.*)$ ]]; then
    VAR_NAME="${BASH_REMATCH[1]}"
    VAR_VALUE="${BASH_REMATCH[2]}"
    
    # Create or update secret
    create_secret_from_env $VAR_NAME "$VAR_VALUE"
  fi
done < .env

echo "Done creating secrets."

# Create service account if it doesn't exist
SERVICE_ACCOUNT="steal-house-crawler"
if ! gcloud iam service-accounts describe $SERVICE_ACCOUNT@$PROJECT_ID.iam.gserviceaccount.com >/dev/null 2>&1; then
  echo "Creating service account $SERVICE_ACCOUNT..."
  gcloud iam service-accounts create $SERVICE_ACCOUNT \
    --display-name="StealHouse Crawler Service Account" \
    --description="Service account for the StealHouse crawler running in Cloud Run" \
    --project=$PROJECT_ID
fi

# Grant secret accessor role to service account
echo "Granting secret accessor permissions to service account..."
while IFS= read -r line || [[ -n "$line" ]]; do
  # Skip comments and empty lines
  [[ $line =~ ^\s*# ]] && continue
  [[ -z "$line" ]] && continue
  
  # Extract variable name
  if [[ $line =~ ^([^=]+)= ]]; then
    SECRET_NAME="${BASH_REMATCH[1]}"
    
    gcloud secrets add-iam-policy-binding $SECRET_NAME \
      --member="serviceAccount:$SERVICE_ACCOUNT@$PROJECT_ID.iam.gserviceaccount.com" \
      --role="roles/secretmanager.secretAccessor" \
      --project=$PROJECT_ID
  fi
done < .env

echo "Secret setup complete!" 