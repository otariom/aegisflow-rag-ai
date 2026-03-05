from pathlib import Path
from typing import List

from pypdf import PdfReader

try:
    from docling.document_converter import DocumentConverter
    DOCLING_AVAILABLE = True
except Exception:
    DOCLING_AVAILABLE = False


def parse_pdf(file_path: str) -> str:
    """
    Extract full text from a PDF.
    Uses Docling if available, otherwise falls back to PyPDF.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # --- Preferred method: Docling ---
    if DOCLING_AVAILABLE:
        try:
            converter = DocumentConverter()
            result = converter.convert(file_path)

            text_parts = []
            for page in result.document.pages:
                text_parts.append(page.text)

            return "\n".join(text_parts)

        except Exception:
            # fallback if docling fails
            pass

    # --- Fallback method: PyPDF ---
    reader = PdfReader(file_path)

    text_parts = []
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text_parts.append(extracted)

    return "\n".join(text_parts)


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 150) -> List[str]:
    """
    Splits large text into overlapping chunks.
    This improves semantic retrieval later.
    """

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def process_document(file_path: str) -> List[str]:
    """
    Complete pipeline:
    PDF -> Text -> Chunks
    """

    text = parse_pdf(file_path)
    chunks = chunk_text(text)

    return chunks