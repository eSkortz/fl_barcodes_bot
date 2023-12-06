from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def get() -> ReplyKeyboardMarkup:
    """функция для создания клавиатуры с одной кнопкой
    для перехода в главное меню

    Returns:
        ReplyKeyboardMarkup: сама клавиатура
    """
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='🔙 В главное меню', callback_data="main_menu"
    ))
    return builder.as_markup(resize_keyboard=True)
