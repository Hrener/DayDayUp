#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
"""


class CQueue:

    def __init__(self):
        self.l1, self.l2 = [], []

    def appendTail(self, value: int) -> None:
        self.l1.append(value)

    def deleteHead(self) -> int:
        if not self.l2:
            if not self.l1:
                return -1
            else:
                self.l2 = self.l1[::-1]
                self.l1 = []
        pop_value = self.l2[-1]
        self.l2.pop(-1)
        return pop_value
