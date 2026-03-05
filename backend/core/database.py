import faiss
import json
import os
import uuid
import numpy as np
from sentence_transformers import SentenceTransformer

# Embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

VECTOR_DIM = 384

# Files where vectors and metadata are stored
FAISS_INDEX_FILE = "aegis_index.faiss"
DOC_STORE_FILE = "aegis_docs.json"

# Load or create FAISS index
if os.path.exists(FAISS_INDEX_FILE):
    index = faiss.read_index(FAISS_INDEX_FILE)
else:
    index = faiss.IndexFlatL2(VECTOR_DIM)

# Load or create document store
if os.path.exists(DOC_STORE_FILE):
    with open(DOC_STORE_FILE, "r", encoding="utf-8") as f:
        doc_store = json.load(f)
else:
    doc_store = {}


def insert_chunks(chunks):
    """
    Convert text chunks into embeddings and store them.
    """

    vectors = []
    ids = []

    for chunk in chunks:
        vector = embedding_model.encode(chunk)
        doc_id = str(uuid.uuid4())

        vectors.append(vector)
        ids.append(doc_id)

        doc_store[doc_id] = chunk

    vectors = np.array(vectors).astype("float32")

    index.add(vectors)

    # Persist index
    faiss.write_index(index, FAISS_INDEX_FILE)

    # Persist text store
    with open(DOC_STORE_FILE, "w", encoding="utf-8") as f:
        json.dump(doc_store, f)


def search(query, top_k=5):
    """
    Retrieve most similar chunks using FAISS.
    """

    query_vector = embedding_model.encode(query)
    query_vector = np.array([query_vector]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []

    for idx in indices[0]:
        if idx < len(doc_store):
            key = list(doc_store.keys())[idx]
            results.append(doc_store[key])

    return results