FROM crawl4ai-base-arm64
# FROM unclecode/crawl4ai:latest

# Set working directory
WORKDIR /app

USER root

# Install PostgreSQL development packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first for better caching
COPY requirements-docker.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy crawler code
COPY crawler_job /app/crawler_job

# Copy recipients file to the container
COPY recipients.txt /app/recipients.txt

# Set environment variables
ENV PYTHONPATH=/app
# Environment variable for verbose mode (can be overridden at runtime)
ENV CRAWLER_VERBOSE=False

ENV PLAYWRIGHT_BROWSERS_PATH=/home/appuser/.cache/ms-playwright

# Create directories for data and logs
RUN mkdir -p /app/logs \
    && mkdir -p /app/browser_data/vesteda \
    && chown -R appuser:appuser /app \
    && chown -R appuser:appuser /home/appuser 

# Create start script to launch Chrome browser and crawler
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

USER appuser

# Default command to run the start script
CMD ["/app/start.sh"]
