# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining22
  Email  ：lining22@staff.weibo.com
  Time  ：2023/3/16
  Desc  ：函数装饰器
"""
from functools import wraps


def decorator(func):
    def wraps_func(*args):
        # print(f"do some thing {args}")
        result = func(*args)
        return result

    return wraps_func


# 带参数的装饰器
def decorator_param(k="1111k"):
    def decorator_(f):
        @wraps(f)
        def wraps_func(*args):
            result = f(*args)
            print(f"do some thing {k}")
            return result

        return wraps_func

    return decorator_


@decorator_param("111")
def func01(s: str):
    print(f"333 {s}")


@decorator
def func(s: str):
    print(f"give me some {s}")


if __name__ == '__main__':
    func01("coffee")
