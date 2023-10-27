# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/10/13
  Desc  ：
"""
from typing import List, Optional


class Solution:
    def avoidFlood01(self, rains: List[int]) -> List[int]:
        """"""
        ans = [-1 for _ in range(len(rains))]
        full_lake = set()  # 已灌满水的湖
        lake_map = {}  # 可抽水的天数
        for i in range(len(rains)):
            if rains[i] == 0:
                lake_map[i] = list(full_lake)
            else:
                if rains[i] not in full_lake:
                    full_lake.add(rains[i])
                else:
                    empty_day = -1
                    for day, can_empty in lake_map.items():
                        if rains[i] in can_empty:
                            empty_day = day
                            break
                    if empty_day == -1:
                        return []
                    ans[empty_day] = rains[i]
                    del lake_map[empty_day]
                    for day, can_empty in lake_map.items():
                        if rains[i] in can_empty:
                            can_empty.remove(rains[i])

        for day in sorted(list(lake_map.keys())):
            is_full = False
            for lake_num in lake_map[day]:
                if lake_num in full_lake:
                    ans[day] = lake_num
                    is_full = True
                    full_lake.remove(lake_num)
            if not is_full:
                ans[day] = 1

        return ans

    def search(self, l1: list, target):
        """二分查找"""

        def dfs(left, right):
            if left > right:
                return None
            if left == right:
                return l1[left] if l1[left] > target else None
            mid = left + (right - left) // 2
            if l1[mid] >= target:
                return dfs(left, mid)
            else:
                return dfs(mid + 1, right)

        return dfs(0, len(l1) - 1)

    def avoidFlood(self, rains: List[int]) -> List[int]:
        """"""
        ans = [1] * len(rains)
        st = []
        mp = {}  # 记录x个湖下雨的天数
        for i in range(len(rains)):
            if rains[i] == 0:
                st.append(i)
            else:
                ans[i] = -1
                if rains[i] in mp:
                    last_rain_idx = mp[rains[i]]  # 上一次下雨的索引
                    day = self.search(st, last_rain_idx)
                    if day is None:
                        return []
                    st.remove(day)
                    ans[day] = rains[i]
                mp[rains[i]] = i
        return ans


if __name__ == '__main__':
    s = Solution()
    cases = [
        [69, 0, 0, 0, 69],
    ]
    for case in cases:
        s.avoidFlood(case)
