from aiogram.types import CallbackQuery
from core.config.config import dispatcher, bot
from aiogram import F


@dispatcher.callback_query(F.data.startswith('all_bots'))
async def all_bots(call: CallbackQuery):
    answer = 'Ответ на сообщение'

    await call.message.reply(answer)


@dispatcher.callback_query(F.data.startswith('ref_system'))
async def ref_system(call: CallbackQuery):
    answer = 'Реферальная система'

    await call.message.reply(answer)
