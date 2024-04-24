from core.utils.commands import set_commands
from aiogram import Bot


async def start_bot(bot: Bot):
    await set_commands(bot)
    print("[-] Бот начал работу")


# При завершении работы бота
async def stop_bot(bot: Bot):
    print("[-] Бот закончил работу")