FROM crawl4ai-base-arm64:latest

# Set working directory
WORKDIR /app

# Install PostgreSQL development packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

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

# Create start script to launch browser and crawler
RUN echo '#!/bin/bash\n\
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
    ' > /app/start.sh && chmod +x /app/start.sh

# Default command to run the start script
CMD ["/app/start.sh"]