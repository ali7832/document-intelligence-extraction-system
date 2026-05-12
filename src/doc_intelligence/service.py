from __future__ import annotations

from doc_intelligence.classifier import classify_document
from doc_intelligence.extractor import extract_fields
from doc_intelligence.schemas import DocumentRequest, ExtractionResult
from doc_intelligence.text_utils import normalize_text


def confidence_score(fields: dict) -> float:
    if not fields:
        return 0.35
    return round(min(0.95, 0.45 + 0.12 * len(fields)), 4)


class DocumentIntelligenceService:
    def analyze(self, request: DocumentRequest) -> ExtractionResult:
        text = normalize_text(request.text)
        document_type = classify_document(text)
        fields = extract_fields(text)
        warnings = [] if fields else ['no_structured_fields_detected']
        return ExtractionResult(
            document_id=request.document_id,
            document_type=document_type,
            fields=fields,
            confidence=confidence_score(fields),
            warnings=warnings,
        )
