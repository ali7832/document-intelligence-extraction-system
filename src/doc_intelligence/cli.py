import json
from pathlib import Path

import typer
from rich.console import Console

from doc_intelligence.schemas import DocumentRequest
from doc_intelligence.service import DocumentIntelligenceService

app = typer.Typer(help='Document intelligence extraction CLI')
console = Console()


@app.command()
def analyze(path: Path = Path('sample_document.json')) -> None:
    request = DocumentRequest(**json.loads(path.read_text(encoding='utf-8')))
    result = DocumentIntelligenceService().analyze(request)
    console.print_json(data=result.model_dump())


@app.command()
def demo() -> None:
    request = DocumentRequest(
        document_id='invoice-001',
        text='Invoice INV-1001 Date: 2026-05-13 Vendor: Acme Corp Total Due: $1250.00',
    )
    result = DocumentIntelligenceService().analyze(request)
    console.print_json(data=result.model_dump())
