"""
Copyright (C) 2025  Clément Dulouard

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from data.referential.departements._constants import _departements_csv_data_url, _departements_geojson_data_url, _departements_data_csv_file, \
    _departements_data_geojson_file
from src.data.extract import download_and_replace_file


def download_all() -> None:
    __download_geojson_data()
    __download_csv_data()


def __download_csv_data() -> None:
    download_and_replace_file(_departements_csv_data_url, _departements_data_csv_file)


def __download_geojson_data() -> None:
    download_and_replace_file(_departements_geojson_data_url, _departements_data_geojson_file)
