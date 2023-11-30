from typing import Any
import aiohttp


async def request_get_json(
    url: str,
    headers={"accept": "application/json"},
):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as resp:
            return await resp.json()


async def request_post_json(url: str, headers: dict, data: Any):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, headers=headers, data=data) as resp:
            return await resp.json()
