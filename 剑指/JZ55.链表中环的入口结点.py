#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""

"""
思路：
    设置快慢指针，都从链表头出发，快指针每次走两步，慢指针一次走一步，假如有环，一定相遇于环中某点(结论1)。
    接着让两个指针分别从相遇点和链表头出发，两者都改为每次走一步，最终相遇于环入口(结论2)。
    两个结论：
        1、设置快慢指针，假如有环，他们最后一定相遇。
        2、两个指针分别从链表头和相遇点继续出发，每次走一步，最后一定相遇与环入口。
"""


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast, slow = pHead, pHead
        while fast and fast.next:
            fast = fast.next.next  # 快：两步
            slow = slow.next  # 慢：一步
            if fast and fast == slow:  # 快慢相同：有环
                slow = pHead  # 从头开始
                while fast != slow:  # 快慢不同：都走1步
                    fast = fast.next
                    slow = slow.next
                return fast
        return None