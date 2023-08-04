# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/5/17
  Desc  ：
"""
import asyncio
import time


def timeit(f):
    def wraps_fun(*args, **kwargs):
        st = time.perf_counter()
        res = f(*args, **kwargs)
        print(f"use time {time.perf_counter() - st}")
        return res

    return wraps_fun


async def func01(a):
    await asyncio.sleep(1)
    return a


async def func02(b):
    await asyncio.sleep(2)
    return b


async def main():
    """"""
    st = time.perf_counter()
    tasks = []
    task1 = asyncio.create_task(func01("a"))
    task2 = asyncio.create_task(func02("b"))
    tasks.append(task1)
    tasks.append(task2)
    results = await asyncio.wait(tasks)
    print(f"use time {time.perf_counter() - st}")
    print(results)


asyncio.run(main())
