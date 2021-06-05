#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入两个无环的单链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""

"""
思路：
    pHead1 = [2, 3, 4, 5]
    pHead2 = [3, 4, 5]
    对两者进行扩展：
    pHead1 = [2, 3, 4, 5] + [3, 4, 5] = [2, 3, 4, 5, 3, 4, 5]
    pHead2 = [3, 4, 5] + [2, 3, 4, 5] = [3, 4, 5, 2, 3, 4, 5]
    同时遍历两者遇到第一个相同的节点时，即为第一个公共结点
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1==None or pHead2==None:return None
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1
