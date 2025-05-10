import pandas as pd

def map_yes_no_to_bool(df):
    """Convert 'Yes'/'No' columns to True/False."""
    yes_no_columns = df.select_dtypes(include='object').columns
    for col in yes_no_columns:
        if df[col].isin(['Yes', 'No']).all():
            df[col] = df[col].map({'Yes': True, 'No': False})
    return df

def preprocess_input(request):
    """Convert input request to a DataFrame and map Yes/No to boolean."""
    df = pd.DataFrame([request.dict()])
    df = map_yes_no_to_bool(df)  # This is now handling the mapping
    return df
