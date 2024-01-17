from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from keyboards import start_k, only_to_main_k
from config import BOT_TOKEN

router = Router()
bot = Bot(token=BOT_TOKEN)


class Patterns(StatesGroup):
    waiting_to_id = State()


async def sth_error(message: Message, error_text: str) -> None:
    markup_inline = only_to_main_k.get()
    await message.answer(
        text=f"⛔️ Что-то пошло не так\n\nТекст ошибки: {error_text}",
        reply_markup=markup_inline,
    )


@router.callback_query(F.data == "main_menu")
async def main_menu(callback: CallbackQuery) -> None:
    try:
        markup_inline = start_k.get()
        await callback.message.delete()
        await callback.message.answer(
            text=(
                "🤖 Привет, я бот созданный для помощи при работе с баркодами. "
                + "Я могу помочь вам создать баркоды, удалить их или просмотреть "
                + "статистику по имеющимся баркодам"
            ),
            reply_markup=markup_inline,
        )
    except Exception as exception:
        await sth_error(callback.message, exception)
