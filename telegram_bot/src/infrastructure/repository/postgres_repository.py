from sqlalchemy import (
    select,
)
from sqlalchemy.orm import (
    aliased,
    joinedload,
    selectinload
)

from src.services.interface import (
    AbstractAddressRepository,
    AbstractAddressHistoryRepository,
    AbstractRepositoryCarNumber,
    AbstractRepositoryCarNumberHistory,
    AbstractCameraConfigRepository
)

from src.services.entities import (
    CarNumberEntity,
    AddressInfoEntity,
    CameraConfigEntity
)

from .adapter import SQLAlchemyAdapter
from .postgres_models import (
    Address,
    AddressHistory,
    CarNumber,
    address__car_number,
    CarNumberHistory,
    CameraConfig,
)


class AddressRepository(AbstractAddressRepository, SQLAlchemyAdapter):
    database_model = Address

    async def get_address_detail(self, pk: int) -> AddressInfoEntity:
        pass
        async with self.async_session() as session:
            response = await session.execute(
                select(self.database_model)
                .options(selectinload(self.database_model.car_numbers))
                .options(joinedload(self.database_model.camera_config))
                .where(self.database_model.id == pk)
            )

            obj = response.scalar_one().__dict__
            car_numbers = []
            for car_number in obj['car_numbers']:
                car_numbers.append(CarNumberEntity.model_validate(car_number.__dict__))
            obj['car_numbers'] = car_numbers
            obj['camera_config'] = CameraConfigEntity.model_validate(obj['camera_config'].__dict__)
            return AddressInfoEntity.model_validate(obj)


class AddressHistoryRepository(AbstractAddressHistoryRepository, SQLAlchemyAdapter):
    database_model = AddressHistory


class CarNumberRepository(AbstractRepositoryCarNumber, SQLAlchemyAdapter):
    database_model = CarNumber


class CarNumberHistoryRepository(AbstractRepositoryCarNumberHistory, SQLAlchemyAdapter):
    database_model = CarNumberHistory


class CameraConfigRepository(AbstractCameraConfigRepository, SQLAlchemyAdapter):
    database_model = CameraConfig


# SELECT
#   address_1.id AS address_1_id,
#   car_number.number AS car_number_number,
#   car_number.is_active AS car_number_is_active,
#   car_number.id AS car_number_id,
#   car_number.dt_created AS car_number_dt_created
# FROM address AS address_1
# JOIN address__car_number AS address__car_number_1 ON address_1.id = address__car_number_1.address_id
# JOIN car_number ON car_number.id = address__car_number_1.car_number_id
# WHERE address_1.id IN ($1::INTEGER)
