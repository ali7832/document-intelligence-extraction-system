from __future__ import annotations

from pydantic import BaseModel


class DocumentRequest(BaseModel):
    document_id: str
    text: str


class ExtractionResult(BaseModel):
    document_id: str
    document_type: str
    fields: dict
    confidence: float
    warnings: list[str]
