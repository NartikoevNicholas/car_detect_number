from sqlalchemy import func
from sqlalchemy.orm import (
    mapped_column,
    DeclarativeBase
)
from sqlalchemy.types import (
    INTEGER,
    TIMESTAMP
)


class Base(DeclarativeBase):
    pass


class AbstractBase(Base):
    __abstract__ = True

    id = mapped_column(
        INTEGER,
        primary_key=True,
        unique=True,
        nullable=False,
    )

    dt_created = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    def __repr__(self):
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f'{col}: {getattr(self, col)}')

        return f'Model - {self.__class__.__name__}. Columns - {", ".join(cols)}'
