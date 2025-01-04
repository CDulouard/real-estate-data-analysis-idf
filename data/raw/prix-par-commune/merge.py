import os

import pandas as pd

from data.referential.communes import load_insee_codes_communes_short_df

insee_codes = load_insee_codes_communes_short_df()

csv_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.csv')]
dfs = [pd.read_csv(file) for file in csv_files]
merged_df = pd.concat(dfs, ignore_index=True)
merged_df = pd.merge(merged_df, insee_codes, left_on="INSEE_COM", right_on="Code INSEE", how="left")
merged_df = merged_df.drop(columns=["Code INSEE", "Unnamed: 0"])
merged_df.rename(columns={'INSEE_COM': 'Code INSEE'}, inplace=True)
merged_df.to_csv(r"../../clean/prix_communes/prix_communes.csv", index=False, sep=";")
