# AegisFlow – Private RAG AI for EU AI Act Compliance

AegisFlow is a **local, privacy-first Retrieval Augmented Generation (RAG) system** designed to analyze regulatory documents such as the **EU AI Act** and internal company policies.
The system retrieves relevant sections from uploaded PDFs and uses a **local LLM** to generate grounded answers.

The goal of the project is to build a **private AI assistant capable of explaining regulatory requirements and helping organizations understand compliance obligations** without sending sensitive data to external APIs.

---

## Overview

AegisFlow allows users to:

* Upload regulatory or internal policy documents
* Ask questions about those documents
* Retrieve relevant sections using semantic search
* Generate explanations using a local LLM

The system ensures that answers are **grounded in the provided documents**, preventing hallucinations.

Example question:

> "What transparency obligations exist for high-risk AI systems under the EU AI Act?"

The system retrieves the relevant legal sections and generates an explanation based on those sections.

---

## Architecture

The system follows a **Retrieval Augmented Generation (RAG)** architecture.

User Question
↓
Embedding Generation
↓
Vector Search (FAISS)
↓
Retrieve Relevant Document Chunks
↓
Prompt Construction
↓
Local LLM (Ollama)
↓
Grounded Answer

---

## Tech Stack

### Backend

* **FastAPI** – API server for document ingestion and querying

### Frontend

* **Streamlit** – Interactive chat interface

### LLM

* **Ollama** running **Llama 3 / Phi-3**

### Retrieval System

* **SentenceTransformers** – Embedding generation
* **FAISS** – Vector similarity search

### Document Processing

* **Docling / PyPDF** – PDF text extraction

### MLOps

* **MLflow** – Experiment tracking

### DevOps

* **GitHub Actions** – CI pipeline
* **pytest** – Automated tests
* **Black / Flake8** – Code quality checks

---

## Project Structure

```
AegisFlow/
│
├── backend/
│   ├── main.py
│   ├── core/
│   │   ├── engine.py
│   │   ├── database.py
│   │   └── prompts.py
│   │
│   ├── services/
│   │   ├── parser.py
│   │   └── llm.py
│   │
│   └── data/
│       ├── regulation/
│       └── load_regulation.py
│
├── frontend/
│   ├── app.py
│   └── api_client.py
│
├── mlops/
│   └── mlflow_tracking.py
│
├── tests/
│   ├── test_api.py
│   └── test_engine.py
│
├── .github/workflows/
│   └── ci.yml
│
├── requirements.txt
└── run.py
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/aegisflow-rag-ai.git
cd aegisflow-rag-ai
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the System

### Start Backend

```
uvicorn backend.main:app --reload
```

API documentation:

```
http://localhost:8000/docs
```

---

### Start Frontend

```
streamlit run frontend/app.py
```

Open:

```
http://localhost:8501
```

---

## Loading Documents

Place regulatory documents inside:

```
backend/data/regulation/
```

Then run:

```
python -m backend.data.load_regulation
```

This will:

* Parse PDFs
* Chunk the text
* Generate embeddings
* Store vectors in the FAISS index

---

## Example Questions

* What transparency obligations exist for high-risk AI systems?
* What documentation must AI providers maintain?
* What responsibilities do AI system providers have under the EU AI Act?

---

## CI Pipeline

GitHub Actions automatically runs:

* dependency installation
* linting checks
* formatting validation
* automated tests
  
Every push triggers the CI pipeline.
---
## Key Features

* Local RAG architecture
* Private AI processing
* EU AI Act document analysis
* Semantic search using embeddings
* FastAPI + Streamlit full-stack application
* CI pipeline and automated testing
* MLflow experiment tracking
---
## Future Improvements
Planned upgrades include:
* citation-aware answers (Article / section references)
* multi-document compliance analysis
* agent-based reasoning workflows
* improved retrieval ranking


Built as a research project exploring **local AI systems for regulatory analysis and compliance automation**.
