# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/20
  Desc  ：比较从集合中判断和从列表中判断的差异
"""
import functools
import time


def cale_time(func):
    @functools.wraps(func)
    def wraps(*arges):
        st = time.perf_counter()
        func(*arges)
        print(f"{func.__name__} 耗时 {time.perf_counter() - st}")

    return wraps


@cale_time
def list_time(query_, num_=1000):
    for _ in range(num_):
        if query_ in base_list:
            return True


@cale_time
def set_time(query_, num_=1000):
    s = set(base_list)
    for _ in range(num_):
        if query_ in s:
            return True


if __name__ == '__main__':
    num = 10

    list_time("每天早睡1小时", num)

    set_time("每天早睡1小时", num)
