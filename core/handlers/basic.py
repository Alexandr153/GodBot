from aiogram import Bot
from aiogram.types import Message


# Команда /start
async def get_start(message: Message):
    await message.reply(f'Приветик')

