import abc
from typing import (
    Dict,
    Any, List
)

from pydantic import BaseModel
from sqlalchemy import (
    select,
    insert,
    update,
    delete,
    and_
)

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.infrastructure.repository.postgres_models import AbstractBase
from src.services.interface import AbstractRepository


class SQLAlchemyAdapter(AbstractRepository, abc.ABC):
    pydantic_model: BaseModel
    database_model: AbstractBase

    def __init__(self, async_session: async_sessionmaker):
        self.async_session: AsyncSession = async_session

    async def add(self, data: 'pydantic_model') -> 'pydantic_model':
        async with self.async_session() as session:
            response = await session.execute(
                insert(self.database_model)
                .values(data.model_dump(exclude_none=True))
                .returning(self.database_model)
            )
            res = self.pydantic_model.model_validate(response.scalar_one().__dict__)
            await session.commit()
            return res

    async def remove(self, pk: Dict[str, Any]) -> 'pydantic_model':
        response = await self.async_session.execute(
            delete(self.database_model)
            .where(*pk)
            .returning(self.pydantic_model)
        )
        return self.pydantic_model.model_validate(response.scalar_one())

    async def find_one(self, data: Dict[str, Any]) -> 'pydantic_model':
        params = []
        for name in self.database_model.__table__.c:
            value = data.get(name.key)
            if value is not None:
                params.append(name.__eq__(value))

        response = await self.async_session.execute(
            select(self.database_model)
            .where(and_(*params))
        )
        obj = response.scalar_one()
        return self.pydantic_model.model_validate(obj) if obj else obj

    async def find_all(self) -> List['pydantic_model']:
        async with self.async_session() as session:
            response = await session.execute(
                select(self.database_model)
            )
            return [self.pydantic_model.model_validate(obj.__dict__) for obj in response.scalars()]

    async def update(self, pk: Any, data: 'pydantic_model') -> 'pydantic_model':
        response = await self.async_session.execute(
            update(self.database_model)
            .where(self.database_model.id.__eq__(pk))
            .values(data.model_dump(exclude_none=True))
            .returning(self.database_model)
        )
        return self.pydantic_model.model_validate(response.scalar_one())
