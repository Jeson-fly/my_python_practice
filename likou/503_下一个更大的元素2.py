# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/6/26
  Desc  ：
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        利用单调递减占实现
        """
        stack = []
        res = [-1 for _ in range(len(nums))]
        for i in range(2 * len(nums) - 1):
            if i >= len(nums):
                i -= len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        [1, 2, 1]
    ]
    for li in cases:
        print(s.nextGreaterElements(li))
