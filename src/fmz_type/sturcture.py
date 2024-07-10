from dataclasses import dataclass


@dataclass
class BaseData:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__getattribute__(key)


@dataclass
class Trade(BaseData):
    Id: str
    Time: int
    Price: float
    Amount: float
    Type: int


@dataclass
class Ticker(BaseData):
    Symbol: str
    High: float
    Low: float
    Sell: float
    Buy: float
    Last: float
    Open: float
    Volume: float
    Time: int
    OpenInterest: float


@dataclass
class Record(BaseData):
    Time: int
    Open: float
    High: float
    Low: float
    Close: float
    OpenInterest: float
    Volume: float


@dataclass
class Order(BaseData):
    Symbol: str
    Id: str
    Price: float
    Amount: float
    DealAmount: float
    AvgPrice: float
    Status: int
    Type: int
    Offest: int
    ContractType: str


@dataclass
class OrderBook(BaseData):
    Price: float
    Amount: float


@dataclass
class Depth(BaseData):
    Asks: list[OrderBook]
    Bids: list[OrderBook]
    Time: int


@dataclass
class Account(BaseData):
    Info: dict
    Balance: float
    FrozenBalance: float
    Stocks: float
    FrozenStocks: float


@dataclass
class Asset(BaseData):
    Currency: str
    Amount: float
    FrozenAmount: float


@dataclass
class Position(BaseData):
    Info: dict
    Symbol: str
    MarginLevel: int
    Amount: int
    FrozenAmount: int
    Price: float
    Profit: float
    Type: int
    ContractType: str
    Margin: float


@dataclass
class Market(BaseData):
    Symbol: str
    BaseAsset: str
    QuoteAsset: str
    TickSize: float
    AmountSize: float
    PricePrecision: int
    AmountPrecision: int
    MinQty: float
    MaxQty: float
    MinNotional: float
    MaxNotional: float
    CtVal: float
    Info: dict
