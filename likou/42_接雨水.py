# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/21
  Desc  ：
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        两个队列，左右队列，单调
        """
        left, left_max_idx, right, right_max_idx = 0, 0, len(height) - 1, len(height) - 1
        rains = 0
        while left < right:
            if height[left_max_idx] <= height[right_max_idx]:
                while left < right:
                    if height[left] <= height[left_max_idx]:
                        rains += height[left_max_idx] - height[left]
                    else:
                        left_max_idx = left
                        break
                    left += 1
            else:
                while left < right:
                    if height[right] <= height[right_max_idx]:
                        rains += height[right_max_idx] - height[right]
                    else:
                        right_max_idx = right
                        break
                    right -= 1
        return rains


if __name__ == '__main__':
    s = Solution()
    cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    ]
    for mater in cases:
        print(s.trap(mater))
