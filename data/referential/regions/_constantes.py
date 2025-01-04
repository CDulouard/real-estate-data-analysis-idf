from pathlib import Path

_regions_data_csv_file = f"{Path(__file__).parent}/code_insee_regions.csv"
_regions_data_geojson_file = f"{Path(__file__).parent}/regions_fr.geojson"
_regions_csv_data_url = "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/regions-et-collectivites-doutre-mer-france@toursmetropole/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
_regions_geojson_data_url = "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/regions-et-collectivites-doutre-mer-france@toursmetropole/exports/geojson?lang=fr&timezone=Europe%2FBerlin"
