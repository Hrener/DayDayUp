#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
描述:

输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""

"""
示例1
输入：{67,0,24,58}
返回值：[58,24,0,67]
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res
