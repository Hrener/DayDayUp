#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。1<=数组长度<=50000

示例1
输入：[1,2,3,2,2,2,5,4,2]
返回值：2
示例2
输入：[3,3,3,3,2,2,2]
返回值：3
示例3
输入：[1]
返回值：1
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        self.dict = {}
        num_len = len(numbers)//2
        for num in numbers:
            if num not in self.dict:
                self.dict[num] = 0
            self.dict[num] += 1
            if self.dict[num] > num_len:
                return num
