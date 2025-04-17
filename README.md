Ok, hier is de aangepaste versie van de documentatie:

# StealHouse Project

StealHouse is a Python-based web crawler system designed to collect rental property listings from various housing websites using modern LLMs (Large Language Models) and the crawl4ai library to intelligently extract and structure housing data.

## Project Overview

The system consists of:
- Python crawler for housing websites (currently supports Vesteda)
- PostgreSQL database for data storage with unified houses schema
- LLM integration for intelligent data extraction
- Notification system (Email, Pushover, Telegram)
- React frontend (in development) for data visualization

## Project Structure

````
├── docs/               # Documentation
├── scripts/            # Scripts and configuration files
│   ├── shell/          # Shell scripts for deployment and maintenance
│   └── docker/         # Docker configuration files
├── crawler_job/        # Backend Python code for crawler
├── tests/              # Test files
└── requirements.txt    # Python dependencies
````

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
   docker-compose -f scripts/docker/docker-compose-local-dev.yml up -d
   ```

5. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

### Running the Crawler Locally

```bash
# Run the Vesteda crawler directly
python -m crawler_job.crawlers.vesteda.vesteda_crawler
```

### Notification System

The system includes support for notifications when new properties are discovered. Supported channels:

1. **Email**: Sends notifications via SMTP
2. **Pushover**: Sends push notifications via the Pushover service
3. **Telegram**: Sends messages via Telegram bot

To configure notifications:

1. Set `NOTIFICATION_CHANNELS_ACTIVE` in your `.env` file to a comma-separated list of channels you want to activate (e.g., `email,pushover,telegram`)
2. Configure the credentials for each channel in your `.env` file:
   - For Email: `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_USER`, `EMAIL_PASSWORD`, `NOTIFICATION_RECIPIENT_EMAIL`
   - For Pushover: `PUSHOVER_TOKEN`, `PUSHOVER_USER_KEY`
   - For Telegram: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`

See `.env.example` for all required configuration options.

### Frontend Development

```bash
npm install
npm run dev
```

## Testing Notifications

You can test if the notification system is working properly by using the following environment variables:

- `TEST_NOTIFICATIONS_ONLY=true` - Only send test notifications without starting the crawler

These can be added to your `.env` file or set directly when running the container:

```bash
# To only run the notification test without crawling
docker run -e TEST_NOTIFICATIONS_ONLY=true <container_name>
```

This is especially useful when testing the notification setup in Docker environments or on deployment.

You can also use the provided scripts in the `scripts` directory:

```bash
# Build and push the Docker image to Google Container Registry
bash scripts/shell/build-and-push-google.sh

# Create or update a Cloud Run job
bash scripts/shell/create-new-job-google.sh

# Run both of the above scripts in sequence
bash scripts/shell/full-deployment.sh
```

## Database Schema

The database uses a unified `houses` table that stores all property information in a single table. This simplifies the data model and improves query performance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.