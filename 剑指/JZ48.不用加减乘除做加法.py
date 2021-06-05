#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
示例1
输入：1,2
返回值：3
"""


class Solution:
    def Add(self, num1, num2):
        # write code here
        '''相加各位 + 计算进位
        十进制思想
        5+7 各位相加：2 进位：10
        2+10 12 0
        12+0
        二进制计算过程
        5+7 各位相加：101^111=010 进位：101&111=101 (<<1=1010)
        2+10 各位相加：010^1010=1000 进位：010&1010=010 <<1=0100
        8+4 1000^0100=1100 1000&0100=0
        12+0'''
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while num2 != 0:
            num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
            num1 = num1 & mask
            num2 = num2 & mask
        return num1 if num1 <= MAX else ~(num1 ^ mask)