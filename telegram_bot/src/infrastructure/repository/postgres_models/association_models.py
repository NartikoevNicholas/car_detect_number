from sqlalchemy import (
    Table,
    Column,
    ForeignKey
)

from .abstract_model import Base


address__car_number = Table(
    'address__car_number',
    Base.metadata,
    Column('address_id', ForeignKey('address.id'), primary_key=True),
    Column('car_number_id', ForeignKey('car_number.id'), primary_key=True),
)
