from __future__ import annotations


def classify_document(text: str) -> str:
    lowered = text.lower()
    if 'invoice' in lowered or 'amount due' in lowered or 'total due' in lowered:
        return 'invoice'
    if 'agreement' in lowered or 'contract' in lowered or 'terms and conditions' in lowered:
        return 'contract'
    if 'receipt' in lowered or 'payment received' in lowered:
        return 'receipt'
    return 'general_document'
