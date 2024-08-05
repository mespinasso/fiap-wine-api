from fastapi import APIRouter

from app.services.wine_service import get_filtered, get_filtered_sum, COMMERCE_FILE_CONFIG
from app.utils.data_search_defaults import FLOOR_YEAR, CEILING_YEAR

router = APIRouter()


@router.get("")
def get_commerce(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None, clear_cache=False):
    wine_data = get_filtered(int(floor_year), (int(ceiling_year) + 1), category, COMMERCE_FILE_CONFIG, clear_cache)
    return [wine.to_dict() for wine in wine_data]


@router.get("/sum")
def get_commerce_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None, clear_cache=False):
    return get_filtered_sum(int(floor_year), (int(ceiling_year) + 1), category, COMMERCE_FILE_CONFIG, clear_cache)
