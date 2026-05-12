from doc_intelligence.extractor import extract_fields


def test_extract_invoice_fields():
    text = 'Invoice INV-1001 Date: 2026-05-13 Vendor: Acme Corp Total Due: $1250.00'
    fields = extract_fields(text)

    assert fields['invoice_number'] == 'INV-1001'
    assert fields['date'] == '2026-05-13'
    assert fields['amount'] == '1250.00'
