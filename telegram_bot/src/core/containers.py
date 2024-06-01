from dependency_injector import containers, providers

from src.services.use_case import AddressService
from src.infrastructure.repository import postgres_repository as pr

from .sqlalchemy_core import (
    get_engine,
    get_async_session
)
from .language import (
    get_locale,
    Language
)


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        packages=['src.handler']
    )

    language: Language = providers.Singleton(
        get_locale,
        locale=config.LOCALE
    )
    engine = providers.Singleton(
        get_engine,
        postgres_settings=config.POSTGRES
    )
    async_session = providers.Factory(
        get_async_session,
        engine
    )

    # repository
    address_repository = providers.Factory(
        pr.AddressRepository,
        async_session=async_session
    )
    address_history_repository = providers.Factory(
        pr.AddressHistoryRepository,
        async_session=async_session
    )
    car_number_repository = providers.Factory(
        pr.CarNumberRepository,
        async_session=async_session
    )
    car_number_history_repository = providers.Factory(
        pr.CarNumberHistoryRepository,
        async_session=async_session
    )
    camera_config_repository = providers.Factory(
        pr.CameraConfigRepository,
        async_session=async_session
    )

    # use_case
    address_service = providers.Factory(
        AddressService,
        config=config,
        address_repo=address_repository
    )
