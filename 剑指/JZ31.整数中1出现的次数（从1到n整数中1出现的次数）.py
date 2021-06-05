#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数
例如，1~13中包含1的数字有1、10、11、12、13因此共出现6次
示例1
输入：13
返回值：6
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        for num in range(1, n+1):
            while num:
                if num % 10 == 1:
                    res += 1
                num = num // 10
        return res
