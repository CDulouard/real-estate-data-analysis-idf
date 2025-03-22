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

import pandas as pd

import data.referential.communes as ref_communes
from data.exposed.departement import Departement


class Commune:
    __insee_data_communes: pd.DataFrame = None
    __geodata_communes: dict = None

    insee_code: str
    name: str
    longitude: float
    latitude: float
    geojson_shape: dict
    departement: Departement | None

    def __init__(self, code_insee: str, load_parents: bool = False):
        if Commune.__insee_data_communes is None or Commune.__geodata_communes is None:
            insee_communes_data_provider = ref_communes.Communes()
            Commune.__geodata_communes = insee_communes_data_provider.get_geojson_communes_dict()
            Commune.__insee_data_communes = insee_communes_data_provider.full_dataframe()

        insee_data_communes = Commune.__insee_data_communes

        commune_data = insee_data_communes[insee_data_communes["Code INSEE"] == code_insee]

        if not len(commune_data):
            raise Exception("INSEE code does not exist")

        self.insee_code = commune_data["Code INSEE"].iloc[0]
        self.name = commune_data["Commune"].iloc[0]

        coordinates = list(map(float, map(str.strip, commune_data["geo_point_2d"].iloc[0].split(","))))
        self.longitude = coordinates[0]
        self.latitude = coordinates[1]

        geodata_communes = Commune.__geodata_communes
        self.geojson_shape = geodata_communes[f"{self.insee_code}"]

        if load_parents:
            try:
                self.departement = Departement(commune_data["Code Département"].iloc[0], load_parents)
            except Exception:
                pass  # DROM-TOM / DROM-COM may not be associated to a departement

    @staticmethod
    def get_all(load_parents: bool = False) -> list["Commune"]:
        insee_communes_data_provider = ref_communes.Communes()
        insee_data_communes = insee_communes_data_provider.full_dataframe()

        return [Commune(insee_code, load_parents) for insee_code in insee_data_communes["Code INSEE"].values]
