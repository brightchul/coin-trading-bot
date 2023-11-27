from config import config
from apis.public.api import 최근_체결_내역, 현재가_정보_조회, 호가_정보_조회

import asyncio


async def main():
    result = await 현재가_정보_조회("HIFI", "KRW")
    print(result, "========")
    print(await 호가_정보_조회("BTC", "KRW"))
    print(await 최근_체결_내역("BTC", "KRW"))


if __name__ == "__main__":
    print(config)
    # asyncio.run(현재가_정보_조회_전체())
    # asyncio.get_event_loop().run_until_complete(현재가_정보_조회_전체())

    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().close()
