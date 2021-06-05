#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

示例1
输入：3
返回值：4
"""

"""
思路一：
    暴力递归穷举
"""

class Solution:
    def jumpFloorII(self, number):
        # write code here
        self.res = 0
        def dp(num):
            if num == 0:
                self.res += 1
                return
            if num < 0:
                return
            for i in range(1, num+1):
                dp(num-i)
        dp(number)
        return self.res


"""
思路：
    归纳
"""


class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)
