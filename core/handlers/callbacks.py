from aiogram.types import CallbackQuery
from core.config.config import dispatcher, bot
from aiogram import F
from core.keyboards.inline import list_of_bots
from aiogram.filters import Command


# Меню со всеми ботами
@dispatcher.callback_query(F.data.startswith('all_bots'))
async def all_bots(call: CallbackQuery):
    answer = ('Ниже представлено краткое описание каждого из доступных ботов: \n\n'
              '<b>TranslatePictureBot</b> - <i>бот, способный распознавать текст с картинки на разных языках,'
              'а так же переводящий его на другие доступеые языки</i>\n\n'
              '<b>AntiCensorshipBot</b> - <i>предназначен по большей части для развлечения, рейдов чатов,'
              'которые блокируют определенные слова, предложения. Вы сможете изменить текст, либо предложение'
              'на набор символов, читаемый человеческим глазом в соответствии с алфавитом языка.</i>\n\n')

    await call.message.reply(answer, reply_markup=list_of_bots)


# Реферальная системв
@dispatcher.callback_query(F.data.startswith('ref_system'))
async def ref_system(call: CallbackQuery):
    answer = 'Реферальная система'

    await call.message.reply(answer)
