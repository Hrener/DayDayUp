#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.min_list = []
        self.list = []

    def push(self, node):
        # write code here
        if not self.min_list:
            self.min_list.append(node)
        else:
            if node < self.min_list[-1]:
                self.min_list.append(node)
        self.list.append(node)

    def pop(self):
        # write code here
        if self.list:
            if self.list[-1] == self.min_list[-1]:
                self.min_list.pop(-1)
            pop_value = self.list[-1]
            self.list.pop(-1)
            return pop_value

    def top(self):
        # write code here
        if len(self.list)>0:
            return self.list[-1]

    def min(self):
        # write code here
        return self.min_list[-1]
