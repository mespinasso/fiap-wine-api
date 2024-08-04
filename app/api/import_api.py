from fastapi import APIRouter

from app.services.trade_service import get_filtered, get_filtered_sum, IMPORT_WINE_FILE_CONFIG, \
    IMPORT_SPARK_FILE_CONFIG, IMPORT_GRAPES_FILE_CONFIG, IMPORT_RAISINS_FILE_CONFIG, IMPORT_JUICE_FILE_CONFIG
from app.utils.data_search_defaults import FLOOR_YEAR, CEILING_YEAR

router = APIRouter()


@router.get("/wine")
def get_wine_imports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_WINE_FILE_CONFIG)
    return [country.to_dict() for country in trade_data]


@router.get("/wine/sum")
def get_wine_imports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_WINE_FILE_CONFIG)


@router.get("/sparkling_wine")
def get_sparkling_wine_imports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_SPARK_FILE_CONFIG)
    return [country.to_dict() for country in trade_data]


@router.get("/sparkling_wine/sum")
def get_sparkling_wine_imports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_SPARK_FILE_CONFIG)


@router.get("/grapes")
def get_grapes_imports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_GRAPES_FILE_CONFIG)
    return [country.to_dict() for country in trade_data]


@router.get("/grapes/sum")
def get_grapes_imports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_GRAPES_FILE_CONFIG)


@router.get("/raisins")
def get_raisins_imports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_RAISINS_FILE_CONFIG)
    return [country.to_dict() for country in trade_data]


@router.get("/raisins/sum")
def get_raisins_imports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_RAISINS_FILE_CONFIG)


@router.get("/juice")
def get_juice_imports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_JUICE_FILE_CONFIG)
    return [country.to_dict() for country in trade_data]


@router.get("/juice/sum")
def get_juice_imports_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_JUICE_FILE_CONFIG)
