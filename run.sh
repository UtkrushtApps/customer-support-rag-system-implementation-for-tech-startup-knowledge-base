#!/bin/bash
set -e

echo "[INFO] Checking Docker daemon status..."
docker info > /dev/null 2>&1 || { echo '[ERROR] Docker daemon is not running.'; exit 1; }

echo "[INFO] Shutting down any existing chroma-db container."
docker-compose down

echo "[INFO] Starting Chroma DB service..."
docker-compose up -d chroma-db

MAX_TRIES=10
TRIES=0
until $(curl --output /dev/null --silent --head --fail http://localhost:8000/api/v1/heartbeat); do
    if [ $TRIES -ge $MAX_TRIES ]; then
      echo "[ERROR] Chroma DB service on localhost:8000 failed to respond after multiple attempts."
      exit 1
    fi
    TRIES=$((TRIES+1))
    echo "[INFO] Waiting for Chroma DB service to become ready... (try $TRIES)"
    sleep 2
done

echo "[INFO] Chroma DB service is running and accessible at http://localhost:8000"
echo "[INFO] Database is empty and ready for use."
