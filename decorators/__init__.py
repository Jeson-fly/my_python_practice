# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining22
  Email  ：993811091@qq.com
  Time  ：2023/3/16
  Desc  ：装饰器
"""
from functools import wraps
import time


# 装饰器函数
def timeit(f):
    @wraps(f)
    def wraps_fun(*args, **kwargs):
        st = time.perf_counter()
        res = f(*args, **kwargs)
        print(f"use time {time.perf_counter() - st}")
        return res

    return wraps_fun


# 装饰器类
class Timeit:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        st = time.perf_counter()
        res = self.fun(*args, **kwargs)
        print(f"class use time {time.perf_counter() - st}")
        return res


# 带参数的类装饰器
class TimeitParam:
    def __init__(self, param):
        self.param = param

    def __call__(self, f):
        @wraps(f)
        def wraps_func(*args, **kwargs):
            st = time.perf_counter()
            res = f(*args, **kwargs)
            print(f"class param use time {self.param} {time.perf_counter() - st}")
            return res

        return wraps_func


# 类函数装饰器
class Test:

    def timeit_in(f):
        def wraps_fun(*args, **kwargs):
            st = time.perf_counter()
            res = f(*args, **kwargs)
            print(f"use time {time.perf_counter() - st}")
            return res

        return wraps_fun

    @timeit_in
    def cls_fun(self, a, b):
        """"""
        time.sleep(1)
        print(a + b)

    timeit_in = staticmethod(timeit_in)


@Test.timeit_in
def func(a, b):
    time.sleep(1)
    print(a + b)


t = Test()
t.cls_fun(1, 2)
func(1, 2)
