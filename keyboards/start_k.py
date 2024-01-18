from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def get() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='📖 Статистика по кодам', callback_data=f"get_barcodes_menu"
    ))
    builder.row(types.InlineKeyboardButton(
        text='✏️ Создать коды', callback_data=f"create_barcodes_menu"
    ))
    builder.row(types.InlineKeyboardButton(
        text='🗑 Удалить коды', callback_data=f"delete_barcodes_menu"
    ))
    return builder.as_markup(resize_keyboard=True)