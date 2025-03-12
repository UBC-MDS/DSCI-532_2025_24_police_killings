import pandas as pd

def load_police_data():
    """Load and preprocess the dataset."""
    return pd.read_parquet('data/processed/clean_data.parquet')
