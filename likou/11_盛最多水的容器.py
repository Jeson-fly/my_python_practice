# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/8/23
  Desc  ：
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针
        left, right = 0, len(height) - 1
        max_value = 0
        while left < right:
            while left < right and height[left] <= height[right]:
                max_value = max(max_value, height[left] * (right - left))
                left += 1
            while left < right and height[left] > height[right]:
                max_value = max(max_value, height[right] * (right - left))
                right -= 1
        return max_value


if __name__ == '__main__':
    s = Solution()
    cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
    ]
    for case in cases:
        s.maxArea(case)
