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
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        合并两个有序列表
        空间复杂度O（m+n）
        时间复杂度O（m+n）
        """
        new_l = []
        nums1_idx = 0
        nums2_idx = 0
        while nums2_idx < len(nums2) or nums1_idx < len(nums1):
            num1 = nums1[nums1_idx] if nums1_idx < len(nums1) else float("inf")
            num2 = nums2[nums2_idx] if nums2_idx < len(nums2) else float("inf")
            if num1 <= num2:
                new_l.append(num1)
                nums1_idx += 1
            else:
                new_l.append(num2)
                nums2_idx += 1
        if len(new_l) % 2 == 0:
            return (new_l[len(new_l) // 2] + new_l[len(new_l) // 2 - 1]) / 2
        return new_l[len(new_l) // 2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        二分查找,排除法一次排除k/2
        """
        def find_k(k):
            num1_left = num2_left = 0



if __name__ == '__main__':
    s = Solution()
    cases = [
        [[1, 2], [3, 4]],
    ]
    for m1, m2 in cases:
        print(s.findMedianSortedArrays(m1, m2))
