import json
from dataclasses import dataclass
import urllib.request

from src.wrappers.dvf_api.data_structures import PriceDistribution, TimeSeries


@dataclass
class DVFAPIResponse:
    name: str
    code: str
    apartment_sales: int | None
    apartment_price_m2: float | None
    house_sales: int | None
    house_price_m2: float | None
    commercial_premises_sales: int | None
    commercial_premises_price_m2: float | None
    total_sales: int | None
    price_m2: float | None

    apartment_sales_historical_data: TimeSeries | None
    apartment_price_m2_historical_data: TimeSeries | None
    house_sales_historical_data: TimeSeries | None
    house_price_m2_historical_data: TimeSeries | None
    commercial_premises_sales_historical_data: TimeSeries | None
    commercial_premises_price_m2_historical_data: TimeSeries | None
    total_sales_historical_data: TimeSeries | None
    price_m2_historical_data: TimeSeries | None

    apartment_distribution: PriceDistribution | None
    house_distribution: PriceDistribution | None
    apartment_house_distribution: PriceDistribution | None
    commercial_premises_distribution: PriceDistribution | None


class DVFClient:
    __base_url: str

    def __init__(self, base_url: str = "https://dvf-api.data.gouv.fr"):
        self.__base_url = base_url

    @staticmethod
    def get_dvf_data(dvf_data_url: str,
                     distribution_data_base_url: str | None = None,
                     historical_data_base_url: str | None = None):
        dvf_raw = urllib.request.urlopen(dvf_data_url).read()
        dvf_json = json.loads(dvf_raw)

        locations: list[DVFAPIResponse] = []
        for location in dvf_json["data"]:
            distribution_json = {}
            if distribution_data_base_url is not None:
                distribution_url = distribution_data_base_url + "/" + str(location["c"])
                distribution_raw = urllib.request.urlopen(distribution_url).read()
                distribution_json = json.loads(distribution_raw)

            historical_data_json = {}
            if historical_data_base_url is not None:
                historical_data_url = historical_data_base_url + "/" + str(location["c"])
                historical_data_raw = urllib.request.urlopen(historical_data_url).read()
                historical_data_json = json.loads(historical_data_raw)

            locations.append(DVFAPIResponse(
                name=location["n"],
                code=location["c"],
                apartment_sales=location["a"],
                apartment_price_m2=location["m_a"],
                house_sales=location["m"],
                house_price_m2=location["m_m"],
                commercial_premises_sales=location["l"],
                commercial_premises_price_m2=location["m_l"],
                total_sales=location["am"],
                price_m2=location["m_am"],
                apartment_sales_historical_data=TimeSeries.from_api_response(historical_data_json, "d",
                                                                             "a") if historical_data_base_url is not None else TimeSeries(
                    records=[]),
                apartment_price_m2_historical_data=TimeSeries.from_api_response(historical_data_json, "d",
                                                                                "m_a") if historical_data_base_url is not None else TimeSeries(
                    records=[]),
                house_sales_historical_data=TimeSeries.from_api_response(historical_data_json, "d",
                                                                         "m") if historical_data_base_url is not None else TimeSeries(
                    records=[]),
                house_price_m2_historical_data=TimeSeries.from_api_response(historical_data_json, "d",
                                                                            "m_m") if historical_data_base_url is not None else TimeSeries(
                    records=[]),
                commercial_premises_sales_historical_data=TimeSeries.from_api_response(historical_data_json, "d",
                                                                                       "l") if historical_data_base_url is not None else TimeSeries(
                    records=[]),
                commercial_premises_price_m2_historical_data=TimeSeries.from_api_response(historical_data_json, "d",
                                                                                          "m_l") if historical_data_base_url is not None else TimeSeries(
                    records=[]),
                total_sales_historical_data=TimeSeries.from_api_response(historical_data_json, "d",
                                                                         "am") if historical_data_base_url is not None else TimeSeries(
                    records=[]),
                price_m2_historical_data=TimeSeries.from_api_response(historical_data_json, "d",
                                                                      "m_am") if historical_data_base_url is not None else TimeSeries(
                    records=[]),
                apartment_distribution=PriceDistribution.from_api_response(distribution_json,
                                                                           "appartement") if distribution_data_base_url is not None else TimeSeries(
                    records=[]),
                house_distribution=PriceDistribution.from_api_response(distribution_json,
                                                                       "maison") if distribution_data_base_url is not None else TimeSeries(
                    records=[]),
                apartment_house_distribution=PriceDistribution.from_api_response(distribution_json,
                                                                                 "apt_maison") if distribution_data_base_url is not None else TimeSeries(
                    records=[]),
                commercial_premises_distribution=PriceDistribution.from_api_response(distribution_json,
                                                                                     "local") if distribution_data_base_url is not None else TimeSeries(
                    records=[])
            ))

        return locations

    def get_departements(self) -> list[DVFAPIResponse]:
        dvf_data_url = self.__base_url + "/" + "departement"
        distribution_data_base_url = self.__base_url + "/" + "distribution"
        historical_data_base_url = self.__base_url + "/" + "departement"

        return DVFClient.get_dvf_data(dvf_data_url, distribution_data_base_url, historical_data_base_url)

    def get_communes_by_departement(self, departement_code: str) -> list[DVFAPIResponse]:
        dvf_data_url = self.__base_url + "/" + "departement" + "/" + departement_code + "/" + "communes"
        distribution_data_base_url = self.__base_url + "/" + "distribution"
        historical_data_base_url = self.__base_url + "/" + "commune"

        return DVFClient.get_dvf_data(dvf_data_url, distribution_data_base_url, historical_data_base_url)

    def get_sections_by_communes(self, commune_code: str) -> list[DVFAPIResponse]:
        dvf_data_url = self.__base_url + "/" + "commune" + "/" + commune_code + "/" + "sections"
        distribution_data_base_url = None
        historical_data_base_url = self.__base_url + "/" + "section"

        return DVFClient.get_dvf_data(dvf_data_url, distribution_data_base_url, historical_data_base_url)


if __name__ == "__main__":
    client = DVFClient()
    departements = client.get_sections_by_communes("07032")
    print(departements[0].__dict__)
