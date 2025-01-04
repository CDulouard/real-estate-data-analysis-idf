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
import copy
from enum import Enum

import pandas as pd

from data.referential.regions._constants import _regions_data_csv_file, _regions_data_geojson_file


class RegionsGeojsonDictKey(Enum):
    CODE_INSEE = "reg_code"
    NOM = "reg_name_upper"


class Regions:
    __dataframe: pd.DataFrame
    __geojson_data: dict

    def __init__(self):
        __full_dataframe = pd.read_csv(_regions_data_csv_file, sep=";", low_memory=False).drop(columns=["Geo Shape"])
        self.__dataframe = __full_dataframe.copy()
        with open(_regions_data_geojson_file, 'r') as file:
            self.__geojson_data = json.load(file)

    @staticmethod
    def __from_string_list_to_string(elem: str) -> str:
        return elem.replace("[", '').replace("]", '')[1:-1]

    @property
    def full_dataframe(self) -> pd.DataFrame:
        return self.__dataframe.copy()

    @property
    def geojson_data(self) -> dict:
        return copy.deepcopy(self.__geojson_data)

    def get_geojson_regions_dict(self,
                                 key: RegionsGeojsonDictKey = RegionsGeojsonDictKey.CODE_INSEE) -> dict:
        geojson = self.geojson_data
        geojson_dict = {}
        for region in geojson["features"]:
            dict_key = region["properties"][key.value][0] if type(
                region["properties"][key.value]) is list else region["properties"][key.value]
            geojson_dict[dict_key] = {
                "type": "FeatureCollection",
                "features": [
                    region
                ]
            }
        return geojson_dict
