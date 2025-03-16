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
from functools import reduce

import pandas as pd

from data.referential.communes._constants import _communes_data_csv_file, _communes_data_geojson_file


class CommunesGeojsonDictKey(Enum):
    CODE_POSTAL = "postal_code"
    CODE_INSEE = "insee_com"
    NOM = "nom_comm"


class Communes:
    __dataframe: pd.DataFrame
    __dataframe_split_by_code_postal: pd.DataFrame
    __geojson_data: dict

    def __init__(self):
        __full_dataframe = pd.read_csv(_communes_data_csv_file, sep=";", low_memory=False)
        __full_dataframe = Communes.__fix_dataframe(__full_dataframe)
        self.__dataframe = __full_dataframe.copy()
        self.__dataframe_split_by_code_postal = Communes.__split_grouped_communes_by_code_postal(
            __full_dataframe.copy())
        with open(_communes_data_geojson_file, 'r') as file:
            self.__geojson_data = json.load(file)

    @staticmethod
    def __get_grouped_communes(df: pd.DataFrame) -> pd.DataFrame:
        return df[df["Code Postal"].str.contains("/")]

    @staticmethod
    def __split_grouped_communes_by_code_postal(df: pd.DataFrame) -> pd.DataFrame:
        grouped_communes = Communes.__get_grouped_communes(df)
        remaining_communes = df[~df["Code INSEE"].isin(grouped_communes["Code INSEE"])]
        split_communes = reduce(
            lambda state, index_row: state + [(i, index_row[1]) for i in index_row[1]["Code Postal"].split("/")],
            grouped_communes.iterrows(), [])
        split_communes_as_df = pd.DataFrame([i[1].replace(i[1]["Code Postal"], i[0]) for i in split_communes])
        return pd.concat([remaining_communes, split_communes_as_df]).reset_index()

    @staticmethod
    def __from_string_list_to_string(elem: str) -> str:
        return elem.replace("[", '').replace("]", '')[1:-1]

    @staticmethod
    def __fix_dataframe(df: pd.DataFrame):
        df["Département"] = df["Département"].apply(Communes.__from_string_list_to_string)
        df["Région"] = df["Région"].apply(Communes.__from_string_list_to_string)
        df["Statut"] = df["Statut"].apply(Communes.__from_string_list_to_string)
        df["geo_shape"] = df["geo_shape"].apply(lambda x: json.loads(x))
        return df.drop(columns=["geo_shape"])

    def full_dataframe(self) -> pd.DataFrame:
        return self.__dataframe.copy()

    def full_dataframe_split_by_code_postal(self) -> pd.DataFrame:
        return self.__dataframe_split_by_code_postal.copy()

    def geojson_data(self) -> dict:
        return copy.deepcopy(self.__geojson_data)

    def get_geojson_communes_dict(self, key: CommunesGeojsonDictKey = CommunesGeojsonDictKey.CODE_INSEE) -> dict:
        geojson = self.geojson_data()
        geojson_dict = {}
        for commune in geojson["features"]:
            geojson_dict[commune["properties"][key.value]] = {
                "type": "FeatureCollection",
                "features": [
                    commune
                ]
            }
        return geojson_dict
