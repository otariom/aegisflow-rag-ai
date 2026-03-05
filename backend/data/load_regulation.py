from pathlib import Path
from backend.core.engine import ingest_document

REGULATION_FOLDER = Path("backend/data/regulation")


def load_regulations():
    """
    Load all regulation PDFs into the vector database.
    """

    pdf_files = list(REGULATION_FOLDER.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in regulation folder.")
        return

    for pdf in pdf_files:
        print(f"Processing: {pdf.name}")

        try:
            result = ingest_document(str(pdf))
            print(f"Indexed {result['chunks_indexed']} chunks\n")

        except Exception as e:
            print(f"Error processing {pdf.name}: {e}")


if __name__ == "__main__":
    load_regulations()
    