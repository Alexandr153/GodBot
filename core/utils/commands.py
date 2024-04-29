from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


# Инлайн команды
async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Аннотация бота'
        ),
        BotCommand(
            command='menu',
            description='Все доступные боты'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())