from pathlib import Path

_departements_data_csv_file = f"{Path(__file__).parent}/code_insee_departements.csv"
_departements_data_geojson_file = f"{Path(__file__).parent}/departements_fr.geojson"
_departements_csv_data_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-france-departement/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
_departements_geojson_data_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-france-departement/exports/geojson?lang=fr&timezone=Europe%2FBerlin"
