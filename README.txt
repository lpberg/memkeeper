# Memkeeper
Memkeeper is a lightweight Flask web application for storing and viewing memories.

## Setup
1. Python3 or greater installed.
2.Install any python modules listed in requirements.txt.
3. Create memories directory in project directory
4. Update docker-compose.yaml to ensure proper mounts

## Building from Dockerfile
docker build --tag py-memkeeper .

## Start docker container
docker compose up -d 
