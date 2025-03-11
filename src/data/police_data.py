import pandas as pd

def load_clean_data():
    """Load and preprocess the dataset."""
    return pd.read_parquet('data/processed/clean_data.parquet')

police_data = load_clean_data()
