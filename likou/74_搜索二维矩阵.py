# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/11
  Desc  ：
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        折半查找法
        """
        # row, col = len(matrix), len(matrix[0])
        # left = [0, 0]
        # right = [row, col]
        # while left[0] <= right[0] and left[1] <= right[1]:
        #     mid = [left[0] + (right[0] - left[0]) // 2, left[1] + (right[1] - left[1]) // 2]
        #     if matrix[mid[0]][mid[1]] == target:
        #         return True
        #     elif matrix[mid[0]][mid[1]] > target:
        #         right = mid
        #     else:
        #         left = mid
        # return False
        m, n = len(matrix), len(matrix[0])

        def dfs(left, right):
            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n
            if left > right:
                return False
            if left == right:
                if matrix[row][col] == target:
                    return True
                return False
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                return dfs(left, mid - 1)
            else:
                return dfs(mid +1, right)

        return dfs(0, m * n - 1)


if __name__ == '__main__':
    s = Solution()
    cases = [
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
    ]
    for mater, tar in cases:
        print(s.searchMatrix(mater, tar))
