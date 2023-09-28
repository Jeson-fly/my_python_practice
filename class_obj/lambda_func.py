# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/8/5
  Desc  ：lambda函数
"""


def func():
    print("调用1次")
    return {"1": 1, "2": 2, "3": 3}


for k, v in func().items():
    print(k, v)
