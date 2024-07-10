from typing import Any, Literal

from fmz_type.sturcture import (
    Account,
    Asset,
    Depth,
    Market,
    Order,
    Position,
    Record,
    Ticker,
    Trade,
)


class Goroutine:
    def __init__(self) -> None: ...

    def wait(self, timeout=0) -> tuple[Any, bool]: ...


class Exchange:
    def __init__(self) -> None: ...

    def GetName(self) -> str:
        """
        获取当前交易所对象绑定的交易所名称
        """
        ...

    def GetAccount(self) -> Account:
        """
        请求交易所账户信息,返回Account对象
        """
        ...

    def GetAssets(self) -> Asset:
        """
        请求交易所账户资产信息
        """
        ...

    def GetLabel(self) -> str:
        """
        获取配置交易所对象时设置的自定义标签
        """
        ...

    def GetCurrency(self) -> str:
        """
        获取当前设置的交易对。
        交易对格式统一为大写，例如：BTC_USDT
        """
        ...

    def SetCurrency(self, s: str):
        """
        切换交易所对象exchange当前的交易对。
        交易对格式统一为大写，例如：BTC_USDT
        """
        ...

    def GetQuoteCurrency(self) -> str:
        """
        获取当前设置的交易对中的计价货币
        """
        ...

    def GetTicker(self, symbol: str | None = None) -> Ticker:
        """
        获取当前设置的交易对、合约代码对应的现货或者合约的Ticker结构，即行情数据

        :param symbol: 交易对, 默认为空
        :return: 行情数据
        """
        ...

    def GetDepth(self, symbol: str | None = None) -> Depth:
        """
        获取订单簿数据

        :param symbol: 交易对, 默认为空
        :return: 订单簿数据
        """
        ...

    def GetTrades(self, symbol: str | None = None) -> Trade:
        """
        获取市场成交数据

        :param symbol: _description_, defaults to None
        :return: 成交数据
        """
        ...

    def GetRecords(self, symbol: str = "", period: int = -1, limit: int = 0) -> Record:
        """
        获取自定义周期的K线数据

        :param symbol: 交易对
        :param period: k线周期
        :param limit: 获取条数
        :return: K线数据
        """
        ...

    def GetPeriod(self) -> int:
        """
        获取当前设置的交易对、合约代码对应的现货或者合约的K线周期
        """
        ...

    def SetMaxBarLen(self, n: int):
        """
        设置K线最大长度
        """
        ...

    def GetRawJSON(self) -> str:
        """
        获取当前交易所对象（exchange、exchanges）最近一次rest请求返回的原始内容
        """
        ...

    def GetRate(self) -> float:
        """
        获取交易所对象当前设置的汇率
        """
        ...

    def SetData(self, k: str, v: Any):
        """
        用于设置策略运行时加载的数据
        """
        ...

    def GetData(self, k: str, timeout=5) -> Any:
        """
        用于获取exchange.SetData()函数加载的数据或外部链接提供的数据
        """
        ...

    def GetMarkets(self) -> dict[str, Market]:
        """
        用于获取交易所市场信息
        """
        ...

    def GetTickers(self) -> list[Ticker]:
        """
        获取交易所所有交易对的Ticker数据
        """
        ...

    def Buy(self, price: float, amount: float, *args: Any) -> str:
        """
        买单函数

        参数price设置为-1用于下市价单，需要交易所的下单接口支持市价单。
        加密货币现货的市价单方式下单，下买单时，下单量参数amount是以计价币为单位的金额数量。
        加密货币期货合约的市价单方式下单，下单量参数amount的单位为合约张数。

        :param price: 订单价格，-1为市价单
        :param amount: 订单量
        :param args: 扩展参数，可以输出附带信息到这条下单日志中，args参数可以传多个
        :return: 订单编号
        """
        ...

    def Sell(self, price: float, amount: float, *args: Any) -> str:
        """
        卖单函数

        参数price设置为-1用于下市价单，需要交易所的下单接口支持市价单。
        加密货币现货的市价单方式下单，下买单时，下单量参数amount是以计价币为单位的金额数量。
        加密货币期货合约的市价单方式下单，下单量参数amount的单位为合约张数。

        :param price: 订单价格，-1为市价单
        :param amount: 订单量
        :param args: 扩展参数，可以输出附带信息到这条下单日志中，args参数可以传多个
        :return: 订单编号
        """
        ...

    def CreateOrder(
        self,
        symbol: str,
        side: Literal["buy", "sell", "closebuy", "closesell"],
        price: float,
        amount: float,
    ) -> str | None:
        """
        创建订单

        :param symbol: 指定订单的具体交易对、合约代码。传空字符串""时 \
                       默认以当前设置的交易对、合约代码下单
        :param side: 订单的交易方向
        :param price: 订单的价格，-1时表示订单为市价单
        :param amount: 订单的下单量
        :return: 下单成功返回订单Id，下单失败返回空值
        """

    def CancelOrder(self, orderId: str, *args: Any) -> bool:
        """
        取消订单

        :param orderId: 指定所要取消的订单
        :return: 订单是否取消成功
        """
        ...

    def GetOrder(self, orderId: int) -> Order:
        """_summary_

        :param orderId: 订单Id
        :return: 订单信息
        """
        ...

    def GetOrders(self, symbol: str = "") -> list[Order]:
        """
        获取当前交易对、合约的所有未完成的订单

        :param symbol: 用于指定所要查询的订单数据的交易对、合约代码。
        :return: Order结构数组
        """
        ...

    def GetHistoryOrders(
        self, symbol: str = "", since: int = 0, limit: int = 0
    ) -> list[Order]:
        """
        用于获取当前交易对、合约的历史订单

        :param symbol: 用于指定所要查询的订单数据的交易对、合约代码, 默认为空字符串
        :param since: 查询的起始时间戳，单位为毫秒
        :param limit: 查询的订单数量
        :return: Order结构数组
        """
        ...

    def SetPrecision(self, pricePrecision: int, amountPrecision: int):
        """
        设置交易所下单精度, 回测系统不支持该函数

        :param pricePrecision: 用来控制价格数据的精度
        :param amountPrecision: 用来控制下单量数据的精度
        """
        ...

    def SetRate(self, rate: float):
        """
        设置交易所对象当前的汇率
        """
        ...

    def IO(self, k: str, *args) -> Any:
        """
        用于交易所对象相关的其它接口调用,
        具体参考https://www.fmz.com/syntax-guide#fun_exchange.io
        """
        ...

    def Log(self, orderType: int, price: float, amount: float, *args: Any):
        """
        用于在日志栏区域输出下单、撤单日志。调用时不会下单，只输出、记录交易日志。
        :param orderType: 订单类型
        :param price: 订单价格
        :param amount: 订单数量
        :param args: 其他参数
        """
        ...

    def Encode(
        self,
        algo: str,
        inputFormat: Literal["raw", "hex", "base64", "string"],
        outputFormat: Literal["raw", "hex", "base64", "string"],
        data: str,
        keyFormat: str,
        key: str,
    ) -> str:
        """
        签名加密计算

        :param algo: 编码计算时使用的算法，
        :param inputFormat: 输入data的数据格式
        :param outputFormat: 输出data的数据格式
        :param data: 需要加密的数据
        :param keyFormat: key的数据格式
        :param key: 签名计算时使用的密钥，可以使用明文字符串。\
                    也可以使用"{{accesskey}}"、"{{secretkey}}"代指 \
                    exchange交易所对象中配置的accessKey和secretKey \
        :return: 加密后的数据
        """
        ...

    def Go(self, method: str, *args) -> Goroutine:
        """
        多线程异步支持函数

        :param method: 指定并发的函数名称
        """
        ...

    def GetPositions(self) -> list[Position]:
        """
        获取当前设置的交易对、合约的持仓信息
        """
        ...

    def SetMarginLevel(self, s: int):
        """
        设置exchange交易所对象当前交易对、合约的杠杆值
        """
        ...

    def SetDirection(self, direction: Literal["buy", "closesell", "sell", "closebuy"]):
        """
        设置`exchange.Buy`函数、`exchange.Sell`函数进行期货合约下单时的订单方向
        """

    def SetContractType(self, symbol: str):
        """
        于设置`exchange`交易所对象当前的合约代码
        """
        ...

    def GetContractType(self):
        """
        用于获取`exchange`交易所对象当前设置的合约代码
        """
        ...

    def SetBase(self, api: str):
        """
        设置`exchange`交易所对象中配置的交易所API接口基地址
        """

    def GetBase(self):
        """
        获取当前交易所API接口基地址
        """
        ...

    def SetProxy(self, proxy: str):
        """
        设置`exchange`交易所对象的代理配置
        """
        ...

    def SetTimeout(self, timeout: int):
        """
        用于设置`exchange`交易所对象的rest请求的超时时间。
        仅限`REST`协议，只用设置一次即可生效。

        :param timeout: 超时时间，单位为毫秒
        """
        ...


exchange = Exchange()
exchanges = [Exchange()]
