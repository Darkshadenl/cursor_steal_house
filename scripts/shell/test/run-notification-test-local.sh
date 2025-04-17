#!/bin/bash

# Build the Docker image
docker build -t stealhouse-crawler-prod .

# Run the Docker container
docker run \
  -e TEST_NOTIFICATIONS_ONLY=true \
  -e NOTIFICATION_CHANNELS_ACTIVE=email,pushover \
  -e EMAIL_RECIPIENTS_FILE=/app/recipients.txt \
  -e SMTP_SERVER=smtp.gmail.com \
  -e SMTP_PORT=587 \
  -e EMAIL_USER=mydutchproductions@gmail.com \
  -e EMAIL_PASSWORD=buxnazbreeohsnwb \
  -e PUSHOVER_TOKEN=ae2sbati9cyr32o8ya4v75e38ed7g7 \
  -e PUSHOVER_USER_KEY=u5vc2draseysnhv5bnw43z1ct5at6e \
  -v $(pwd)/recipients.txt:/app/recipients.txt \
  stealhouse-crawler-prod 