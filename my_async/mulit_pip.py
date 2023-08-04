# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/7/18
  Desc  ：多进程通信，管道

"""
from multiprocessing import Pipe, Process


def sub_process(pipe_connect):
    pipe_connect.send(["hello world"])
    print(id(pipe_connect))


if __name__ == '__main__':
    multi_sub, multi_pub = Pipe(True)
    p = Process(target=sub_process, args=(multi_pub,))
    p.start()
    print(multi_sub.recv())
    print(id(multi_sub), id(multi_pub))
    p.join()
