from app.parsers.trade_csv_parser import parse_data
from app.utils.data_search_defaults import DATA_SOURCE_URL_PREFIX, FLOOR_YEAR, CEILING_YEAR
from app.utils.file_retriever import retrieve_file

IMPORT_WINE_FILE_CONFIG = (f'{DATA_SOURCE_URL_PREFIX}ImpVinhos.csv', 'ImpVinhos')


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
