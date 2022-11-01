from fastapi import APIRouter

router = APIRouter()


@router.get("/health_check/", tags=["system"])
async def health_check():
    return {"success": True}
