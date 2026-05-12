# Flask Server Start

A lightweight server health dashboard built with Python Flask,
containerised with Docker. Displays live CPU, memory, and disk
usage in the browser.

## What it shows
- CPU usage %
- Memory usage (used / total GB)
- Disk usage (used / total GB)

## Tech stack
- Python 3.11
- Flask
- psutil
- Docker + Docker Compose

## Run with Docker (easiest)

Pull and run directly from Docker Hub — no setup needed:

    docker run -p 5000:5000 navdeep11/flask-server-start

Open your browser at http://localhost:5000

## Run with Docker Compose

    git clone https://github.com/navdeepdhaliwal1/flask-server-start
    cd flask-server-start
    docker compose up

Open your browser at http://localhost:5000

## Run locally without Docker

    pip install flask psutil
    python3 app.py

Open your browser at http://localhost:5000

## Project structure

    flask-server-start/
    ├── app.py              # Flask app with stats endpoints
    ├── Dockerfile          # Container build instructions
    ├── docker-compose.yml  # Multi-container configuration
    └── requirements.txt    # Python dependencies

## Docker commands

    # Build the image
    docker build -t flask-server-start .

    # Run the container
    docker run -p 5000:5000 flask-server-start

    # Run in background
    docker compose up -d

    # Stop
    docker compose down

    # View logs
    docker compose logs

## Docker Hub

Image is publicly available at:
https://hub.docker.com/r/navdeep11/flask-server-start
