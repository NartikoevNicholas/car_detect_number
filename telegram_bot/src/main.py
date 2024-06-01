import asyncio

from aiogram import(
    Bot,
    Dispatcher
)

from src import get_dispatcher
from src.core import (
    Container,
    get_default_settings
)
from src.core.settings import DefaultSettings


async def main() -> None:
    # get config application
    config: DefaultSettings = get_default_settings()

    # dependencies injection
    container: Container = Container()
    container.config.from_dict(config.model_dump())

    # telegram bot up
    bot: Bot = Bot(token=config.TELEGRAM_TOKEN)
    dispatcher: Dispatcher = get_dispatcher()
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
