from typing import Any, Generic, Literal, TypeVar, TypedDict

from pydantic import BaseModel


RequestReturnType = Literal["json", "text"]

OrderCoinCurrency = Literal[
    "BTC",
    "ETH",
    "ETC",
    "XRP",
    "BCH",
    "QTUM",
    "BTG",
    "EOS",
    "ICX",
    "TRX",
    "ELF",
    "KNC",
    "GLM",
    "ZIL",
    "WAXP",
    "POWR",
    "LRC",
    "STEEM",
    "STRAX",
    "ZRX",
    "SNT",
    "ADA",
    "CTXC",
    "BAT",
    "THETA",
    "LOOM",
    "WAVES",
    "LINK",
    "ENJ",
    "VET",
    "MTL",
    "IOST",
    "AMO",
    "BSV",
    "ORBS",
    "TFUEL",
    "VALOR",
    "CON",
    "ANKR",
    "MIX",
    "CRO",
    "FX",
    "CHR",
    "MBL",
    "MXC",
    "FCT2",
    "WOM",
    "BOA",
    "MEV",
    "SXP",
    "COS",
    "EL",
    "HIVE",
    "XPR",
    "VRA",
    "FIT",
    "EGG",
    "BORA",
    "ARPA",
    "CTC",
    "APM",
    "CKB",
    "AERGO",
    "EVZ",
    "QTCON",
    "UNI",
    "YFI",
    "UMA",
    "AAVE",
    "COMP",
    "BAL",
    "RSR",
    "NMR",
    "RLC",
    "UOS",
    "SAND",
    "STPT",
    "BEL",
    "OBSR",
    "ORC",
    "POLA",
    "ADP",
    "DVI",
    "GHX",
    "MVC",
    "BLY",
    "WOZX",
    "ANV",
    "GRT",
    "BIOT",
    "SNX",
    "SOFI",
    "GRACY",
    "OXT",
    "MAP",
    "AQT",
    "PLA",
    "WIKEN",
    "CTSI",
    "MANA",
    "LPT",
    "MKR",
    "SUSHI",
    "ASM",
    "PUNDIX",
    "CELR",
    "FRONT",
    "RLY",
    "OCEAN",
    "BFC",
    "ALICE",
    "OGN",
    "COTI",
    "CAKE",
    "BNT",
    "XVS",
    "SWAP",
    "CHZ",
    "AXS",
    "DAO",
    "SIX",
    "DAI",
    "SHIB",
    "MATIC",
    "WOO",
    "ACH",
    "VELO",
    "XLM",
    "ONT",
    "META",
    "KLAY",
    "ONG",
    "ALGO",
    "JST",
    "XTZ",
    "MLK",
    "DOT",
    "ATOM",
    "SSX",
    "TEMCO",
    "DOGE",
    "KSM",
    "CTK",
    "BNB",
    "NFT",
    "SUN",
    "XEC",
    "AGIX",
    "SOL",
    "FNSA",
    "EGLD",
    "MASK",
    "DFA",
    "C98",
    "MED",
    "1INCH",
    "CRV",
    "BOBA",
    "DYDX",
    "MINA",
    "FLOW",
    "JOE",
    "GALA",
    "BTT",
    "JASMY",
    "TITAN",
    "REQ",
    "CSPR",
    "AVAX",
    "TDROP",
    "HBAR",
    "FANC",
    "NPT",
    "REI",
    "T",
    "MBX",
    "GMT",
    "TAVA",
    "DAR",
    "APE",
    "WNCG",
    "ALT",
    "XCN",
    "GXA",
    "AZIT",
    "FLR",
    "SFP",
    "FITFI",
    "STAT",
    "CRTS",
    "VIX",
    "LBL",
    "FLZ",
    "LM",
    "GRND",
    "APT",
    "BLUR",
    "OAS",
    "HOOK",
    "ENTC",
    "ONIT",
    "OP",
    "ROA",
    "EVER",
    "GMX",
    "STX",
    "XPLA",
    "ARB",
    "INJ",
    "HFT",
    "RPL",
    "IMX",
    "CFX",
    "ACS",
    "FXS",
    "CELO",
    "LDO",
    "FTM",
    "FET",
    "SUI",
    "NCT",
    "FLOKI",
    "ALEX",
    "ID",
    "RNDR",
    "STG",
    "GAL",
    "ILV",
    "MAV",
    "RSS3",
    "AGI",
    "RDNT",
    "ASTR",
    "WLD",
    "FLUX",
    "LEVER",
    "EDU",
    "SEI",
    "PEPE",
    "CYBER",
    "ARKM",
    "PYR",
    "PENDLE",
    "STORJ",
    "API3",
    "ZTX",
    "TIA",
    "SPURS",
    "HIFI",
]

OrderCurrency = Literal["ALL"] | OrderCoinCurrency

PaymentCurrency = Literal["KRW", "BTC"]


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
    type: Literal["bid", "ask"]
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
