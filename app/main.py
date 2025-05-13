from fastapi import FastAPI, HTTPException
from app.schemas import CommercialPropertyInput
import joblib
import traceback

app = FastAPI()

# Load your model and pipeline
model_dict = joblib.load("app/model/commercial_rent_model.pkl")
model = model_dict['model']
features = model_dict['features']

@app.post("https://commercial-fastapi.onrender.com/predict")
def predict_rent(data: CommercialPropertyInput):
    try:
        # Debug: Print incoming request data
        print("Received data:", data)

        # Convert to DataFrame
        input_df = data.to_df()

        # Debug: Show processed dataframe
        print("Input DataFrame:", input_df)

        # Predict
        prediction = model.predict(input_df)

        # Debug: Show prediction result
        print("Prediction:", prediction[0])

        return {"predicted_rent": round(prediction[0], 2)}

    except Exception as e:
        # Print full traceback in the console
        traceback.print_exc()

        # Return readable error message
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
