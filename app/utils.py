import pandas as pd
import numpy as np

# Preprocess input data before feeding to the model
def preprocess_input(request):
    # Convert request data to a DataFrame
    data = {
        "city": [request.city],
        "area": [request.area],
        "location": [request.location],
        "zone": [request.zone],
        "location_hub": [request.location_hub],
        "property_type": [request.property_type],
        "ownership": [request.ownership],
        "size_in_sqft": [request.size_in_sqft],
        "carpet_area_sqft": [request.carpet_area_sqft],
        "private_washroom": [1 if request.private_washroom == 'Yes' else 0],
        "public_washroom": [1 if request.public_washroom == 'Yes' else 0],
        "floor_no": [request.floor_no],
        "total_floors": [request.total_floors],
        "amenities_count": [request.amenities_count],
        "electric_charge_included": [1 if request.electric_charge_included == 'Yes' else 0],
        "water_charge_included": [1 if request.water_charge_included == 'Yes' else 0],
        "property_age": [request.property_age],
        "possession_status": [request.possession_status],
        "posted_by": [request.posted_by],
        "rent_increase_per_year": [request.rent_increase_per_year],
        "negotiable": [1 if request.negotiable == 'Yes' else 0],
        "brokerage": [1 if request.brokerage == 'Yes' else 0]
    }
    
    df = pd.DataFrame(data)
    
    # You can include any feature engineering, encoding, or scaling here as necessary
    # For example, you can one-hot encode categorical features like city, area, etc.
    
    return df

# A utility function to map 'Yes'/'No' to boolean values
def map_yes_no_to_bool(value):
    return 1 if value == 'Yes' else 0
