from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the trained model
model = joblib.load("app/commercial_rent_model.pkl")

# Request schema for input
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

@app.post("/predict")
def predict_rent(data: CommercialProperty):
    # Convert the data to DataFrame for model prediction
    input_df = pd.DataFrame([data.dict()])
    predicted_rent = model.predict(input_df)[0]
    return {"predicted_rent": round(predicted_rent, 2)}
