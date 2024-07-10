import time
from typing import Any, Callable, Sequence, TypeVar

T = TypeVar("T")


def Version() -> str:
    return "3.6"


def Sleep(millisecond: float):
    """休眠函数

    例如执行Sleep(1000)函数时，程序会休眠1秒。
    支持休眠时间小于1毫秒的操作，例如设置Sleep(0.1)。
    支持最小参数为0.000001，即纳秒级休眠，1纳秒等于1e-6毫秒。

    :param millisecond: 参数用于设置休眠时长，毫秒数
    """
    time.sleep(millisecond)


def IsVirtual() -> bool:
    """
    判断当前运行环境是否是回测系统，用来兼容回测与实盘的差异
    """
    ...


def SetErrorFilter(filters: str):
    """
    过滤错误日志
    """


def GetPid() -> str:
    """
    获取实盘进程Id
    """
    ...


def _G(k: str, v: Any):
    """
    持久化保存数据，该函数实现了一个可保存的全局字典功能
    """
    ...


def _D(Timestamp: int, Fmt: str) -> str:
    """
    将毫秒时间戳或者Date对象转换为时间字符串

    :param Timestamp: 为数值类型，值为毫秒数
    :param Fmt: 为字符串类型，默认为：yyyy-MM-dd hh:mm:ss
    :return: 字符串类型
    """
    ...


def _N(num: float, precision: int) -> float:
    """格式化一个浮点数

    :param num: 浮点数
    :param precision: 精度
    :return: 格式化后的浮点数
    """
    ...


def _C(function: Callable[..., T], *args: Any) -> T:
    """
    该函数为重试函数，用于获取行情、获取未完成订单等接口的容错
    """
    ...


def _Cross(arr1: Sequence[int | float], arr2: Sequence[int | float]) -> int:
    """
    计算两条指标线的交叉状态，正数为上穿周期, 负数表示下穿的周期, 0指当前价格一样

    :param arr1: 慢线指标数组
    :param arr2: 快线指标数组
    :return: 上穿周期或下穿周期
    """
    ...
