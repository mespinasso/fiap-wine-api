from app.parsers.trade_csv_parser import parse_data
from app.utils.data_search_defaults import DATA_SOURCE_URL_PREFIX, FLOOR_YEAR, CEILING_YEAR
from app.utils.file_retriever import retrieve_file

IMPORT_WINE_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ImpVinhos.csv', 'ImpVinhos')
IMPORT_SPARK_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ImpEspumantes.csv', 'ImpEspumantes')
IMPORT_GRAPES_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ImpFrescas.csv', 'ImpFrescas')
IMPORT_RAISINS_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ImpPassas.csv', 'ImpPassas')
IMPORT_JUICE_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ImpSuco.csv', 'ImpSuco')

EXPORT_WINE_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ExpVinho.csv', 'ExpVinhos')
EXPORT_SPARK_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ExpEspumantes.csv', 'ExpEspumantes')
EXPORT_GRAPES_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ExpUva.csv', 'ExpUva')
EXPORT_JUICE_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ExpSuco.csv', 'ExpSuco')


def _get_by_date_interval(initial_year: int, final_year: int, config):
    if initial_year < FLOOR_YEAR:
        initial_year = FLOOR_YEAR

    if final_year > CEILING_YEAR:
        final_year = CEILING_YEAR

    raw_data = retrieve_file(download_url=config[0], file_name=config[1])
    trade_data = parse_data(raw_data, initial_year, final_year)

    return trade_data


def get_filtered(initial_year: int, final_year: int, country_name, config):
    trade_data = _get_by_date_interval(initial_year, final_year, config)

    if country_name is not None:
        trade_data = [country for country in trade_data if country.name == country_name]

    return trade_data

def get_filtered_sum(initial_year: int, final_year: int, country_name, config):
    trade_data = get_filtered(initial_year, final_year, country_name, config)
    trade_summed_data = [country.to_dict() for country in trade_data]

    for trade_data_entry in trade_summed_data:
        trade_data_entry['total_amount'] = sum(yd['amount'] for yd in trade_data_entry['data'])
        trade_data_entry['total_value'] = sum(yd['value'] for yd in trade_data_entry['data'])

        del trade_data_entry['data']

    return trade_summed_data
