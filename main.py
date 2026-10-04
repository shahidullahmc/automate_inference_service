from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

# Define schema to validate incoming payloads
class CustomerData(BaseModel):
    age: int
    income: float

@app.get("/")
def read_root():
    """Health check / root endpoint."""
    return {"message": "Welcome to the Inference API"}

@app.post("/predict", summary="Predict purchase probability")
async def predict(data: CustomerData):
    """
    Receives customer data and returns a random purchase probability (0 or 1).
    """
    prediction = np.random.choice([0, 1])
    return {"prediction": int(prediction)}
