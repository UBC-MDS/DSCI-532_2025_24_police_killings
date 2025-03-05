import pandas as pd

def load_clean_data():
    """Load and preprocess the dataset."""
    return pd.read_csv('data/processed/clean_data.csv')

police_data = load_clean_data()