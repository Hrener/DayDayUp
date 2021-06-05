#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，从同一个方向看总共有多少种不同的方法？
比如n=3时，2*3的矩形块有3种不同的覆盖方法(从同一个方向看)：
"""

"""
思路：
排放只有两种选择：
    1. 竖着摆（需1个）
    2. 横着摆（需两个）
类似跳台阶问题（斐波那契）
"""


class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:return 0
        a, b = 1, 1
        while number > 1:
            a, b = b, a + b
            number -= 1
        return b
