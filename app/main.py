from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Optional
from app.schemas import RentInput

app = FastAPI()

# Load the trained model
model = joblib.load("app/model/commercial_rent_model.pkl")

# Helper function to map 'Yes'/'No' to boolean
def map_yes_no_to_bool(value):
    if value.lower() == 'yes':
        return True
    elif value.lower() == 'no':
        return False
    return None

@app.get("/")
def home():
    return {"message": "Commercial Rent Prediction API is running."}

@app.post("/predict")
def predict_rent(data: RentInput):
    input_dict = data.dict()

    # Apply the map_yes_no_to_bool function to relevant columns
    input_dict['private_washroom'] = map_yes_no_to_bool(input_dict['private_washroom'])
    input_dict['public_washroom'] = map_yes_no_to_bool(input_dict['public_washroom'])
    input_dict['electric_charge_included'] = map_yes_no_to_bool(input_dict['electric_charge_included'])
    input_dict['water_charge_included'] = map_yes_no_to_bool(input_dict['water_charge_included'])
    input_dict['negotiable'] = map_yes_no_to_bool(input_dict['negotiable'])

    # Convert the processed input to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Predict the rent using the model
    prediction = model.predict(input_df)[0]

    # Return the predicted rent
    return {"predicted_rent": round(prediction, 2)}
