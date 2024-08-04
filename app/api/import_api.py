from fastapi import APIRouter

from app.services.trade_service import get_filtered, get_filtered_sum, IMPORT_WINE_FILE_CONFIG
from app.utils.data_search_defaults import FLOOR_YEAR, CEILING_YEAR

router = APIRouter()


@router.get("")
def get_imports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    trade_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_WINE_FILE_CONFIG)
    return [country.to_dict() for country in trade_data]


@router.get("/sum")
def get_imports(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, country_name=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), country_name, IMPORT_WINE_FILE_CONFIG)
