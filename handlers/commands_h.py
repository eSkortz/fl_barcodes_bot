from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import start_k
from config import USERS_WHITELIST

router = Router()


@router.message(Command("start"))
async def start_command(message: Message) -> None:
    """функция для отработки команды start

    Args:
        message (Message): сообщение пользователя с командой
    """
    if message.chat.id in USERS_WHITELIST:
        markup_inline = start_k.get()
        await message.answer(
            text=(
                "🤖 Привет, я бот для получения баркодов в формате docx"
            ),
            reply_markup=markup_inline
        )
    else:
        await message.answer('⛔️ Извините, у вас нет доступа')


@router.message(Command("recipient"))
async def recipient_command(message: Message) -> None:
    """функция для получения id пользователя
    для последующего его добавления в whitelist 
    в config

    Args:
        message (Message): сообщение пользователя с командой
    """
    await message.reply(f"{message.chat.id}")