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
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        先水平旋转，再沿对角线旋转
        """
        n = len(matrix)
        # 水平旋转
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
        # 对角线旋转
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]


if __name__ == '__main__':
    s = Solution()
    cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]
    for mater in cases:
        print(s.rotate(mater))
