from fastapi import APIRouter

from app.utils.file_retriever import purge_all_files as purge

router = APIRouter()


@router.delete("/data_files")
async def purge_all_files():
    purge()
    return {"message": "Files successfully deleted"}
