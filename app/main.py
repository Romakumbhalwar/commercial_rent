from fastapi import FastAPI
from app.schemas import RentRequest, RentResponse
from app.utils import preprocess_input
from app.utils import map_yes_no_to_bool 
import joblib

app = FastAPI()

# Load model (dictionary with model and features)
model_bundle = joblib.load("app/model/commercial_rent_model.pkl")
model = model_bundle
features = model_bundle['features']

@app.post("/predict", response_model=RentResponse)
def predict_rent(request: RentRequest):
    input_df = preprocess_input(request)

    # Reorder columns to match model training
    input_df = input_df[features]

    prediction = model.predict(input_df)[0]
    return RentResponse(predicted_rent=round(prediction, 2))
