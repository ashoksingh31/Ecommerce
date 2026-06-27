from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, FastAPI!"
    }


def test_create_user():
    payload = {
        "name": "Ashok",
        "age": 28
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 200
    assert response.json() == payload