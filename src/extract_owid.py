import requests
import json
from datetime import datetime
from pathlib import Path
import pandas as pd

def extract_covid_data():
    url = "https://ourworldindata.org/grapher/weekly-covid-cases.csv"
    
    print(f"[INFO] Iniciando extração em {datetime.now().isoformat()}")
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erro ao acessar API: {response.status_code}")
    
    data = pd.read_csv(url)
    
    # Save raw data
    raw_path = Path("Data_Engineering/covid19-pipeline/data/raw")
    raw_path.mkdir(parents=True, exist_ok=True)
    
    file_name = raw_path / f"covid_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    data.to_csv(file_name, index=False)

    print(f"[INFO] Dados salvos em {file_name}")
    return data

if __name__ == "__main__":
    extract_covid_data()