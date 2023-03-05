#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2023/3/5 15:12
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 
"""
import time
from heapq import nsmallest
from operator import itemgetter


class LFUCache(object):
    def __init__(self, maxsize, alive_second):
        """"""
        self.maxsize = int(maxsize)
        # self.key_index = int(key_index)
        self.alive_second = int(alive_second)
        # self.user_function = user_function
        # self.fun_path = reflect.get_obj_path(user_function)
        self.hits = 0
        self.misses = 0
        self.cache = {}  # mapping of args to results
        self.counter = {}  # times each key has been accessed

    def clear_key(self, key):
        """
        清理指定的缓存内容
        """
        if key in self.cache:
            del self.cache[key]
        if key in self.counter:
            del self.counter[key]

    def clear_keys(self, keys):
        """
        清理指定的缓存内容
        """
        for key in keys:
            if key in self.cache:
                del self.cache[key]
            if key in self.counter:
                del self.counter[key]

    def clear(self):
        """
        清理所有缓存内容
        """
        self.cache.clear()
        self.counter.clear()
        self.hits = 0
        self.misses = 0

    def get_lfu_cache(self, key):
        """
        获取 LFU 算法的缓存
        """

        if self.alive_second > 0:
            ct = time.time()
            if key in self.counter:
                if ct - self.counter[key] > self.alive_second:
                    if key in self.cache:
                        del self.cache[key]
            self.counter[key] = ct
        else:
            if key in self.counter:
                self.counter[key] += 1
            else:
                self.counter[key] = 1

        # get cache entry or compute if not found
        try:
            result = self.cache[key]
            self.hits += 1
        except KeyError:
            if key in self.cache:  # recheck
                result = self.cache[key]
                self.hits += 1
            else:
                # self.cache[key] = result
                self.misses += 1
                # purge least frequently used cache entry
                if len(self.cache) > self.maxsize:
                    for key, _ in nsmallest(self.maxsize // 10, self.counter.items(), key=itemgetter(1)):
                        if key in self.cache:
                            del self.cache[key]
                        if key in self.counter:
                            del self.counter[key]
        return None
