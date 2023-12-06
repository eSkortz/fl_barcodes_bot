from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def get() -> ReplyKeyboardMarkup:
    """функция для создания клавиатуры под стартовое меню

    Returns:
        ReplyKeyboardMarkup: сама клавиатура
    """
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='📑 Cформировать коды', callback_data=f"get_patterns"
    ))
    return builder.as_markup(resize_keyboard=True)