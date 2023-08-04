# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/6/22
  Desc  ：
"""
from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        """

        :param land:
        :return:
        """


if __name__ == '__main__':
    cases = [
        [
            [0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1]
        ],
    ]
    s = Solution()
    for case in cases:
        print(s.pondSizes(case))
