# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining22
  Email  ：993811091@qq.com
  Time  ：2023/3/19
  Desc  ：多继承
"""


class A:
    def ping(self):
        print(f"A ping {self}")


class B(A):
    def pong(self):
        print(f"B pong {self}")


class C(A):
    def pong(self):
        print(f"C pong {self}")


class D(B, C):
    def ping(self):
        super().ping()
        print(f"C print {self}")

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()
d.pong()
C.pong(d)
