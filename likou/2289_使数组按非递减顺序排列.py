# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/7/5
  Desc  ：
"""
from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        """
        寻找下一个大于等于自身的数，返回最大的间隔
        """
        stack = []
        res = 0
        for idx, num in enumerate(nums):
            step = 0
            while stack and nums[stack[-1]] <= num:
                i = stack.pop()
                step = idx - i - 1
            stack.append(idx)
            res = max(res, step)
        return res


if __name__ == '__main__':
    # s = Solution()
    # cases = [
    #     [10,1,2,3,4,5,6,1,2,3]
    # ]
    # for li in cases:
    #     print(s.totalSteps(li))
    print(set(range(1, 10, 1)))
    a = 0
    for i in range(a, 10):
        a += 3
        print(i, a)
    for i in range(10,11):
        print(f"2222  {i}")
