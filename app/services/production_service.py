from app.utils.file_retriever import retrieve_file
from app.parsers.wine_csv_parser import parse_wine_data

PRODUCTION_DATA_URL = 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'
PRODUCTION_DATA_FILE_NAME = 'Producao'


def get_all():
    raw_data = retrieve_file(download_url=PRODUCTION_DATA_URL, file_name=PRODUCTION_DATA_FILE_NAME)
    wine_data = parse_wine_data(raw_data, 2020, 2023)

    return wine_data
