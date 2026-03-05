from backend.services.parser import process_document
from backend.core.database import insert_chunks, search
from backend.services.llm import generate_response
from backend.core.prompts import build_prompt, followup_questions
from mlops.mlflow_tracking import log_llm_run


def ingest_document(file_path: str):
    """
    Full ingestion pipeline

    PDF → parsing → chunking → embeddings → vector storage
    """

    chunks = process_document(file_path)

    if not chunks:
        raise ValueError("No text extracted from the document.")

    insert_chunks(chunks)

    return {"chunks_indexed": len(chunks)}


def query_engine(question: str):
    """
    Full AI reasoning pipeline
    """

    # Retrieve relevant document chunks
    retrieved_chunks = search(question)

    # Build grounded prompt
    prompt = build_prompt(question, retrieved_chunks)

    # Generate answer using local LLM
    answer = generate_response(prompt)

    # Log run for LLMOps tracking
    log_llm_run(
        question=question,
        prompt=prompt,
        answer=answer,
        model="llama3.2"
    )

    return {
        "answer": answer,
        "sources": retrieved_chunks,
        "followups": followup_questions()
    }