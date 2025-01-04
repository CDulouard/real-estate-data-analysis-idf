from data.referential.departements._constantes import _departements_csv_data_url, _departements_geojson_data_url, _departements_data_csv_file, \
    _departements_data_geojson_file
from src.data.extract import download_and_replace_file


def download_all() -> None:
    __download_geojson_data()
    __download_csv_data()


def __download_csv_data() -> None:
    download_and_replace_file(_departements_csv_data_url, _departements_data_csv_file)


def __download_geojson_data() -> None:
    download_and_replace_file(_departements_geojson_data_url, _departements_data_geojson_file)
