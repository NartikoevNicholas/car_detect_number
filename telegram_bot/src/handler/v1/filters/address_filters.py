from time import time

from aiogram.types import Message
from aiogram.filters import BaseFilter

from src.core.settings import TelegramCommands
from src.services.helpers import Singleton


class AddressAppendFilter(BaseFilter, Singleton):
    filter_key = TelegramCommands.add_address
    address_append = {}

    async def __call__(self, message: Message):
        key = f'{message.from_user.id}{self.filter_key}'
        old_timestamp = self.address_append.get(key)
        if old_timestamp is None: return False
        del self.address_append[key]
        return time() - old_timestamp < 300

    def append(self, user_id):
        self.address_append[f'{user_id}{self.filter_key}'] = time()
