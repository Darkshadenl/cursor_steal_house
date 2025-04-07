# StealHouse Deployment Guide

This document outlines the deployment procedures for the StealHouse application, with a specific focus on the crawler component.

## Table of Contents
1. [Docker Setup](#docker-setup)
2. [Local Development Setup](#local-development-setup)
3. [Google Cloud Run Deployment](#google-cloud-run-deployment)
4. [Environment Variables](#environment-variables)
5. [Troubleshooting](#troubleshooting)

## Docker Setup

### Crawler Docker Configuration

The crawler is containerized using Docker with a custom configuration that supports both local development and cloud deployment scenarios.

#### Dockerfile Highlights

```dockerfile
FROM crawl4ai-base-arm64:latest

# Set working directory
WORKDIR /app

# Install PostgreSQL development packages and Cloud SQL Proxy dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    postgresql-client \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Cloud SQL Proxy
RUN wget https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.9.0/cloud-sql-proxy.linux.amd64 -O /usr/local/bin/cloud-sql-proxy \
    && chmod +x /usr/local/bin/cloud-sql-proxy

# Copy requirements.txt first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browser
RUN playwright install chromium && playwright install-deps

# Copy crawler code
COPY crawler_job /app/crawler_job

# Set environment variables
ENV PYTHONPATH=/app
# Environment variable for verbose mode (can be overridden at runtime)
ENV CRAWLER_VERBOSE=False

# Create a directory for logs
RUN mkdir -p /app/logs
# Create directory for browser data
RUN mkdir -p /app/browser_data/vesteda

# Start script to handle Cloud SQL Proxy integration
RUN echo '#!/bin/bash\n\
\n\
# Start Cloud SQL Proxy if CLOUD_SQL_INSTANCE is set\n\
if [ -n "$CLOUD_SQL_INSTANCE" ]; then\n\
  echo "Starting Cloud SQL Proxy for instance: $CLOUD_SQL_INSTANCE..."\n\
  # Start Cloud SQL Proxy in background\n\
  /usr/local/bin/cloud-sql-proxy --port=5432 "$CLOUD_SQL_INSTANCE" &\n\
  PROXY_PID=$!\n\
  \n\
  # Wait for proxy to start up\n\
  echo "Waiting for Cloud SQL Proxy to start..."\n\
  sleep 5\n\
  \n\
  # Override database host to use local proxy\n\
  export POSTGRES_HOST=127.0.0.1\n\
fi\n\
\n\
# Launch chrome in background with remote debugging\n\
echo "Starting Chrome with remote debugging..."\n\
\n\
# Get path to the Chromium executable\n\
CHROMIUM_PATH=$(find /root/.cache/ms-playwright -name chrome -type f | head -n 1)\n\
\n\
# Launch Chromium with remote debugging\n\
$CHROMIUM_PATH --headless --disable-gpu --remote-debugging-address=0.0.0.0 --remote-debugging-port=9222 --no-sandbox &\n\
\n\
# Wait for Chrome to start\n\
echo "Waiting for Chrome to start..."\n\
sleep 5\n\
\n\
# Run the crawler\n\
echo "Starting crawler..."\n\
python -m crawler_job.crawlers.vesteda.vesteda_crawler\n\
\n\
# If proxy was started, clean up\n\
if [ -n "$PROXY_PID" ]; then\n\
  echo "Stopping Cloud SQL Proxy..."\n\
  kill $PROXY_PID\n\
fi\n\
' > /app/start.sh && chmod +x /app/start.sh

# Default command to run the start script
CMD ["/app/start.sh"]
```

#### Key Features

1. **Base Image:** Uses the `crawl4ai-base-arm64` image which includes the Crawl4AI library and Playwright.
2. **PostgreSQL Support:** Installs the necessary PostgreSQL development packages to support database connections.
3. **Cloud SQL Proxy:** Integrates Google Cloud SQL Proxy for secure connections to Google Cloud SQL instances.
4. **Browser Configuration:** Sets up Chromium with remote debugging to support the `use_managed_browser=True` configuration used by the crawler.
5. **Environment Variables:** Configurable via Docker environment variables, including a `CRAWLER_VERBOSE` option.
6. **Start Script:** Includes a custom start script that:
   - Starts the Cloud SQL Proxy if `CLOUD_SQL_INSTANCE` is provided
   - Launches a headless Chrome browser with remote debugging
   - Runs the crawler with the proper configurations
   - Cleans up processes on completion

## Local Development Setup

### Building the Docker Image

To build the Docker image locally:

```bash
# Make sure you're in the project root directory
docker build -t stealhouse-crawler .
```

### Running the Crawler Locally

For local development with a local PostgreSQL database:

```bash
docker compose -f docker-compose-dev.yml up -d crawler
```

Note: Always use `docker compose` (without hyphen) as the modern replacement for `docker-compose`.

To run just the crawler container with a local database:

```bash
docker run -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=welkom123 \
  -e POSTGRES_DB=mydb \
  -e POSTGRES_HOST=host.docker.internal \
  -e POSTGRES_PORT=5432 \
  -e VESTEDA_EMAIL=your_email@example.com \
  -e VESTEDA_PASSWORD='your_password' \
  -e CRAWLER_VERBOSE=True \
  stealhouse-crawler
```

## Google Cloud Run Deployment

The crawler is designed to run as a scheduled job on Google Cloud Run, with secure access to Cloud SQL databases.

### Building and Pushing the Docker Image

```bash
# Build the image
docker build -t gcr.io/[YOUR-PROJECT-ID]/stealhouse-crawler .

# Push to Google Container Registry
docker push gcr.io/[YOUR-PROJECT-ID]/stealhouse-crawler
```

### Deploying as a Cloud Run Job

```bash
gcloud run jobs create stealhouse-crawler \
  --image gcr.io/[YOUR-PROJECT-ID]/stealhouse-crawler \
  --set-env-vars="CLOUD_SQL_INSTANCE=[YOUR-INSTANCE-CONNECTION-NAME]" \
  --set-env-vars="POSTGRES_USER=[DB-USER]" \
  --set-env-vars="POSTGRES_PASSWORD=[DB-PASSWORD]" \
  --set-env-vars="POSTGRES_DB=[DB-NAME]" \
  --set-env-vars="VESTEDA_EMAIL=[YOUR-EMAIL]" \
  --set-env-vars="VESTEDA_PASSWORD=[YOUR-PASSWORD]" \
  --set-env-vars="CRAWLER_VERBOSE=True"
```

### Setting Up a Schedule

To run the crawler job on a schedule (e.g., every 6 hours):

```bash
gcloud scheduler jobs create http stealhouse-crawler-scheduler \
  --schedule="0 */6 * * *" \
  --uri="https://[REGION]-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/[PROJECT-ID]/jobs/stealhouse-crawler:run" \
  --http-method=POST \
  --oauth-service-account-email=[SERVICE-ACCOUNT]@[PROJECT-ID].iam.gserviceaccount.com
```

### Cloud SQL Proxy Integration

The Docker image includes Cloud SQL Proxy for secure access to Cloud SQL instances. When `CLOUD_SQL_INSTANCE` is specified, the container will:

1. Start the Cloud SQL Proxy with the specified instance
2. Override `POSTGRES_HOST` to `127.0.0.1` to connect through the proxy
3. Securely connect to the database without exposing it to the public internet

This approach provides:
- Secure connections to Cloud SQL instances
- Automatic TLS encryption
- IAM-based authentication
- No need to expose the database to the public internet

## Environment Variables

The crawler supports the following environment variables:

| Variable             | Description                                                          | Required           | Default |
| -------------------- | -------------------------------------------------------------------- | ------------------ | ------- |
| `POSTGRES_USER`      | Database username                                                    | Yes                | -       |
| `POSTGRES_PASSWORD`  | Database password                                                    | Yes                | -       |
| `POSTGRES_DB`        | Database name                                                        | Yes                | -       |
| `POSTGRES_HOST`      | Database host address (set automatically when using Cloud SQL Proxy) | Yes                | -       |
| `POSTGRES_PORT`      | Database port                                                        | Yes                | 5432    |
| `VESTEDA_EMAIL`      | Email for Vesteda login                                              | Yes                | -       |
| `VESTEDA_PASSWORD`   | Password for Vesteda login                                           | Yes                | -       |
| `CRAWLER_VERBOSE`    | Enable verbose logging                                               | No                 | False   |
| `CLOUD_SQL_INSTANCE` | Cloud SQL instance connection name (format: project:region:instance) | Only for Cloud SQL | -       |

## Troubleshooting

### Common Docker Issues

1. **D-Bus Errors**: The crawler container may show D-Bus errors like:
   ```
   Unable to init server: Could not connect: Connection refused
   ```
   These are generally non-critical for headless operation and can be safely ignored.

2. **Browser Connection Issues**: If Chrome fails to start, check:
   - The `--no-sandbox` flag is present in the start script
   - The container has adequate memory (at least 1GB recommended)
   - You're running the latest version of the Docker image

3. **Database Connection Issues**:
   - For local development, ensure the host is set to `host.docker.internal`
   - For Cloud SQL, verify the instance name and service account permissions
   - Ensure the PostgreSQL port (default 5432) is not blocked by a firewall

### Cloud Run Specific Issues

1. **Service Account Permissions**: Ensure the service account has:
   - `cloudsql.client` role for Cloud SQL access
   - Appropriate roles for Secret Manager if used for credentials

2. **Memory and CPU Allocation**: For larger crawl jobs, increase the memory allocation:
   ```bash
   gcloud run jobs update stealhouse-crawler --memory 2Gi
   ```

3. **Timeout Issues**: If the crawler exceeds the default timeout:
   ```bash
   gcloud run jobs update stealhouse-crawler --timeout 30m
   ``` 