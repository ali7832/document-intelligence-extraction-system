from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class DocumentIntelligenceSettings:
    environment: str = os.getenv('DOCINTEL_ENV', 'local')
    service_name: str = os.getenv('DOCINTEL_SERVICE_NAME', 'document-intelligence-extraction-system')
    extraction_version: str = os.getenv('DOCINTEL_EXTRACTION_VERSION', 'rules-extractor-v1')
    audit_store_path: str = os.getenv('DOCINTEL_AUDIT_STORE_PATH', 'document_extractions.jsonl')
    minimum_confidence_threshold: float = float(os.getenv('DOCINTEL_MINIMUM_CONFIDENCE_THRESHOLD', '0.50'))
    max_document_chars: int = int(os.getenv('DOCINTEL_MAX_DOCUMENT_CHARS', '20000'))


settings = DocumentIntelligenceSettings()
