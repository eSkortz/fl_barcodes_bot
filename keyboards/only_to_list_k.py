from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get(value: str) -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="🗑 Удалить код", callback_data=f"delete_barcode_by_value|{value}"
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text="🔙 К списку кодов", callback_data="get_all_barcodes|0"
        )
    )
    return builder.as_markup(resize_keyboard=True)
