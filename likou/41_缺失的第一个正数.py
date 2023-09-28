# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/14
  Desc  ：
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        修改原数组，两次遍历
        """
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums):
                if i + 1 == nums[i]:
                    break
                replace_idx = nums[i] - 1
                nums[i], nums[replace_idx] = nums[replace_idx], nums[i]
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    cases = [
        [3, 4, -1, 1],
    ]
    for mater in cases:
        print(s.firstMissingPositive(mater))
