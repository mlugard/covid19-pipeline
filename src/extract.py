from kaggle.api.kaggle_api_extended import KaggleApi
import os

def download_kaggle_dataset(dataset: str, dest_folder: str = "Data Engineering/covid19-pipeline/data/raw", unzip: bool = True):
    os.makedirs(dest_folder, exist_ok=True)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=dest_folder, unzip=unzip, force=True)
    print(f"Dataset baixado em: {dest_folder}")

if __name__ == "__main__":
    download_kaggle_dataset("imdevskp/corona-virus-report")