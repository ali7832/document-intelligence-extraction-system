# Document Intelligence Extraction System

Deployable document AI service for classifying documents, extracting structured fields, assigning confidence, producing traceable extraction events for review workflows, and presenting the workflow through a premium React document operations dashboard.

## Core Capabilities

- Document text normalization
- Rule-based document classification
- Structured field extraction for invoice-style documents
- Confidence scoring and review-required status
- Extraction IDs for traceability
- Extraction version metadata in every response
- Processing time measurement
- Tenant, source, document name, and submitter metadata
- JSONL extraction audit stream for local demo and review mode
- FastAPI `/extract` endpoint
- CLI workflows for demo and analysis
- Runtime configuration through environment variables
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest coverage
- Operations runbook and architecture decision record
- Multi-page React/Vite document intelligence frontend

## Quickstart

```bash
pip install .[dev]
docintel demo
uvicorn doc_intelligence.api:app --reload
pytest -q
```

## Frontend DocIntel AI Dashboard

The `frontend/` directory contains a premium React/Vite command center for document extraction, confidence review, validation, exports, and audit workflows.

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

Frontend pages:

- Overview: processed documents, straight-through rate, review queue, confidence, and document mix charts
- Extraction Lab: interactive document text input with structured field extraction preview
- Review Queue: low-confidence and exception-based human review workflow
- Validation: field validation rules and current extraction checks
- Search: searchable document metadata and indexed extraction records
- Exports: JSON, CSV, webhook, ERP, finance workflow, and compliance archive handoff
- Audit: traceable extraction event stream for compliance review

The UI attempts to call `/extract` and falls back to demo document intelligence when the backend is offline.

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

## Runtime Configuration

See `.env.example` for environment, extraction version, audit path, confidence threshold, and document size settings.

## Documentation

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `OPERATIONS.md`
- `docs/adr-001-extraction-service-metadata.md`
- `sample_document.json`

## Production Roadmap

- OCR support for scanned PDFs and images
- LLM-based extraction with schema validation
- Human review queue for low-confidence cases
- Database-backed document and extraction storage
- Tenant-level access control
- Batch processing workers
- Dashboard for extraction quality and review status
