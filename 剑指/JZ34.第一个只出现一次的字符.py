#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）

示例1
输入："google"
返回值：4
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ss = list(s)
        for i in ss:
            if ss.count(i) == 1:
                return s.index(i)
        return -1
