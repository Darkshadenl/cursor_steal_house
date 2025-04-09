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

# Copy recipients file to the container
COPY recipients.txt /app/recipients.txt

# Set environment variables
ENV PYTHONPATH=/app
# Environment variable for verbose mode (can be overridden at runtime)
ENV CRAWLER_VERBOSE=False

# Create directories for data and logs
RUN mkdir -p /app/logs
RUN mkdir -p /app/browser_data/vesteda

# Create start script to launch Cloud SQL Proxy, Chrome browser, and crawler
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
    # Check if we should only run test notifications\n\
    if [ "$TEST_NOTIFICATIONS_ONLY" = "true" ]; then\n\
    echo "Running in test notifications only mode. Skipping Chrome startup..."\n\
    # Run the crawler with test notifications only\n\
    python -m crawler_job.crawlers.vesteda.vesteda_crawler\n\
    # Exit after testing notifications\n\
    exit 0\n\
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