from typing import Any, Literal


def Log(*args):
    """
    输出日志
    """
    ...


def LogProfit(profit: float, *args):
    """
    记录盈亏值，打印盈亏数值并根据盈亏数值绘制收益曲线。
    如果以字符&结尾，只绘制收益图表，不打印收益日志

    :param profit: 收益数据
    """


def LogProfitReset(remain: int):
    """
    清空所有收益日志、收益图表

    :param remain: 指定保留的日志条数
    """
    ...


def LogStatus(msgs: Any):
    """
    此信息不保存到日志列表里，只更新当前实盘的状态信息，
    在实盘页面日志区域上方的状态栏显示，
    可多次调用更新状态。参数值：Msg可以为任意类型
    """
    ...


def EnableLog(enable: bool):
    """
    打开或者关闭订单信息的日志记录
    """


def LogReset(remain: int):
    """
    清空所有日志，remain用于指定保留的日志条数
    """


def LogVacuum():
    """
    用于在调用LogReset()函数清除日志后，回收SQLite删除数据时占用的储存空间
    """


class Chart:
    def __init__(self, options: Any) -> None: ...

    def add(self, series: int, data: Any, index: int = -1):
        """
        添加数据到图表

        :param series: 用于设置数据系列索引
        :param data: 用于设置写入的具体数据，是一个数组
        :param index: 用于设置数据索引，是整数。指定修改数据的具体索引位置，
        支持使用负数表示，设置为-1指数据集的最后一个数据
        """

    def reset(self, remain: int | None = None):
        """
        用于清空图表数据，remain用于指定保留数据的条数。不传参数remain表示清除全部数据。
        """


class KLineChart:
    def __init__(self, options: Any) -> None:
        pass

    def barcolor(
        self,
        color: str,
        offset: int | None = None,
        editable: bool = True,
        show_last: bool = True,
        title: str | None = None,
        display: Literal["none", "all"] = "all",
    ):
        """
        设置柱状图颜色
        """
        ...

    def bgcolor(
        self,
        color: str,
        offset: int = 0,
        editable: bool = True,
        show_last: bool = True,
        title: str | None = None,
        display: Literal["none", "all"] = "all",
        overlay: bool = False,
    ): ...

    """
    指定颜色填充K线的背景
    """

    def plot(
        self,
        series: Any,
        title: str | None = None,
        color: str | None = None,
        linewidth: int = 1,
        style: Literal[
            "stepline_diamond",
            "stepline",
            "cross",
            "areabr",
            "area",
            "circles",
            "columns",
            "histogram",
            "linebr",
            "line",
        ] = "line",
        trackprice=None,
        histbase=None,
        offset: int = 0,
        join=None,
        editable: bool = True,
        show_last: bool = False,
        display: Literal["none", "all"] = "all",
    ):
        """
        绘制一系列数据
        """
        ...

    def fill(self, hline1, hline2, color, title, editable, fillgaps, display):
        """
        使用提供的颜色填充两个绘图或hline之间的背景
        """
        ...
