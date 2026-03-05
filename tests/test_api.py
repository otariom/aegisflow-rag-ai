from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health_check():
    """
    Test if the API root endpoint is running.
    """

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "AegisFlow backend running"}


def test_query_endpoint():
    """
    Test the query endpoint with a simple question.
    """

    payload = {"question": "What is AI transparency?"}

    response = client.post("/query", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "followups" in data