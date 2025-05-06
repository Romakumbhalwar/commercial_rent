from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

def map_yes_no_to_bool(value):
    if value == 'Yes':
        return True
    elif value == 'No':
        return False
    return value

# Load model
model = joblib.load("app/model/commercial_rent_model.pkl")

# FastAPI app
app = FastAPI()

# Define request schema
class CommercialProperty(BaseModel):
    city: str
    area: str
    location: str
    zone: str
    location_hub: str
    property_type: str
    ownership: str
    size_in_sqft: float
    carpet_area_sqft: float
    private_washroom: str
    public_washroom: str
    floor_no: str
    total_floors: str
    amenities_count: int
    electric_charge_included: str
    water_charge_included: str
    property_age: str
    possession_status: str
    posted_by: str
    rent_increase_per_year: str
    negotiable: str
    brokerage: str

# Prediction endpoint
@app.post("/predict")
def predict_rent(data: CommercialProperty):
    # Convert to DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Predict rent
    prediction = model.predict(input_df)[0]
    
    return {"predicted_rent": round(prediction, 2)}
