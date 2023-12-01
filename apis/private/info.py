import base64
import hmac, hashlib
import math
import time
import urllib.parse
from apis.common_types import (
    OrderCoinCurrency,
    OrderCurrency,
    OrderType,
    PaymentCurrency,
)
from apis.util import request_post_json

from config import config
from typing import Literal, NotRequired, TypedDict

API_URL = "https://api.bithumb.com"
API_KEY = config["CONNECT_KEY"] or ""
API_SECRET = config["SECRET_KEY"] or ""

contents = ""


def microtime(get_as_float=False) -> str:
    if get_as_float:
        return f"{time.time()}"
    else:
        return "%f %d" % math.modf(time.time())


def body_callback(buf):
    global contents
    contents = buf


def usecTime():
    mt = microtime(False)
    mt_array = mt.split(" ")[:2]
    return mt_array[1] + mt_array[0][2:5]


def create_header(endpoint, params):
    # 1. Api-Sign and Api-Nonce information generation.
    # 2. Request related information from the Bithumb API server.
    #
    # - nonce: it is an arbitrary number that may only be used once.
    # - api_sign: API signature information created in various combinations values.

    endpoint_item_array = {"endpoint": endpoint}

    uri_dictionary = dict(endpoint_item_array, **params)

    str_data = urllib.parse.urlencode(uri_dictionary)
    nonce = usecTime()
    """it is an arbitrary number that may only be used once."""

    utf8_data = f"{endpoint}{chr(0)}{str_data}{chr(0)}{nonce}".encode("utf-8")
    utf8_key = API_SECRET.encode("utf-8")

    h = hmac.new(bytes(utf8_key), utf8_data, hashlib.sha512)
    utf8_hex_output = h.hexdigest().encode("utf-8")

    api_sign = base64.b64encode(utf8_hex_output)
    """API signature information created in various combinations values."""

    utf8_api_sign = api_sign.decode("utf-8")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "Api-Key": API_KEY,
        "Api-Nonce": nonce,
        "Api-Sign": utf8_api_sign,
    }

    return headers


async def request_private_api(endpoint, params):
    data = dict({"endpoint": endpoint}, **params)
    headers = create_header(endpoint, data)

    return await request_post_json(API_URL + endpoint, headers, data)


class 회원_정보_조회_params(TypedDict):
    order_currency: OrderCoinCurrency
    """주문 통화 (코인)"""
    payment_currency: NotRequired[PaymentCurrency]
    """결제 통화 (마켓)"""


async def 회원_정보_조회(params: 회원_정보_조회_params):
    return await request_private_api("/info/account", params)


class 보유자산_조회_params(TypedDict):
    currency: OrderCurrency


async def 보유자산_조회(params: 보유자산_조회_params):
    return await request_private_api("/info/balance", params)


class 입금지갑_주소_조회_params(TypedDict):
    currency: OrderCoinCurrency


async def 입금지갑_주소_조회(params: 입금지갑_주소_조회_params):
    return await request_private_api("/info/wallet_address", params)


class 최근_거래정보_조회_params(TypedDict):
    order_currency: OrderCoinCurrency
    """주문 통화 (코인)"""
    payment_currency: NotRequired[PaymentCurrency]
    """결제 통화 (마켓)"""


async def 최근_거래정보_조회(params):
    return await request_private_api("/info/ticker", params)


class 거래_주문내역_조회_params(TypedDict):
    order_id: NotRequired[str]
    """매수/매도 주문 등록된 주문번호 (입력 시 해당 데이터만 추출)"""
    type: NotRequired[OrderType]
    """거래유형 (bid : 매수 ask : 매도)"""
    count: NotRequired[int]
    """1~1000 (기본값 : 100)"""
    after: NotRequired[int]
    """
    입력한 시간보다 나중의 데이터 추출 YYYY-MM-DD hh:mm:ss 의 UNIX Timestamp 
    (2014-11-28 16:40:01 = 1417160401000)
    """
    order_currency: OrderCoinCurrency
    """주문 통화 (코인)"""
    payment_currency: NotRequired[PaymentCurrency]
    """결제 통화 (마켓)"""


async def 거래_주문내역_조회(params: 거래_주문내역_조회_params):
    """Request Parameter에서 order_id 또는 type을 입력하면 order_id, type이 필수 값으로 적용"""
    return await request_private_api("/info/orders", params)


class 거래_주문내역_상세_조회_params(TypedDict):
    order_id: str
    """매수/매도 주문 등록된 주문번호 (입력 시 해당 데이터만 추출)"""
    order_currency: OrderCoinCurrency
    """주문 통화 (코인)"""
    payment_currency: NotRequired[PaymentCurrency]
    """결제 통화 (마켓)"""


async def 거래_주문내역_상세_조회(params: 거래_주문내역_상세_조회_params):
    """
    회원의 매수/매도 체결 내역 상세 정보를 제공합니다.

    [취소주문에 대한 취소 결과 확인하기]
    Order status 가 Cancel 상태임을 확인합니다.
    아래 계산을 통해 취소 완료 수량(Cancel_qty)를 계산할 수 있습니다.
    Cancel_qty = Order_qty - (contract 내에 각 units 총합)
    """
    return await request_private_api("/info/order_detail", params)


class 거래_체결내역_조회_params(TypedDict):
    offset: NotRequired[int]
    """0~ (기본값 : 0)"""
    count: NotRequired[int]
    """1~50 (기본값 : 20)"""
    searchGb: NotRequired[Literal[0, 1, 2, 3, 4, 5, 9]]
    """0:전체, 1:매수 완료, 2:매도 완료, 3:출금 중, 4:입금, 5:출금, 9:KRW 입금 중"""
    order_currency: OrderCoinCurrency
    """주문 통화 (코인)"""
    payment_currency: NotRequired[PaymentCurrency]
    """결제 통화 (마켓)"""


async def 거래_체결내역_조회(params: 거래_체결내역_조회_params):
    """회원의 거래 완료 내역 정보를 제공합니다."""
    return await request_private_api("/info/user_transactions", params)
