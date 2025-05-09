import pandas as pd
from app.schemas import RentRequest

# Function to map 'Yes'/'No' values to 1/0
def map_yes_no_to_bool(value: str) -> int:
    return 1 if value == 'Yes' else 0

# Function to preprocess the input data before prediction
def preprocess_input(request: RentRequest):
    data = request.dict()
    df = pd.DataFrame([data])

    # Convert numerical fields
    df['size_in_sqft'] = pd.to_numeric(df['size_in_sqft'], errors='coerce')
    df['carpet_area_sqft'] = pd.to_numeric(df['carpet_area_sqft'], errors='coerce')

    # Extract numbers from string fields like floor and age
    df['floor_no'] = df['floor_no'].str.extract(r'(\d+)').fillna(0).astype(int)
    df['total_floors'] = df['total_floors'].str.extract(r'(\d+)').fillna(0).astype(int)
    df['property_age'] = df['property_age'].str.extract(r'(\d+)-?')[0].fillna(0).astype(int)

    # Convert 'Yes'/'No' to 1/0 for boolean fields
    df['electric_charge_included'] = df['electric_charge_included'].map(map_yes_no_to_bool)
    df['water_charge_included'] = df['water_charge_included'].map(map_yes_no_to_bool)
    df['private_washroom'] = df['private_washroom'].map(map_yes_no_to_bool)
    df['public_washroom'] = df['public_washroom'].map(map_yes_no_to_bool)
    df['negotiable'] = df['negotiable'].map(map_yes_no_to_bool)
    df['brokerage'] = df['brokerage'].map(map_yes_no_to_bool)

    # Clean percentage string and convert to float
    df['rent_increase_per_year'] = df['rent_increase_per_year'].str.replace('%', '').astype(float)

    return df
