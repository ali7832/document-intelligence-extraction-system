from __future__ import annotations

import re


def extract_fields(text: str) -> dict:
    fields: dict = {}

    invoice_match = re.search(r'invoice\s*#?:?\s*([A-Z0-9-]+)', text, re.IGNORECASE)
    amount_match = re.search(r'(?:amount due|total due|total)\s*:?\s*\$?([0-9,.]+)', text, re.IGNORECASE)
    date_match = re.search(r'(?:date|invoice date)\s*:?\s*([0-9]{4}-[0-9]{2}-[0-9]{2})', text, re.IGNORECASE)
    vendor_match = re.search(r'(?:vendor|company)\s*:?\s*([A-Za-z0-9 &.-]+)', text, re.IGNORECASE)

    if invoice_match:
        fields['invoice_number'] = invoice_match.group(1)
    if amount_match:
        fields['amount'] = amount_match.group(1)
    if date_match:
        fields['date'] = date_match.group(1)
    if vendor_match:
        fields['vendor'] = vendor_match.group(1).strip()

    return fields
