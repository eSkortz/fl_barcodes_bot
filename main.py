import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import (
    commands_h,
    main_h,
    create_barcodes_h,
    get_barcodes_h,
    delete_barcodes_h,
)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main() -> None:
    dp.include_routers(
        commands_h.router,
        main_h.router,
        create_barcodes_h.router,
        get_barcodes_h.router,
        delete_barcodes_h.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.create_task(dp.start_polling(bot))


if __name__ == "__main__":
    asyncio.run(main())
