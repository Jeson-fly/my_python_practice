# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/7/25
  Desc  ：
"""
from typing import List
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        """
        递归，每次都选取最大的数，减半，直到减半的和大于等于初始数组和的一半
        """
        half_reduse = sum(nums) / 2
        cur_reduse = 0
        count = 0
        while cur_reduse < half_reduse:
            max_idx = 0
            for i in range(1, len(nums)):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            cur_reduse += nums[max_idx] / 2
            nums[max_idx] /= 2
            count += 1

        return count

    def heapq_func(self, nums):
        """大根堆解法"""
        target = sum(nums) / 2
        queue = []  # 优先队列（大根堆）
        count = 0
        for num in nums:
            heapq.heappush(queue, -num)
        while target > 0:
            num = heapq.heappop(queue)
            target += num / 2
            heapq.heappush(queue, num / 2)
            count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    cases = [
        [6, 58, 10, 84, 35, 8, 22, 64, 1, 78, 86, 71, 77],
    ]
    for l1 in cases:
        print(s.heapq_func(l1))
