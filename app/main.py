from fastapi import FastAPI
import joblib
import numpy as np
from app.schemas import CommercialPropertyFeatures

# ✅ Define the missing function used in the model
def map_yes_no_to_bool(value):
    return 1 if value == 'Yes' else 0

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Load trained model
model = joblib.load("app/model/commercial_rent_model.pkl")

# ✅ Prediction endpoint
@app.post("/predict")
def predict_rent(features: CommercialPropertyFeatures):
    try:
        # Convert gated security field
        gated_sec_bool = map_yes_no_to_bool(features.gated_security)

        # Prepare input (ensure it matches training order)
        input_data = np.array([[
            features.area,
            features.size,
            features.property_type,
            features.furnishing,
            features.security,
            features.maintenance,
            features.brokerage,
            features.amenities,
            features.age,
            features.floor,
            features.total_floor,
            features.carpet_area,
            features.lease_type,
            gated_sec_bool,
            features.location
        ]], dtype=object)

        prediction = model.predict(input_data)
        return {"predicted_rent": round(prediction[0], 2)}

    except Exception as e:
        return {"error": str(e)}
