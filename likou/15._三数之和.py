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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        排序+双指针
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_total = nums[left] + nums[right] + nums[i]
                if three_total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif three_total > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        [-1,0,1,2,-1,-4],
    ]
    for mater in cases:
        print(s.threeSum(mater))