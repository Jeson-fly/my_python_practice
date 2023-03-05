#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2023/3/5 15:12
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 
"""
import time
from typing import Any
from collections import OrderedDict


class OrderedCache(object):
    """
    利用OrderedDict构建的cache
    当满了的时候，最后一次被访问时间最早的将被删除
    """

    def __init__(self, max_size=256):
        self.max_size = max_size
        self._cache = OrderedDict()

    def __contains__(self, item):
        return item in self._cache

    # def has_key(self, key):
    #     return key in self._cache

    def get(self, key, defalult=None):
        if key in self._cache:
            ret = self._cache[key]
            self._cache.move_to_end(key)
        else:
            ret = defalult
        return ret

    def set(self, key, value):
        if key in self._cache:
            del self._cache[key]
        if len(self._cache) >= self.max_size:
            pop_item = self._cache.popitem(last=False)
        self._cache[key] = value

    def setdefault(self, key, default=None):
        """
        D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
        """
        data = self.get(key)
        if data:
            ret = data
        else:
            self.set(key, default)
            ret = default
        return ret

    def remove(self, key):
        if key in self._cache:
            del self._cache[key]

    def pop(self, key):
        return self.remove(key)

    def items(self):
        return self._cache.items()

    def clear_all(self):
        self._cache.clear()

    def info(self) -> dict:
        return {
            "max_size": self.max_size,
            "count": len(self._cache)
        }


class CacheData(object):
    def __str__(self):
        return f"{self.__class__.__name__}<{self.dump()}>"

    def __repr__(self):
        return self.__str__()

    def __init__(self):
        """"""
        self.data: Any = None
        self.key: str = ''
        self.hit: int = 0
        self.last_hit_ts: int = 0
        self.create_ts: int = 0

    def dump(self):
        return {
            'key': self.key,
            'hit': self.hit,
            'last_hit_ts': self.last_hit_ts,
            'data': self.data.dump()
        }


class LiveCache(object):
    """有过期时间的缓存"""

    def __contains__(self, item):
        return item in self._cache

    def __str__(self):
        return "{}<{}>".format(self.__class__.__name__, self.dump())

    def __repr__(self):
        return self.__str__()

    def __init__(self, max_length=2000, live_ts=-1):
        # self._cache: Dict[int, HeadCacheData] = {}
        self._cache = OrderedCache(max_length)
        #  缓存长度数量的限制控制
        self.max_length = max_length
        self.live_ts = live_ts

    def dump(self):
        return {
            key: data.dump()
            for key, data in self._cache.items()
        }

    def get(self, key) -> Any:
        _cache = self._cache.get(key)
        if _cache:

            now_ts = time.time()

            if now_ts - _cache.create_ts > self.live_ts >= 0:
                self._cache.remove(key)
                return None

            _cache.hit += 1
            _cache.last_hit_ts = time.time()
            return _cache.data

        return None

    def set(self, key, data: Any):
        self._cache.setdefault(key, CacheData())
        _cache = self._cache.get(key)
        _cache.hit += 1
        _cache.last_hit_ts = time.time()
        _cache.create_ts = time.time()
        _cache.data = data
        _cache.key = key

    def setdefault(self, key, default=None):
        """
        D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
        """
        data = self.get(key)
        if data:
            ret = data
        else:
            self.set(key, default)
            ret = default
        return ret

    def remove(self, key):
        self._cache.remove(key)

    def pop(self, key):
        return self.remove(key)

    def items(self):
        return self._cache.items()


if __name__ == '__main__':
    cache = OrderedCache(5)
    cache.set(1, 1)
    print(cache._cache)
    cache.set(2, 2)
    print(cache._cache)
    cache.set(3, 3)
    print(cache._cache)
    cache.set(4, 4)
    print(cache._cache)
    cache.set(5, 5)
    print(cache._cache)
    cache.set(6, 6)
    print(cache._cache)
    cache.get(3)
    print(cache._cache)
    cache.set(7, 7)
    print(cache._cache)
    cache.set(8, 8)
    print(cache._cache)
    cache.set(9, 9)
    print(cache._cache)
    cache.set(10, 10)
    print(cache._cache)
    cache.remove(10)
    print(cache._cache)
    cache.clear_all()
    print(cache._cache)
