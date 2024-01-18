from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import os

from keyboards import only_to_main_k, create_barcodes_k
from handlers.main_h import sth_error
from config import BOT_TOKEN
from utils.func_utils import generate_codes, save_codes_to_docx
from utils.api_utils import create_codes


router = Router()
bot = Bot(token=BOT_TOKEN)


class CreateBarcodes(StatesGroup):
    waiting_to_amount = State()
    waiting_to_list = State()


@router.callback_query(F.data == "create_barcodes_menu")
async def generate(callback: CallbackQuery) -> None:
    try:
        markup_inline = create_barcodes_k.get()
        await callback.message.delete()
        await callback.message.answer(
            text=(
                "🔎 Выберите опцию.\n\n"
                + "В случае выбора опции '🎲 Создать случайные коды' - "
                + "вам будет необходимо только задать их кол-во, сами коды "
                + "будут сгенерированы рандомно с помощью алгоритма\n\n"
                + "В случае выбора опции '📝 Создать определенные коды' - вы должны будете "
                + "отправить сообщением все необходимые коды, разделив их запятой.\n\n"
                + "В ответ вы получите сообщение с docx-файлом, содержащим созданные вами коды"
            ),
            reply_markup=markup_inline,
        )
    except Exception as exception:
        await sth_error(callback.message, exception)


@router.callback_query(F.data == "create_random_barcodes")
async def generate(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        await callback.message.delete()
        markup_inline = only_to_main_k.get()
        message = await callback.message.answer(
            text="🛎 Пришлите мне кол-во String Art кодов, которое необходимо сгенерировать",
            reply_markup=markup_inline
        )
        await state.set_state(CreateBarcodes.waiting_to_amount)
        await state.update_data(id_to_delete=message.message_id)
    except Exception as exception:
        await sth_error(callback.message, exception)


@router.message(CreateBarcodes.waiting_to_amount)
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
            await create_codes(codes=codes)
            filename = save_codes_to_docx(codes, message.chat.id)

            docx_file = FSInputFile(f"{filename}")
            markup_inline = only_to_main_k.get()
            await message.answer_document(
                document=docx_file, reply_markup=markup_inline
            )
            os.remove(f"{filename}")

    except Exception as exception:
        await sth_error(message, exception)


@router.callback_query(F.data == "create_barcodes_by_list")
async def generate(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        await callback.message.delete()
        markup_inline = only_to_main_k.get()
        message = await callback.message.answer(
            text="🛎 Пришлите мне String Art коды для создания через запятую",
            reply_markup=markup_inline
        )
        await state.set_state(CreateBarcodes.waiting_to_list)
        await state.update_data(id_to_delete=message.message_id)
    except Exception as exception:
        await sth_error(callback.message, exception)


@router.message(CreateBarcodes.waiting_to_list)
async def waiting_to_message(message: Message, state: FSMContext) -> None:
    try:
        message_text = message.text
        state_data = await state.get_data()
        id_to_delete = state_data["id_to_delete"]
        await bot.delete_message(chat_id=message.chat.id, message_id=id_to_delete)
        await message.delete()

        try:
            message_text = message_text.replace(" ", "")
            codes = message_text.split(",")
            for code in codes:
                if len(code) != 8:
                    raise ValueError
        except Exception:
            markup_inline = only_to_main_k.get()
            await message.answer(
                text="⛔️ Проверьте корректность введенных данных",
                reply_markup=markup_inline,
            )
        else:
            await create_codes(codes=codes)
            filename = save_codes_to_docx(codes, message.chat.id)

            docx_file = FSInputFile(f"{filename}")
            markup_inline = only_to_main_k.get()
            await message.answer_document(
                document=docx_file, reply_markup=markup_inline
            )
            os.remove(f"{filename}")

    except Exception as exception:
        await sth_error(message, exception)
