# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/7/27
  Desc  ：
"""
from dataclasses import dataclass, field, asdict


@dataclass
class Test:
    a: str = field(default="")
    b: int = field(default=0)
    c: str = field(default="")
    def __post_init__(self):
        self.c = self.a + "kkkk"


t = Test("yyy")
print(asdict(t))
