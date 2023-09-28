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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        """
        p_list = [0] * 26
        for i in range(len(p)):
            p_list[ord(p[i]) - ord("a")] += 1

        target_list = [0] * 26
        left = right = 0
        res = []
        while right < len(s):
            if right < len(p):
                target_list[ord(s[right]) - ord("a")] += 1
                if right == len(p) - 1 and target_list == p_list:
                    res.append(left)
            else:
                target_list[ord(s[left]) - ord("a")] -= 1
                target_list[ord(s[right]) - ord("a")] += 1
                left += 1
                if target_list == p_list:
                    res.append(left)
            right += 1
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        ["cbaebabacd", "abc"],
    ]
    for v1, v2 in cases:
        print(s.findAnagrams(v1, v2))
