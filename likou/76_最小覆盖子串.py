# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/21
  Desc  ：
"""

from typing import List


class Solution:
    def minWindow1(self, s: str, t: str) -> str:
        """
        先遍历一遍s，找到所有的情况
        """
        t_list = [0] * 58
        for i in range(len(t)):
            t_list[ord(t[i]) - ord("A")] += 1

        tmp_list = []
        contain_idx = []
        for j in range(len(s)):
            if s[j] in t:
                for k in range(len(tmp_list)):
                    if k in contain_idx:
                        continue
                    tmp_list[k][0][ord(s[j]) - ord("a")] += 1
                    if tmp_list[k][0] == t_list:
                        tmp_list[k][1].append(j)
                        contain_idx.append(k)
                j_list = [0] * 58
                j_list[ord(s[j]) - ord("a")] += 1
                tmp_list.append([j_list, [j]])

        sub_min = len(s) + 1
        sub_str = ""

        for idx in contain_idx:
            start, end = tmp_list[idx][1][0], tmp_list[idx][1][1]
            if end - start + 1 < sub_min:
                sub_min = end - start + 1
                sub_str = s[start:end + 1]
        return sub_str

    def minWindow(self, s: str, t: str) -> str:
        """"""

        def check():
            for word, count in t_map.items():
                if cur_map.get(word, 0) < count:
                    return False
            return True

        t_map = {}
        cur_map = {}
        sub_min = len(s)+1
        sub_str = ""
        for i in range(len(t)):
            t_map.setdefault(t[i], 0)
            t_map[t[i]] += 1

        left = rigth = 0

        while rigth < len(s):
            while rigth < len(s):
                if check():
                    if rigth - left + 1 <= sub_min:
                        sub_min = rigth - left + 1
                        sub_str = s[left:rigth]
                    break
                else:
                    cur_map.setdefault(s[rigth], 0)
                    cur_map[s[rigth]] += 1
                    rigth += 1
            while left < rigth:
                if not check():
                    break
                else:
                    if rigth - left + 1 <= sub_min:
                        sub_min = rigth - left + 1
                        sub_str = s[left:rigth]
                    cur_map[s[left]] -= 1
                    left += 1
        return sub_str

if __name__ == '__main__':
    mo = Solution()
    cases = [
        ["ab", "a"],
    ]
    for s_1, s_2 in cases:
        print(mo.minWindow(s_1, s_2))
        # print(ord("A"),ord("a"),ord("z"),ord("Z"))