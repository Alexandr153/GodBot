from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_start = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Список ботов",
            callback_data="all_bots"
        )
    ],
    [
        InlineKeyboardButton(
            text="Реферальная программа",
            callback_data="ref_system"
        )
    ]
])

list_of_bots = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="TranslatePictureBot",
            callback_data="Translate_Picture_Bot"
        )
    ],
    [
        InlineKeyboardButton(
            text="AntiCensorshipBot",
            callback_data="Anti_Censorship_Bot"
        )
    ]
])
