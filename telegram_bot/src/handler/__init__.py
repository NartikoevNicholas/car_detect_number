from src.handler.v1 import (
    start_handler,
    address_handler
)


routers = [
    start_handler.router,
    address_handler.router
]


__all__ = [
    'routers'
]
