import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.schemas import RentRequest, RentResponse
from app.utils import preprocess_input
import uvicorn

# Define the function to map 'yes'/'no' to boolean if it's not already present
def map_yes_no_to_bool(value: str) -> bool:
    if value.lower() == 'yes':
        return True
    elif value.lower() == 'no':
        return False
    else:
        return None

# Load the model (ensure the path to the model is correct)
model = joblib.load("app/model/commercial_rent_model.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Commercial Rent Prediction API"}

@app.post("/predict", response_model=RentResponse)
def predict_rent(request: RentRequest):
    try:
        print("Incoming request data:", request)
        
        # Preprocess input data
        input_df = preprocess_input(request)
        print("Preprocessed input DataFrame:", input_df)
        
        # Make the prediction
        prediction = model.predict(input_df)[0]
        print("Predicted rent:", prediction)
        
        # Return the prediction
        return RentResponse(predicted_rent=round(prediction, 2))
    except Exception as e:
        print("Prediction error:", str(e))
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# Run the FastAPI app (if this script is run directly)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
