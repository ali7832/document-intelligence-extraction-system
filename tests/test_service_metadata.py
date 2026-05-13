from doc_intelligence.schemas import DocumentRequest
from doc_intelligence.service import DocumentIntelligenceService


def test_document_service_returns_extraction_metadata():
    request = DocumentRequest(
        document_id='invoice-001',
        document_name='invoice.pdf',
        source='api',
        submitted_by='ops@example.com',
        tenant_id='tenant-a',
        text='Invoice INV-1001 Date: 2026-05-13 Vendor: Acme Corp Total Due: $1250.00',
    )

    result = DocumentIntelligenceService().analyze(request)

    assert result.extraction_id
    assert result.document_id == 'invoice-001'
    assert result.document_type == 'invoice'
    assert result.extraction_version
    assert result.processing_time_ms >= 0
    assert result.status in {'completed', 'review_required'}
    assert result.fields['invoice_number'] == 'INV-1001'
