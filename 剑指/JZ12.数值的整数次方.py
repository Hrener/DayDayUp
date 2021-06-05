#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
描述:

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0。不得使用库函数，同时不需要考虑大数问题，也不用考虑小数点后面0的位数。

示例1
输入：2.00000,3
返回值：8.00000
示例2
输入：2.10000,3
返回值：9.26100
示例3
输入：2.00000,-2
返回值：0.25000
说明：2的-2次方等于1/4=0.25
"""


class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 1
        if exponent < 0:
            flag = -1
            exponent = -1*exponent
        res = 1
        for i in range(exponent):
            res *= base
        if flag == -1:
            res = 1/res
        return res
