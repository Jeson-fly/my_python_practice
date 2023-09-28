# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/15
  Desc  ：
"""
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        计算
        """
        def find_max_idx(start,end):
            max_idx=start
            for i in range(start,end+1):
                if nums[max_idx]<=nums[i]:
                    max_idx=i
            return max_idx
        max_idx=find_max_idx(0,k-1)
        res = [nums[max_idx]]
        for i in range(1,len(nums)-k+1):
            if max_idx<i:
                max_idx=find_max_idx(i,i+k-1)
            else:
                if nums[max_idx]<=nums[i+k-1]:
                    max_idx=i+k-1
            res.append(nums[max_idx])
        return res

if __name__ == '__main__':
    s = Solution()
    cases = [
        [[-7,-8,7,5,7,1,6,0],4],
    ]
    for l,k in cases:
        print(s.maxSlidingWindow(l,k))