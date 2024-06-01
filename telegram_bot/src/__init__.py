from aiogram import Dispatcher

from src.handler import routers
from src.handler.v1.middlewares import DeleteHistoryMiddleware


def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)
    dp.update.outer_middleware(DeleteHistoryMiddleware())
    return dp


__all__ = [
    'get_dispatcher'
]
