#!/bin/bash

# StealHouse notification test runner
# This script runs the notification test job in Google Cloud

# Display a brief explanation
echo "StealHouse Notification Test"
echo "This will deploy and run a one-time notification test job in Google Cloud"
echo "No crawling will be performed - only notifications will be tested"
echo "----------------------------------------------------------------------"
echo ""

# Execute the build-push-test-job script
cd "$(dirname "$0")/.." # Navigate to project root
./ter\ test/build-push-test-job-google.sh 