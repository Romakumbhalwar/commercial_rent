from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Optional

from schemas import RentInput

app = FastAPI()

# Load trained model
model = joblib.load("app/model/commercial_rent_model.pkl")

@app.get("/")
def home():
    return {"message": "Commercial Rent Prediction API is running."}

@app.post("/predict")
def predict_rent(data: RentInput):
    input_dict = data.dict()
    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    return {"predicted_rent": round(prediction, 2)}
