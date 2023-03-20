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

    def __init__(self):
        self.x = "111"

    def __getattr__(self, item):
        # 方式一
        # try:
        #     super().__getattribute__(item)
        # except Exception as e:
        #     print(e)

        # 方式二
        print(f"类属性 {self.__dict__}")
        if item not in self.__dict__:
            return "default_value"
        return super(GetDefaultAttrs, self).__getattr__(item)


t = GetDefaultAttrs()
print(t.y)

print(t.x)
