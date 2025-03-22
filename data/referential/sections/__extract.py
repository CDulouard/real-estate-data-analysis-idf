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
import json

import pandas as pd

from data.referential.sections._constants import _sections_geojson_data_url, _sections_data_csv_file, \
    _sections_data_geojson_file
from src.data.extract import download_and_replace_file, extract_gzip


def download_all() -> None:
    __download_geojson_data()
    __build_csv_dataset()


def __build_csv_dataset() -> None:
    with open(_sections_data_geojson_file, 'r') as file:
        geojson_data = json.load(file)
        sections = [{"id": section["properties"]["id"],
                     "code_insee_commune": section["properties"]["commune"],
                     "prefixe": section["properties"]["prefixe"],
                     "code": section["properties"]["code"],
                     "geo_shape": section["geometry"]["coordinates"]}
                    for section in geojson_data["features"]]
        sections_df = pd.DataFrame(sections)
        sections_df.to_csv(_sections_data_csv_file, sep=";", index=False)


def __download_geojson_data() -> None:
    # Geojson file are provided as gzip files
    archive_name = _sections_data_geojson_file + ".gz"
    download_and_replace_file(_sections_geojson_data_url, archive_name)
    extract_gzip(archive_name)
