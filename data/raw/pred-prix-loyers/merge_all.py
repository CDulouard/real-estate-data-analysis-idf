import pandas as pd
from data.referential.communes import load_insee_codes_communes_short_df


def add_static_column(df, column_name, static_value):
    df[column_name] = static_value
    return df


maisons = pd.read_csv("pred-maison-mef-dhup.csv", encoding='latin1', sep=";")
maisons = add_static_column(maisons, "type", "maison")

appartement = pd.read_csv("pred-appartement-mef-dhup.csv", encoding='latin1', sep=";")
appartement = add_static_column(appartement, "type", "appartement")

apartement_1_2 = pd.read_csv("pred-appartement-1-2-mef-dhup.csv", encoding='latin1', sep=";")
apartement_1_2 = add_static_column(apartement_1_2, "type", "apartement_1_2")

apartement_3 = pd.read_csv("pred-appartement-3-mef-dhup.csv", encoding='latin1', sep=";")
apartement_3 = add_static_column(apartement_3, "type", "apartement_3")

all_datasets = pd.concat([maisons, appartement, apartement_1_2, apartement_3], ignore_index=True)
insee_codes = load_insee_codes_communes_short_df()

all_datasets = pd.merge(all_datasets, insee_codes, left_on="INSEE_C", right_on="Code INSEE", how="inner")
all_datasets = all_datasets.drop(columns=["INSEE_C", "LIBGEO"])

all_datasets.to_csv("../../clean/loyers/loyers_par_ville_2024.csv", index=False, sep=";", encoding='utf8')
