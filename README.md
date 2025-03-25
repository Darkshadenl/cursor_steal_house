# StealHouse Project

StealHouse is a Python-based web crawler system designed to collect rental property listings from various housing websites using modern LLMs (Large Language Models) and the crawl4ai library to intelligently extract and structure housing data.

## Project Overview

The system consists of:
- Python crawler for housing websites (currently supports Vesteda)
- PostgreSQL database for data storage
- LLM integration for intelligent data extraction
- React frontend (in development) for data visualization

## Project Structure

```
├── docs/               # Documentation
├── python_scripts/     # Backend Python code
│   ├── crawlers/       # Web crawlers for different sites
│   ├── db_models/      # Database models and repositories
│   └── services/       # Shared services (LLM, etc.)
├── src/                # React frontend
└── docker-compose.yml  # Local Docker configuration
```

## Local Development Setup

### Prerequisites

- Python 3.8+
- Node.js 16+
- Docker and Docker Compose
- Git

### Backend Setup

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root with required variables (see `.env.example`).

4. **Start the database**:
   ```bash
   docker-compose up -d
   ```

5. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

### Running the Crawler Locally

```bash
cd python_scripts/crawlers/vesteda
python vesteda_crawler.py
```

### Frontend Development

```bash
npm install
npm run dev
```

## Deployment Options

This project can be deployed to Google Cloud Platform in several ways:

### 1. Manual Deployment with `deploy-cloud-run.sh`

This approach uses a bash script to deploy directly from your local machine:

1. **Set up Google Cloud CLI and authentication**:
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

2. **Update the project ID in the script**:
   Edit `deploy-cloud-run.sh` and set your Google Cloud project ID.

3. **Run the deployment script**:
   ```bash
   chmod +x deploy-cloud-run.sh
   ./deploy-cloud-run.sh
   ```

This script will:
- Build the Docker image locally
- Push the image to Google Container Registry
- Deploy to Cloud Run with environment variables from your `.env` file

### 2. CI/CD with Cloud Build

For automated deployment from your GitHub repository:

1. **Connect your repository to Cloud Build**:
   - In Google Cloud Console, go to Cloud Build → Triggers
   - Connect your GitHub repository
   - Create a trigger for the main branch

2. **Set up secrets in Secret Manager**:
   ```bash
   chmod +x cloud_secrets_setup.sh
   # Update PROJECT_ID in the script
   ./cloud_secrets_setup.sh
   ```

3. **Push to your repository**:
   ```bash
   git add .
   git commit -m "Deploy to Cloud Run"
   git push
   ```

The build will automatically:
- Build the Docker image
- Deploy to Cloud Run
- Inject environment variables from Secret Manager

### 3. Infrastructure as Code with Terraform

For reproducible infrastructure deployment:

1. **Initialize Terraform**:
   ```bash
   terraform init
   ```

2. **Apply the configuration**:
   ```bash
   terraform apply -var="project_id=YOUR_PROJECT_ID"
   ```

This will create:
- Secrets in Secret Manager
- A service account with appropriate permissions
- The Cloud Run service
- A Cloud Scheduler job for periodic execution

## Database Options for Cloud Deployment

### Option 1: Cloud SQL (Recommended for Production)

1. Create a Cloud SQL PostgreSQL instance in Google Cloud
2. Update the database connection parameters in your secrets
3. Run migrations:
   ```bash
   # Install Cloud SQL Proxy
   curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.0.0/cloud-sql-proxy.linux.amd64
   chmod +x cloud-sql-proxy
   
   # Connect to Cloud SQL
   ./cloud-sql-proxy --port 5432 YOUR_PROJECT:YOUR_REGION:YOUR_INSTANCE
   
   # In another terminal
   alembic upgrade head
   ```

### Option 2: Connect to Existing Docker Container

Requires exposing your Docker container to the internet with appropriate security measures:

1. Configure port forwarding or a public IP address
2. Set up firewall rules and security
3. Update the `POSTGRES_HOST` environment variable

## Scheduled Crawler Execution

The crawler can be scheduled to run periodically using Cloud Scheduler:

1. In Google Cloud Console, go to Cloud Scheduler
2. Create a new job that targets your Cloud Run service
3. Set the schedule (e.g., `0 8 * * *` for daily at 8 AM)
4. Use the service account created during deployment

## Monitoring and Logs

- View logs in Google Cloud Logging
- Set up alerts for crawler failures in Cloud Monitoring
- Check Cloud Run metrics for resource usage

## Known Issues and Limitations

- The crawler requires Chrome browser, which is included in the container
- Memory usage can be high due to browser automation
- Long-running crawls may hit Cloud Run timeouts (currently set to 3600s)

## Contributing

Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
