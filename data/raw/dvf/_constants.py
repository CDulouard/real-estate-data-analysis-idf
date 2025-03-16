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
_dvf_base_url = "https://dvf-api.data.gouv.fr/dvf/csv/"
_dvf_departement_parameter = "dep"

_dtype_maping_only_string = {
    "id_mutation": "string",
    "numero_disposition": "string",
    "nature_mutation": "string",
    "valeur_fonciere": "string",
    "adresse_numero": "string",
    "adresse_suffixe": "string",
    "adresse_nom_voie": "string",
    "adresse_code_voie": "string",
    "code_postal": "string",
    "code_commune": "string",
    "nom_commune": "string",
    "code_departement": "string",
    "ancien_code_commune": "string",
    "ancien_nom_commune": "string",
    "id_parcelle": "string",
    "ancien_id_parcelle": "string",
    "numero_volume": "string",
    "lot1_numero": "string",
    "lot1_surface_carrez": "string",
    "lot2_numero": "string",
    "lot2_surface_carrez": "string",
    "lot3_numero": "string",
    "lot3_surface_carrez": "string",
    "lot4_numero": "string",
    "lot4_surface_carrez": "string",
    "lot5_numero": "string",
    "lot5_surface_carrez": "string",
    "nombre_lots": "string",
    "code_type_local": "string",
    "type_local": "string",
    "surface_reelle_bati": "string",
    "nombre_pieces_principales": "string",
    "code_nature_culture": "string",
    "nature_culture": "string",
    "code_nature_culture_speciale": "string",
    "nature_culture_speciale": "string",
    "surface_terrain": "string",
    "longitude": "string",
    "latitude": "string",
    "section_prefixe": "string"
}

_float_columns = ["valeur_fonciere",
                  "lot1_surface_carrez",
                  "lot2_surface_carrez",
                  "lot3_surface_carrez",
                  "lot4_surface_carrez",
                  "lot4_surface_carrez",
                  "lot5_surface_carrez",
                  "nombre_lots",
                  "surface_reelle_bati",
                  "nombre_pieces_principales",
                  "surface_terrain",
                  "longitude",
                  "latitude"
                  ]

_date_columns = ["date_mutation"]

_dtype_mapping_with_numerical_values = {
    "id_mutation": "string",
    "numero_disposition": "string",
    "nature_mutation": "string",
    "valeur_fonciere": "float64",
    "adresse_numero": "string",
    "adresse_suffixe": "string",
    "adresse_nom_voie": "string",
    "adresse_code_voie": "string",
    "code_postal": "string",
    "code_commune": "string",
    "nom_commune": "string",
    "code_departement": "string",
    "ancien_code_commune": "string",
    "ancien_nom_commune": "string",
    "id_parcelle": "string",
    "ancien_id_parcelle": "string",
    "numero_volume": "string",
    "lot1_numero": "string",
    "lot1_surface_carrez": "float64",
    "lot2_numero": "string",
    "lot2_surface_carrez": "float64",
    "lot3_numero": "string",
    "lot3_surface_carrez": "float64",
    "lot4_numero": "string",
    "lot4_surface_carrez": "float64",
    "lot5_numero": "string",
    "lot5_surface_carrez": "float64",
    "nombre_lots": "float64",
    "code_type_local": "string",
    "type_local": "string",
    "surface_reelle_bati": "float64",
    "nombre_pieces_principales": "float64",
    "code_nature_culture": "string",
    "nature_culture": "string",
    "code_nature_culture_speciale": "string",
    "nature_culture_speciale": "string",
    "surface_terrain": "float64",
    "longitude": "float64",
    "latitude": "float64",
    "section_prefixe": "string"
}
