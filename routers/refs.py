from fastapi import APIRouter

router = APIRouter()


@router.get("/country/list/", tags=["refs"])
async def country_list():
    return {"list": True}


@router.get("/country/detail/{id}", tags=["refs"])
async def country_detail():
    return {"detail": True}


@router.post("/country/add/", tags=["refs"])
async def country_add():
    return {"add": True}


@router.put("/country/edit/{id}", tags=["refs"])
async def country_edit():
    return {"edit": True}


@router.delete("/country/delete/{id}", tags=["refs"])
async def country_delete():
    return {"delete": True}
