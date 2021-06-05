#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述：
输入一个字符串,包括数字字母符号,可以为空
返回值描述：
如果是合法的数值表达则返回该数字，否则返回0

示例1
输入："+2147483647"
返回值：2147483647
示例2
输入："1a33"
返回值：0
"""


class Solution:
    def StrToInt(self, s):
        # write code here
        reasonal_str = ['0','1','2','3','4','5','6','7','8','9','+','-']
        flag = 1
        res = 0
        for str_ in s:
            if str_ in reasonal_str:
                if str_ == '+':
                    flag = 1
                    continue
                elif str_ == '-':
                    flag = -1
                    continue
                else:
                    res=res*10+reasonal_str.index(str_)
            else:
                res = 0
                break
        return res*flag

