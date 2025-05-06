from fastapi import FastAPI
import joblib
import pandas as pd
from app.schemas import RentInput
from app.utils import map_yes_no_to_bool  # ✅ import from utils

app = FastAPI()

model = joblib.load("app/model/commercial_rent_model.pkl")

@app.get("/")
def home():
    return {"message": "Commercial Rent Prediction API is running."}

@app.post("/predict")
def predict_rent(data: RentInput):
    input_dict = data.dict()
    input_dict['private_washroom'] = map_yes_no_to_bool(input_dict['private_washroom'])
    input_dict['public_washroom'] = map_yes_no_to_bool(input_dict['public_washroom'])
    input_dict['electric_charge_included'] = map_yes_no_to_bool(input_dict['electric_charge_included'])
    input_dict['water_charge_included'] = map_yes_no_to_bool(input_dict['water_charge_included'])
    input_dict['negotiable'] = map_yes_no_to_bool(input_dict['negotiable'])

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    return {"predicted_rent": round(prediction, 2)}
