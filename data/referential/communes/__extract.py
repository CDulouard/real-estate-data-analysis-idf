from pathlib import Path

from src.data.extract import download_and_replace_file

__csv_data_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/correspondance-code-insee-code-postal/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
__geojson_data_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/correspondance-code-insee-code-postal/exports/geojson?lang=fr&timezone=Europe%2FBerlin"
__output_csv_file_path = f"{Path(__file__).parent}/code_insee_code_postal.csv"
__output_geojson_file_path = f"{Path(__file__).parent}/communes_fr.geojson"


def download_all() -> None:
    __download_geojson_data()
    __download_csv_data()


def __download_csv_data() -> None:
    download_and_replace_file(__csv_data_url, __output_csv_file_path)


def __download_geojson_data() -> None:
    download_and_replace_file(__geojson_data_url, __output_geojson_file_path)
