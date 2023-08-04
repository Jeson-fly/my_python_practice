# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/6/26
  Desc  ：
"""


# 单调栈

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_long = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) > 1 and s[stack[-1]] == "(":
                    stack.pop()
                    max_long = max(max_long, i - stack[-1])
                else:
                    stack.append(i)

        return max_long
