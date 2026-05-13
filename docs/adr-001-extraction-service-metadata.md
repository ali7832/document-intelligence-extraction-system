# ADR-001: Extraction Service Metadata and Audit Stream

## Status

Accepted

## Context

Document intelligence systems need more than extracted fields. Operations teams need extraction IDs, confidence status, pipeline versioning, processing time, tenant/source metadata, and an audit trail for review and demo workflows.

## Decision

Add extraction metadata to the API contract and persist every extraction event to a JSONL audit stream. The `DocumentIntelligenceService` owns classification, extraction, confidence scoring, status assignment, timing, and audit logging.

## Consequences

Benefits:

- Every extraction can be traced by extraction ID.
- Low-confidence results can be routed to review.
- API responses expose processing time and extractor version.
- JSONL audit storage supports local demos and simple operational review.

Tradeoffs:

- Rule-based extraction is transparent and fast, but production systems should add OCR, LLM extraction, schema validation, and human review workflows.
- JSONL audit storage should be replaced by a database or event stream for production scale.
