import datetime
from dataclasses import dataclass
from typing import Any


def parse_date(date_str):
    """
    Parses a date string into a datetime object, handling multiple formats.
    Supported formats:
    - YYYY-MM-DD
    - YYYY-MM
    - YYYY
    - DD-MM-YYYY
    - MM-DD-YYYY
    - Variations with "/", ".", etc.
    """
    date_formats = [
        "%Y-%m-%d",  # 2023-03-15
        "%Y-%m",  # 2023-03 (defaults to first day)
        "%Y",  # 2023 (defaults to Jan 1)
        "%d-%m-%Y",  # 15-03-2023
        "%m-%d-%Y",  # 03-15-2023 (US format)
        "%d/%m/%Y",  # 15/03/2023
        "%m/%d/%Y",  # 03/15/2023
        "%d.%m.%Y",  # 15.03.2023
        "%m.%d.%Y",  # 03.15.2023
    ]

    for fmt in date_formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError("Invalid date format. Use YYYY-MM-DD, YYYY-MM, YYYY, DD-MM-YYYY, MM-DD-YYYY, etc.")


@dataclass
class PriceDistribution:
    price_buckets: list[list[float, float]]
    values: list[float]

    @staticmethod
    def from_api_response(api_response: dict, key: str) -> "PriceDistribution":
        # Some departement does not have any value
        if api_response[key]["xaxis"] is None or api_response[key]["yaxis"] is None:
            return PriceDistribution(price_buckets=[], values=[])

        if len(api_response[key]["xaxis"]) != len(api_response[key]["yaxis"]):
            raise Exception("Price bucket and values differs in length")
        return PriceDistribution(price_buckets=api_response[key]["xaxis"], values=api_response[key]["yaxis"])


@dataclass
class TimeSeriesRecord:
    date: datetime.datetime
    value: Any

    def __lt__(self, other) -> bool:
        return self.date < other.date


@dataclass
class TimeSeries:
    records: list[TimeSeriesRecord]

    @staticmethod
    def from_api_response(api_response: dict, date_key: str, value_key: str) -> "TimeSeries":
        records = []
        for record in api_response["data"]:
            records.append(TimeSeriesRecord(
                date=parse_date(record[date_key]),
                value=record[value_key]
            ))
        return TimeSeries(records=sorted(records))
