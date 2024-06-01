from abc import(
    ABC,
    abstractmethod,
)
from typing import (
    Dict,
    List,
    Any
)

from pydantic import BaseModel

from src.services.entities import (
    AddressEntity,
    AddressInfoEntity,
    AddressHistoryEntity,
    CarNumberEntity,
    CarNumberHistoryEntity,
    CameraConfigEntity
)


class AbstractRepository(ABC):
    pydantic_model: BaseModel

    @abstractmethod
    async def add(self, data: 'pydantic_model') -> 'pydantic_model':
        raise NotImplementedError

    @abstractmethod
    async def remove(self, pk: Dict[str, Any]) -> 'pydantic_model':
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, data: Dict[str, Any]) -> 'pydantic_model':
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> List['pydantic_model']:
        raise NotImplementedError

    @abstractmethod
    async def update(self, pk: Any, data: 'pydantic_model') -> 'pydantic_model':
        raise NotImplementedError


class AbstractRepositoryCarNumber(AbstractRepository, ABC):
    pydantic_model = CarNumberEntity


class AbstractRepositoryCarNumberHistory(AbstractRepository, ABC):
    pydantic_model = CarNumberHistoryEntity


class AbstractAddressRepository(AbstractRepository, ABC):
    pydantic_model = AddressEntity

    @abstractmethod
    async def get_address_detail(self, pk: int) -> AddressInfoEntity:
        raise NotImplementedError


class AbstractAddressHistoryRepository(AbstractRepository, ABC):
    pydantic_model = AddressHistoryEntity


class AbstractCameraConfigRepository(AbstractRepository, ABC):
    pydantic_model = CameraConfigEntity
