from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import only_to_main_k
from handlers.main_h import sth_error
from config import BOT_TOKEN
from utils.api_utils import delete_codes


router = Router()
bot = Bot(token=BOT_TOKEN)


class DeleteBarcodes(StatesGroup):
    waiting_to_amount = State()
    waiting_to_list = State()


@router.callback_query(F.data == "delete_barcodes_menu")
async def generate(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        await callback.message.delete()
        message = await callback.message.answer(
            text="🗑 Пришлите мне коды для удаления через запятую"
        )
        await state.set_state(DeleteBarcodes.waiting_to_list)
        await state.update_data(id_to_delete=message.message_id)
    except Exception as exception:
        await sth_error(callback.message, exception)


@router.message(DeleteBarcodes.waiting_to_list)
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
            await delete_codes(codes=codes)
            markup_inline = only_to_main_k.get()
            await message.answer(
                text="✅ Коды успешно удалены", reply_markup=markup_inline
            )

    except Exception as exception:
        await sth_error(message, exception)

    
@router.callback_query(F.data.startswith("delete_barcode_by_value"))
async def generate(callback: CallbackQuery) -> None:
    try:
        value = callback.data.split('|')[1]
        await delete_codes(codes=[value])

        markup_inline = only_to_main_k.get()
        await callback.message.delete()
        await callback.message.answer(
            text="✅ Код успешно удален из базы данных",
            reply_markup=markup_inline
        )
    except Exception as exception:
        await sth_error(callback.message, exception)
