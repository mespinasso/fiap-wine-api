from fastapi import APIRouter

from app.models.user_auth_model import UserAuth
from app.services.auth_service import AuthHandler

router = APIRouter()

auth_handler = AuthHandler()


@router.post('/register', status_code=201)
def register(auth_details: UserAuth):
    auth_handler.register_user(auth_details)


@router.post('/login')
def login(auth_details: UserAuth):
    return auth_handler.authenticate_user(auth_details)
