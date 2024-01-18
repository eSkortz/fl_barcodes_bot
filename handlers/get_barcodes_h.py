from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import only_to_main_k, get_barcodes_k, only_to_list_k, barcodes_list_k
from handlers.main_h import sth_error
from config import BOT_TOKEN
from utils.api_utils import get_codes


router = Router()
bot = Bot(token=BOT_TOKEN)


class GetBarcodes(StatesGroup):
    waiting_to_code = State()


@router.callback_query(F.data == "get_barcodes_menu")
async def get_barcodes_menu(callback: CallbackQuery) -> None:
    try:
        markup_inline = get_barcodes_k.get()
        await callback.message.delete()
        await callback.message.answer(
            text=(
                "🔎 Выберите опцию.\n\n"
                + "При выборе опции '🗂 Посмотреть все коды' - "
                + "вы получите динамический список всех кодов, "
                + "зарегестрированных в системе.\n\nПри выборе опции "
                + "'📰 Информация об определенном коде' - вам нужно будет "
                + "ввести его значение в сообщении и в случае, если такой "
                + "код зарегестрирован в системе, - вам будет "
                + "выведена информация по нему"
            ),
            reply_markup=markup_inline,
        )
    except Exception as exception:
        await sth_error(callback.message, exception)


@router.callback_query(F.data == "get_info_by_barcode")
async def get_code_from_message(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        await callback.message.delete()
        message = await callback.message.answer(
            text="🛎 Пришлите String Art код, по которому хотите получить информацию"
        )
        await state.set_state(GetBarcodes.waiting_to_code)
        await state.update_data(id_to_delete=message.message_id)
    except Exception as exception:
        await sth_error(callback.message, exception)


@router.message(GetBarcodes.waiting_to_code)
async def processing_message_code(message: Message, state: FSMContext) -> None:
    try:
        message_text = message.text
        state_data = await state.get_data()
        id_to_delete = state_data["id_to_delete"]
        await bot.delete_message(chat_id=message.chat.id, message_id=id_to_delete)
        await message.delete()

        finded_code = None
        codes = await get_codes()
        for code in codes:
            if code["value"] == message_text:
                finded_code = code

        if finded_code is not None:
            markup_inline = only_to_list_k.get(value=finded_code["value"])
            text = (
                "📰 Информация по String Art коду:\n\n"
                + f"id: {finded_code['id']}\n"
                + f"Кол-во использований: {finded_code['timesUsed']}\n"
                + f"Значение: {finded_code['value']}"
            )
            await message.answer(text=text, reply_markup=markup_inline)
        else:
            raise ValueError

    except Exception as exception:
        await sth_error(message, exception)


@router.callback_query(F.data.startswith("get_all_barcodes"))
async def get_codes_list(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        page = int(callback.data.split("|")[1])
        await callback.message.delete()

        codes = await get_codes()
        markup_inline = barcodes_list_k.get(codes=codes, page=page)

        await callback.message.answer(
            text=(
                f"🗂 Список зарегистрированных String Art кодов (стр. "
                + f"{page//10+1}/{len(codes)//10+1 if len(codes)%10!=0 else len(codes)//10})"
            ),
            reply_markup=markup_inline,
        )
    except Exception as exception:
        await sth_error(callback.message, exception)


@router.callback_query(F.data.startswith("get_barcode_info"))
async def get_codes_list(callback: CallbackQuery) -> None:
    try:
        barcode_id = int(callback.data.split("|")[1])
        await callback.message.delete()

        codes = await get_codes()
        finded_code = None
        for code in codes:
            if code["id"] == barcode_id:
                finded_code = code

        if finded_code is not None:
            markup_inline = only_to_list_k.get(value=finded_code["value"])
            text = (
                "📰 Информация по String Art коду:\n\n"
                + f"id: {finded_code['id']}\n"
                + f"Кол-во использований: {finded_code['timesUsed']}\n"
                + f"Значение: {finded_code['value']}"
            )
            await callback.message.answer(text=text, reply_markup=markup_inline)
        else:
            raise ValueError

    except Exception as exception:
        await sth_error(callback.message, exception)
