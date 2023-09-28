# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/8/21
  Desc  ：
"""
import hashlib
import time
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        使用hash表
        """
        num_dict = {}
        max_len = 0
        for num in nums:
            if num not in num_dict:
                left_len = num_dict.get(num - 1, 0)
                right_len = num_dict.get(num + 1, 0)
                cur_len = left_len + right_len + 1
                if cur_len > max_len:
                    max_len = cur_len
                num_dict[num] = cur_len
                num_dict[num - left_len] = cur_len
                num_dict[num + right_len] = cur_len
        return max_len


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for cur in res:
                res.append(cur + [num])
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        [1, 2, 3]
    ]
    for case in cases:
        s.subsets(case)
