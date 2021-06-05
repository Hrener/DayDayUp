#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

示例1
输入：{1,2,3,3,4,4,5}
返回值：{1,2,5}
"""

"""
思路：
    创建结果res_head头结点，next指向输入pHead。并复制res_head头结点给pre1。
    pre1 -> res_head -> 0
               pHead -> 1
                        2
                        3
                        3
                        4
                        4
                        5
    遍历pHead:
        若pHead.val 不等于 pHead.next.val，pre1.next -> pHead， pre1 = pre1.next， pHead = pHead.next
            res_head -> 0
               pre1  -> 1
               pHead -> 2
                        3
                        3
                        4
                        4
                        5
                        
            res_head -> 0
                        1
               pre1  -> 2
               pHead -> 3
                        3
                        4
                        4
                        5
        若pHead.val 等于 pHead.next.val，pHead指向下一个不为None的节点，继续判断
            res_head -> 0
                        1
               pre1  -> 2
               pHead -> 4
                        4
                        5
        若pHead.val 等于 pHead.next.val，pHead指向下一个不为None的节点，继续判断
            res_head -> 0
                        1
               pre1  -> 2
               pHead -> 5
        继续
            res_head -> 0
                        1
                        2
               pre1  -> 5
               pre1.next = None
        返回结果
        return res_head.next
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return
        res_head = ListNode(None)
        res_head.next = pHead
        pre1 = res_head
        while pHead:
            if not pHead.next:
                pre1.next = pHead
                break
            if pHead.val != pHead.next.val:
                pre1.next = pHead
                pre1 = pre1.next
                pHead = pHead.next
            else:
                tem = pHead.val
                while pHead and pHead.val == tem:
                    pHead = pHead.next
                if not pHead:pre1.next = None
        return res_head.next
