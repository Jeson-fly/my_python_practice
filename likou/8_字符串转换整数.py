# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/6/29
  Desc  ：
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        stack = []
        prefix = None
        for item in s:
            if item == " ":
                continue
            if "0" <= item <= "9" or item in ["-", "+"]:
                stack.append(item)
            else:
                break
        res = 0
        for idx, num in enumerate(stack[::-1]):
            res += int(num) * 10 ** idx

        if prefix:
            res = -res
        if res < -2 ** 31:
            return -2 ** 31
        elif res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        "   -42",
    ]
    for li in cases:
        print(s.myAtoi(li))
