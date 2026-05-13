from __future__ import annotations

import time
from uuid import uuid4

from doc_intelligence.audit import append_extraction_event
from doc_intelligence.classifier import classify_document
from doc_intelligence.config import settings
from doc_intelligence.extractor import extract_fields
from doc_intelligence.schemas import DocumentRequest, ExtractionResult
from doc_intelligence.text_utils import normalize_text


def confidence_score(fields: dict) -> float:
    if not fields:
        return 0.35
    return round(min(0.95, 0.45 + 0.12 * len(fields)), 4)


class DocumentIntelligenceService:
    def analyze(self, request: DocumentRequest) -> ExtractionResult:
        started = time.perf_counter()
        extraction_id = str(uuid4())

        if len(request.text) > settings.max_document_chars:
            raise ValueError('document exceeds configured character limit')

        text = normalize_text(request.text)
        document_type = classify_document(text)
        fields = extract_fields(text)
        confidence = confidence_score(fields)
        warnings = [] if fields else ['no_structured_fields_detected']
        if confidence < settings.minimum_confidence_threshold:
            warnings.append('low_confidence_extraction')

        result = ExtractionResult(
            extraction_id=extraction_id,
            document_id=request.document_id,
            document_type=document_type,
            fields=fields,
            confidence=confidence,
            status='review_required' if warnings else 'completed',
            warnings=warnings,
            extraction_version=settings.extraction_version,
            processing_time_ms=round((time.perf_counter() - started) * 1000, 2),
        )

        append_extraction_event(
            {
                'extraction_id': extraction_id,
                'document_id': request.document_id,
                'tenant_id': request.tenant_id,
                'source': request.source,
                'document_name': request.document_name,
                'submitted_by': request.submitted_by,
                'result': result.model_dump(),
            },
            settings.audit_store_path,
        )
        return result
