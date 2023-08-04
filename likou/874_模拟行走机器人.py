# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：lining@qq.com
  Time  ：2023/7/19
  Desc  ：
"""
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 方向
        pos_x, pos_y, d = 0, 0, 0
        res = 0
        mp = set([tuple(i) for i in obstacles])
        for value in commands:
            if value in [-1, -2]:
                d += 1 if value == -1 else -1
                d %= 4
                continue
            for _ in range(value):
                if (pos_x + directions[d][0], pos_y + directions[d][1]) in mp:
                    break
                pos_x += directions[d][0]
                pos_y += directions[d][1]
                res = max(res, pos_x ** 2+ pos_y ** 2)

        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        [[4, -1, 4, -2, 4], [[2, 4]]]
    ]
    for l1, l2 in cases:
        print(s.robotSim(l1, l2))
