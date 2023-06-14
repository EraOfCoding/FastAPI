from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data

class UpdateShanyrakRequest(AppModel):
    shanyrak_id: str


@router.delete("/{shanyrak_id:str}")
def create_shanyraks(
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    
    svc.repository.delete_shanyrak(shanyrak_id, jwt_data.user_id)

    return Response(status_code=200)
