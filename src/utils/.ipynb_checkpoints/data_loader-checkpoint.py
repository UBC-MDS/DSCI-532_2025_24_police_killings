import pandas as pd

def load_clean_data():
    """Load and preprocess the dataset."""
    return pd.read_csv('data/processed/clean_data.csv')

data = load_clean_data()