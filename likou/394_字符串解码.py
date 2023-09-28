# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/8
  Desc  ：
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        pre_num = 0
        for i in range(len(s)):
            if s[i] == "]":
                tmp_str = ""
                cur_s = stack.pop()
                while cur_s != "[":
                    tmp_str = cur_s + tmp_str
                    cur_s = stack.pop()
                cur_num = 0
                tail = 1
                while stack and stack[-1].isdigit():
                    cur_num += int(stack.pop()) * tail
                    tail *= 10

                stack.append(tmp_str * cur_num)
            else:
                stack.append(s[i])

        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    cases = [
        "3[a]2[bc]",
        "3[a2[c]]"
    ]
    for case in cases:
        s.decodeString(case)
