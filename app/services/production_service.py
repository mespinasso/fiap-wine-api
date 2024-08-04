from app.parsers.wine_csv_parser import parse_wine_data
from app.utils.data_search_defaults import DATA_SOURCE_URL_PREFIX, FLOOR_YEAR, CEILING_YEAR
from app.utils.file_retriever import retrieve_file

PRODUCTION_DATA_URL = f'{DATA_SOURCE_URL_PREFIX}Producao.csv'
PRODUCTION_DATA_FILE_NAME = 'Producao'


def _get_by_date_interval(initial_year: int, final_year: int):
    if initial_year < FLOOR_YEAR:
        initial_year = FLOOR_YEAR

    if final_year > CEILING_YEAR:
        final_year = CEILING_YEAR

    raw_data = retrieve_file(download_url=PRODUCTION_DATA_URL, file_name=PRODUCTION_DATA_FILE_NAME)
    wine_data = parse_wine_data(raw_data, initial_year, final_year)

    return wine_data


def get_filtered(initial_year: int, final_year: int, category):
    wine_data = _get_by_date_interval(initial_year, final_year)

    if category is not None:
        wine_data = [wine for wine in wine_data if wine.category == category]

    return wine_data


def get_filtered_sum(initial_year: int, final_year: int, category):
    wine_data = get_filtered(initial_year, final_year, category)
    wine_summed_data = [wine.to_dict() for wine in wine_data]

    for wine_data_entry in wine_summed_data:
        wine_data_entry['sum'] = sum([ywd['amount'] for ywd in wine_data_entry['data']])
        del wine_data_entry['data']

    return wine_summed_data
