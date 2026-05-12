from fastapi import FastAPI

from doc_intelligence.schemas import DocumentRequest, ExtractionResult
from doc_intelligence.service import DocumentIntelligenceService

app = FastAPI(title='Document Intelligence Extraction System')
_service = DocumentIntelligenceService()


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}


@app.post('/extract', response_model=ExtractionResult)
def extract(request: DocumentRequest) -> ExtractionResult:
    return _service.analyze(request)
