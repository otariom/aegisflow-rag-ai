import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def generate_response(prompt: str) -> str:
    """
    Sends a prompt to the local Ollama LLM and returns the generated response.
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code != 200:
            raise Exception(f"Ollama error: {response.text}")

        data = response.json()

        return data.get("response", "")

    except Exception as e:
        return f"LLM Error: {str(e)}"