# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/18
  Desc  ：
"""
import array
import math


class BaseMethod:

    def __iter__(self):
        """实现可迭代"""

    def __bytes__(self):
        """bytes()调用"""

    def __eq__(self, item):
        """判断对象相等"""

    def __abs__(self):
        """abs（）方法"""

    def __contains__(self, item):
        """判断包含关系"""

    def __bool__(self):
        """bool（）调用"""

    def __repr__(self):
        """返回字符串"""

    def __str__(self):
        """返回字符串"""

    def __hash__(self):
        """对象可散列"""

    def __format__(self, format_spec):
        """格式化输出"""


class TestVector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name} {self.x}  {self.y}"

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec=''):
        """"""


class Test01:
    def __init__(self):
        self.x = "qqq"

    def __getattr__(self, item):
        cls = type(self)
        print(item)
        if not hasattr(cls, item):
            return "default"


t = Test01()
t.i
