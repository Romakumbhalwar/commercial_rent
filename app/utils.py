import pandas as pd

def map_yes_no_to_bool(value):
    if isinstance(value, str):
        return value.strip().lower() == 'yes'
    return False

def preprocess_input(request):
    """Convert input request to a DataFrame and map Yes/No to boolean."""
    df = pd.DataFrame([request.dict()])
    df = map_yes_no_to_bool(df)
    return df
