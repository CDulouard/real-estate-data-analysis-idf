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

import pandas as pd

from data.clean.dvf._constants import _insee_code_column_raw_dvf, _insee_code_column_referential, _unused_columns, \
    _columns_to_drop_after_join, _columns_to_rename, _dvf_data_csv_file
from data.referential.communes import Communes
from data.raw.dvf import DVF


def __drop_insee_code_not_in_referential(raw_dvf_df: pd.DataFrame,
                                         referential_communes_df: pd.DataFrame) -> pd.DataFrame:
    unique_communes_dvf = list(raw_dvf_df["code_commune"].dropna().unique())
    unique_communes = list(referential_communes_df["Code INSEE"].dropna().unique())
    communes_not_in_referential = [commune for commune in unique_communes_dvf if commune not in unique_communes]
    return raw_dvf_df[~raw_dvf_df["code_commune"].isin(communes_not_in_referential)].copy()


def __drop_unused_columns(dvf_df: pd.DataFrame) -> pd.DataFrame:
    return dvf_df.drop(columns=_unused_columns).copy()


def __enrich_dvf_with_referential(dvf_df: pd.DataFrame,
                                  referential_communes_df: pd.DataFrame) -> pd.DataFrame:
    merged_df = dvf_df.merge(referential_communes_df, left_on=_insee_code_column_raw_dvf,
                             right_on=_insee_code_column_referential, how="left").copy()
    return merged_df.drop(columns=_columns_to_drop_after_join)


def __rename_columns(dvf_df: pd.DataFrame) -> pd.DataFrame:
    return dvf_df.rename(columns=_columns_to_rename)


def clean_all() -> None:
    raw_dvf: pd.DataFrame = DVF().full_dataframe()
    communes: pd.DataFrame = Communes().full_dataframe()

    clean_dvf = __drop_unused_columns(__drop_insee_code_not_in_referential(raw_dvf, communes))
    enriched_dvf = __enrich_dvf_with_referential(clean_dvf, communes)
    dvf_with_renamed_columns = __rename_columns(enriched_dvf)

    dvf_with_renamed_columns.to_csv(_dvf_data_csv_file, index=False, sep=";", decimal=".")

    logging.info(f"Successfully saved DVF records")
