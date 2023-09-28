# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/20
  Desc  ：
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        二分查找，向左侧保留
        """
        res = [-1, - 1]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if left <= right and nums[right] == target:
            res[0] = right
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left+1) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid
            else:
                right = mid - 1
        if left <= right and nums[left] == target:
            res[1] = left
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        [[5, 7, 7, 8, 8, 10], 8],
    ]
    for mater, tar in cases:
        print(s.searchRange(mater, tar))
