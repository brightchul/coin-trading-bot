from apis.common_types import (
    OrderCoinCurrency,
    OrderType,
    PaymentCurrency,
)
from apis.private.info import request_private_api
from typing import TypedDict

"""
출금하기 API는 생략
https://apidocs.bithumb.com/reference/%EC%BD%94%EC%9D%B8-%EC%B6%9C%EA%B8%88%ED%95%98%EA%B8%B0-%EA%B0%9C%EC%9D%B8
"""


class 지정가_주문하기_params(TypedDict):
    order_currency: OrderCoinCurrency
    """주문 통화 (가상자산)"""
    payment_currency: PaymentCurrency
    """결제 통화 (마켓) 입력값"""
    units: float
    """주문 수량 [최대 주문 금액] 50억 원"""
    price: float
    """Currency 거래가, 주문 금액은 최소 500 KRW 이상입니다."""
    type: OrderType
    """거래 유형(bid : 매수 ask : 매도)"""


async def 지정가_주문하기(params: 지정가_주문하기_params):
    return await request_private_api("/trade/place", params)


class 시장가_매수하기_params(TypedDict):
    units: float
    """가상자산 매수 수량 [최대 주문 금액] 10억 원"""
    order_currency: OrderCoinCurrency
    """주문 통화 (가상자산)"""
    payment_currency: PaymentCurrency
    """결제 통화 (마켓)"""


async def 시장가_매수하기(params: 시장가_매수하기_params):
    """
    주문 금액은 최소 500 KRW 이상입니다.
    원화(KRW) 마켓은 NH농협은행 계좌 연결을 하셔야 거래가 가능합니다.
    """
    return await request_private_api("/trade/market_buy", params)


class 시장가_매도하기_params(TypedDict):
    units: OrderCoinCurrency
    """가상자산 매도 수량 [최대 주문 금액] 10억 원	Float / 필수"""
    order_currency: OrderCoinCurrency
    """주문 통화 (가상자산)"""
    payment_currency: PaymentCurrency
    """결제 통화 (마켓)"""


async def 시장가_매도하기(params: 시장가_매도하기_params):
    """
    주문 금액은 최소 500 KRW 이상입니다.
    원화(KRW) 마켓은 NH농협은행 계좌 연결을 하셔야 거래가 가능합니다.
    """
    return await request_private_api("/trade/market_sell", params)


class 자동_주문하기_params(TypedDict):
    order_currency: OrderCoinCurrency
    """주문 통화 (가상자산)"""
    payment_currency: PaymentCurrency
    """결제 통화 (마켓)"""
    watch_price: float
    """주문 접수가 진행되는 가격 (자동 주문 시)"""
    price: float
    """Currency 거래가"""
    units: float
    """주문 수량 [최대 주문 금액] 50억 원"""
    type: OrderType
    """주문 요청 구분 (bid : 매수 ask : 매도)"""


async def 자동_주문하기(params: 자동_주문하기_params):
    return await request_private_api("/trade/stop_limit", params)


class 주문_취소하기_params(TypedDict):
    type: OrderType
    """거래유형 (bid : 매수 ask : 매도)"""
    order_id: str
    """매수 / 매도 주문 등록된 주문 번호"""
    order_currency: OrderCoinCurrency
    """주문 통화 (가상자산)"""
    payment_currency: PaymentCurrency
    """결제 통화 (마켓) 입력값"""


async def 주문_취소하기(params: 주문_취소하기_params):
    return await request_private_api("/trade/cancel", params)
