from fastapi import FastAPI

from app.api import production_api

app = FastAPI(
    title="Wine API 🍷",
    summary="Embrapa Wine Database API",
    version="1.0.0",
    terms_of_service="http://vitibrasil.cnpuv.embrapa.br/",
    contact={
        "name": "Matheus Espinasso",
        "url": "https://www.linkedin.com/in/matheuscoelhoespinasso"
    }
)

app.include_router(production_api.router, prefix="/v1/production", tags=["Production"])
