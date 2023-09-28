# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/16
  Desc  ：类装饰器
"""
from func import wraps


class Decorator:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __call__(self, *args, **kwargs):
        """"""


# 把Ta们放在一起是为了让大家能更方便地看清无传参装饰和有传参装饰器的比对区别。

collected_functions = []  # 用于收集使用过decorator_with_params装饰器的函数


class ClsBasedDecoratorWithoutParams(object):
    """
    基于类的无传参装饰器。
    """

    def __init__(self, original_func):
        print('在基于类的装饰器中...')
        print('传入的函数为：{}'.format(original_func))
        self._func = original_func

    def __call__(self, *args, **kwargs):
        print('开始装饰...')
        print('传入的参数：args={}, kwargs={}'.format(args, kwargs))
        collected_functions.append(self._func)
        self._func(*args, **kwargs)
        print('有活儿干了...')
        return self._func


class ClsBasedDecoratorWithParams(object):
    """
    基于类的传参装饰器。
    """

    def __init__(self, *_args, **_kwargs):
        print('在基于类的装饰器中...')
        print('装饰器接收到的参数是：args={}, kwargs={}'.format(_args, _kwargs))

    def __call__(self, original_func):
        print('传入的函数为：{}'.format(original_func))
        collected_functions.append(original_func)
        original_func()
        print('有活儿干了...')
        return original_func


if __name__ == '__main__':
    @ClsBasedDecoratorWithoutParams  # 无传参装饰器
    def class_based_decorator_without_params(string):
        print('不干活儿...')


    class_based_decorator_without_params(string='hello_world')


    @ClsBasedDecoratorWithParams('hello')  # 有传参装饰器
    def class_based_decorator_with_params(*args, **kwargs):
        print('不干活儿...')


    class_based_decorator_with_params(string='能看到我吗')

    print('collected_functions:{}'.format(collected_functions))
