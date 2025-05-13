import pandas as pd

# app/utils.py

def map_yes_no_to_bool(value):
    if isinstance(value, str):
        if value.strip().lower() == "yes":
            return True
        elif value.strip().lower() == "no":
            return False
    return value


def preprocess_input(request):
    """Convert input request to a DataFrame and map Yes/No to boolean."""
    df = pd.DataFrame([request.dict()])
    df = map_yes_no_to_bool(df)
    return df
