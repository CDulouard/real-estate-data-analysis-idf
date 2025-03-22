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

import data.referential.regions as ref_regions


class Region:
    __insee_data_regions: pd.DataFrame = None
    __geodata_regions: dict = None

    insee_code: str
    name: str
    longitude: float
    latitude: float
    geojson_shape: dict

    def __init__(self, code_insee: str):
        if Region.__insee_data_regions is None or Region.__geodata_regions is None:
            insee_regions_data_provider = ref_regions.Regions()
            Region.__geodata_regions = insee_regions_data_provider.get_geojson_regions_dict()
            Region.__insee_data_regions = insee_regions_data_provider.full_dataframe()

        insee_data_regions = Region.__insee_data_regions

        region_data = insee_data_regions[insee_data_regions["Code Officiel Région"] == code_insee]

        if not len(region_data):
            raise Exception("INSEE code does not exist")

        self.insee_code = f"{region_data["Code Officiel Région"].iloc[0]:02}"
        self.name = region_data["Nom Officiel Région"].iloc[0]

        coordinates = list(map(float, map(str.strip, region_data["Geo Point"].iloc[0].split(","))))
        self.longitude = coordinates[0]
        self.latitude = coordinates[1]

        geodata_regions = Region.__geodata_regions

        self.geojson_shape = geodata_regions[self.insee_code]

    @staticmethod
    def get_all() -> list["Region"]:
        insee_regions_data_provider = ref_regions.Regions()
        insee_data_regions = insee_regions_data_provider.full_dataframe()

        return [Region(insee_code) for insee_code in insee_data_regions["Code Officiel Région"].values]
