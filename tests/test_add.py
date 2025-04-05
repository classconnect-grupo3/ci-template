from fastapi.testclient import TestClient
from app import create_app

app = create_app()
client = TestClient(app)


def test_add():
    response = client.get("/add/5")
    assert response.status_code == 200
    assert response.json() == {"result": "6"}
