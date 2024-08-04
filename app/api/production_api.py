from fastapi import APIRouter

from app.services.production_service import get_all as get_all_svc

router = APIRouter()


@router.get("/")
def get_all():
    return [wine.to_dict() for wine in get_all_svc()]
