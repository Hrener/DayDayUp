#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

示例1
输入：{1,3,5},{2,4,6}
返回值：{1,2,3,4,5,6}
"""

"""
思路：
    创建一个链表头，然后比较两个链表，由小到大将节点分别接在后面
    首先判断当前两个链表是否为空
        1. 若一个为空，则将另一个接在后面
        2. 若两个都不为空，则进行比较，将较小的节点接在后面
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        Head = ListNode(None)
        head = Head
        while pHead1 or pHead2:
            if not pHead1:
                head.next = pHead2
                break
            if not pHead2:
                head.next = pHead1
                break
            if pHead1.val <= pHead2.val:
                head.next = pHead1
                head = head.next
                pHead1 = pHead1.next
            else:
                head.next = pHead2
                head = head.next
                pHead2 = pHead2.next
        return Head.next
