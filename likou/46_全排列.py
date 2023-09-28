# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/19
  Desc  ：
"""
import copy
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(s):
            if len(s) == len(nums):
                res.append(copy.deepcopy(s))
                return
            for num in nums:
                if num not in s:
                    s.append(num)
                    backtrack(s)
                    s.pop()

        backtrack([])
        return res

if __name__ == '__main__':
    m = Solution()
    cases = [
        [1, 2, 3]
    ]
    for case in cases:
        m.permute(case)