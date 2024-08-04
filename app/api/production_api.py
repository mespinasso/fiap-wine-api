from fastapi import APIRouter

from app.services.production_service import get_filtered as get_filtered_svc, get_filtered_sum as get_filtered_sum_svc
from app.utils.data_search_defaults import FLOOR_YEAR, CEILING_YEAR

router = APIRouter()


@router.get("")
def get_all(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    return [wine.to_dict() for wine in get_filtered_svc(int(floor_year), (int(ceiling_year) + 1), category)]


@router.get("/sum")
def get_filtered_sum(floor_year=FLOOR_YEAR, ceiling_year=CEILING_YEAR - 1, category=None):
    return get_filtered_sum_svc(int(floor_year), (int(ceiling_year) + 1), category)
