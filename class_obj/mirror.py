# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/3/19
  Desc  ：上下文管理
"""


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_writer = sys.stdout.write
        sys.stdout.write = self.original_writer
        return "JABBERWOCKY"

    def reverse_write(self, text):
        self.original_writer(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_writer
        if exc_type is ZeroDivisionError:
            print("please do not divide by zero")
            return True
