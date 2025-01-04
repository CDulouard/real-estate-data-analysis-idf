import data.referential.communes as communes
import data.referential.departements as departements
import data.referential.regions as regions


def download_all() -> None:
    communes.download_all()
    departements.download_all()
    regions.download_all()
