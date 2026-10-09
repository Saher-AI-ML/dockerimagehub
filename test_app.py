from app import app 
from fastapi.testclient import TestClient

client = TestClient(app)

def test_welcome_message():
    response = client.get("/")

    assert response.status_code == 200 
    assert response.text == "Hello there"