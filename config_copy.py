# ! Необходимо сделать переименовать в config.py и заполнить все авторизационные данные

BOT_TOKEN = ""

USERS_WHITELIST = []

API_URL = "https://string-art.vercel.app/api"
DOC_URL = "https://string-art.vercel.app/api/doc"
API_TOKEN = ""


def batch_length_generator(step: int, data: list):
    return (data[x : x + step] for x in range(0, len(data), step))


def equal_split(list_to_split, n_parts):
    k, m = divmod(len(list_to_split), n_parts)
    return (
        list_to_split[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)]
        for i in range(n_parts)
    )
