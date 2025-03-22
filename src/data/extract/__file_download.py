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

import gzip
import requests
import os
import logging
import tempfile
import shutil


def download_raw_file(url: str, output_file: str) -> None:
    response = requests.get(url)

    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            file.write(response.content)
        logging.info(f"File {output_file} downloaded successfully")
    else:
        logging.error(f"Failed to retrieve the file {output_file}. Status code: {response.status_code}")
        raise Exception("Download failed")


def delete_file_if_exist(target_file: str) -> None:
    if os.path.exists(target_file):
        os.remove(target_file)
        logging.info(f"File '{target_file}' has been deleted.")
    else:
        logging.info(f"File '{target_file}' does not exist, nothing to do")


def download_and_replace_file(url: str, output_file: str) -> None:
    logging.info(f"Preparing to replace the file: {output_file}")
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name

    try:
        logging.info(f"Downloading the file to a temporary location: {temp_path}")
        download_raw_file(url, temp_path)
        delete_file_if_exist(output_file)
        shutil.move(temp_path, output_file)
        logging.info(f"File {output_file} has been replaced successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
            logging.info(f"Temporary file {temp_path} has been removed.")
        raise


def extract_gzip(gzip_file: str) -> None:
    output_directory = os.path.dirname(gzip_file)
    output_file = os.path.basename(gzip_file)[:-3]
    with gzip.open(gzip_file, 'rb') as f_in:
        with open(f"{output_directory}/{output_file}", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
