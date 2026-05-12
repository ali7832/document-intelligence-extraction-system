# Deployment Guide

## Local Development

```bash
pip install .[dev]
uvicorn doc_intelligence.api:app --reload
```

## CLI Demo

```bash
docintel demo
docintel analyze sample_document.json
```

## Docker

```bash
docker build -t document-intelligence .
docker run -p 8000:8000 document-intelligence
```

## Docker Compose

```bash
docker-compose up --build
```

## Health Check

```bash
curl http://localhost:8000/health
```

## Extract Document Fields

```bash
curl -X POST http://localhost:8000/extract \
  -H 'Content-Type: application/json' \
  -d @sample_document.json
```
