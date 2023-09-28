# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/28
  Desc  ：
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_pos = 0
        step = 0
        cur_idx = 0
        while max_pos < len(nums) - 1:
            tmp_max=0
            max_idx = cur_idx
            for i in range(cur_idx + 1, min(len(nums), cur_idx + nums[cur_idx])):
                if i + nums[i] > tmp_max:
                    max_idx = i
                    tmp_max=i+nums[i]
            cur_idx = max_idx
            max_pos = max_idx + nums[max_idx]
            step += 1
        return step


if __name__ == '__main__':
    s = Solution()
    cases = [
        [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3],
    ]
    for case in cases:
        s.jump(case)
