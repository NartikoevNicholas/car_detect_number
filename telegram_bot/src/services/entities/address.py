from typing import (
    List,
    Optional
)
from datetime import datetime

from pydantic import BaseModel

from .car_number import CarNumberEntity
from .camera_config import CameraConfigEntity


class AddressEntity(BaseModel):
    id: Optional[int] = None
    address: str
    is_active: bool
    dt_created: Optional[datetime] = None


class AddressHistoryEntity(BaseModel):
    id: int
    address_id: int
    address: str
    is_active: bool
    dt_created: Optional[datetime] = None


class AddressInfoEntity(AddressEntity):
    car_numbers: List[CarNumberEntity] = []
    camera_config: Optional[CameraConfigEntity] = None
