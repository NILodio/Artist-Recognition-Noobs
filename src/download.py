import os
from kaggle.api.kaggle_api_extended import KaggleApi
from decouple import config



from config import logging
import zipfile

LOGGER = logging.create_log('download')

import subprocess
import os
import zipfile

LOGGER.info("Downloading dataset from Kaggle...")
class KaggleDatasetDownloader:
    def __init__(self, dataset_name, download_path='.'):
        self.dataset_name = dataset_name
        self.download_path = download_path

    def download_dataset(self):
        # Run the Kaggle download command using subprocess
        command = f'kaggle datasets download -d {self.dataset_name} -p {self.download_path}'

        try:
            subprocess.run(command, shell=True, check=True)
            LOGGER.info(f"Dataset '{self.dataset_name}' downloaded successfully.")
            print(f"Dataset '{self.dataset_name}' downloaded successfully.")
        except subprocess.CalledProcessError as e:
            LOGGER.error(f"Error downloading dataset '{self.dataset_name}': {e}")
            print(f"Error downloading dataset '{self.dataset_name}': {e}")

    def extract_zip(self):
        zip_file_path = os.path.join(self.download_path, f'{self.dataset_name.split("/")[1]}.zip')
        extract_path = os.path.join(self.download_path, 'extracted')

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        LOGGER.info(f"Dataset '{self.dataset_name}' extracted to '{extract_path}'.")
        print(f"Dataset '{self.dataset_name}' extracted to '{extract_path}'.")

if __name__ == "__main__":
    LOGGER.error("This is an error message")
    dataset_name = 'ikarus777/best-artworks-of-all-time'
    download_path = './data'  # Specify your desired download path
    downloader = KaggleDatasetDownloader(dataset_name, download_path)
    downloader.download_dataset()
    downloader.extract_zip()
