from pathlib import Path

import pandas as pd


def load_prix_par_commune() -> pd.DataFrame:
    data = pd.read_csv(f"{Path(__file__).parent}/prix_communes.csv", sep=";", low_memory=False)
    return data
