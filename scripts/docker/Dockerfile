FROM crawl4ai-base:arm64

# Set working directory
WORKDIR /app

USER root

# Install PostgreSQL development packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    postgresql-client \
    bzip2 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements-docker.txt first for better caching
COPY requirements_docker.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements_docker.txt

# Copy crawler code
COPY crawler_job /app/crawler_job

# Copy recipients file to the container
COPY recipients_docker.json /app/recipients_docker.json

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

# Create .crawl4ai directory and chromium.path for crawl4ai
RUN mkdir -p /home/appuser/.crawl4ai \
    && printf "/home/appuser/.cache/ms-playwright/chromium-1179/chrome-linux/chrome" > /home/appuser/.crawl4ai/chromium.path \
    && chmod 444 /home/appuser/.crawl4ai/chromium.path

# Default command to run the start script
CMD ["/app/start.sh"]
