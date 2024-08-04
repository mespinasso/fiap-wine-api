from fastapi import APIRouter

from app.services.wine_service import get_filtered, get_filtered_sum, WINE_GRAPE_PRO_FILE_CONFIG, \
    AMER_GRAPE_PRO_FILE_CONFIG, TABLE_GRAPE_PRO_FILE_CONFIG, DCL_GRAPE_PRO_FILE_CONFIG
from app.utils.data_search_defaults import FLOOR_YEAR, CEILING_YEAR

router = APIRouter()


@router.get("/wine_grapes")
def get_wine_grape_production(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    wine_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), category, WINE_GRAPE_PRO_FILE_CONFIG)
    return [wine.to_dict() for wine in wine_data]


@router.get("/wine_grapes/sum")
def get_wine_grape_production_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), category, WINE_GRAPE_PRO_FILE_CONFIG)


@router.get("/american_hybrid_grapes")
def get_wine_grape_production(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    wine_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), category, AMER_GRAPE_PRO_FILE_CONFIG)
    return [wine.to_dict() for wine in wine_data]


@router.get("/american_hybrid_grapes/sum")
def get_wine_grape_production_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), category, AMER_GRAPE_PRO_FILE_CONFIG)


@router.get("/table_grapes")
def get_wine_grape_production(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    wine_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), category, TABLE_GRAPE_PRO_FILE_CONFIG)
    return [wine.to_dict() for wine in wine_data]


@router.get("/table_grapes/sum")
def get_wine_grape_production_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), category, TABLE_GRAPE_PRO_FILE_CONFIG)


@router.get("/declassified_grapes")
def get_wine_grape_production(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    wine_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), category, DCL_GRAPE_PRO_FILE_CONFIG)
    return [wine.to_dict() for wine in wine_data]


@router.get("/declassified_grapes/sum")
def get_wine_grape_production_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), category, DCL_GRAPE_PRO_FILE_CONFIG)
