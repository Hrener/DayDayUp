#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。n≤39

示例1
输入：4
返回值：3
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:return 0
        a, b = 0, 1
        while n > 1:
            a, b, = b, a + b
            n -= 1
        return b
