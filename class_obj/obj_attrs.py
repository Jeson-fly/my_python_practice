# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/20
  Desc  ：类属性
"""
import pickle


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

    def __getstate__(self, *args, **kwargs):
        """序列化调用函数"""
        return self.__dict__

    def __setstate__(self, state):
        """反序列化调用函数"""
        # print(state)
        # print(self.__dir__())
        # print("iiii", self.__class__.__module__)
        # state["c"]=5555
        self.__dict__ = state


class Test(GetDefaultAttrs):
    def __init__(self):
        self.ab = "1"
        self.d = "2"
        self.c = "3"

    def get_key(self, key):
        return "1111"

    def kkkk(self, yyyy):
        return "2222"


t = Test()

res = pickle.dumps(t)
print(res)
pickle_t: Test = pickle.loads(
    b'\x80\x03c__main__\nTest\nq\x00)\x81q\x01}q\x02(X\x02\x00\x00\x00abq\x03X\x01\x00\x00\x001q\x04X\x01\x00\x00\x00dq\x05X\x01\x00\x00\x002q\x06ub.')
print(pickle_t.kkkk(111))
print(pickle_t.c)

print(t.ab)
