import pandas as pd

# app/utils.py

def map_yes_no_to_bool(df):
    df = df.copy()
    bool_cols = ['private_washroom', 'public_washroom', 'electric_charge_included', 'water_charge_included']
    mapping = {'Yes': True, 'No': False}
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].map(mapping)
    return df

def preprocess_input(request):
    """Convert input request to a DataFrame and map Yes/No to boolean."""
    df = pd.DataFrame([request.dict()])
    df = map_yes_no_to_bool(df)
    return df
