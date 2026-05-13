# Operations Runbook

## Purpose

This service analyzes document text, classifies the document type, extracts structured fields, assigns confidence, and records extraction events for review.

## Runtime Configuration

Configuration is controlled through `.env.example`:

- `DOCINTEL_ENV`: deployment environment.
- `DOCINTEL_SERVICE_NAME`: service identifier.
- `DOCINTEL_EXTRACTION_VERSION`: extraction pipeline version.
- `DOCINTEL_AUDIT_STORE_PATH`: JSONL extraction audit path.
- `DOCINTEL_MINIMUM_CONFIDENCE_THRESHOLD`: threshold for review-required status.
- `DOCINTEL_MAX_DOCUMENT_CHARS`: maximum accepted text length.

## Extraction Lifecycle

1. Document text is submitted to `/extract`.
2. The service creates an extraction ID.
3. Text is normalized and classified.
4. Structured fields are extracted.
5. Confidence and status are assigned.
6. Extraction result is written to the JSONL audit stream.
7. The API returns fields, confidence, warnings, extraction version, and processing time.

## Demo Readiness

Expose `/health` and `/extract`. Health returns service name, environment, and extraction version.

## Production Roadmap

- OCR support for scanned PDFs and images.
- LLM-based extraction with schema validation.
- Human review queue for low-confidence cases.
- Database-backed document and extraction storage.
- Tenant-level access control.
- Batch processing workers.
- Dashboard for extraction quality and review status.
