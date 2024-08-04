from app.parsers.wine_csv_parser import parse_data
from app.utils.data_search_defaults import DATA_SOURCE_URL_PREFIX, FLOOR_YEAR, CEILING_YEAR
from app.utils.file_retriever import retrieve_file

PRODUCTION_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}Producao.csv', 'Producao', 'produto', ';')

WINE_GRAPE_PRO_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ProcessaViniferas.csv', 'ProcessaViniferas', 'cultivar', ';')
AMER_GRAPE_PRO_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ProcessaAmericanas.csv', 'ProcessaAmericanas', 'cultivar', '\t')
TABLE_GRAPE_PRO_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ProcessaMesa.csv', 'ProcessaMesa', 'cultivar', '\t')
DCL_GRAPE_PRO_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ProcessaSemclass.csv', 'ProcessaSemclass', 'cultivar', '\t')

COMMERCE_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}Comercio.csv', 'Comercio', 'produto', ';')


def _get_by_date_interval(initial_year: int, final_year: int, config):
    if initial_year < FLOOR_YEAR:
        initial_year = FLOOR_YEAR

    if final_year > CEILING_YEAR:
        final_year = CEILING_YEAR

    raw_data = retrieve_file(download_url=config[0], file_name=config[1])
    wine_data = parse_data(raw_data, initial_year, final_year, config[2], config[3])

    return wine_data


def get_filtered(initial_year: int, final_year: int, category, config):
    wine_data = _get_by_date_interval(initial_year, final_year, config)

    if category is not None:
        wine_data = [wine for wine in wine_data if wine.category == category]

    return wine_data


def get_filtered_sum(initial_year: int, final_year: int, category, config):
    wine_data = get_filtered(initial_year, final_year, category, config)
    wine_summed_data = [wine.to_dict() for wine in wine_data]

    for wine_data_entry in wine_summed_data:
        wine_data_entry['sum'] = sum([ywd['amount'] for ywd in wine_data_entry['data']])
        del wine_data_entry['data']

    return wine_summed_data
