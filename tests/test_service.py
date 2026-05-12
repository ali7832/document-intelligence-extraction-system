from doc_intelligence.schemas import DocumentRequest
from doc_intelligence.service import DocumentIntelligenceService


def test_service_analyzes_invoice():
    request = DocumentRequest(
        document_id='invoice-001',
        text='Invoice INV-1001 Date: 2026-05-13 Vendor: Acme Corp Total Due: $1250.00',
    )
    result = DocumentIntelligenceService().analyze(request)

    assert result.document_type == 'invoice'
    assert result.confidence > 0.5
    assert result.fields['invoice_number'] == 'INV-1001'
