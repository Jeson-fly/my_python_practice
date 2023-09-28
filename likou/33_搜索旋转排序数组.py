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
    def search(self, nums: List[int], target: int) -> int:
        """
        二分查找
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if nums[mid] <= nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] > nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    cases = [
        [[5, 1, 3], 3],
        [[4, 5, 6, 7, 8, 1, 2, 3], 8],
    ]
    for mater, tar in cases:
        print(s.search(mater, tar))
