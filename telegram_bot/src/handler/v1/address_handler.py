from time import time
from typing import List


from dependency_injector.wiring import Provide, inject
from aiogram import Router
from aiogram.types import (
    Message,

    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from src.core import Container
from src.core.language import Language
from src.core.settings import TelegramCommands
from src.services.use_case import AddressService
from src.services.entities import AddressEntity
from .filters import AddressAppendFilter

router = Router(name='addresses')


@router.callback_query(lambda c: c.data == TelegramCommands.addresses)
@inject
async def command_addresses(callback_query: CallbackQuery,
                            lang: Language = Provide[Container.language],
                            address_service: AddressService = Provide[Container.address_service]) -> List:
    addresses = await address_service.get_all_addresses()
    buttons = []
    for addr in addresses:
        buttons.append(
            [InlineKeyboardButton(
                text=addr.address,
                callback_data=TelegramCommands.address_info + str(addr.id))]
        )

    buttons.append([
        InlineKeyboardButton(text=lang.ADD_ADDRESS, callback_data=TelegramCommands.add_address),
        InlineKeyboardButton(text=lang.BACK, callback_data=TelegramCommands.back)
    ])

    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback_query.bot.answer_callback_query(callback_query.id)
    message = await callback_query.bot.send_message(
        callback_query.from_user.id,
        lang.ADDRESS_MESSAGE,
        reply_markup=inline_keyboard
    )
    return [message.message_id]


@router.callback_query(lambda c: c.data == TelegramCommands.add_address)
@inject
async def command_add_address(callback_query: CallbackQuery,
                              lang: Language = Provide[Container.language]) -> List:
    AddressAppendFilter().append(callback_query.from_user.id)
    message = await callback_query.bot.send_message(
        callback_query.from_user.id,
        lang.INPUT_ADDRESS,
    )
    return [message.message_id]


@router.message(AddressAppendFilter())
@inject
async def command_insert_address(message: Message,
                                 lang: Language = Provide[Container.language],
                                 address_service: AddressService = Provide[Container.address_service]) -> List:
    buttons = [[
        InlineKeyboardButton(text=lang.ADD_ADDRESS, callback_data=TelegramCommands.add_address),
        InlineKeyboardButton(text=lang.BACK, callback_data=TelegramCommands.back)
    ]]

    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    data = AddressEntity(address=message.text, is_active=True)
    address_id = await address_service.add_new_address(data)
    message = await message.answer(
        lang.APPEND_ADDR_SUCCESSFUL if address_id else lang.APPEND_ADDR_SUCCESSFUL,
        reply_markup=inline_keyboard
    )
    return [message.message_id]


@router.callback_query(lambda c: c.data.__contains__(TelegramCommands.address_info))
@inject
async def command_address_info(callback_query: CallbackQuery,
                               lang: Language = Provide[Container.language],
                               address_service: AddressService = Provide[Container.address_service]) -> List:
    address_id = int(callback_query.data.replace(TelegramCommands.address_info, ''))
    address_info = await address_service.get_address_info(address_id)

    address_buttons = [
        [
            InlineKeyboardButton(text=lang.DEL_ADDRESS, callback_data=TelegramCommands.del_address),
            InlineKeyboardButton(text=lang.EDIT_ADDRESS, callback_data=TelegramCommands.del_address),
            InlineKeyboardButton(text=lang.BACK, callback_data=TelegramCommands.back)
        ],
        [InlineKeyboardButton(text=lang.ADDRESS_ADD_CAR_NUMBER, callback_data=TelegramCommands.back)]
    ]

    car_buttons = []
    for car_numbers in address_info.car_numbers:
        car_buttons.append([
            InlineKeyboardButton(
                text=car_numbers.number,
                callback_data=TelegramCommands.address_info + str(car_numbers.id)
            )
        ])

    camera_config_buttons = [
        [
            InlineKeyboardButton(
                text=lang.CAMERA_CONFIG_BUTTON.format(
                    address_info.camera_config.host,
                    address_info.camera_config.port
                ),
                callback_data=TelegramCommands.camera_config_info + str(address_info.camera_config.id)
            )
        ]
    ]

    # messages
    addr_message = await callback_query.bot.send_message(
        callback_query.from_user.id,
        lang.ADDRESS_INFO_MESSAGE.format(address_info.address),
        reply_markup=InlineKeyboardMarkup(inline_keyboard=address_buttons)

    )
    car_message = await callback_query.bot.send_message(
        callback_query.from_user.id,
        lang.ADDRESS_CAR_MESSAGE.format(address_info.address),
        reply_markup=InlineKeyboardMarkup(inline_keyboard=car_buttons)
    )
    camera_config_message = await callback_query.bot.send_message(
        callback_query.from_user.id,
        lang.ADDRESS_CAMERA_CONFIG_MESSAGE,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=camera_config_buttons
        )
    )
    return [addr_message.message_id, car_message.message_id, camera_config_message.message_id]
