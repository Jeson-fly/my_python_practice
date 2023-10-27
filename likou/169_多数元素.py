# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/10/17
  Desc  ：
"""
from typing import List


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        """
        hash map
        时间复杂度o(n)
        空间复杂度o(n)
        """
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

            if m[num] >= len(nums) / 2:
                return num

    def majorityElement(self, nums: List[int]) -> int:
        """
        摩尔投票，
        时间复杂度o(n)
        空间复杂度o(1)
        推论一： 若记众数的票数为 +1非众数的票数为−1 ，则一定有所有数字的票数和>0。
        推论二： 若数组的前a个数字的票数和=0 ，则 数组剩余(n−a)个数字的票数和一定仍>0 ，即后(n−a)个数字的众数仍为x。
        """
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x


if __name__ == '__main__':
    s = Solution()
    cases = [
        [2, 2, 1, 1, 1, 2, 2],
    ]
    for case in cases:
        s.majorityElement(case)
