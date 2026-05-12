# Document Intelligence Extraction System

Production-ready document intelligence platform for extracting structured fields, classifying documents, and serving document analysis through APIs and CLI workflows.

## Features

- Document text normalization
- Rule-based field extraction
- Document classification
- Confidence scoring
- FastAPI extraction API
- CLI workflows for demo and analysis
- JSON document example
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest test suite
- Architecture and deployment documentation

## Quickstart

```bash
pip install .[dev]
docintel demo
uvicorn doc_intelligence.api:app --reload
pytest -q
```

## API

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/extract \
  -H 'Content-Type: application/json' \
  -d @sample_document.json
```

## Docker

```bash
docker-compose up --build
```

## Docs

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `sample_document.json`

## Portfolio Highlights

- Demonstrates document AI, extraction pipelines, API design, and production engineering
- Useful for invoices, contracts, forms, receipts, KYC, and enterprise document workflows
- Strong foundation for OCR, LLM extraction, vector search, human review queues, and enterprise document automation
