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

_dvf_data_csv_file = f"{Path(__file__).parent}/dvf.csv"

_insee_code_column_raw_dvf = "code_commune"
_insee_code_column_referential = "Code INSEE"

_unused_columns = ["ancien_code_commune", "ancien_nom_commune", "ancien_id_parcelle"]
_columns_to_drop_after_join = ["code_postal", "code_commune", "nom_commune", "code_departement"]

_columns_to_rename = {
    "Code INSEE": "code_insee",
    "Code Postal": "code_postal",
    "Commune": "commune",
    "Département": "departement",
    "Région": "region",
    "Statut": "statut",
    "Altitude Moyenne": "altitude_moyenne",
    "Superficie": "superficie",
    "Population": "population",
    "ID Geofla": "id_geofla",
    "Code Commune": "code_commune",
    "Code Canton": "code_canton",
    "Code Arrondissement": "code_arrondissement",
    "Code Département": "code_departement",
    "Code Région": "code_region"
}
