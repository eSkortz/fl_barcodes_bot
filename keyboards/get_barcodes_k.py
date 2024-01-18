from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="🗂 Посмотреть все коды", 
            callback_data=f"get_all_barcodes|0"
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text="📰 Информация об определенном коде",
            callback_data=f"get_info_by_barcode",
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text="🔙 В главное меню", 
            callback_data="main_menu"
        )
    )
    return builder.as_markup(resize_keyboard=True)