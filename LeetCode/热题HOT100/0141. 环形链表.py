#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
给定一个链表，判断链表中是否有环。如果链表中存在环，则返回 true 。 否则，返回 false 。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        list_ = []
        while head:
            if head not in list_:
                list_.append(head)
            else:
                return True
            head = head.next
        return False


# 快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        low = head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next
            if fast == low:return True
        return False
