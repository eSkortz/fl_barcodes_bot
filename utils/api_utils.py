import aiohttp
from config import API_TOKEN, API_URL


headers = {"Authorization": API_TOKEN}


async def create_codes(codes: list) -> dict:
    async with aiohttp.ClientSession() as session:
        body = {"codes": codes}
        async with session.put(
            url=f"{API_URL}/codes", headers=headers, json=body
        ) as response:
            response = await response.json()
        return response


async def get_codes() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{API_URL}/codes", headers=headers) as response:
            response = await response.json()
        return response


async def delete_codes(codes: list) -> list:
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
