from data.referential.regions._constantes import _regions_csv_data_url, _regions_geojson_data_url, _regions_data_csv_file, \
    _regions_data_geojson_file
from src.data.extract import download_and_replace_file


def download_all() -> None:
    __download_geojson_data()
    __download_csv_data()


def __download_csv_data() -> None:
    download_and_replace_file(_regions_csv_data_url, _regions_data_csv_file)


def __download_geojson_data() -> None:
    download_and_replace_file(_regions_geojson_data_url, _regions_data_geojson_file)
