#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 

示例:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_list = []
        self.list = []

    def push(self, val: int) -> None:
        if not self.min_list:
            self.min_list.append(val)
        else:
            if val < self.min_list[-1]:
                self.min_list.append(val)
        self.list.append(val)

    def pop(self) -> None:
        if self.list:
            if self.list[-1] == self.min_list[-1] and self.min_list[-1] not in self.list[:-1]:
                self.min_list.pop(-1)
            pop_value = self.list[-1]
            self.list.pop(-1)
            return pop_value

    def top(self) -> int:
        if len(self.list) > 0:
            return self.list[-1]

    def getMin(self) -> int:
        return self.min_list[-1] if len(self.min_list) > 0 else 0

