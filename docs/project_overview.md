# StealHouse Project Overview

## Introduction
StealHouse is a Python-based web crawler system designed to collect rental property listings from various housing websites. The system uses modern LLMs (Large Language Models) and the crawl4ai library to intelligently extract and structure housing data.

## Project Goals
- Create a comprehensive database of rental properties from multiple sources
- Provide users with personalized housing recommendations
- Automate parts of the rental application process using AI

## Current Status
The project currently has a functional crawler for the Vesteda housing website. The system can:
- Log in to the Vesteda portal
- Browse available rental properties
- Extract property details into structured data
- Store data in a PostgreSQL database

## Future Plans
- Add support for additional housing websites
- Develop a React frontend to display property data
- Implement user preferences and matching algorithms
- Create automated application/motivation letter generation

## System Requirements
- Python 3.8+
- PostgreSQL
- Node.js (for frontend)
- API keys for supported LLM providers (Gemini, DeepSeek)

## Project Structure
```
├── docs/               # Documentation
├── python_scripts/     # Backend Python code
│   ├── crawlers/       # Web crawlers for different sites
│   ├── db_models/      # Database models and repositories
│   └── services/       # Shared services (LLM, etc.)
├── src/                # React frontend
└── docker-compose.yml  # Docker configuration
``` 