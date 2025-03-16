import pandas as pd

import data.referential.departements as ref_departements
from data.domain.region import Region


class Departement:
    __insee_data_departements: pd.DataFrame = None
    __geodata_departements: dict = None

    insee_code: str
    name: str
    longitude: float
    latitude: float
    geojson_shape: dict
    region: Region

    def __init__(self, code_insee: str, load_parent: bool = False):
        if Departement.__insee_data_departements is None or Departement.__geodata_departements is None:
            insee_departements_data_provider = ref_departements.Departements()
            Departement.__geodata_departements = insee_departements_data_provider.get_geojson_departements_dict()
            Departement.__insee_data_departements = insee_departements_data_provider.full_dataframe()

        insee_data_departements = Departement.__insee_data_departements

        departement_data = insee_data_departements[insee_data_departements["Code Officiel Département"] == code_insee]

        if not len(departement_data):
            raise Exception("INSEE code does not exist")

        self.insee_code = departement_data["Code Officiel Département"].iloc[0]
        self.name = departement_data["Nom Officiel Département"].iloc[0]

        coordinates = list(map(float, map(str.strip, departement_data["Geo Point"].iloc[0].split(","))))
        self.longitude = coordinates[0]
        self.latitude = coordinates[1]

        geodata_departements = Departement.__geodata_departements

        self.geojson_shape = geodata_departements[f"{self.insee_code}"]

        if load_parent:
            try:
                self.region = Region(departement_data["Code Officiel Région"].iloc[0])
            except Exception:
                pass  # DROM-TOM / DROM-COM may not be associated to a region

    @staticmethod
    def get_all(load_parent: bool = False) -> list["Departement"]:
        insee_departements_data_provider = ref_departements.Departements()
        insee_data_departements = insee_departements_data_provider.full_dataframe()

        return [Departement(insee_code, load_parent) for insee_code in
                insee_data_departements["Code Officiel Département"].values]
