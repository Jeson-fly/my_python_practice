# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/10/16
  Desc  ：
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                if count < 2:
                    count += 1
                    slow += 1
                    nums[slow] = nums[fast]
            else:
                count = 1
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


if __name__ == '__main__':
    s = Solution()
    cases = [
        [2,2,1,1,1,2,2],
    ]
    for case in cases:
        s.removeDuplicates(case)
