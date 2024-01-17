from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get(codes: list, page: int) -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    last_index = page + 10 if page + 10 < len(codes) else len(codes)
    for index in range(page, last_index):
        code = codes[index]
        builder.row(
            types.InlineKeyboardButton(
                text=f"📰 {code['value']}",
                callback_data=f"get_barcode_info|{code['id']}",
            )
        )
    builder.row(
        types.InlineKeyboardButton(
            text="⬅️ Назад",
            callback_data=f"get_all_barcodes|{page - 10 if page != 0 else 0}",
        ),
        types.InlineKeyboardButton(
            text="Вперед ➡️",
            callback_data=f"get_all_barcodes|{page + 10 if page + 10 < len(codes) else page}",
        ),
    )
    builder.row(
        types.InlineKeyboardButton(text="🔙 В главное меню", callback_data="main_menu")
    )
    return builder.as_markup(resize_keyboard=True)
