from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import start_k, only_to_main_k
from config import BOT_TOKEN, API_URL
import os
import uuid
import aiohttp
from docx import Document
from docx.shared import Pt

# Создаем экземпляр роутера и бота
router = Router()
bot = Bot(token=BOT_TOKEN)


# Определение состояний для finite state machine (FSM)
class Patterns(StatesGroup):
    waiting_to_id = State()


# Функция обработки ошибок
async def sth_error(message: Message, error_text: str) -> None:
    await message.delete()
    markup_inline = only_to_main_k.get()
    await message.answer(
        text=f"⛔️ Что-то пошло не так\n\nТекст ошибки: {error_text}",
        reply_markup=markup_inline,
    )


# Обработчик для основного меню
@router.callback_query(F.data == "main_menu")
async def main_menu(callback: CallbackQuery) -> None:
    try:
        markup_inline = start_k.get()
        await callback.message.delete()
        await callback.message.answer(
            text="🤖 Привет, я бот для получения баркодов в формате docx",
            reply_markup=markup_inline,
        )
    except Exception as exception:
        await sth_error(callback.message, exception)


# Обработчик для запроса генерации кодов
@router.callback_query(F.data == "get_patterns")
async def generate(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        await callback.message.delete()
        message = await callback.message.answer(
            text="📑 Пришлите мне кол-во кодов, которое необходимо сгенерировать"
        )
        await state.set_state(Patterns.waiting_to_id)
        await state.update_data(id_to_delete=message.message_id)
    except Exception as exception:
        await sth_error(callback.message, exception)


# Обработчик ввода количества кодов
@router.message(Patterns.waiting_to_id)
async def waiting_to_message(message: Message, state: FSMContext) -> None:
    try:
        message_text = message.text
        state_data = await state.get_data()
        id_to_delete = state_data["id_to_delete"]
        await bot.delete_message(chat_id=message.chat.id, message_id=id_to_delete)
        await message.delete()

        try:
            int(message_text)
        except Exception:
            markup_inline = only_to_main_k.get()
            await message.answer(
                text="⛔️ Проверьте корректность введенных данных",
                reply_markup=markup_inline,
            )
        else:
            count = int(message_text)
            codes = generate_codes(count)
            await send_codes_to_url(url=API_URL, codes=codes)
            filename = save_codes_to_docx(codes)

            docx_file = FSInputFile(f"{filename}")
            markup_inline = only_to_main_k.get()
            await message.answer_document(
                document=docx_file, reply_markup=markup_inline
            )
            os.remove(f"{filename}")

    except Exception as exception:
        await sth_error(message, exception)


# Функция генерации случайных кодов
def generate_codes(count: int) -> list:
    codes = []
    for _ in range(count):
        code = str(uuid.uuid4().hex)[:8]
        codes.append(code)
    return codes


# Функция сохранения кодов в docx файл
def save_codes_to_docx(codes: list) -> str:
    doc = Document()
    doc.styles["Normal"].font.size = Pt(21)
    doc.styles["Normal"].font.bold = True
    for code in codes:
        doc.add_paragraph(code)
        doc.add_paragraph("------------------------------------------------------")
    filename = f"{str(uuid.uuid4())}.docx"
    doc.save(filename)
    return filename


# Функция отправки кодов по указанному URL
async def send_codes_to_url(codes: list, url: str) -> list:
    async with aiohttp.ClientSession() as session:
        responses = []
        for code in codes:
            body = {"code": code}
            async with session.post(url, json=body) as response:
                responses.append(await response.json())
        return responses
