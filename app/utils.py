import pandas as pd
import joblib
from app.schemas import RentRequest

# Function to load the model
model = joblib.load("app/model/commercial_rent_model.pkl")

# Function to map 'Yes'/'No' values to boolean (for specific fields)
def map_yes_no_to_bool(value: str) -> int:
    return 1 if value == 'Yes' else 0

# Function to preprocess the input data
def preprocess_input(request: RentRequest):
    data = request.dict()
    df = pd.DataFrame([data])

    # Clean and convert numerical/encoded features
    df['size_in_sqft'] = pd.to_numeric(df['size_in_sqft'], errors='coerce')
    df['carpet_area_sqft'] = pd.to_numeric(df['carpet_area_sqft'], errors='coerce')
    df['floor_no'] = df['floor_no'].str.extract(r'(\d+)').fillna(0).astype(int)
    df['total_floors'] = df['total_floors'].str.extract(r'(\d+)').fillna(0).astype(int)
    df['property_age'] = df['property_age'].str.extract(r'(\d+)-?')[0].fillna(0).astype(int)
    
    # Map 'Yes'/'No' to 1/0 for boolean fields
    df['electric_charge_included'] = df['electric_charge_included'].map(map_yes_no_to_bool)
    df['water_charge_included'] = df['water_charge_included'].map(map_yes_no_to_bool)
    df['private_washroom'] = df['private_washroom'].map(map_yes_no_to_bool)
    df['public_washroom'] = df['public_washroom'].map(map_yes_no_to_bool)
    df['negotiable'] = df['negotiable'].map(map_yes_no_to_bool)
    df['brokerage'] = df['brokerage'].map(map_yes_no_to_bool)

    # Clean 'rent_increase_per_year' and convert to float
    df['rent_increase_per_year'] = df['rent_increase_per_year'].str.replace('%', '').astype(float)

    return df
