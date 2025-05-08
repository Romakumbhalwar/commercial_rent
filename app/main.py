import joblib
from fastapi import FastAPI
from app.schemas import RentRequest, RentResponse
from app.utils import load_model, preprocess_input
import uvicorn

app = FastAPI()
model = joblib.load("app/model/commercial_rent_model.pkl")

@app.get("/")
def home():
    return {"message": "Welcome to Commercial Rent Prediction API"}

@app.post("/predict", response_model=RentResponse)
def predict_rent(request: RentRequest):
    input_df = preprocess_input(request)
    prediction = model.predict(input_df)[0]
    return RentResponse(predicted_rent=round(prediction, 2))