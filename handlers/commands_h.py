from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import start_k
from config import USERS_WHITELIST

router = Router()


@router.message(Command("start"))
async def start_command(message: Message) -> None:
    if message.chat.id in USERS_WHITELIST:
        markup_inline = start_k.get()
        await message.answer(
            text=(
                "🤖 Привет, я бот String Art созданный для помощи при работе с кодами. "
                + "Я могу помочь вам создать коды, удалить их или просмотреть "
                + "статистику по имеющимся кодам"
            ),
            reply_markup=markup_inline,
        )
    else:
        await message.answer("⛔️ Извините, у вас нет доступа")


@router.message(Command("recipient"))
async def recipient_command(message: Message) -> None:
    await message.reply(f"{message.chat.id}")
