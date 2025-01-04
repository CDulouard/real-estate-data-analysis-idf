import pandas as pd
from pathlib import Path


def load_loyers_par_ville_df() -> pd.DataFrame:
    data = pd.read_csv(f"{Path(__file__).parent}/loyers_par_ville_2024.csv", sep=";", low_memory=False)
    return data
