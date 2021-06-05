#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），
请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

"""
思路：
    递归clone:将末端复制的节点逐步接到上一个节点
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return
        clone_pHead = RandomListNode(pHead.label)
        clone_pHead.random = pHead.random
        clone_pHead.next = self.Clone(pHead.next)
        return clone_pHead
