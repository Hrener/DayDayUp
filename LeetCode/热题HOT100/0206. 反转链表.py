#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        end_tem = None
        while head:
            cur = head.next
            head.next = end_tem
            end_tem = head
            head = cur
        return end_tem


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:return
        pre = ListNode(head.val)
        head = head.next
        while head:
            # 保存下一个节点
            cur = head.next
            # 将pre接到当前节点之后
            head.next = pre
            # 当前节点作为pre
            pre = head
            # 下一个节点作为当前节点
            head = cur
        return pre

