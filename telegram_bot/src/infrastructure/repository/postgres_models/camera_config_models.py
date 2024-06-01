from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    relationship,
    mapped_column,
)
from sqlalchemy.types import (
    INTEGER,
    String
)


from .abstract_model import AbstractBase


class CameraConfig(AbstractBase):
    __tablename__ = 'camera_config'

    address_id: Mapped[INTEGER] = mapped_column(
        INTEGER,
        ForeignKey('address.id', ondelete='CASCADE')
    )
    host: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    port: Mapped[INTEGER] = mapped_column(
        INTEGER,
        nullable=False,
        default=554
    )

    address_config: Mapped['Address'] = relationship(
        back_populates='camera_config',
        single_parent=True
    )
