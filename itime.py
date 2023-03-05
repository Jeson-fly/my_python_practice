#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2023/3/5 15:39
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 时间处理工具
"""
import datetime
import time

import dateutil.relativedelta


def get_day_past_seconds(timestamp=None):
    """
    今日零点到现在过去的秒数
    """
    if timestamp is None:
        timestamp = get_cur_timestamp()
    nt = time.localtime(timestamp)
    return nt[3] * 3600 + nt[4] * 60 + nt[5]


def parse_timestamp(time_str):
    """
    解析时间字符串:%Y-%m-%d %H:%M:%S，返回时间戳
    """
    if not time_str:
        return 0
    return int(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')))


def get_cur_timestamp():
    """
    获取现在时间戳（秒）
    :return:
    """
    # 线上禁用
    # 为了方便测试更改服务器时间
    # 测试开关 0-使用正确时间 1-使用设置时间

    return int(round(time.time()))


def get_real_standard_timestamp():
    """
    获取标准时间，根据服务器本地时间获取
    :return:
    """

    return int(round(time.time()))


def get_zero_timestamp(timestamp=None):
    """
    获取当天零点时间戳（秒）
    :return:
    """
    if not timestamp:
        timestamp = get_cur_timestamp()
    past_second = get_day_past_seconds(timestamp)
    return int(timestamp - past_second)


def get_end_timestamp(timestamp=None):
    """
    获取当天结束的时间戳（秒）
    :return:
    """
    zero_ts = get_zero_timestamp(timestamp)
    return zero_ts + 24 * 60 * 60


def calc_refresh_d_hour(last_timestamp, hour=0, minute=0, second=0):
    """
    每天刷新检测，返回是否刷新，剩余刷新时间
    :param last_timestamp: 上次刷新时间
    :param hour: 刷新时间点
    :param minute: 刷新时间分钟
    :param second: 刷新时间秒
    :return:
    """
    need_refresh = False
    now_time = get_cur_timestamp()
    past_second = get_day_past_seconds(now_time)
    # 今天该更新的时间，现在的时间减去
    refresh_time = 60 * 60 * hour + minute * 60 + second
    should_time = now_time - past_second + refresh_time
    # 上次刷新时间
    last_should_time = should_time - 24 * 60 * 60

    # 检测
    if now_time >= should_time > last_timestamp:
        need_refresh = True
    # 上次刷新时间
    if last_should_time > last_timestamp:
        need_refresh = True

    # 计算剩余刷新时间，已经更新过时加上周期
    if now_time >= should_time:
        left_time = should_time + 24 * 60 * 60 - now_time
    else:
        left_time = should_time - now_time

    return need_refresh, left_time


def get_next_this_time(time_str):
    """
    获取下一个这个时间的时间戳，例：现在是早上八点，获取下一个15：00：00，也就是今天下午15：00：00的时间戳
    一天是 86400 秒
    :param time_str: "15:00:00" 时：分：秒
    :return:timeStamp
    """
    h, m, s = [int(i) for i in time_str.split(":")]  # 目前是八点
    timestamp = get_cur_timestamp()
    nt = time.localtime(timestamp)
    next_time = timestamp - (nt[3] * 3600 + nt[4] * 60 + nt[5]) + h * 3600 + m * 60 + s
    if next_time <= timestamp:
        next_time += 86400
    return next_time


def get_today_this_ts(fmt_time: str, ts: int):
    """
    获取今天达到此时间点的时间戳
    :param fmt_time: 字符串，8:00:00 - 24小时制
    :param ts: 时间戳
    :return:
    """
    h, m, s = [int(i) for i in fmt_time.split(":")]
    # ts = itime.get_cur_timestamp()
    day_passed_seconds = get_day_past_seconds(ts)
    return ts - day_passed_seconds + h * 3600 + m * 60 + s


def get_past_day(start_ts, end_ts=None):
    """过去的天数"""
    cur_ts = end_ts if end_ts else get_cur_timestamp()
    if start_ts and cur_ts > start_ts:
        return int((cur_ts - start_ts) / (24 * 60 * 60))


def is_the_same_day(ts1, ts2=None):
    """判断是否是同一天"""
    if not ts2:
        ts2 = get_cur_timestamp()
    cur_zero_ts = get_zero_timestamp(ts2)
    if cur_zero_ts <= ts1 < cur_zero_ts + 60 * 60 * 24:
        return True
    return False


def get_week_start_timestamp(timestamp=None):
    """
    获取timestamp这个时间所在周的开始时间
    """
    if timestamp is None:
        timestamp = get_cur_timestamp()
    dt = datetime.datetime.fromtimestamp(timestamp)
    return (timestamp - dt.date().weekday() * 86400 -
            dt.hour * 3600 - dt.minute * 60 - dt.second)


def get_week_end_timestamp(timestamp=None):
    """获取周结束时间"""
    return get_week_start_timestamp(timestamp) + 7 * 24 * 60 * 60


def get_month_start_timestamp(timestamp=None):
    """
    获取timestamp这个时间所在的月开始时间
    """
    if timestamp is None:
        timestamp = get_cur_timestamp()
    dt = datetime.datetime.fromtimestamp(timestamp)
    return (timestamp - (dt.day - 1) * 24 * 60 * 60 -
            dt.hour * 60 * 60 - dt.minute * 60 - dt.second)


def get_month_end_timestamp(timestamp=None):
    """
    获取timestamp所在月的结束时间戳
    """
    if timestamp is None:
        timestamp = get_cur_timestamp()
    dt = datetime.datetime.fromtimestamp(timestamp)
    year = dt.year
    # 如果是最后一个月，则跳转到第二年
    if dt.month == 12:
        year += 1

    return int(datetime.datetime(year, dt.month % 12 + 1, 1).timestamp())


def get_cur_time_str(timestamp=None):
    """
    获取当前时间的字符串
    时间字符串: %Y-%m-%d %H:%M:%S
    """
    if not timestamp:
        timestamp = get_cur_timestamp()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


def get_cur_month(timestamp=None) -> int:
    """获取当前月份"""
    if not timestamp:
        timestamp = get_cur_timestamp()
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.month


def get_n_month_ago_date(n: int) -> str:
    """获取n个月前的今天"""
    # now_timestamp = int(time.mktime(time.strptime("2021-03-31 00:00:00", '%Y-%m-%d %H:%M:%S')))
    now_timestamp = get_cur_timestamp()
    now_date = datetime.datetime.fromtimestamp(now_timestamp)
    date = now_date + dateutil.relativedelta.relativedelta(months=-n)
    return date.strftime("%Y-%m-%d %H:%M:%S")


def check_is_exp(t1: int, cycle: str, t2=None) -> bool:
    """
    检查过期
    :param t1
    :param cycle : "1d":1天,"1w"：1周,"1m"：1月
    :param t2
    """
    _cycle = cycle[-1]
    num = int(cycle[:-1])

    if not t2:
        t2 = get_cur_timestamp()
    if cycle == "d":
        return get_zero_timestamp(t1) + num * 24 * 60 * 60 < t2
    elif cycle == "w":
        return get_week_start_timestamp(t1) + num * 7 * 24 * 60 * 60 < t2
    # 月级别暂时只支持间隔1个月
    elif cycle == "m":
        return get_month_end_timestamp(t1) < t2
    return False


def get_real_past_days(ts1: int, ts2: int = 0) -> int:
    """
    获取实际过去的天数，以0点为分割
    :param ts1:
    :param ts2:
    :return:
    """
    if not ts2:
        ts2 = get_cur_timestamp()
    # 同一天返回0
    if is_the_same_day(ts1, ts2):
        return 0
    # 非同一天，获取前后的0点，然后计算天数
    return (get_zero_timestamp(ts2) - get_zero_timestamp(ts1)) // 86400


def get_timestamp_hour(timestamp=None) -> int:
    """获取某个时间戳对应的小时"""
    if not timestamp:
        timestamp = get_cur_timestamp()
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.hour


if __name__ == "__main__":
    """"""
    # print(get_month_start_timestamp())
    # print(get_month_end_timestamp())
    print(parse_timestamp("2022-06-08 00:00:00"))
