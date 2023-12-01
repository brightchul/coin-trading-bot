from typing import Any, Generic, Literal, TypeVar, TypedDict
from pydantic import BaseModel
from apis.common_types import OrderCurrency, OrderType, PaymentCurrency


RequestReturnType = Literal["json", "text"]


class JsonSuccessResponse(TypedDict):
    status: str
    data: Any


class JsonFailResponse(TypedDict):
    status: str
    message: str


class CoinInfoData(BaseModel):
    opening_price: str
    """시가 00시 기준"""
    closing_price: str
    """종가 00시 기준"""
    min_price: str
    """저가 00시 기준"""
    max_price: str
    """고가 00시 기준"""
    units_traded: str
    """거래량 00시 기준"""
    acc_trade_value: str
    """거래금액 00시 기준"""
    prev_closing_price: str
    """전일종가"""
    units_traded_24H: str
    """최근 24시간 거래량"""
    acc_trade_value_24H: str
    """최근 24시간 거래금액"""
    fluctate_24H: str
    """최근 24시간 변동가"""
    fluctate_rate_24H: str
    """최근 24시간 변동률"""
    date: str
    """타임 스탬프"""


class BasicResponse(BaseModel):
    status: str
    """결과 상태 코드(정상: 0000, 그 외 에러 코드 참조)"""


DataT = TypeVar("DataT")


class SuccessResponse(BasicResponse, Generic[DataT]):
    data: DataT


class FailResponse(BasicResponse):
    message: str


class CoinPriceData(BaseModel):
    quantity: str
    """	Currency 수량"""
    price: str
    """Currency 거래가"""


class CoinOrderPricesData(BaseModel):
    timestamp: str
    order_currency: OrderCurrency
    """주문 통화 (코인)"""
    payment_currency: PaymentCurrency
    """결제 통화 (마켓)"""
    bids: list[CoinPriceData]
    """매수 요청 내역"""

    asks: list[CoinPriceData]
    """매도 요청 내역"""


class TransactionData(BaseModel):
    transaction_date: str
    """거래 체결 시간 타임 스탬프 (YYYY-MM-DD HH:MM:SS)"""
    type: OrderType
    """거래 유형 bid : 매수 ask : 매도"""
    units_traded: str
    """Currency 거래량"""
    price: str
    """Currency 거래가	"""
    total: str
    """총 거래 금액"""


class DepositData(BaseModel):
    deposit_status: int
    """입금 가능 여부 (1:입금가능 / 0:입금불가)"""
    withdrawal_status: int
    """입금 가능 여부 (1:입금가능 / 0:입금불가)"""
