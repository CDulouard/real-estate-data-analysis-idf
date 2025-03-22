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

from pathlib import Path

_sections_data_csv_file = f"{Path(__file__).parent}/sections_cadastre.csv"
_sections_data_geojson_file = f"{Path(__file__).parent}/sections_cadastre.geojson"
_sections_geojson_data_url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/2025-01-01/geojson/france/cadastre-france-sections.json.gz"

_dtype_mapping_with_numerical_values = {
    "id": "string",
    "code_insee_commune": "string",
    "prefixe": "string",
    "code": "string",
    "geojson_shape": "object"
}
