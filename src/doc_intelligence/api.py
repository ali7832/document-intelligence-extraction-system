from fastapi import FastAPI

from doc_intelligence.config import settings
from doc_intelligence.schemas import DocumentRequest, ExtractionResult, HealthResponse
from doc_intelligence.service import DocumentIntelligenceService

app = FastAPI(title='Document Intelligence Extraction System', version='0.2.0')
_service = DocumentIntelligenceService()


@app.get('/health', response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status='ok',
        service_name=settings.service_name,
        environment=settings.environment,
        extraction_version=settings.extraction_version,
    )


@app.post('/extract', response_model=ExtractionResult)
def extract(request: DocumentRequest) -> ExtractionResult:
    return _service.analyze(request)
