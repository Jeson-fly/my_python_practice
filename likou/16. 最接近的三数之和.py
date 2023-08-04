# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/6/22
  Desc  ：
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        暴力方法 O(n**3)
        """
        total = sum(nums[:3])
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                two_nums = nums[i] + nums[j] - target
                target_num = nums[j + 1]
                for k in range(j + 1, len(nums)):
                    if abs(target_num + two_nums) > abs(two_nums + nums[k]):
                        target_num = nums[k]
                if abs(target - total) > abs(two_nums + target_num):
                    total = two_nums + target_num + target

        return total

    def threeSumClosest_1(self, nums: List[int], target: int) -> int:
        """
        先排序，再使用双指针
        :param nums:
        :param target:
        :return:
        """
        nums.sort()
        total = sum(nums[:3])
        for i in range(len(nums) - 2):
            target_sum = target - nums[i]
            left, right = i + 1, len(nums) - 1
            cur_sum = nums[left] + nums[right]
            while left < right:
                two = nums[left] + nums[right]
                if abs(target_sum - cur_sum) > abs(target_sum - nums[left] - nums[right]):
                    cur_sum = nums[left] + nums[right]
                if two > target_sum:
                    right -= 1
                elif two == target_sum:
                    return 0
                else:
                    left += 1
            if abs(target - total) > abs(target_sum - cur_sum):
                total = cur_sum + nums[i]
        return total


if __name__ == '__main__':
    s = Solution()
    cases = [
        [[-1, 2, 1, -4], 1],
        [[0, 0, 0], 1]
    ]
    for li, targ in cases:
        print(s.threeSumClosest(li, targ))
