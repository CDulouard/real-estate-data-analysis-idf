from pathlib import Path

_communes_data_csv_file = f"{Path(__file__).parent}/code_insee_code_postal.csv"
_communes_data_geojson_file = f"{Path(__file__).parent}/communes_fr.geojson"
_communes_csv_data_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/correspondance-code-insee-code-postal/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
_communes_geojson_data_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/correspondance-code-insee-code-postal/exports/geojson?lang=fr&timezone=Europe%2FBerlin"
