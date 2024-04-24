import asyncio
from aiogram.filters import Command, CommandStart
from core.utils.commands import set_commands
from dataclasses import dataclass
from typing import Union, Optional
import psycopg2
from core.config.config import bot, dispatcher as dp
from core.state.states import stop_bot, start_bot


import core.handlers.commands.start


async def main() -> None:

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

