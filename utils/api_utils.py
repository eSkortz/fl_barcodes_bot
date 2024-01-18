import aiohttp
from config import API_URL, LOGIN_CODE


async def get_token() -> dict:
    async with aiohttp.ClientSession() as session:
        body = {"code": f"{LOGIN_CODE}"}
        async with session.post(
            url=f"{API_URL}/auth/login", json=body
        ) as response:
            response = await response.json()
            headers = {"Authorization": response["token"]}
            return headers


async def create_codes(codes: list) -> dict:
    headers = await get_token()
    async with aiohttp.ClientSession() as session:
        body = {"codes": codes}
        async with session.put(
            url=f"{API_URL}/codes", headers=headers, json=body
        ) as response:
            response = await response.json()
        return response


async def get_codes() -> dict:
    headers = await get_token()
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API_URL}/codes", headers=headers) as response:
            response = await response.json()
        return response


async def delete_codes(codes: list) -> list:
    headers = await get_token()
    async with aiohttp.ClientSession() as session:
        responses = []
        for code in codes:
            body = {"code": code}
            async with session.delete(
                url=f"{API_URL}/codes", headers=headers, json=body
            ) as response:
                response = await response.json()
                responses.append(response)
        return response
