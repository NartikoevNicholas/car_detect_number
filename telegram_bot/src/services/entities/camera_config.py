from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class CameraConfigEntity(BaseModel):
    id: Optional[int] = None
    address_id: Optional[int] = None
    host: str
    port: int
    dt_created: Optional[datetime] = None
