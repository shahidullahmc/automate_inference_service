from fastapi.testclient import TestClient
from main import app

# Create a test client instance using the FastAPI app
client = TestClient(app)

def test_read_root():
    """Test the root endpoint status and welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    # Optional: check response payload if your root returns JSON
    # assert response.json() == {"message": "Welcome to the Inference API"}

def test_predict_valid_data():
    """Test /predict endpoint with valid payload."""
    payload = {
        "age": 25,
        "income": 5000
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    
    # Verify the structure of the JSON response
    data = response.json()
    assert "prediction" in data or "result" in data  # Adjust key based on main.py output

def test_predict_missing_field():
    """Test /predict endpoint validation error when body is incomplete."""
    invalid_payload = {
        "age": 25
        # "income" is missing
    }
    response = client.post("/predict", json=invalid_payload)
    # FastAPI automatically returns 422 Unprocessable Entity for invalid schema
    assert response.status_code == 422
    