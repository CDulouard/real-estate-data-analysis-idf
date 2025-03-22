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

import data.referential.sections as ref_sections
from data.exposed.commune import Commune


class Section:
    __insee_data_sections: pd.DataFrame = None
    __geodata_sections: dict = None

    id: str
    code_insee_commune: str
    prefixe: str
    code: str
    geojson_shape: dict
    commune: Commune

    def __init__(self, id_section: str, load_parents: bool = False):
        Section.__load_referential()

        insee_data_sections = Section.__insee_data_sections

        section_data = insee_data_sections[insee_data_sections["id"] == id_section]

        if not len(section_data):
            raise Exception("Section ID does not exist")

        self.id = section_data["id"].iloc[0]
        self.code_insee_commune = section_data["code_insee_commune"].iloc[0]
        self.prefixe = section_data["prefixe"].iloc[0]
        self.code = section_data["code"].iloc[0]

        geodata_sections = Section.__geodata_sections
        self.geojson_shape = geodata_sections[f"{self.id}"]

        if load_parents:
            try:
                self.commune = Commune(section_data["code_insee_commune"].iloc[0], load_parents)
            except Exception:
                pass  # DROM-TOM / DROM-COM may cause issue

    @staticmethod
    def __load_referential() -> None:
        if Section.__insee_data_sections is None or Section.__geodata_sections is None:
            insee_sections_data_provider = ref_sections.Section()
            Section.__geodata_sections = insee_sections_data_provider.get_geojson_sections_dict()
            Section.__insee_data_sections = insee_sections_data_provider.full_dataframe()

    @staticmethod
    def get_by_commune(code_insee_commune: str, load_parents: bool = False) -> list["Section"]:
        Section.__load_referential()

        sections = Section.__insee_data_sections[
            Section.__insee_data_sections["code_insee_commune"] == code_insee_commune]

        return [Section(section_id, load_parents) for section_id in sections["id"].values]
