from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="🎲 Создать случайные баркоды", callback_data=f"create_random_barcodes"
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text="📝 Создать определенные баркоды",
            callback_data=f"create_barcodes_by_list",
        )
    )
    builder.row(
        types.InlineKeyboardButton(text="🔙 В главное меню", callback_data="main_menu")
    )
    return builder.as_markup(resize_keyboard=True)
