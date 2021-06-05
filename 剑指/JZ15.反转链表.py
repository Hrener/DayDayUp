#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个链表，反转链表后，输出新链表的表头。

示例1
输入：{1,2,3}
返回值：{3,2,1}
"""


"""
思路：
      1 -> 2 -> 3
空 <- 1 <- 2 <- 3
首先创建一个空节点作为反转链表的链尾tail，然后遍历正向链表，将每个节点指向它前一个节点。
赋值时要注意pHead = pHead.next的位置，避免出现浅拷贝问题  
"""


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        tail = None
        while pHead:
            tem = pHead
            pHead = pHead.next
            tem.next = tail
            tail = tem
        return tail

