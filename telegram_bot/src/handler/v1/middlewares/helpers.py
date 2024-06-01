from typing import (
    Callable,
    Dict,
    Any,
    List,
    Union,
    Awaitable,
    Optional
)

from aiogram import BaseMiddleware
from aiogram.types import (
    Message,
    User,
)
from aiogram.methods import SendMessage
from aiogram.client.bot import Bot
from aiogram.types.update import Update
from aiogram.dispatcher.middlewares.user_context import EventContext


class DeleteHistoryMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.messages: dict = {}

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        bot: Bot = data['bot']
        user: User = data['event_from_user']
        event_content: EventContext = data['event_context']
        message: Message = event.event if isinstance(event.event, Message) else event.event.message

        messages: Optionl[List[int]] = await handler(event, data)
        await bot.delete_message(event_content.chat_id, message.message_id)
        if isinstance(messages, list) and self.messages.get(user.id) is not None:
            await bot.delete_messages(event_content.chat_id, self.messages.get(user.id))
            self.messages[user.id] = messages
