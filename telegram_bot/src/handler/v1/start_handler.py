from typing import List

from dependency_injector.wiring import Provide, inject
from aiogram import (
    Router,
    types as tp
)
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from src.core import Container
from src.core.language import Language
from src.core.settings import TelegramCommands

router = Router(name='start')


@router.message(CommandStart())
@inject
async def command_start_handler(message: tp.Message,
                                lang: Language = Provide[Container.language]) -> List:
    buttons = [
        [InlineKeyboardButton(text=lang.ADDRESSES, callback_data=TelegramCommands.addresses)],
        [InlineKeyboardButton(text=lang.CAR_NUMBERS, callback_data='button1')],
        [InlineKeyboardButton(text=lang.CAMERAS_CONFIG, callback_data='button1')],
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    text = lang.START_MESSAGE.format(message.from_user.first_name)
    start_message = await message.answer(text, reply_markup=inline_keyboard)
    return [start_message.message_id]


# @router.message()
# async def command_start_handler(message: tp.Message) -> None:
#     return None
#
