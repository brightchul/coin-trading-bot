import asyncio
from apis.private.info import (
    거래_주문내역_상세_조회,
    거래_주문내역_상세_조회_params,
    거래_주문내역_조회,
    거래_주문내역_조회_params,
    거래_체결내역_조회,
    거래_체결내역_조회_params,
    보유자산_조회,
    보유자산_조회_params,
    입금지갑_주소_조회,
    입금지갑_주소_조회_params,
    최근_거래정보_조회,
    최근_거래정보_조회_params,
    회원_정보_조회,
    회원_정보_조회_params,
)
from apis.public.api import show_json


async def main():
    payload1: 회원_정보_조회_params = {
        "order_currency": "BTC",
        "payment_currency": "KRW",
    }
    print(f"회원_정보_조회 : { await 회원_정보_조회(payload1)}\n")

    payload2: 보유자산_조회_params = {
        "currency": "BTC",
    }
    print(f"보유자산_조회 : { await 보유자산_조회(payload2)}\n")

    payload3: 입금지갑_주소_조회_params = {
        "currency": "BTC",
    }
    print(f"보유자산_조회 : { await 입금지갑_주소_조회(payload3)}\n")

    payload4: 최근_거래정보_조회_params = {
        "order_currency": "ROA",
        "payment_currency": "KRW",
    }
    result4 = await 최근_거래정보_조회(payload4)
    print(f"최근_거래정보_조회 : {result4}\n")
    show_json(result4)

    payload5: 거래_주문내역_조회_params = {
        "count": 100,
        "order_currency": "ROA",
        "payment_currency": "KRW",
    }
    print(f"거래_주문내역_조회 : { await 거래_주문내역_조회(payload5)}\n")

    # payload6: 거래_주문내역_상세_조회_params = {
    #     "order_id": "100",
    #     "order_currency": "ROA",
    #     "payment_currency": "KRW",
    # }
    # print(f"거래_주문내역_상세_조회 : { await 거래_주문내역_상세_조회(payload6)}\n")

    payload7: 거래_체결내역_조회_params = {
        "order_currency": "ROA",
        "payment_currency": "KRW",
    }
    result7 = await 거래_체결내역_조회(payload7)
    print(f"거래_체결내역_조회 : {result7}\n")
    show_json(result7)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
