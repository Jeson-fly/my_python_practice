# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/5/24
  Desc  ：
"""


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
