#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个链表，输出该链表中倒数第k个结点。如果该链表长度小于k，请返回空。

示例1
输入：{1,2,3,4,5},1
返回值：{5}
"""

"""
思路：
    快慢指针
"""


class Solution:
    def FindKthToTail(self , pHead , k ):
        # write code here
        len_p = 0
        head = pHead
        while pHead:
            len_p += 1
            pHead = pHead.next
            if len_p > k:
                head = head.next
        return None if len_p < k else head
