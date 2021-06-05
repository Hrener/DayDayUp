#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

"""
归纳：
n = 1, res1 = 1
n = 2, res2 = 2 = res1 + 1
n = 3, res3 = 3 = res2 + res1
n = 4, res4 = 5 = res3 + res2
...
可以看出为斐波那契数列
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        a, b = 1, 1
        while number > 1:
            a, b = b, a + b
            number -= 1
        return b
