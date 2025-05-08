from fastapi import FastAPI, HTTPException
from app.schemas import RentRequest, RentResponse
from app.utils import load_model, preprocess_input
import uvicorn

app = FastAPI()
model = joblib.load("app/model/commercial_rent_model.pkl")

@app.get("/")
def home():
    return {"message": "Welcome to Commercial Rent Prediction API"}

@app.post("/predict", response_model=RentResponse)
def predict_rent(request: RentRequest):
    try:
        print("Incoming request data:", request)
        input_df = preprocess_input(request)
        print("Preprocessed input DataFrame:", input_df)
        prediction = model.predict(input_df)[0]
        print("Predicted rent:", prediction)
        return RentResponse(predicted_rent=round(prediction, 2))
    except Exception as e:
        print("Prediction error:", str(e))
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")