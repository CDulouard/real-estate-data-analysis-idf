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

import data.referential.communes as communes
import data.referential.departements as departements
import data.referential.regions as regions
import data.referential.sections as sections


def download_all() -> None:
    communes.download_all()
    departements.download_all()
    regions.download_all()
    sections.download_all()
