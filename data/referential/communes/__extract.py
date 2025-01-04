from data.referential.communes._constantes import _communes_data_csv_file, _communes_data_geojson_file, \
    _communes_csv_data_url, _communes_geojson_data_url
from src.data.extract import download_and_replace_file


def download_all() -> None:
    __download_geojson_data()
    __download_csv_data()


def __download_csv_data() -> None:
    download_and_replace_file(_communes_csv_data_url, _communes_data_csv_file)


def __download_geojson_data() -> None:
    download_and_replace_file(_communes_geojson_data_url, _communes_data_geojson_file)
