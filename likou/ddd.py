# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/7/5
  Desc  ：
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        单调递减栈
        """
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for idx, value in enumerate(temperatures):
            while stack:
                if temperatures[stack[-1]] < value:
                    i = stack.pop()
                    res[i] = idx - i
                else:
                    stack.append(idx)
                    break
            if not stack:
                stack.append(idx)
        return res


if __name__ == '__main__':

    s = Solution()
    cases = [
        [73, 74, 75, 71, 69, 72, 76, 73]
    ]
    for li in cases:
        print(s.dailyTemperatures(li))
