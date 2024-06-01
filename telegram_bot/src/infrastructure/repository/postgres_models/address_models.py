from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    relationship,
    mapped_column,
)
from sqlalchemy.types import (
    INTEGER,
    Boolean,
    String
)


from .abstract_model import AbstractBase
from .association_models import address__car_number


class Address(AbstractBase):
    __tablename__ = 'address'

    address: Mapped[String] = mapped_column(
        String,
        unique=True,
        nullable=False
    )
    is_active: Mapped[Boolean] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )

    car_numbers: Mapped[List["CarNumber"]] = relationship(
        secondary=address__car_number,
        back_populates="addresses"
    )

    camera_config: Mapped['CameraConfig'] = relationship(
        back_populates='address_config'
    )


class AddressHistory(AbstractBase):
    __tablename__ = 'address_history'

    address_id: Mapped[INTEGER] = mapped_column(
        INTEGER,
        ForeignKey('address.id'),
        nullable=False
    )
    address: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    is_active: Mapped[Boolean] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )
