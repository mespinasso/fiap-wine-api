from fastapi import FastAPI

from app.api import production_api, processing_api, commerce_api, import_api, export_api, admin_api, auth_api

description = """
## Sobre a API

A Wine API oferece uma maneira fácil de consumir dados sobre a produção, processamento e comercialização de vinhos.
Utilize os endpoints disponíveis para acessar os dados fornecidos pela Embrapa.

## Endpoints públicos

Você pode consultar todos os dados através dos endpoints públicos de consulta, sem necessidade de de cadastrar 
na aplicação.

## Endpoints protegidos

A seção de gerenciamento da API, que permite a exclusão de todos os arquivos de cache dos dados da Embrapa, somente pode
ser acessada após registro e autenticação do usuário.
"""

app = FastAPI(
    title="Wine API 🍷",
    summary="Embrapa Wine Database API",
    description=description,
    version="1.0.0",
    contact={
        "name": "Matheus Espinasso",
        "url": "https://www.linkedin.com/in/matheuscoelhoespinasso"
    },
    license_info={
        "name": "Embrapa",
        "url": "http://vitibrasil.cnpuv.embrapa.br/",
    }
)

app.include_router(auth_api.router, prefix="/v1/auth", tags=["Authentication"])
app.include_router(production_api.router, prefix="/v1/production", tags=["Production"])
app.include_router(processing_api.router, prefix="/v1/processing", tags=["Processing"])
app.include_router(commerce_api.router, prefix="/v1/commerce", tags=["Commerce"])
app.include_router(import_api.router, prefix="/v1/imports", tags=["Imports"])
app.include_router(export_api.router, prefix="/v1/exports", tags=["Exports"])
app.include_router(admin_api.router, prefix="/v1/admin", tags=["Administration"])
