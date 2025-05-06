from fastapi import FastAPI
from app.schemas import CommercialProperty
import pandas as pd
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load trained model pipeline
model = joblib.load("app/model/commercial_rent_model.pkl")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Commercial Rent Prediction API"}

# Predict endpoint
@app.post("/predict")
def predict_rent(data: CommercialProperty):
    input_data = data.dict()
    
    # Only keep the features used in training
    used_features = [
        'city', 'area', 'location', 'zone', 'property_type', 'ownership',
        'size_in_sqft', 'carpet_area_sqft', 'private_washroom', 'public_washroom',
        'floor_no', 'total_floors', 'amenities_count', 'electric_charge_included',
        'water_charge_included', 'possession_status'
    ]
    
    # Filter input to only include necessary features
    filtered_input = {k: input_data[k] for k in used_features}
    
    # Convert input to DataFrame
    input_df = pd.DataFrame([filtered_input])
    
    # Predict rent
    predicted_rent = model.predict(input_df)[0]
    
    # Return prediction
    return {"predicted_rent": round(predicted_rent, 2)}
