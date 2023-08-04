# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.cm
  Time  ：2023/4/6
  Desc  ：元类编程
"""


def record_factory(cla_name, field_names):
    """类工厂"""
    try:
        field_names = field_names.split(",")
    except Exception as e:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        return ";".join([f"{name},{getattr(self, name)}" for name in self.__slots__])

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)
    return type(cla_name, (object,), cls_attrs)


Dog = record_factory("Dog", "color,age")
o = Dog("black", 12)
print(o)
