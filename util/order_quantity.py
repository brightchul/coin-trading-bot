import math

CoinMinimumWithdrawalQuantity = {
    "BTC": 0.002,
    "ETH": 0.01,
    "ETC": 0.1,
    "XRP": 21,
    "BCH": 0.002,
    "QTUM": 0.1,
    "BTG": 0.002,
    "EOS": 0.5,
    "ICX": 4,
    "TRX": 150,
    "ELF": 7,
    "OMG": 2,
    "KNC": 2,
    "GLM": 30,
    "ZIL": 30,
    "WAXP": 5,
    "POWR": 23,
    "LRC": 42,
    "EOSDAC": 10,
    "STEEM": 0.01,
    "STRAX": 0.2,
    "ZRX": 6,
    "REP": 0.08,
    "XEM": 4,
    "SNT": 23,
    "ADA": 1,
    "CTXC": 60,
    "BAT": 3,
    "WTC": 1.4,
    "THETA": 0.5,
    "LOOM": 22,
    "WAVES": 2,
    "LINK": 0.11,
    "MEETONE": 10,
    "HORUS": 10,
    "ADD": 100,
    "ENJ": 2,
    "VET": 200,
    "MTL": 0.9,
    "CHL": 100,
    "BLACK": 10,
    "ATD": 100,
    "IOST": 1000,
    "TMTG": 360,
    "QKC": 2000,
    "ATOLO": 430,
    "AMO": 7000,
    "BSV": 0.002,
    "BXA": 15,
    "ORBS": 24,
    "TFUEL": 8,
    "VALOR": 5,
    "CON": 460,
    "ANKR": 27,
    "MIX": 360,
    "CRO": 38,
    "FX": 10,
    "CHR": 12,
    "MBL": 3500,
    "MXC": 72,
    "WIN": 1,
    "FCT2": 0.03,
    "TRV": 100,
    "DAD": 12,
    "WOM": 15,
    "SOC": 360,
    "BOA": 10,
    "MEV": 600,
    "SXP": 0.9,
    "COS": 97,
    "APIX": 36,
    "EL": 170,
    "BASIC": 460,
    "HIVE": 18,
    "XPR": 800,
    "VRA": 300,
    "FIT": 720,
    "EGG": 360,
    "BORA": 1,
    "ARPA": 35,
    "CTC": 12,
    "APM": 100,
    "CKB": 170,
    "AERGO": 13,
    "ANW": 28,
    "CENNZ": 60,
    "EVZ": 44,
    "CYCLUB": 170,
    "SRM": 0.7,
    "QTCON": 56,
    "UNI": 0.13,
    "YFI": 0.0001,
    "UMA": 0.17,
    "AAVE": 0.01,
    "COMP": 0.01,
    "REN": 8,
    "BAL": 0.27,
    "RSR": 220,
    "NMR": 0.12,
    "RLC": 2,
    "UOS": 6,
    "SAND": 7,
    "STPT": 63,
    "GOM2": 320,
    "RINGX": 28,
    "BEL": 0.8,
    "OBSR": 200,
    "ORC": 2,
    "POLA": 15,
    "AWO": 270,
    "ADP": 59,
    "DVI": 9,
    "IBP": 100,
    "GHX": 9,
    "MIR": 0.5,
    "CBK": 0.5,
    "ONX": 5,
    "MVC": 25,
    "BLY": 56,
    "WOZX": 3,
    "ANV": 2,
    "GRT": 3,
    "MM": 2,
    "BIOT": 77,
    "XNO": 12,
    "SNX": 0.2,
    "SOFI": 2,
    "COLA": 3,
    "OXT": 6,
    "LINA": 34,
    "ASTA": 37,
    "MAP": 34,
    "AQT": 0.9,
    "PLA": 24,
    "WIKEN": 40,
    "CTSI": 9,
    "MANA": 5,
    "LPT": 0.13,
    "MKR": 0.0014,
    "SUSHI": 0.23,
    "ASM": 72,
    "PUNDIX": 0.7,
    "CELR": 84,
    "CWD": 100,
    "ARW": 0.5,
    "BCDC": 0.25,
    "FRONT": 55,
    "RLY": 5,
    "OCEAN": 4,
    "BFC": 10,
    "ALICE": 0.4,
    "OGN": 47,
    "COTI": 75,
    "CAKE": 0.23,
    "BNT": 1.5,
    "XVS": 0.17,
    "SWAP": 32,
    "CHZ": 9,
    "AXS": 0.07,
    "DAO": 6,
    "SIX": 4,
    "DAI": 5,
    "MATIC": 3,
    "WOO": 32,
    "ACH": 600,
    "BAKE": 1.3,
    "VELO": 10,
    "ANC": 2,
    "BCD": 2,
    "XLM": 20,
    "VSYS": 100,
    "IPX": 80,
    "WICC": 32,
    "ONT": 7,
    "LUNA": 12,
    "NEWS": 10,
    "AION": 35,
    "META": 300,
    "KLAY": 2,
    "ONG": 25,
    "ALGO": 4,
    "JST": 250,
    "XTZ": 1.2,
    "MLK": 20,
    "WEMIX": 1,
    "DOT": 1.5,
    "ATOM": 1,
    "SSX": 15,
    "TEMCO": 2000,
    "LZM": 25,
    "HIBS": 1000,
    "QI": 2.5,
    "BURGER": 0.9,
    "DOGE": 17,
    "KSM": 0.02,
    "CTK": 5,
    "XYM": 25,
    "BNB": 0.01,
    "NFT": 20000,
    "SUN": 200,
    "XEC": 1000,
    "PCI": 10,
    "SOL": 0.06,
    "LN": 0.05,
    "EGLD": 0.003,
    "GO": 2,
    "DFA": 12,
    "C98": 0.8,
    "MED": 3,
    "SGB": 10,
    "1INCH": 12,
    "BOBA": 7.5,
    "RPG": 0.15,
    "GALA": 55,
    "PURSE": 750,
    "BTT": 300000,
    "EFI": 60,
    "TITAN": 10,
    "REQ": 150,
    "CSPR": 5,
    "SOLO": 0.5,
    "AVAX": 0.1,
    "TDROP": 3,
    "SPRT": 1.5,
    "NPT": 0.1,
    "REI": 0.5,
    "T": 200,
    "AQUA": 1,
    "MBX": 0.02,
    "GMT": 0.3,
}
"""빗썸 코인별 출금 최소 수량"""


def get_order_minimum_quantity(price: float):
    if price < 0:
        raise ValueError(f"price:{price}는 0보다 작을수 없습니다.")

    if price < 100:
        return 10
    elif price < 1000:
        return 1
    elif price < 10_000:
        return 0.1
    elif price < 100_000:
        return 0.01
    elif price < 1_000_000:
        return 0.001
    else:
        return 0.0001


def check_order_minimum_quantity(price: float, quantity: float):
    """빗썸 코인별 최소 주문 수량 보다 더 작은 단위까지 주문했는지 확인"""
    if price < 0 or quantity < 0:
        raise ValueError(f"price:{price}, quantity:{quantity}는 0보다 작을수 없습니다.")

    return quantity >= get_order_minimum_quantity(price)


def trunc_order_minimum_quantity(price: float, quantity: float):
    """최소 주문수량보다 작은 단위로 주문량이 나왔을 때 그 수량을 잘라준다"""
    if price < 0 or quantity < 0:
        raise ValueError(f"price:{price}, quantity:{quantity}는 0보다 작을수 없습니다.")

    order_min_quanltity = get_order_minimum_quantity(price)
    return math.trunc(quantity / order_min_quanltity) * order_min_quanltity
