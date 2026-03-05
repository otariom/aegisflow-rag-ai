from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import shutil

from backend.core.engine import ingest_document, query_engine

app = FastAPI(title="AegisFlow API", version="1.0")

# Allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("backend/data/internal")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def health_check():
    return {"status": "AegisFlow backend running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a PDF and send it to the ingestion engine.
    """

    try:
        file_path = UPLOAD_DIR / file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = ingest_document(str(file_path))

        return {
            "message": f"{file.filename} processed successfully",
            "chunks_indexed": result["chunks_indexed"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query")
async def query_system(request: QueryRequest):
    """
    Send a question to the AI engine.
    """

    try:
        result = query_engine(request.question)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))