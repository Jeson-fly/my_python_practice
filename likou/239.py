# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/6/21
  Desc  ：
"""

"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2： 
输入：nums = [1], k = 1
输出：[1]
"""
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        双端队列
        :param nums:
        :param k:
        :return:
        """
        q= deque()


if __name__ == '__main__':
    s = Solution()
    case: List[List[list, int]] = [
        [[1, 3, -1, -3, 5, 3, 6, 7], 3],
        [[1], 1],
    ]

    for arr, k in case:
        print(s.maxSlidingWindow(arr, k))
