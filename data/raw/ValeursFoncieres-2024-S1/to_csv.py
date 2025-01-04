import pandas as pd
from data.referential.communes import load_insee_codes_communes_short_df

# Input and output file paths
input_file = "ValeursFoncieres-2024-S1.txt"  # Replace with your input file name
output_file = "../../clean/valeurs_foncieres/valeurs_foncieres_2024_S1.csv"  # Replace with your desired output file name

columns_to_drop = ["Identifiant de document",
                   "Reference document",
                   "1 Articles CGI",
                   "2 Articles CGI",
                   "3 Articles CGI",
                   "4 Articles CGI",
                   "5 Articles CGI",
                   "Identifiant local"]

dtype_mapping = {'No disposition': 'Int64',
                 'Nature mutation': 'string',
                 'Valeur fonciere': 'float64',
                 'No voie': 'Int64',
                 'B/T/Q': 'string',
                 'Type de voie': 'string',
                 'Code voie': 'string',
                 'Voie': 'string',
                 'Code postal': 'string', # Used to join dfs, must be string in this case
                 'Commune': 'string',
                 'Code departement': 'string',
                 'Code commune': 'Int64',
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
                 'Surface terrain': 'float64'}

with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

header = lines[0].strip().split("|")
data = [line.strip().split("|") for line in lines[1:]]

df = pd.DataFrame(data, columns=header)
df = df.drop(columns=columns_to_drop, errors="ignore")

df.to_csv(output_file, index=False, sep=";")

# Yes I was really lazy for this one...
data = pd.read_csv(output_file,
                   sep=";",
                   decimal=",",
                   low_memory=False,
                   dtype=dtype_mapping,
                   parse_dates=["Date mutation"])

insee_codes = load_insee_codes_communes_short_df()

data = data.drop(columns=["Commune", "Code departement", "Code commune"])
data = pd.merge(data, insee_codes, left_on="Code postal", right_on="Code Postal", how="inner")
data = data.drop(columns=["Code postal"])

data.to_csv(output_file, index=False, sep=";", decimal=".")

print(f"Data successfully written to {output_file}")
