FROM python:3.9-slim

WORKDIR /app

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    procps \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome for browser automation
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python application files
COPY python_scripts/ ./python_scripts/
COPY alembic.ini .

# Create directory for browser data
RUN mkdir -p ./browser_data/vesteda

# Set environment variables (these will be overridden at runtime)
ENV POSTGRES_USER=placeholder
ENV POSTGRES_PASSWORD=placeholder
ENV POSTGRES_DB=placeholder
ENV POSTGRES_PORT=5432
ENV POSTGRES_HOST=placeholder
ENV DEEPSEEK_API_KEY=placeholder
ENV GOOGLE_API_KEY=placeholder
ENV VESTEDA_EMAIL=placeholder
ENV VESTEDA_PASSWORD=placeholder

# Command to run the crawler
CMD ["python", "-m", "python_scripts.crawlers.vesteda.vesteda_crawler"] 