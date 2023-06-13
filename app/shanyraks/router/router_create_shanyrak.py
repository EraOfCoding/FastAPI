from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class CreateShanyrakResponse(AppModel):
    id: Any = Field(alias="_id")

class CreateShanyrakRequest(AppModel):
    type: str
    price: float
    address: str
    area: str
    rooms_count: int
    description: str


@router.post("/", response_model=CreateShanyrakResponse)
def create_shanyraks(
    input: CreateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    id = svc.repository.create_shanyrak(jwt_data.user_id, input.dict())
    return CreateShanyrakResponse(id=id)
