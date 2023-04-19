from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_log_entry():
    log_data = {
        "app_id": "myapp",
        "trace_id": "1234",
        "severity": "info",
        "timestamp": "2022-01-01T12:00:00.000000",
        "message": "Test log entry"
    }
    response = client.post("/log", json=log_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Log entry created successfully"}

def test_create_log_entry_missing_data():
    log_data = {
        "app_id": "myapp",
        "trace_id": "1234",
        "severity": "info",
        "message": "Test log entry"
    }
    response = client.post("/log", json=log_data)
    assert response.status_code == 422

def test_get_log_entries():
    response = client.get("/log")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
