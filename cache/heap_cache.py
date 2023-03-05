#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2023/3/5 15:23
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 队列缓存
"""
import heapq
import time
from typing import Any, Dict, List


class HeapItem(object):
    def __init__(self, key):
        self.hit = 0  # 命中次数
        self.hit_ts = time.time()  # 最后一次访问时间
        # self.create_ts = 0  # 创建时间
        self.key = key  # cache key

    @property
    def score(self):
        return self.hit_ts

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __le__(self, other):
        return self.score <= other.score

    def __eq__(self, other):
        return self.score == other.score


class CacheItem(object):
    def __init__(self, data):
        self.create_ts = time.time()  # 创建时间
        self.data = data


class HeapCache(object):

    def __init__(self, max_length=2000, live_ts=-1):
        self._max_length = max_length
        self._live_ts = live_ts

        self._heap: List[HeapItem] = []

        self._cache: Dict[int, CacheItem] = {}

    def set(self, key, data: Any):
        """"""
        self._cache[key] = CacheItem(data)
        heapq.heappush(self._heap, HeapItem(key))
        self.fix_length()

    def get(self, key):
        item = self._cache.get(key)
        if time.time() - item.create_ts > self._live_ts >= 0:
            self._cache.pop(key)
            return None
        return item.data

    def fix_length(self):
        """"""
        while len(self._cache) > self._max_length:
            self.pop()

    def pop(self):
        """"""
        item = heapq.heappop(self._heap)
        self._cache.pop(item.key)

    def remove(self, key):
        self._cache.pop(key)

    def setdefault(self, key, default):
        data = self.get(key)
        if data:
            ret = data
        else:
            self.set(key, default)
            ret = default
        return ret


if __name__ == '__main__':
    cache = HeapCache(max_length=5, live_ts=-1)
    cache.set(1, 1)
    print(cache._cache, cache._heap)
    cache.set(2, 2)
    print(cache._cache, cache._heap)
    cache.set(3, 3)
    print(cache._cache, cache._heap)
    cache.set(4, 4)
    print(cache._cache, cache._heap)
    cache.set(5, 5)
    print(cache._cache, cache._heap)
    cache.set(6, 6)
    print(cache._cache, cache._heap)
    cache.get(3)
    print(cache._cache, cache._heap)
    cache.set(7, 7)
    print(cache._cache, cache._heap)
    cache.set(8, 8)
    print(cache._cache, cache._heap)
    cache.set(9, 9)
    print(cache._cache, cache._heap)
    cache.set(10, 10)
    print(cache._cache, cache._heap)
    cache.remove(10)
    print(cache._cache, cache._heap)