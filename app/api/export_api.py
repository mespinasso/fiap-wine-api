from fastapi import APIRouter

from app.services.trade_service import get_filtered, get_filtered_sum, EXPORT_WINE_FILE_CONFIG, \
    EXPORT_SPARK_FILE_CONFIG, EXPORT_GRAPES_FILE_CONFIG, EXPORT_JUICE_FILE_CONFIG
from app.utils.data_search_defaults import FLOOR_YEAR, CEILING_YEAR

router = APIRouter()


@router.get("/wine")
def get_wine_exports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None, clear_cache=False):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, EXPORT_WINE_FILE_CONFIG, clear_cache)
    return [country.to_dict() for country in trade_data]


@router.get("/wine/sum")
def get_wine_exports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None, clear_cache=False):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, EXPORT_WINE_FILE_CONFIG, clear_cache)


@router.get("/sparkling_wine")
def get_sparkling_wine_exports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None, clear_cache=False):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, EXPORT_SPARK_FILE_CONFIG, clear_cache)
    return [country.to_dict() for country in trade_data]


@router.get("/sparkling_wine/sum")
def get_sparkling_wine_exports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None, clear_cache=False):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, EXPORT_SPARK_FILE_CONFIG, clear_cache)


@router.get("/grapes")
def get_grapes_exports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None, clear_cache=False):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, EXPORT_GRAPES_FILE_CONFIG, clear_cache)
    return [country.to_dict() for country in trade_data]


@router.get("/grapes/sum")
def get_grapes_exports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None, clear_cache=False):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, EXPORT_GRAPES_FILE_CONFIG, clear_cache)


@router.get("/juice")
def get_juice_exports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None, clear_cache=False):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, EXPORT_JUICE_FILE_CONFIG, clear_cache)
    return [country.to_dict() for country in trade_data]


@router.get("/juice/sum")
def get_juice_exports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None, clear_cache=False):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, EXPORT_JUICE_FILE_CONFIG, clear_cache)
