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

from data.raw.dvf._constants import _dtype_mapping_with_numerical_values, _dvf_data_csv_file, _date_columns


class DVF:
    __dataframe: pd.DataFrame

    def __init__(self):
        self.__dataframe = pd.read_csv(_dvf_data_csv_file,
                                       parse_dates=_date_columns,
                                       dtype=_dtype_mapping_with_numerical_values,
                                       sep=";")

    def full_dataframe(self) -> pd.DataFrame:
        return self.__dataframe.copy()
