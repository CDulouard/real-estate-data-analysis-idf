from pathlib import Path

import pandas as pd

dtype_mapping = {
    'No disposition': 'Int64',
    'Nature mutation': 'string',
    'Valeur fonciere': 'float64',
    'No voie': 'Int64',
    'B/T/Q': 'string',
    'Type de voie': 'string',
    'Code voie': 'string',
    'Voie': 'string',
    'Prefixe de section': 'float64',
    'Section': 'string',
    'No plan': 'Int64',
    'No Volume': 'string',
    '1er lot': 'string',
    'Surface Carrez du 1er lot': 'float64',
    '2eme lot': 'string',
    'Surface Carrez du 2eme lot': 'float64',
    '3eme lot': 'string',
    'Surface Carrez du 3eme lot': 'float64',
    '4eme lot': 'string',
    'Surface Carrez du 4eme lot': 'float64',
    '5eme lot': 'string',
    'Surface Carrez du 5eme lot': 'float64',
    'Nombre de lots': 'Int64',
    'Code type local': 'string',
    'Type local': 'string',
    'Surface reelle bati': 'float64',
    'Nombre pieces principales': 'Int64',
    'Nature culture': 'string',
    'Nature culture speciale': 'string',
    'Surface terrain': 'float64',
    'Code INSEE': 'string',
    'Code Postal': 'string',
    'Commune': 'string',
    'Département': 'string',
    'Région': 'string',
    'ID Geofla': 'string',
    'Code Commune': 'string',
    'Code Canton': 'string',
    'Code Arrondissement': 'string',
    'Code Département': 'string',
    'Code Région': 'string'
}


def load_valeurs_foncieres_df() -> pd.DataFrame:
    dataset = f"{Path(__file__).parent}/valeurs_foncieres_2024_S1.csv"
    dataset = f"{Path(__file__).parent}/extract.csv"
    data = pd.read_csv(dataset,
                       sep=";",
                       low_memory=False,
                       dtype=dtype_mapping,
                       parse_dates=["Date mutation"])
    return data
