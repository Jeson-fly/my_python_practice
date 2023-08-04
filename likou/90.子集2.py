# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/6/25
  Desc  ：
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        before_num = None
        tmp = []
        for item in nums:
            if not res:
                res.extend([[], [nums[0]]])
                tmp = [[nums[0]]]
            elif item == before_num:
                t = []
                for idx in range(len(tmp)):
                    t.append(tmp[idx] + [item])
                res.extend(t)
                tmp = t
            else:
                tmp = []
                for i in res:
                    tmp.append(i + [item])
                res.extend(tmp)
            before_num = item
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        [1, 1],
        [1, 2, 2],
    ]
    for case in cases:
        s.subsetsWithDup(case)
