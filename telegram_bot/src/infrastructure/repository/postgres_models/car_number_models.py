from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    relationship,
    mapped_column
)
from sqlalchemy.types import (
    String,
    INTEGER,
    Boolean
)


from .abstract_model import AbstractBase
from .association_models import address__car_number


class CarNumber(AbstractBase):
    __tablename__ = 'car_number'

    number: Mapped[String] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )
    is_active: Mapped[Boolean] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )

    addresses: Mapped[List["Address"]] = relationship(
        secondary=address__car_number,
        back_populates="car_numbers"
    )




class CarNumberHistory(AbstractBase):
    __tablename__ = 'car_number_history'

    car_number_id: Mapped[INTEGER] = mapped_column(
        INTEGER,
        ForeignKey('car_number.id'),
    )
    number: Mapped[String] = mapped_column(
        String,
        unique=False,
        nullable=False,
    )
    is_active: Mapped[Boolean] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )
