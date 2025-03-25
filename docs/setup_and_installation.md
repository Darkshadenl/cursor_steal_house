# StealHouse Setup and Installation Guide

## Prerequisites

Before setting up the StealHouse project, ensure you have the following prerequisites installed:

- Python 3.8 or higher
- Node.js 16 or higher
- Docker and Docker Compose
- Git

## Clone the Repository

```bash
git clone <repository-url>
cd steal_house
```

## Backend Setup

### 1. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root with the following variables:

```
# Database Configuration
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=steal_house
POSTGRES_PORT=5432
POSTGRES_HOST=localhost

# LLM API Keys
DEEPSEEK_API_KEY=your_deepseek_api_key
GOOGLE_API_KEY=your_google_api_key

# Vesteda Credentials (for crawler)
VESTEDA_EMAIL=your_vesteda_email
VESTEDA_PASSWORD=your_vesteda_password
```

### 4. Start the Database

```bash
docker-compose up -d
```

### 5. Run Database Migrations

```bash
alembic upgrade head
```

## Frontend Setup

### 1. Install JavaScript Dependencies

```bash
npm install
```

### 2. Start the Development Server

```bash
npm run dev
```

## Running the Crawler

### 1. Manual Execution

```bash
# Make sure you're in the virtual environment
cd python_scripts/crawlers/vesteda
python vesteda_crawler.py
```

### 2. Scheduled Execution

You can set up a cron job to run the crawler periodically:

```bash
# Example crontab entry (run daily at 8 AM)
0 8 * * * cd /path/to/steal_house && /path/to/venv/bin/python python_scripts/crawlers/vesteda/vesteda_crawler.py
```

## Troubleshooting

### Database Connection Issues

If you encounter database connection issues:

1. Check if the Docker container is running:
   ```bash
   docker ps
   ```

2. Verify database connection using psql:
   ```bash
   psql -h localhost -p 5432 -U your_user -d steal_house
   ```

### Crawler Issues

1. **Browser automation problems:**
   - Make sure the browser_data directory exists and is writable
   - Try running with headless=False to see what's happening

2. **Authentication failures:**
   - Verify your Vesteda credentials in the .env file
   - Check if the website structure has changed

### LLM Integration Issues

1. **API key errors:**
   - Verify your API keys in the .env file
   - Check API usage quotas and limits

2. **Extraction failures:**
   - Review the extraction schema to ensure it matches current website structure
   - Try using a different LLM provider 