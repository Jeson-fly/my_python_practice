#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2023/3/5 11:46
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 创建对象
"""


class Mate(type):
    """
    第一次创建对象的过程中，调用__init__方法，初始化参数值，后面不再初始化参数值
    只可以改动对象的属性

    """

    def __call__(cls, *args, **kwargs):
        instance = getattr(cls, "INSTANCE", None)

        if instance is None:
            instance = cls.__new__(cls, *args, **kwargs)
            instance.__init__(*args, **kwargs)
        return instance


class Singleton(object, metaclass=Mate):
    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.INSTANCE is None:
            cls.INSTANCE = object.__new__(cls, *args, **kwargs)
        return cls.INSTANCE


class MyTest1(Singleton):
    """"""

    def __init__(self):
        self.name = ""
        self.age = 18


if __name__ == '__main__':
    t1 = MyTest1()
    t1.name = "lining"
    t1.age = 32
    t1_id = id(t1)
    t2 = MyTest1()
    t2.name = "lining2"

    t2_id = id(t2)
    print(t1.__dict__, t2.__dict__)
    assert t1.name == t2.name
    assert id(t2) == t1_id
    assert t1.age == t2.age
