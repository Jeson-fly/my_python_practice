# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/9/26
  Desc  ：
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        转化成列表
        """
        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        node_list.sort(key=lambda x: x.val)
        dummy = ListNode()
        cur_node = dummy
        for node in node_list:
            cur_node.next = node
            cur_node = cur_node.next
        return dummy.next


if __name__ == '__main__':
    model = Solution()
    cases = [
        [4, 2, 1, 3],
        [-1, 5, 3, 4, 0],
        []
    ]
    cases_node = []
    for case in cases:
        nodes = [ListNode()]
        for val in case:
            nodes[-1].next = ListNode(val)
            nodes.append(nodes[-1].next)
        cases_node.append(nodes[0].next)

    for head_node in cases_node:
        model.sortList(head_node)
