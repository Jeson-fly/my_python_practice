# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/20
  Desc  ：
"""


class Test:
    def __init__(self):
        self.x = "111"

    def __getattr__(self, item):
        # 方式一
        # try:
        #     super().__getattribute__(item)
        # except Exception as e:
        #     print(e)

        # 方式二
        if item not in self.__dict__:
            return None
        return super(Test, self).__getattr__(item)


t = Test()
print(t.y)
