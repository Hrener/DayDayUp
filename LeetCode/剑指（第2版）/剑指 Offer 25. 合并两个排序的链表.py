#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
示例1：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        res_tem = res
        while l1 and l2:
            if l1.val <= l2.val:
                res_tem.next = l1
                res_tem = res_tem.next
                l1 = l1.next
            else:
                res_tem.next = l2
                res_tem = res_tem.next
                l2 = l2.next
        res_tem.next = l1 if l1 else l2
        return res.next
