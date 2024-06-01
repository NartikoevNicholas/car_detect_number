from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class CarNumberEntity(BaseModel):
    id: Optional[int] = None
    number: str
    is_active: bool
    dt_created: Optional[datetime] = None


class CarNumberHistoryEntity(BaseModel):
    id: int
    car_number_id: int
    number: str
    is_active: bool
    dt_created: Optional[datetime] = None
