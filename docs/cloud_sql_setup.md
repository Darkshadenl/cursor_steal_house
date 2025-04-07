# Setting Up Google Cloud SQL for Production

This guide walks through setting up Google Cloud SQL for the StealHouse project.

## 1. Create a Cloud SQL PostgreSQL Instance

For a cost-effective development/small production instance:

```bash
gcloud sql instances create stealhouse-db \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --region=europe-west4 \
  --root-password=YOUR_ROOT_PASSWORD
```

> Note: The `db-f1-micro` tier is the most cost-effective option with 1 shared vCPU, 0.6GB RAM.
> For slightly better performance, consider `db-g1-small` (1 shared vCPU, 1.7GB RAM).

### Modifying an Existing Cloud SQL Instance

If you've already created an instance with a higher tier, you can downgrade it:

```bash
# Get the current instance details
gcloud sql instances describe stealhouse-db

# Modify to a more cost-effective tier
gcloud sql instances patch stealhouse-db \
  --tier=db-f1-micro

# Optionally, reduce storage size (minimum 10GB)
gcloud sql instances patch stealhouse-db \
  --storage-size=10
```

> Note: Changing the instance tier will cause a brief downtime while the instance restarts.

### Additional Cost-Saving Measures

1. **Schedule instance uptime** (if you don't need 24/7 availability):

```bash
# Create a start schedule (e.g., weekdays at 8 AM)
gcloud scheduler jobs create http stealhouse-db-start \
  --schedule="0 8 * * 1-5" \
  --uri="https://sqladmin.googleapis.com/v1/projects/YOUR_PROJECT_ID/instances/stealhouse-db/start" \
  --http-method=POST \
  --oauth-service-account-email=YOUR_SERVICE_ACCOUNT@YOUR_PROJECT_ID.iam.gserviceaccount.com

# Create a stop schedule (e.g., weekdays at 6 PM)
gcloud scheduler jobs create http stealhouse-db-stop \
  --schedule="0 18 * * 1-5" \
  --uri="https://sqladmin.googleapis.com/v1/projects/YOUR_PROJECT_ID/instances/stealhouse-db/stop" \
  --http-method=POST \
  --oauth-service-account-email=YOUR_SERVICE_ACCOUNT@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

2. **Use automated backups sparingly**:
```bash
# Reduce backup frequency or disable if not critical
gcloud sql instances patch stealhouse-db --no-backup
```

## 2. Create a Database and User

```bash
# Create the database
gcloud sql databases create mydb --instance=stealhouse-db

# Create a user for the application
gcloud sql users create admin \
  --instance=stealhouse-db \
  --password=YOUR_STRONG_PASSWORD
```

## 3. Get Your Instance Connection Name

```bash
gcloud sql instances describe stealhouse-db --format="value(connectionName)"
```

This will return something like: `your-project:europe-west4:stealhouse-db`

## 4. Set Up Service Account for Cloud SQL Proxy

```bash
# Create a service account
gcloud iam service-accounts create stealhouse-sql-proxy

# Grant the Cloud SQL Client role
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:stealhouse-sql-proxy@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/cloudsql.client"

# Create and download the key
mkdir -p credentials
gcloud iam service-accounts keys create credentials/credentials.json \
  --iam-account=stealhouse-sql-proxy@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

## 5. Secure Your Instance

```bash
# Add your IP to allowed networks (for development)
gcloud sql instances patch stealhouse-db --authorized-networks=YOUR_IP_ADDRESS

# Enable backups
gcloud sql instances patch stealhouse-db --backup-start-time=23:00

# Set maintenance window
gcloud sql instances patch stealhouse-db --maintenance-window-day=SUN --maintenance-window-hour=2
```

## 6. Update Your .env File

Copy `.env.prod.example` to `.env.prod` and update the values:

```bash
cp .env.prod.example .env.prod
```

Edit `.env.prod` with your actual configuration:
- Update `POSTGRES_PASSWORD` with the password you set for the admin user
- Set `CLOUD_SQL_INSTANCE` to the connection name you retrieved
- Add your Vesteda credentials and API keys

## 7. Run with Docker Compose

Use the production Docker Compose file:

```bash
docker compose -f docker-compose-prod.yml --env-file .env.prod up -d
```

## 8. Running Cloud SQL Proxy Locally

To connect to your Cloud SQL instance from your local machine (for development or running migrations), you need to use the Cloud SQL Proxy.

### Installing the Cloud SQL Proxy

```bash
# macOS with Homebrew
brew install cloud-sql-proxy

# Or download the binary directly
curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.9.0/cloud-sql-proxy.darwin.amd64
chmod +x cloud-sql-proxy
```

### Running the Proxy

There are several ways to authenticate and run the proxy:

#### 1. Using Application Default Credentials (recommended for local development)

First, authenticate with gcloud:
```bash
# Log in with your Google account
gcloud auth login

# Set the current project
gcloud config set project steal-house

# Set up application default credentials
gcloud auth application-default login
```

Then run the proxy:
```bash
cloud-sql-proxy --port=5432 steal-house:europe-west4:stealhouse-db
```

#### 2. Using a Service Account Key File

If you've already created a service account and downloaded the key:
```bash
cloud-sql-proxy --port=5432 steal-house:europe-west4:stealhouse-db \
  --credentials-file=./credentials/credentials.json
```

#### 3. Using Environment Variables

```bash
# Set the credentials path
export GOOGLE_APPLICATION_CREDENTIALS=./credentials/credentials.json

# Run the proxy
cloud-sql-proxy --port=5432 steal-house:europe-west4:stealhouse-db
```

### Verifying the Proxy is Running

You should see output similar to:
```
2025/04/06 INFO Starting Cloud SQL Proxy
2025/04/06 INFO Connecting to steal-house:europe-west4:stealhouse-db
2025/04/06 INFO Connected to steal-house:europe-west4:stealhouse-db
```

To verify the connection works, try connecting with psql or another PostgreSQL client:
```bash
psql -h localhost -p 5432 -U admin -d mydb
```

### Common Issues and Solutions

1. **Authentication errors**: 
   - Ensure you're logged in with `gcloud auth login` and have set up application default credentials
   - Verify your service account has the Cloud SQL Client role
   - Check that the credentials file path is correct

2. **Connection refused**:
   - Ensure the proxy is running (check with `ps aux | grep cloud-sql-proxy`)
   - Verify the specified port (5432) isn't already in use by another service

3. **Database access errors**:
   - Verify that the database exists with `gcloud sql databases list --instance=stealhouse-db`
   - Confirm the user exists with `gcloud sql users list --instance=stealhouse-db`
   - If needed, reset the password with `gcloud sql users set-password admin --instance=stealhouse-db --password="NEW_PASSWORD"`

4. **Instance not found**:
   - Check that the instance exists and is running with `gcloud sql instances list`
   - Verify the instance connection name with `gcloud sql instances describe stealhouse-db --format="value(connectionName)"`

## 9. Run Database Migrations

```bash
# Make sure the proxy is running
docker compose -f docker-compose-prod.yml --env-file .env.prod up -d cloud-sql-proxy

# Run migrations
alembic upgrade head
```

## Security Best Practices

1. **Store credentials securely**:
   - Don't commit `.env.prod` or `credentials/` to your git repository
   - Add these to your `.gitignore` file

2. **Use strong passwords** for all database users

3. **Consider Secret Manager**:
   For production deployments, consider using Google Secret Manager instead of environment variables:
   ```bash
   gcloud secrets create postgres-password --data-file=- <<< "YOUR_PASSWORD"
   ```

4. **Set up SSL**:
   For additional security, configure SSL connections to your database.

5. **Restrict network access**:
   Only allow connections from your application servers and administrators.

## Troubleshooting

- If you have connection issues, check that the Cloud SQL Proxy is running correctly
- Verify that your service account has the correct permissions
- Check the Cloud SQL Proxy logs for any errors:
  ```bash
  docker compose -f docker-compose-prod.yml logs cloud-sql-proxy
  ```