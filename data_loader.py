import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_excel(file_path):
    return pd.read_excel(file_path)

def validate_schema(df, required_columns):
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        return False, f"Missing columns: {missing}"

    return True, "Schema valid"
