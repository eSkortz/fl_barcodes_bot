from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def get() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='📖 Список баркодов', callback_data=f"get_barcodes_menu"
    ))
    builder.row(types.InlineKeyboardButton(
        text='✏️ Создать баркоды', callback_data=f"create_barcodes_menu"
    ))
    builder.row(types.InlineKeyboardButton(
        text='🗑 Удалить баркоды', callback_data=f"delete_barcodes_menu"
    ))
    return builder.as_markup(resize_keyboard=True)