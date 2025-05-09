
def map_yes_no_to_bool(df):
    """
    Convert 'Yes'/'No' string values in specific columns to boolean True/False.
    """
    df = df.copy()
    bool_cols = ['private_washroom', 'public_washroom', 'electric_charge_included', 'water_charge_included']
    mapping = {'Yes': True, 'No': False}
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].map(mapping)
    return df
