from fastapi import APIRouter

from controllers.vk import VKController


router = APIRouter()


@router.get("/vk/authorize", tags=["vk"])
async def vk_authorize(user_id: str = None):
    vk = VKController()
    data = vk.get_users(user_id)

    response = {
        "data": data
    }
    return response


@router.get("/vk/{user_id}", tags=["vk"])
async def vk_get_user(user_id: str = None):
    vk = VKController()
    data = vk.get_users(user_id)

    response = {
        "data": data
    }
    return response
