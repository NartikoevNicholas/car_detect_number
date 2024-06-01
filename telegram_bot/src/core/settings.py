import os

from pathlib import Path
from functools import lru_cache

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):
    ROOT_DIR: str = str(Path(__file__).resolve().parent.parent.parent)
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file=os.path.join(ROOT_DIR, '.env'),
        env_file_encoding='utf-8'
    )


class PostgresSettings(Settings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str


class DefaultSettings(Settings):
    DEBUG: bool
    TELEGRAM_TOKEN: str
    LOCALE: str
    POSTGRES: PostgresSettings = PostgresSettings()


class TelegramCommands:
    addresses: str = 'addresses'
    add_address: str = 'add_address'
    del_address: str = 'del_address'
    edit_address: str = 'edit_address'
    address_info: str = 'address_info'
    camera_config_info: str = 'camera_config_info'
    back: str = 'back'


@lru_cache()
def get_default_settings() -> DefaultSettings:
    return DefaultSettings()
