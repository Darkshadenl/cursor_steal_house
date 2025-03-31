Ok, hier is de aangepaste versie van de documentatie:

# StealHouse Project

StealHouse is a Python-based web crawler system designed to collect rental property listings from various housing websites using modern LLMs (Large Language Models) and the crawl4ai library to intelligently extract and structure housing data.

## Project Overview

The system consists of:
- Python crawler for housing websites (currently supports Vesteda)
- PostgreSQL database for data storage
- LLM integration for intelligent data extraction
- React frontend (in development) for data visualization

## Project Structure

````
├── docs/               # Documentation
├── python_scripts/     # Backend Python code
│   ├── crawlers/       # Web crawlers for different sites
│   ├── db_models/      # Database models and repositories
│   └── services/       # Shared services (LLM, etc.)
├── src/                # React frontend
└── docker-compose.yml  # Local Docker configuration
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
   docker-compose -f docker-compose-local-dev.yml up -d
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.