from fastapi import FastAPI
from app.api import production_api

app = FastAPI()

app.include_router(production_api.router, prefix="/v1/production", tags=["production"])
