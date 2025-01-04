import json
from pathlib import Path

import pandas as pd


def from_string_list_to_string(elem: str) -> str:
    return elem.replace("[", '').replace("]", '')[1:-1]


def fix_geo_shape(record: dict) -> dict:
    fixed_record = record.copy()
    fixed_record["coordinates"][0] = [[point[1], point[0]] for point in record["coordinates"][0]]
    return fixed_record


def load_insee_codes_communes_df() -> pd.DataFrame:
    data = pd.read_csv(f"{Path(__file__).parent}/correspondance-code-insee-code-postal.csv", sep=";", low_memory=False)
    data["Département"] = data["Département"].apply(from_string_list_to_string)
    data["Région"] = data["Région"].apply(from_string_list_to_string)
    data["Statut"] = data["Statut"].apply(from_string_list_to_string)
    data["geo_shape"] = data["geo_shape"].apply(lambda x: json.loads(x))
    data["geo_shape"] = data["geo_shape"].apply(fix_geo_shape)
    return data


def load_insee_codes_communes_short_df() -> pd.DataFrame:
    columns_to_drop = ["Statut", "Altitude Moyenne", "Superficie", "Population", "geo_point_2d", "geo_shape"]
    return load_insee_codes_communes_df().drop(columns=columns_to_drop)
