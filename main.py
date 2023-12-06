import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import commands_h, main_h

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляра бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Асинхронная функция, запускающая бота
async def main() -> None:
    # Включение роутеров (обработчиков) команд и основного функционала
    dp.include_routers(commands_h.router, main_h.router)

    # Удаление вебхука (если он установлен) и удаление ожидающих обновлений
    await bot.delete_webhook(drop_pending_updates=True)

    # Запуск бота с использованием polling (получение обновлений через long polling)
    await asyncio.create_task(dp.start_polling(bot))

# Запуск асинхронной функции main, если файл запускается напрямую, а не импортируется
if __name__ == '__main__':
    asyncio.run(main())
