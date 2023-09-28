# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/12
  Desc  ：
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, below, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while True:
            for i in range(left, right+1, 1):
                res.append(matrix[top][i])
            top += 1
            if top > below:
                break
            for i in range(top, below+1, 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[below][i])
            below -= 1
            if top > below:
                break
            for i in range(below, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res
if __name__ == '__main__':
    s = Solution()
    cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]
    for mater in cases:
        print(s.spiralOrder(mater))