from fastapi import FastAPI, HTTPException
from app.schemas import CommercialPropertyInput
import joblib
import traceback
from app.utils import preprocess_input

app = FastAPI()

# Load your model and pipeline
model = joblib.load("app/model/commercial_rent_model.pkl")

@app.post("/predict")
def predict_rent(data: CommercialPropertyInput):
    try:
        # Preprocess input
        input_df = preprocess_input(data)

        # Debug: Show processed dataframe
        print("Processed DataFrame:", input_df)

        # Predict
        prediction = model.predict(input_df)

        # Debug: Show prediction result
        print("Prediction:", prediction[0])

        return {"predicted_rent": round(prediction[0], 2)}

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
