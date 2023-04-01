# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/20
  Desc  ：类属性
"""


class GetDefaultAttrs:
    """获取默认属性值"""

    def __getattr__(self, item):
        #     """
        #     仅当在self、Class和超类中找不到指定属性时才会触发该函数
        #     :param item:
        #     :return:
        #     """
        #     # 方式一
        #     # try:
        #     #     super().__getattribute__(item)
        #     # except Exception as e:
        #     #     print(e)
        #
        #     # 方式二
        print(f"类属性 {self.__dict__}")
        return "default_value"


class Test(GetDefaultAttrs):
    def __init__(self):
        self.ab = "1"


t = Test()
print(t.y)

print(t.ab)
