from aiogram import Bot, Dispatcher, F
import asyncio
from core.config.config import API_BOT, DATABASE, DB_USER, DB_PASSWORD, DB_HOST, AdminID
from aiogram.filters import Command, CommandStart
from core.utils.commands import set_commands
from dataclasses import dataclass
from typing import Union, Optional
from core.handlers.basic import get_start
from aiogram.types import Message
import psycopg2


# Конфиг базы данных
@dataclass(frozen=True)
class DataBaseConfig:
    db_host: str        # URL адресс базы данных
    db_user: str        # username пользователя базы данных
    db_password: str    # Праоль к базе данных
    database: str       # Название базы данных


# Общий конфиг
@dataclass(frozen=True)
class TgBot:
    token: str
    adminids: Optional[list[int]]


# Для удобного взаимодействия
@dataclass
class ApplyConfig:
    tg_bot: TgBot
    db: DataBaseConfig


# При старте бота применяем функции
async def start_bot(bot: Bot):
    await set_commands(bot)
    print("[-] Бот начал работу")


# При завершении работы бота
async def stop_bot(bot: Bot):
    print("[-] Бот закончил работу")


async def main():
    config = ApplyConfig(tg_bot=TgBot(token=API_BOT,
                                      adminids=AdminID),
                         db=DataBaseConfig(db_host=DB_HOST,
                                           db_user=DB_USER,
                                           db_password=DB_PASSWORD,
                                           database=DATABASE))

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # При старте бота
    dp.startup.register(start_bot)
    # При остановке бота
    dp.shutdown.register(stop_bot)
    # Команда /start
    dp.message.register(get_start, CommandStart())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())

