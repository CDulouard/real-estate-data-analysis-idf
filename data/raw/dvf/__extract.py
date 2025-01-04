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

import logging
from io import BytesIO
import requests

import pandas as pd

from data.referential.departements import Departements

from data.raw.dvf._constants import _dvf_base_url, _dvf_departement_parameter, _dtype_mapping, _float_columns, \
    _dvf_data_csv_file


def __fetch_data_of_departement(departement_code: str) -> pd.DataFrame:
    params = {
        _dvf_departement_parameter: departement_code
    }
    response = requests.get(_dvf_base_url, params=params)
    if response.status_code != 200:
        logging.error(
            f"Failed to retrieve data for departement number {departement_code}. Status code: {response.status_code}")
        raise Exception("Download failed")

    if not response.content:
        logging.info(f"No data to retrieve for departement number {departement_code}")
        return pd.DataFrame()

    response_dataframe = pd.read_csv(BytesIO(response.content), parse_dates=["date_mutation"], dtype=_dtype_mapping,
                                     low_memory=False)
    for float_column in _float_columns:
        response_dataframe[float_column] = pd.to_numeric(response_dataframe[float_column], errors="coerce")

    logging.info(f"Successfully retrieved data for departement number {departement_code}")
    return response_dataframe


def __fetch_data_of_all_departements() -> pd.DataFrame:
    departements = Departements()
    code_list = departements.get_departements_codes_list()
    departements_dataframes = []
    for i, code in enumerate(code_list):
        logging.info(f"Downloading DVF data for departement {i + 1} on {len(code_list)}")
        departements_dataframes.append(__fetch_data_of_departement(code))
    full_df = pd.concat(departements_dataframes, ignore_index=True)
    logging.info(f"Successfully retrieved {len(full_df)} DVF records")
    return full_df


def download_all() -> None:
    dvf_df = __fetch_data_of_all_departements()
    dvf_df.to_csv(_dvf_data_csv_file, index=False, sep=";", decimal=".")
    logging.info(f"Successfully saved DVF records")
