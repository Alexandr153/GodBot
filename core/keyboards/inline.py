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
