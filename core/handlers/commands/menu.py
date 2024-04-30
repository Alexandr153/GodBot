from aiogram.filters import Command
from core.config.config import dispatcher, bot
from aiogram.types import Message
from core.keyboards.inline import list_of_bots


@dispatcher.message(Command("menu"))
async def all_bots(message: Message):
    answer = ('Ниже представлено краткое описание каждого из доступных ботов: \n\n'
              '<b>TranslatePictureBot</b> - <i>бот, способный распознавать текст с картинки на разных языках,'
              'а так же переводящий его на другие доступеые языки</i>\n\n'
              '<b>AntiCensorshipBot</b> - <i>предназначен по большей части для развлечения, рейдов чатов,'
              'которые блокируют определенные слова, предложения. Вы сможете изменить текст, либо предложение'
              'на набор символов, читаемый человеческим глазом в соответствии с алфавитом языка.</i>\n\n')

    await message.reply(answer, reply_markup=list_of_bots)