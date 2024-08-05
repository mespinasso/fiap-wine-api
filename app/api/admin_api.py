from fastapi import APIRouter, Depends

from app.services.auth_service import AuthHandler
from app.utils.file_retriever import purge_all_files as purge

router = APIRouter()
auth_handler = AuthHandler()


@router.delete("/data_files")
async def purge_all_files(logged_in_username=Depends(auth_handler.auth_wrapper)):
    purge()
    print(f'The user [{logged_in_username}] has performed the purge operation')

    return {"message": f"Files successfully deleted. User [{logged_in_username}] action was logged."}
