from aiogram.types import Message
from aiogram.filters import Command
from core.config.config import bot, dispatcher
from core.keyboards.inline import inline_start


@dispatcher.message(Command("start"))
async def get_start(message: Message) -> None:
    await message.reply(f'Добро пожаловать в <b>GodBot</b> - бота, собранного из множества других ботов.\n\n'
                        f'Вы можете использовать любого из них по необходимости абсолютно бесплатно. '
                        f'Название ботов и их описание вы можете получить, нажав кнопку ниже.\n\n'
                        f'<i>Если у вас возникли вопросы, или вы нашли ошибку, недоработку в боте, '
                        f'напишите старшему разработчику бота:</i> <a href="tg://user?id=1989630218">Александр</a>',
                        reply_markup=inline_start)

