from fastapi import APIRouter

from app.services.wine_service import get_filtered as get_filtered_svc, get_filtered_sum as get_filtered_sum_svc, \
    PRODUCTION_FILE_CONFIG
from app.utils.data_search_defaults import FLOOR_YEAR, CEILING_YEAR

router = APIRouter()


@router.get("")
def get_filtered(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    wine_data = get_filtered_svc(int(floor_year), (int(ceiling_year) + 1), category, PRODUCTION_FILE_CONFIG)
    return [wine.to_dict() for wine in wine_data]


@router.get("/sum")
def get_filtered_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    return get_filtered_sum_svc(int(floor_year), (int(ceiling_year) + 1), category, PRODUCTION_FILE_CONFIG)
