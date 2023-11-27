import aiohttp
import json

from typing import Dict, cast
from apis.public.types import (
    CoinInfoData,
    CoinOrderPricesData,
    DepositData,
    FailResponse,
    JsonFailResponse,
    JsonSuccessResponse,
    OrderCoinCurrency,
    OrderCurrency,
    PaymentCurrency,
    SuccessResponse,
    TransactionData,
)


async def request_get_json(
    url: str,
    headers={"accept": "application/json"},
):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as resp:
            return await resp.json()


def show_json(json_data):
    text = json.dumps(json_data, indent=2)
    print(text)


STATUS_SUCCESS = "0000"


async def 현재가_정보_조회(order_currency: OrderCurrency, payment_currency: PaymentCurrency):
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"
    resp_json = await request_get_json(url)

    if resp_json["status"] == STATUS_SUCCESS:
        return SuccessResponse[CoinInfoData](**cast(JsonSuccessResponse, resp_json))
    else:
        return FailResponse(**cast(JsonFailResponse, resp_json))


async def 호가_정보_조회(order_currency: OrderCurrency, payment_currency: PaymentCurrency):
    url = (
        f"https://api.bithumb.com/public/orderbook/{order_currency}_{payment_currency}"
    )
    resp_json = await request_get_json(url)

    if resp_json["status"] == STATUS_SUCCESS:
        return SuccessResponse[CoinOrderPricesData](
            **cast(JsonSuccessResponse, resp_json)
        )
    else:
        return FailResponse(**cast(JsonFailResponse, resp_json))


async def 최근_체결_내역(
    order_currency: OrderCurrency, payment_currency: PaymentCurrency, count=20
):
    url = f"https://api.bithumb.com/public/transaction_history/{order_currency}_{payment_currency}?count={count}"
    resp_json = await request_get_json(url)

    if resp_json["status"] == STATUS_SUCCESS:
        return SuccessResponse[list[TransactionData]](
            **cast(JsonSuccessResponse, resp_json)
        )
    else:
        return FailResponse(**cast(JsonFailResponse, resp_json))


async def 입출금_지원_현황(order_currency: OrderCoinCurrency):
    url = f"https://api.bithumb.com/public/assetsstatus/{order_currency}"
    resp_json = await request_get_json(url)

    if resp_json["status"] == STATUS_SUCCESS:
        return SuccessResponse[DepositData](**cast(JsonSuccessResponse, resp_json))
    else:
        return FailResponse(**cast(JsonFailResponse, resp_json))


async def 입출금_지원_현황_전체():
    url = f"https://api.bithumb.com/public/assetsstatus/ALL"
    resp_json = await request_get_json(url)

    if resp_json["status"] == STATUS_SUCCESS:
        return SuccessResponse[Dict[OrderCoinCurrency, DepositData]](
            **cast(JsonSuccessResponse, resp_json)
        )
    else:
        return FailResponse(**cast(JsonFailResponse, resp_json))
