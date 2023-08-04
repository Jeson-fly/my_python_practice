# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/5/24
  Desc  ：
"""
import func
import unittest


class Test(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(func.is_prime(3))
        self.assertFalse(func.is_prime(4))