import requests

BACKEND_URL = "http://localhost:8000"


def upload_document(file):
    """
    Sends a PDF file to the backend for processing.
    """

    url = f"{BACKEND_URL}/upload"

    files = {"file": (file.name, file, "application/pdf")}

    try:
        response = requests.post(url, files=files)

        if response.status_code != 200:
            return {"error": response.text}

        return response.json()

    except Exception as e:
        return {"error": str(e)}


def ask_question(question: str):
    """
    Sends a user question to the backend AI engine.
    """

    url = f"{BACKEND_URL}/query"

    payload = {
        "question": question
    }

    try:
        response = requests.post(url, json=payload)

        if response.status_code != 200:
            return {"error": response.text}

        return response.json()

    except Exception as e:
        return {"error": str(e)}