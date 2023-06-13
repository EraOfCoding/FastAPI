from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data

class FindShanyrakResponse(AppModel):
    type: str
    price: float
    address: str
    area: str
    rooms_count: int
    description: str

class FindShanyrakRequest(AppModel):
    id: Any = Field(alias="_id")



@router.get("/{shanyrak_id: str}", response_model=FindShanyrakResponse)
def create_shanyraks(
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyrak_info = svc.repository.get_shanyrak_by_id(shanyrak_id)

    if shanyrak_info is None:
        return Response(status_code=404)
    return FindShanyrakResponse(**shanyrak_info)
