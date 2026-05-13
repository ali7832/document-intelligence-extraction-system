from __future__ import annotations

from pydantic import BaseModel, Field


class DocumentRequest(BaseModel):
    document_id: str
    text: str = Field(..., min_length=1)
    source: str = 'api'
    document_name: str | None = None
    submitted_by: str | None = None
    tenant_id: str = 'default'


class ExtractionResult(BaseModel):
    extraction_id: str
    document_id: str
    document_type: str
    fields: dict
    confidence: float
    status: str
    warnings: list[str]
    extraction_version: str
    processing_time_ms: float


class HealthResponse(BaseModel):
    status: str
    service_name: str
    environment: str
    extraction_version: str
