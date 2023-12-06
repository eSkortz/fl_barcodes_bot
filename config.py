from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
import time
import asyncio
import functools


# Токен вашего бота (пустой в примере, замените на реальный токен)
BOT_TOKEN = ''

# Список пользователей, имеющих доступ к вашему боту
USERS_WHITELIST = [5408815987]

# URL для взаимодействия с API
API_URL = 'http://localhost:3000/api/codes'

# Функция для генерации батчей данных с фиксированным размером
def batch_length_generator(step: int, data: list):
    return (data[x : x + step] for x in range(0, len(data), step))

# Функция для разделения списка на равные части
def equal_split(list_to_split, n_parts):
    k, m = divmod(len(list_to_split), n_parts)
    return (
        list_to_split[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)]
        for i in range(n_parts)
    )

# Декоратор для повторного выполнения асинхронной функции в случае ошибки
def retry_async(num_attempts):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for try_index in range(num_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    print(
                        f"Exception occurred: {e}. Retrying... ({try_index}/{num_attempts})"
                    )
                    await asyncio.sleep(1)
            else:
                print(f"Failed after {num_attempts} attempts.")

        return wrapper

    return decorator

# Декоратор для повторного выполнения асинхронной функции в случае ошибки с ограниченным количеством попыток
def do_retry_on_fail_async(func):
    async def wrapper(*args, **kwargs):
        reconnct_tries = 5
        for try_index in range(reconnct_tries):
            try:
                print(try_index, reconnct_tries)
                return await func(*args, **kwargs)
            except:
                print(f"Unable to execute: {func.__name__}")
                await asyncio.sleep(1)

    return wrapper

# Декоратор для повторного выполнения функции в случае ошибки с ограниченным количеством попыток
def do_retry_on_fail(func):
    def wrapper(*args, **kwargs):
        reconnct_tries = 5
        for try_index in range(reconnct_tries):
            try:
                print(try_index, reconnct_tries)
                return func(*args, **kwargs)
            except:
                print(f"Unable to execute: {func.__name__}")
                time.sleep(1)

    return wrapper

# Пример создания подключения к базе данных (закомментировано)
# engine = create_engine(
#     f"postgresql+psycopg2://{DB_LOGIN}:{DB_PASSWORD}@{DB_IP}/{DB_NAME}",
# )

# Пример создания асинхронного подключения к базе данных (закомментировано)
# engine_async = create_async_engine(
#     f"postgresql+asyncpg://{DB_LOGIN}:{DB_PASSWORD}@{DB_IP}/{DB_NAME}",
# )
