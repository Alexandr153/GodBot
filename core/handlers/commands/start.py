from aiogram.types import Message
from aiogram import dispatcher, Bot
from aiogram.filters import Command
from core.config.config import bot, dispatcher


@dispatcher.message(Command("start"))
async def get_start(message: Message) -> None:
    await message.reply(f'Приветик')

