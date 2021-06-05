#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class Solution:
    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, node):
        # write code here
        self.l1.append(node)

    def pop(self):
        # return xx
        if not self.l2:
            while self.l1:
                self.l2.append(self.l1.pop(-1))
        return self.l2.pop(-1)
