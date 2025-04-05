from fastapi.testclient import TestClient
from app import create_app

app = create_app()
client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
